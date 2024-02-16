# schema.yaml - here we define the complete data ( data name , data column name , data types)


import yaml
import os, sys
import pandas as pd

def write_schema_yaml(csv_file):
    # read the data 
    df =pd.read_csv(csv_file)
    # check numcerical column\
    num_cols = len(df.columns)
    #column name
    columns_names  =df.columns.tolist()
    #data typpes
     # whatever the data we have ad we have to convert into string format
    columns_dtypes =df.dtypes.astype(str).tolist()  ## becoz like  whatever the data we are going to store
    #so all the datatype we are going to convert  into string but later part we will do the modification 
    #(not here we are going to do in shcema.yaml)

     # after that I m going to define the  complete schema .
     # we are going to define in dictionary format 


# Creating the Schema Dictionary
    schema = {
        "Filename" : os.path.basename(csv_file),
        "NumberofColumns" : num_cols,
        "Columnname" : dict(zip(columns_names ,columns_dtypes))
     }  # with the help of this variable we are going to findout the dataset name .Here dataset name is TRAIN.CSV

     # Next wee need the
     #  number of columns
     # columnname :

     # Next we are going to write the schema to schema.yaml >so wahtever the schema that we are able to create here now we
     # are goint to write into the YAML FORMAT (34:15)
     # fiirst the current working dir
    ROOT_DIR  =os.getcwd()
    # join the complete path 
    SCHEMA_PATH = os.path.join(ROOT_DIR ,"config" , "schema.yaml") # with the help of ROOT DIR we will get the complete working directory From our working directory we are going to findout config folder and then from config folder we are going to findout the schema.yaml file .
    #and then we can store our complete scheme information under the this particular file 

    with open(SCHEMA_PATH, "w") as file:
     
     
     yaml.dump(schema,file)  # yaml.dump becoz we are going to dump complete data into the yaml format.
     # first parameter is "schema" and second is "file" 
