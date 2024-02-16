"""under this folder I m going to create a file with the help of this particular file what we can we can push entire data in our local system """

"""with the help of this file we can push entire data to our local systemm """

#step 1 : neccessary import library 
import pandas as pd 
import os ,sys
import json
import pymongo # our data are available over mongodb ,so with pymngo we can fetch the data to local system  

from dotenv import load_dotenv ## why dotenv ? becox we need to import information from this particular .Env file 


# step 2 : define mongodb client 
def mongdb_client():
    #step3 :we need to define the root directory 
    ROOT_DIR = os.getcwd()
    env_file_path = os.path.join(ROOT_DIR ,".env")

    load_dotenv(dotenv_path = env_file_path)

    username = os.getenv("USER_NAME")
    password = os.getenv("PASS_WORD")
    clsuter_name = os.getenv("CLUSTER_LABEL")
# step
    mongo_db_url =f"mongodb+srv://{username}:{password}@{clsuter_name}.mongodb.net/?retryWrites=true&w=majority"
#23:00 why we need this particular link becassue we can access this complete becoz  
    print(mongo_db_url)
# define the complete client
    client =pymongo.MongoClient(mongo_db_url)

    return client


