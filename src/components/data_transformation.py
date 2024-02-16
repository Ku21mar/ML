import os 
import sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from src.entity.artifact_entity import *
from src.entity.config_entity import *
from src.constant import *
from src.utils import read_yaml_file,create_yaml_file_numerical_columns,create_yaml_file_categorical_columns_from_dataframe, save_numpy_array_data, save_object
from src.constant import *
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
import re
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer


# Before writing the code under our" feature engineering" that we need to 
# define some of the variable related to schema file where we need to
#  read our schema information 


# class Feature_engineering:
#     pass
#     #1 handling ,issing data
#     #2 drop columns
#     #3 above 70% drop nan columns
#     #4 trim outliers
#     #5 remove outliers
#     #6 handling categorical data 
#     #7 transform our data 
#     #8 handle dataetime data handling 
#     #9 imbalanced data handling 
    




# class DataPrecessor:
#     pass


# class DataTransformation:
#     pass


# # Data transfomation file path  (CONSTANT INIT) 
# TARGET_COLUMN_KEY =  "target_column"
# NUMERICAL_COLUMN_KEY ="numerical_columns"
# CATEGORICAL_COLUMN_KEY = "categorical_columns"
# OUTLIERS_COLUMN_KEY = "outliers_Columns"
# DROP_COLUMN_KEY = "drop_columns"
# SCALING_COLUMN_KEY = " scaling_columns"



# Reading data in Transformation Schema 
# transformation_yaml = read_yaml_file(file_path=TRANFORMATION_YAML_FILE_PATH)

# # Column data accessed from Schema.yaml
# target_column = transformation_yaml[TARGET_COLUMN_KEY]
# numerical_columns = transformation_yaml[NUMERICAL_COLUMN_KEY] 
# categorical_columns=transformation_yaml[CATEGORICAL_COLUMN_KEY]
# drop_columns=transformation_yaml[DROP_COLUMN_KEY]

# # Transformation 
# outlier_columns=transformation_yaml[OUTLIERS_COLUMN_KEY]
# scaling_columns=transformation_yaml[SCALING_COLUMN_KEY]

# Beforre writing code under the featute engineering we need to define some the variable 
# some of the variable related to schema file where we need to read our schema information
#becoz lets us the operation we arre going to perform like the FEATURE ENGINEERINg
# To perforem feature engineering we need data , based on the data we can perform 
# a complete feature engineering step\


"""So  all the data avialable information are avialable under our CONFIG Folder
Where we have config.yaml  , scheam.yaml and transformation.yaml 
"""

"""so what are going to do first of all  we are going to read our transforamtion.yaml file so fir these one we need one helper function (READ_YAML_FILE)"""
#  Step 1----- : Reading data in Transformation Schema 
transformation_yaml = read_yaml_file(file_path=TRANFORMATION_YAML_FILE_PATH)

# step 2 : Next we are going to Access our target column ,num col and categorical col and drop col( from where ?) from our tranformation.yaml file 
# Column data accessed from Schema.yaml

#  inforamtion access from transforamton.yaml to data_transforamtion.py
target_column = transformation_yaml[TARGET_COLUMN_KEY]
numerical_columns = transformation_yaml[NUMERICAL_COLUMN_KEY] 
categorical_columns=transformation_yaml[CATEGORICAL_COLUMN_KEY]
drop_columns=transformation_yaml[DROP_COLUMN_KEY]

# Transformation 
outlier_columns=transformation_yaml[OUTLIERS_COLUMN_KEY]
scaling_columns=transformation_yaml[SCALING_COLUMN_KEY]


class Feature_Engineering(BaseEstimator, TransformerMixin):
    
    def __inti__(self):
        logging.info("**********Feature Engineering started ************")


    def drop_columns(self,X:pd.DataFrame):
        columns_to_Drop = drop_columns
        X.drop(columns =columns_to_Drop,axis=1,inplace =True)
        logging.info(f"Droping columns:{columns_to_Drop}")
        return X

    def replace_space_with_underscore(self,df):
        df = df.rename(columns = lambda x:x.replace(" ", "_"))
        return df


      #--------Numcerical feature only----------  

    def replace_nan_with_random(self, df,column_label):
        if column_label not in df.columns:
            print(f"Columns :{column_label} not found in the Dataframe ")
            return df
        
    # copy our complete data 
        original_data =df[column_label].copy()
        #after that we are goijg to find out the null value and based on null value we are going to find out the index value 

        nan_indicas = df[df[column_label].isna()].index
    
    # now we are going to find out numcrical nan value 
        num_nan = len(nan_indicas) # check the length of null values 
    # define our existing data here we can call our original data 
        existing_values = original_data.dropna().values 
    # after that wr are going to create new variable call random_values
        random_values = np.random.choice(existing_values , num_nan)  # calling our existinf value and then we are calling numerical nan value 


    # find out the mean and median for original data 
        # we ill also find out the mean and median for new data as well( num_nan)
         
        original_mean = original_data.mean()

        original_median  = original_data.median()
        new_mean = df[column_label].mean()
        new_median =df[column_label].median()


        return df
    
# whatever the nae we have we are goinf to replace nan with random values

#--------------- categorical columns----------------------
    def drop_rows_with_nan(self ,X:pd.DataFrame,column_label:str):

        X = X.dropna(subset=[column_label])
        X =X.reset_index(drop =True)

        return X
    
    
# handling the outlier using quantile
    def trim_outlier_by_quantile(self,df,column_label, upper_quantile =0.95 , lower_quantile =0.5):
        if column_label not in df.columns:
            print(f"Column:{column_label} not found in the dataFrame ")

            return df
        
        columns_data = df[column_label]
        lower_bound = columns_data.quantile(lower_quantile)
        upper_bound = columns_data.quantile(upper_quantile)


        trimmed_data = columns_data.clip(lower =lower_bound , upper =upper_bound)
       # call column label
        df[column_label]= trimmed_data

        return df 
    
    
# Now we are going to create the next function and next function  
    # after the triming that we can create a function  to remove the outlier 

    def removing_outlier(self, X):
        for column in outlier_columns:
            X =self.trim_outlier_by_quantile(df=X,column_label=column)
            
        return X


    def run_data_modification(self, data):
        X=data.copy() # copy original data 

        X= self.replace_space_with_underscore(X)

        try:
            X = self.drop_columns(X)
        except Exception as e:
            print("Error dropping columns")

#next we ill define the for lopp ans in for loop that we can define our columns so "ABC" OR 'XYZ' columns
        #that we are going to replaces.


        for column in [ "Artist_Reputation" ,"Height","Width"]:  
            X =self.replace_nan_with_random(X,column_label = column)       

        logging.info("DRooping rows with nan")
        for column in  ["Weight", 'Material',"remote_Location"]:
            X =self.drop_rows_with_nan(X,column_label =column)


        X = self.removing_outlier(X)


# define a function to peform data wrangling 
    def data_wrangling(self,X): # es function ke help se we can call our run_data_modification function 
            
            try:
                data_modified =self.run_data_modification(data =X)
                return data_modified
            except Exception as e:
                raise CustomException(e,sys) from e       
#with the help of these above function that we are going to modified our complete data 
         
# --------------------------------fit and transform--------------------------------------------
# after that next function that we r going to define to fit our data

    def fit(self ,X ,y=None):
        
        return self


# Next we are going to apply data transformation 
    def transform(self,X:pd.DataFrame, y=None): #here we are going too call data_wrangling  under this transform function becoz
#now weare able to do modification till herE( data_wrangling) 
            try:
                data_modified = self.data_wrangling(X)

                logging.info("Data Wrangling completed")
                return data_modified
            

            except Exception as e:
                raise CustomException(e,sys) from e    


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#with the help of these all function we are able to do a complete feature elengineering 
            # drop columns
            # replace space woith underscire 
            #replace nan with random
            # drop row with nan
            # trim outlier by quantile 
            #remove the outlier
            # apply the complete run the data modificatiion
            # functioin to do complete data arangling 
            # fit and transform 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
trf1 =ColumnTransformer([
    ("impute_age",SimpleImputer(),[2]),
    ("impute_embarked",SimpleImputer(strategy = "most_frequent"),[6])
], remainder = 'passthrough')

# pipeline (list of tuple we have to passs and har tuple me do chije hogi first us particular tranformer ka naam and uska object ))
pipe = Pipeline([
    ('trf1', trf1),
    ("trf2", trf2),
    ('trf3',trf3),
    ('trf4' ,trf4),
    ('trf5',trf5)
])
"""


class DataPrecessor:
    def __init__(self,numerical_cols, categorical_cols):
        self.numerical_cols = numerical_cols
        self.categorical_cols = categorical_cols



        categorical_transfomer =Pipeline(

            steps =[
                ('ohe', OneHotEncoder(handle_unknown ='ignore'))
            ]
        )

        numerical_transformer = Pipeline(
            steps= [
                ('log_transoform',FunctionTransformer(np.log1p, validate =False))
            ]
        )


# create a columnTransformer to appplly the transformation
        self.preprocessor=ColumnTransformer(
            transfomer=[
                ('cat', categorical_transfomer,self.categorical_cols),
                ("num", numerical_transformer, self.numerical_cols)
            ], remainder="passthrough"
        )

    def get_preprecessors(self):
        return self.preprocessor
    

#next we are going to define Fit_transform , apply fit_transofm on data 
    

    def fit_transform(self, data):
        transformed_data =self.preprocessor.fit_transform(data)

        return transformed_data
    
class DataTransformation:


# Def init (self,  data transformation config:we are going to call DataTransformationConfig 
# now second we are going to call our previous output so prviouse outiput that we have data_ingestion _config and DataIngestionConfig call
    def __init__(self,data_transforamtion_config:DataTransformationConfig,
                 data_ingestion_artifact : DataIngestionartifact):
        try:
            # we are going to call one by one data _transformation_config and data_ingestion_config 
            self.data_transforamtion_config= data_transforamtion_config
            self.data_ingestion_artifact= data_ingestion_artifact
            # our previous data_ingestion_config because whahtever the operation that we are going to perform data transformation operation  
            #we need to perform over oiur previous data that we need our data ingestion 

        except Exception as e:
            raise CustomException(e,sys) from e
        

    def get_feature_engineering_object(self):
        try:
            feature_engineering =Pipeline(
                    steps =[("fe",feature_engineering())])
                    
            return feature_engineering
              

        except Exception as e:
            raise CustomException(e,sys) from e
            

    def separate_numerical_categorical_columns(self,df):
        numerical_columns = []
        categorical_columns = []

        for column in df.columns:
            if df[column].dtype =='int64' or df[column].dtype =='float64':
                numerical_columns.append(column)

            else:
                categorical_columns.append(column)

        return numerical_columns , categorical_columns


    def inititate_data_transformation(self):
        try:
            # data validation Artifact ---> accessing train and test files

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path =self.data_ingestion_artifact.test_file_path 

            #Read the data to convert into dataframe

            train_df =pd.read_csv(train_file_path)
            test_df =pd.read_csv(test_file_path)
            


            logging.info(f"Target Columns: {target_column}")
            logging.info(f"Numerical Column: {numerical_columns}")
            logging.info(f"Categroical Column : {categorical_columns}")

            # all columns  (add the complete data [num + cat+ target])

            col = numerical_columns + categorical_columns + target_column

            logging.info("Allcolumns:{}".format(col))

            # Apply the Feature Engineering function 

            logging.info(f'Obtaining feature engineering object.')
            fe_obj =self.get_feature_engineering_object()

            #applying feature enginerring object on trainning dataframe

            train_df =fe_obj.fit_transform(X=train_df)

            test_df =fe_obj.transform(test_df)

            # Train data
            #Feature Engineering of train and test Completed
            feature_eng_train_df:pd.DataFrame =train_df.copy()

            logging.info(f" Columns in feature enginering Train {feature_eng_train_df.columns}")
            logging.info(f"Feature Engineering - Train Completed")          

            # Test Data
            feature_eng_test_df:pd.DataFrame = test_df.copy()
           # feature_eng_test_df.to_csv("feature_eng_test_df.csv")
            logging.info(f" Columns in feature enginering test {feature_eng_test_df.columns}")
            logging.info(f"Saving feature engineered training and testing dataframe.")
            
            # Getting numerical and categorical of Transformed data 

            input_feature_train_df = feature_eng_test_df.drop(columns = target_column ,axis =1)

            train_target = feature_eng_test_df[target_column]

            input_feature_test_df = feature_eng_test_df.drop(columns =target_column ,axis =1)

            test_target = feature_eng_test_df[target_column]

        
                                    ############ Input Fatures transformation########
            ### Preprocessing 
            logging.info("*" * 20 + " Applying preprocessing object on training dataframe and testing dataframe " + "*" * 20)
            
            logging.info(f" Scaling Columns : {scaling_columns}")
        
            # Transforming Data 
            numerical_cols,categorical_cols=self.separate_numerical_categorical_columns(df=input_feature_train_df)
            
            # Saving column labels for prediction
            create_yaml_file_numerical_columns(column_list=numerical_cols,
                                               yaml_file_path=PREDICTION_YAML_FILE_PATH)  ## PREDICTION_YAML_FILE_PATH --constant file 
            
            create_yaml_file_categorical_columns_from_dataframe(dataframe=input_feature_train_df,categorical_columns=categorical_cols,
                                                                yaml_file_path=PREDICTION_YAML_FILE_PATH)
            
            logging.info(f"Transformed data numerical columns :{numerical_cols}")
            logging.info(f"Transformed data categorical columns: {categorical_cols}")

  # with the help of these function we can save our data numerical data into numerical yaml and cateroical data into categroical yaml
            # so that this particular information  we can use whenerver we want to build the web application during the prediction    



        except Exception as e:
            raise CustomException(e, sys) from e
        

        # 20:12

        #now we are going to perform a next step 
        # we can save our complete column our cateroficla colum for input  train feature as well as input  test feature andthen we can apply data preprocessing class
        # and after that we can call our target column s

#________________________________________________________________

#  Next we are going to setting our complete column in order ( what we can do nnext ?)
        
# first we  are going to call numerical column as well as our categroical columns
        # then we can define input feature for train and input feature for test 


        column_order  = numerical_columns + categorical_columns

# now we are going to create two variable one for input feature for train data and one for inout feature for test data
        

        input_feature_train_df =
        input_feature_test_df