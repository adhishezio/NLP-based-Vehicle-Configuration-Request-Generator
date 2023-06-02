# -*- coding: utf-8 -*-
"""
Created on Tue May 16 2023

@author: adhish
"""

import spacy

class BooleanFormulas:
    def __init__(self):
        self.roof_abbreviations = {"sunroof": "S403A", "panorama glass roof": "S402A", "panorama glass roof sky lounge": "S407A"}
        self.package_abbreviations = {"M Sport Package": "P337A", "M Sport Package Pro": "P33BA", "Comfort Package EU": "P7LGA", "Comfort Package.": "P7LGA", "Comfort Package":"P7LGA"}
        self.steering_wheel_abbreviations = {"left-hand drive": "LL", "right-hand drive": "RL"}

        # Load the spaCy Custom NER model
        self.nlp = spacy.load("model-best")

        # Operator mapping
        self.operator_mapping = {
            "AND": "+",
            "OR": "/",
            "AND NOT": "+-",
            "OR NOT": "/-"
        }

    def identify_entities(self, user_prompt):
    
        """
        Identifies relevant entities in the user prompt using NER processing.

        Args:
        - user_prompt: The user prompt text

        Returns:
        - identified_entities: A list of identified entities and their labels
        """
        
        # Perform NER processing on the user prompt
        doc = self.nlp(user_prompt)

        identified_entities = []

        # Identify relevant entities based on the custom NER model
        for ent in doc.ents:
            if ent.label_ == "OPERATORS":
                identified_entities.append((ent.text.lower(), ent.label_))
            elif ent.label_ == "ROOF CONFIGURATION":
                identified_entities.append((ent.text.lower(), ent.label_))
            elif ent.label_ == "AVAILABLE PACKAGES":
                identified_entities.append((ent.text, ent.label_))
            elif ent.label_ == "STEERING WHEEL CONFIGURATION":
                identified_entities.append((ent.text.lower(), ent.label_))

        return identified_entities

    def convert_to_abbreviations(self, entity, label):
    
        """
        Converts entity to its corresponding abbreviation based on the label.

        Args:
        - entity: The entity text
        - label: The label of the entity

        Returns:
        - abbreviation: The corresponding abbreviation or the original entity
        """
        if label == "ROOF CONFIGURATION":
            return self.roof_abbreviations.get(entity.lower(), entity)
        elif label == "AVAILABLE PACKAGES":
            return self.package_abbreviations.get(entity, entity)
        elif label == "STEERING WHEEL CONFIGURATION":
            return self.steering_wheel_abbreviations.get(entity, entity)
        else:
            return entity

    def construct_boolean_formula(self, identified_elements):
        
        """
        Constructs the boolean formula from the identified elements.

        Args:
        - identified_elements: A list of identified entities and their labels

        Returns:
        - boolean_formula: The constructed boolean formula

        """    
        symbol_mapping = {
            "all": "+",
            "with": "+",
            "without": "-",
            "except": "-",
            "and": "+",
            "or": "/",
            "at the same time": "+",
        }

        boolean_formula = ""
        stack = []

        for element, label in identified_elements:
            if element in symbol_mapping:
                symbol = symbol_mapping[element]
                if symbol == "or":
                    # Check if there is a pending "and" expression
                    if stack and stack[-1] == "+":
                        boolean_formula += "("
                        stack.append("(")

                    boolean_formula += symbol
                else:
                    boolean_formula += symbol
                    stack.append(symbol)
            else:
                abbreviation = self.convert_to_abbreviations(element, label)
                boolean_formula += abbreviation


        return boolean_formula
    

    def add_parentheses(self, boolean_formula):
        """
        Adds parentheses to the given boolean formula.

        Args:
            boolean_formula (str): The boolean formula to which parentheses need to be added.

        Returns:
            str: The boolean formula with parentheses added.

        Example:
            If boolean_formula is "+A/B+C", the function will return "+(A/B)+C".

        """
        result = ""
        abbreviation = boolean_formula.split('+')

        # Iterate through abbreviations and add parentheses
        for i, abbr in enumerate(abbreviation):
            if '/' in abbr:
                result += '(' + abbr + ')'
            else:
                result += abbr
            
            # Add '+' between abbreviations, except for the last one
            if i < len(abbreviation) - 1:
                result += '+'

        return result
