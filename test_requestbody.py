# -*- coding: utf-8 -*-
"""
Created on Wed May 17 2023

@author: adhish
"""

import pytest 
from RequestBody import GenerateRequestBody

def test_generate_request_body():
    # Create an instance of the CustomModule class
    custom_module = GenerateRequestBody()

    # Define the user prompt
    # Test case 1
    user_prompt_1 = "I want to order a BMW iX xDrive40 with right-hand drive configuration. I will be ordering it at the 1st of October 2022."

    # Generate the request body using the CustomModule
    request_body = custom_module.generate_request_body(user_prompt_1)

    # Define the expected request body
    expected_request_body = {
        "modelTypeCodes": ["11CF"],
        "booleanFormulas": ["+RL"],
        "dates": ["2022-10-01"]
    }

    # Check if the generated request body matches the expected request body
    assert request_body == expected_request_body

    # Test case 2 
    user_prompt_2 = "Hello, is the X7 xDrive40i available without a panorama glass roof and with the EU Comfort Package. I need the vehicle on the 8th of November 2024."
    expected_request_body_1 = {
        "modelTypeCodes": ["21EM"],
        "booleanFormulas": ["-S402A+P7LGA"],
        "dates": ["2024-11-08"]
    }
    assert custom_module.generate_request_body(user_prompt_2) == expected_request_body_1

    # Test case 3
    user_prompt_3 = "I am planning to order the BMW M8 with a sunroof or panorama glass roof sky lounge, and the M Sport Package on 12th April 2018. Is this configuration possible?"
    expected_request_body_2 = {
        "modelTypeCodes": ["DZ01"],
        "booleanFormulas": ["+(S403A/S407A)+P337A"],
        "dates": ["2018-04-12"]
    }
    assert custom_module.generate_request_body(user_prompt_3) == expected_request_body_2

    # Test case 4
    user_prompt_4 = "I am planning to order the BMW 318i with a Panorama Glass Roof Sky Lounge or sunroof, and the Comfort Package EU on July, 10th 2024. Is this configuration possible?"
    expected_request_body_3 = {
        "modelTypeCodes": ["28FF"],
        "booleanFormulas": ["+(S407A/S403A)+P7LGA"],
        "dates": ["2024-07-10"]
    }
    assert custom_module.generate_request_body(user_prompt_4) == expected_request_body_3
