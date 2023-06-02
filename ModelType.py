# -*- coding: utf-8 -*-
"""
Created on Mon May 15 2023

@author: adhish
"""

import spacy
import datefinder

class ModelTypeCode:
    def __init__(self):
        """
        Initializes the ModelTypeCode class.

        Attributes:
            nlp: The spaCy model used for Named Entity Recognition (NER).
            sales_descriptions: A dictionary mapping sales descriptions to model type codes.
            
        """
        
        # Load the custom NER model
        self.nlp = spacy.load("./model-best")

        # Abbreviations for Sales descriptions and corresponding model type codes
        self.sales_descriptions = {
            "iX xDrive50": "21CF",
            "iX xDrive40": "11CF",
            "X7 xDrive40i": "21EM",
            "X7 xDrive40d": "21EN",
            "M8": "DZ01",
            "318i": "28FF"
        }

    def identify_entities(self, user_prompt):
        """
        Identifies entities in the user prompt using Named Entity Recognition (NER).

        Args:
            user_prompt (str): The user prompt to be processed.

        Returns:
            list: A list of identified entities as tuples (entity, label).

        """
            
        # Perform NER processing on the user prompt
        doc = self.nlp(user_prompt)

        identified_entities = []

        # Identify relevant entities based on the custom NER model
        for ent in doc.ents:
            identified_entities.append((ent.text, ent.label_))

        return identified_entities

    def generate_model_type_codes(self, user_prompt):
        """
        Generates model type codes based on identified sales descriptions in the user prompt.

        Args:
            user_prompt (str): The user prompt to be processed.

        Returns:
            list: A list of generated model type codes.

        """
        model_type_codes = []

        identified_entities = self.identify_entities(user_prompt)

        # Extract the identified entities into model type codes
        for entity, label in identified_entities:
            if label == "SALES DESCRIPTION" and entity in self.sales_descriptions:
                model_type_codes.append(self.sales_descriptions[entity])

        return model_type_codes

    def extract_date(self, prompt):
        """
        Extracts a date from the given prompt using datefinder.

        Args:
            prompt (str): The prompt to extract the date from.

        Returns:
            str: The extracted date in the format 'YYYY-MM-DD', or None if no date is found.

        """
        matches = list(datefinder.find_dates(prompt))
        if len(matches) > 0:
            date_obj = matches[0]
            date_formatted = date_obj.strftime('%Y-%m-%d')
        else:
            date_formatted = None
        
        return date_formatted
