import os ,sys
#
# first of all we are going to call our current working directory ( why)
#becoz we need a information whatever the information that i have mentioned in config.yaml. I need a complete information under
# our constant file

#Step 1 Fetch the current working directory
ROOT_DIR = os.getcwd()

#STEP 2 : CALL CONFIG 
CONFIG_DIR = "config"

#STEP 3 : dEFINE THE SCHEMA FILE 
SCHEMA_FILE  = "config.yaml"

#STEP 4 : Join the complete path 
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR ,SCHEMA_FILE)  #  <<<<<<<<<<---------------->>>>>>>>>
# with help of this variable we are able to access our config.yaml

#Now we are creating the Varaible realted to our Data Ingestion  pipeline  
# _______________________________________________________________________________________________________________________


#artifact / data_ingestion/ raw_data & ingested_data / train & test
# data_ingestion_config:
#   data_base : Machine_Learning 
#   collection_name: DATASET
#   data_ingestion: data_ingestion
#   raw_data_dir: raw_data
#   ingested_dir: ingested_data
# ingested_train_dir : Train 
# ingested_test_dir :Test
#_________________________________________________________________________________________________________________________

#artifact / data_ingestion/ raw_data & ingested_data / train & test

DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_DATABASE_NAME = "Machine_Learning"
DATA_INGESTION_COLLECTION_NAME = "DATASET"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"  # with help of this data_ingestion we'ill get artifact dir (artifact / data_ingestion/) under this we have data ingestion dir 
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_INGESTED_DIR_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"

#apart from above one that we need to call the config file key as well 
# CONFIG_FILE_KEY   =  "config.yaml"    # not "config."yaml 
CONFIG_FILE_KEY   =  "config" 
#we have to call the "config folder" not config.yaml"  


#_______________________________________________________________________
# These are the complete variable related to data ingestion pipeline 
#______________________________________________________________________________________________________________________________________________________________________________


# __________DATA_TRANSFORMATION________________________________________________


#first of all I m going to call our ROOT DIR becauase here i m going to define the schema I m going to call root dir becoz i want to read the completed inforamtion whatever the information we g=have under the schema.yaml
# how we can do ?  We need to call the root dir and then we 've to call the config anmd then we can selectthe schema yaml 
# STEP 1:  CALL THE SCHEMA FILE PATH 

ROOT_DIR = os.getcwd()
CONFIG_DIR = "config"
SCHEMA_FILE = "schema.yaml"

SCHEMA_FILE_PATH = os.path.join(ROOT_DIR ,CONFIG_DIR ,SCHEMA_FILE)

# step :2 next we are going to define our Data transfomation file path 
"""we are going to define the varaible related to our data transformation .
    Let me creating one more varaible called transformation.yaml why we need this
    becoz under our transformation yaml file that we can define oue entre informatiion 
    related to whatever the operation we are going to perform ."""
# transformation File path 
ROOT_DIR=os.getcwd()
CONFIG_DIR='config'
TRANSFORMATION_FILE='transformation.yaml'
TRANFORMATION_YAML_FILE_PATH=os.path.join(ROOT_DIR,CONFIG_DIR,TRANSFORMATION_FILE)


# Data transfomation file path 
TARGET_COLUMN_KEY =  "target_column"
NUMERICAL_COLUMN_KEY ="numerical_columns"
CATEGORICAL_COLUMN_KEY = "categorical_columns"
OUTLIERS_COLUMN_KEY = "outliers_Columns"
DROP_COLUMN_KEY = "drop_columns"
SCALING_COLUMN_KEY = " scaling_columns"


# data_transformationrealted variables key
"""here i m going to create the variable realted to all object whatever the object /vars and values
 that we hvae related to data_transformation_config file"""

" jo bhi object create kiye the config.yaml me related to data_transformation_config"

# 46:33 data_transformation 

""""data_transformation_config:   ## first of all we are going to create an object , we can say object Data_transformation_config object anmd under this object these( below) are complete vars and value we have .first of all we are goig to create the multiple directory
  data_transformation_dir : data_transformation
  transformed_dir: transformed_data
  transformed_train_dir : train
  transformed_test_dir : test
  procedding_dir : processed
# after preprocessing complete  data _trnsformation and feature eng what i want ? i want to save the pickel file for tht again i m going to create a vars called preprocessed_object_file_name
  prrprocessed_object_file_name : processed.pkl
  feature_eng_file : feature_eng.pkl


"""

"""DATA_TRANSFORMATION_CONFIG = data_transformation_config 


DATA_TRANSFORMATION_CONFIG ----[  ye variable hua ]

 esi variable ko humlog " config entity " me bolate hai """

# data_transformationrealted variables key
DATA_TRANSFORMATION_CONFIG_KEY = "data_transformation_config"
DATA_TRANSFORMATION= "data_transformation_dir"
DATA_TRANSFORMATION_DIR_NAME_KEY = "transformed_dir"
DATA_TRANSFORMATION_TRAIN_DIR_NAME_KEY = "transformed_train_dir"
DATA_TRANSFORMATION_TEST_DIR_NAME_KEY = "transformed_test_dir"
DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY ="preprocessing_dir"
DATA_TRANSFORMATION_PREPROCESSOR_NAME_KEY ="preprocessed_object_file_name"
DATA_TRANSFORMATION_FEA_ENG_FILE_NAME_KEY = "feature_eng_file" 

# ONE MORE FILE WE ARE GOING TO CREATE  SO THAT WE CAN STORE/COPY FEATURE ENG AND PROCESSED FILE  INTO PREDOICTION FILE 

PICKLE_FOLDER_NAME_KEY = "prediction_file"


#Predicionn file path 
ROOT_DIR=os.getcwd()
CONFIG_DIR='config'
PREDICTION_YAML_FILE  = "prediction.yaml"

#join the complete path 


PREDICTION_YAML_FILE_PATH = os.path.join(ROOT_DIR ,CONFIG_DIR ,PREDICTION_YAML_FILE)