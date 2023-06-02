
# NLP-based Vehicle Configuration Request Generator
This README file provides instructions on how to run and test the application. 

## Description
The NLP-based Vehicle Configuration Request Generator is an application designed to convert unstructured prompts provided by users into request bodies that adhere to the specific format required by the BMW Group. These request bodies are used by the BMW Group to assess the feasibility of vehicle configurations for specific vehicle models and dates. The application leverages natural language processing (NLP) techniques to accurately interpret and transform user prompts into structured request bodies.

The primary goal of this project is to showcase proficiency in working with NLP models and demonstrate the ability to convert natural language into the prescribed request body format. The success of the application depends on adhering to the defined format and guidelines provided in the requirements section.

By using the NLP-based Vehicle Configuration Request Generator, users can conveniently input their desired vehicle configurations in natural language and obtain a formatted request body that can be used for assessment purposes by the BMW Group.

## Key Features
* Natural language processing to analyze user prompts
* Entity identification using a custom NER model
* Generation of model type codes based on identified sales descriptions
* Construction of boolean formulas representing configuration options
* Extraction of dates from user prompts
* Conversion of user prompts into structured request bodies
* Compatibility with the official BMW Group request body format
* Test-driven development using pytest for robustness and accuracy

## Prerequisites
Before running the application, make sure you have the following prerequisites installed:
* Python (version 3.6 or above)
* pip (Python package installer)

## Installation
To install the dependencies required by the application, navigate to the project directory and run the following command:

```bash
pip install -r requirements.txt
```
This will install the necessary packages specified in the requirements.txt file.

## Running the Application
To run the application, execute the following command in the project directory:

```bash
python RequestBody.py
```
This will execute the application and generate the request body based on the user prompts.

## Testing the Application
To test the application, ensure that the dependencies are installed by following the installation steps mentioned above.

In the project directory, run the following command to execute the tests:

```bash
pytest test_requestbody.py
```
This will run the test cases defined in the test_requestbody.py file and provide the test results.

## Conclusion
By following the steps mentioned in this README file, you will be able to install, run, and test the application successfully.
In this task, the goal was to develop an application that can take user prompts as input and convert them into a request body format used by the BMW Group. The request body represents a configuration for a vehicle and is used to determine its feasibility based on the given vehicle model and date.