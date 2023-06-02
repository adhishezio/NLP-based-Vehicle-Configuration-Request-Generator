# -*- coding: utf-8 -*-
"""
Created on Wed May 17 2023

@author: adhish
"""
from BooleanDetection import BooleanFormulas
from ModelType import ModelTypeCode

class GenerateRequestBody:
    def __init__(self):
        # Create an instance of the BooleanFormulas class
        self.boolean_formulas = BooleanFormulas()
        # Create an instance of the ModelTypeCode class
        self.model_type = ModelTypeCode()

    def generate_request_body(self, prompt):
        # Identify entities using BooleanFormulas class
        identified_entities = self.boolean_formulas.identify_entities(prompt)
        # Construct boolean formula using identified entities
        boolean_formula = self.boolean_formulas.construct_boolean_formula(identified_entities)
        # Generate model type codes using ModelTypeCode class
        model_type_codes = self.model_type.generate_model_type_codes(prompt)
        # Add parentheses to the boolean formula using BooleanFormulas class
        boolean_formula_with_parentheses = self.boolean_formulas.add_parentheses(boolean_formula)
        # Extract dates using ModelTypeCode class
        dates = self.model_type.extract_date(prompt)
        
        # Create the request body dictionary
        request_body = {
            "modelTypeCodes": model_type_codes,
            "booleanFormulas": [boolean_formula_with_parentheses],
            "dates": [dates]
        }
        
        return request_body

# Usage example
custom_module = GenerateRequestBody()
user_prompt = "I am planning to order the BMW 318i with a Panorama Glass Roof Sky Lounge or sunroof, and the Comfort Package EU on July, 10th 2024. Is this configuration possible?"
request_body = custom_module.generate_request_body(user_prompt)
print('Request Body:' + str(request_body) )

