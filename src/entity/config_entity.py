import os,sys
from src.exception import CustomException

from src.logger import logging 
from datetime import datetime 
from src.constant import *

from src.utils import read_yaml_file

#
config_data =read_yaml_file(CONFIG_FILE_PATH)  ## ---------

class TrainingPipelineConfig:
    def __init__(self):

        try:
            self.artifact_dir =os.path.join(os.getcwd(),"artifact" ,f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}")

        except Exception as e:
            raise CustomException(e,sys)
        

class DataIngestionConfig:
    def __init__(self,training_pipeline_config : TrainingPipelineConfig):
        try:
            data_ingestion_key = config_data[DATA_INGESTION_CONFIG_KEY]  # becasuse with the helop of thisvariable   we are goint to read complete information from constant file

#artifact / data_ingestion/ raw_data & ingested_data / train & test
# data_ingestion_config:
#   data_base : Machine_Learning 
#   collection_name: DATASET
#   data_ingestion: data_ingestion
#   raw_data_dir: raw_data
#   ingested_dir: ingested_data
# ingested_train_dir : Train 
# ingested_test_dir :Test 
            # next waht we can do -- we can CREATE a collection and database 
            self.database_name = data_ingestion_key[DATA_INGESTION_DATABASE_NAME]
            self.collecion_name = data_ingestion_key[DATA_INGESTION_COLLECTION_NAME]
            #next we r going to define directory for what? 
            # for data ingestion dir / raw data / ingested data /train data/test data
            self.data_ingestion_dir =os.path.join(training_pipeline_config.artifact_dir,data_ingestion_key[DATA_INGESTION_ARTIFACT_DIR])
            self.raw_data_dir =os.path.join(self.data_ingestion_dir ,data_ingestion_key[DATA_INGESTION_RAW_DATA_DIR_KEY])

            self.ingested_data_dir =os.path.join(self.raw_data_dir,data_ingestion_key[DATA_INGESTION_INGESTED_DIR_KEY])

            self.train_file_path =os.path.join(self.ingested_data_dir,data_ingestion_key[DATA_INGESTION_TRAIN_DIR_KEY])
            self.test_file_path =os.path.join(self.ingested_data_dir,data_ingestion_key[DATA_INGESTION_TEST_DIR_KEY])

            self.test_size =0.2
            #12700x
            #12700x
        except Exception as e:
            raise CustomException(e,sys) 




# data _transformation_config  :::calling from config.ymal file into this config,.entity
   
"""data_transformation_config:   
  data_transformation_dir : data_transformation
  transformed_dir: transformed_data
  transformed_train_dir : train
  transformed_test_dir : test
  procedding_dir : processed

  prrprocessed_object_file_name : processed.pkl
  feature_eng_file : feature_eng.pkl
"""

# DATA_TRANSFORMATION_CONFIG = "data_transformation_config"
# DATA_TRANSFORMATION= "data_transformation_dir"
# DATA_TRANSFORMATION_DIR_NAME_KEY = "transformed_dir"
# DATA_TRANSFORMATION_TRAIN_DIR_KEY = "transformed_train_dir"
# DATA_TRANSFORMATION_TEST_DIR_KEY = "transformed_test_dir"
# DATA_TRANSFORMATION_PRECESSING_DIR_KEY ="procedding_dir"
# DATA_TRANSFORMATION_PRECESSED_DIR_KEY ="preprocessed_object_file_name"
# DATA_TRANSFORMATION_FEGG_ENG_FILE_KEY = "feature_eng_file" 

# ONE MORE FILE WE ARE GOING TO CREATE  SO THAT WE CAN STORE/COPY FEATURE ENG AND PROCESSED FILE  INTO PREDOICTION FILE 



"""DATA_TRANSFORMATION_CONFIG = data_transformation_config 
DATA_TRANSFORMATION_CONFIG ---- ye variable hua
 esi variable ko humlog xonfig entity me bolate hai """


class DataTransformationConfig:
    
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        
        
        data_transformation_key=config_data[DATA_TRANSFORMATION_CONFIG_KEY]
        
# artifact/data_transformation/transformed_data ( train and test ) & preprocessed ( preprocessed.pkl & fea_eng.pkl)

        self.data_transformation_dir = os.path.join(training_pipeline_config.artifact_dir , data_transformation_key[DATA_TRANSFORMATION])
        self.transformation_dir = os.path.join(self.data_transformation_dir,data_transformation_key[DATA_TRANSFORMATION_DIR_NAME_KEY])
        self.transformed_train_dir = os.path.join(self.transformation_dir,data_transformation_key[DATA_TRANSFORMATION_TRAIN_DIR_NAME_KEY])
        self.transformed_test_dir = os.path.join(self.transformation_dir,data_transformation_key[DATA_TRANSFORMATION_TEST_DIR_NAME_KEY])
        self.preprocessed_dir = os.path.join(self.data_transformation_dir,data_transformation_key[DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY])
        self.feature_engineering_object_file_path =os.path.join(self.preprocessed_dir,data_transformation_key[DATA_TRANSFORMATION_FEA_ENG_FILE_NAME_KEY])
        self.preprocessor_file_object_file_path=os.path.join(self.preprocessed_dir,data_transformation_key[DATA_TRANSFORMATION_PREPROCESSOR_NAME_KEY])




