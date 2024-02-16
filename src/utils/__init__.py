# copy all the library from config.yaml

import os,sys
from src.exception import CustomException
import yaml
from src.logger import logging 
from datetime import datetime 
from src.constant import *


def read_yaml_file(file_path:str)->dict:
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise CustomException(e ,sys)
    



def create_yaml_file_numerical_columns(column_list, yaml_file_path):
    
    if os.path.exists(yaml_file_path):
        # If the file already exists, replace its content with the new data
        numerical_columns = {"numerical_columns": column_list}
        
        with open(yaml_file_path, 'w') as yaml_file:
            yaml.dump(numerical_columns, yaml_file)
    else:
        # If the file doesn't exist, create a new YAML file with the data
        numerical_columns = {"numerical_columns": column_list}
        
        with open(yaml_file_path, 'w') as yaml_file:
            yaml.dump(numerical_columns, yaml_file)

def create_yaml_file_categorical_columns_from_dataframe(dataframe, categorical_columns, yaml_file_path):
    # Check if the YAML file already exists
    try:
        with open(yaml_file_path, 'r') as existing_yaml_file:
            existing_data = yaml.safe_load(existing_yaml_file)
    except FileNotFoundError:
        # If the file doesn't exist, initialize with an empty dictionary
        existing_data = {}

    # Create a dictionary of column categories
    column_categories_dict = {}

    for column in categorical_columns:
        if column in dataframe.columns:
            categories = dataframe[column].unique().tolist()
            column_categories_dict[column] = categories

    # Add the new data to the existing dictionary
    existing_data["categorical_columns"] = column_categories_dict

    # Write the combined data back to the YAML file
    with open(yaml_file_path, 'w') as yaml_file:
        yaml.dump(existing_data, yaml_file)