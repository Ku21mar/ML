# Reading the data with the help of modular code 
#now wea re going to modify in data_dump file ( here i m creating another file for data_dump_modfication so that we can understand the difference bewteen data_dump and data_dump_modification file )
## import necessary library 
import os ,sys
import pandas as pd
import pymongo
import json
# from pymongo.mongo_client import MongoClient
from schema import write_schema_yaml


## MONGODB CONNECTION  URI 
## mongodb :: amii6363t@gmail.com
# uri = "mongodb+srv://kumar21:qwerty123456@cluster0.vbh9imy.mongodb.net/?retryWrites=true&w=majority"
uri =  "mongodb+srv://Abhishek11:<Abhishek123>@cluster0.t4mqlop.mongodb.net/?retryWrites=true&w=majority"


# I need a data so let me create one of the variable called DATA_FILE_PATH\
##----------------------------- READING THE DATA WITH URL PATH DIRECTLY  _______________________________-0---------_-0----0--0-0-0--0-0-0--0-0-0-0-0-0-0-0-0-0-0-0-
DATA_FILE_PATH = (r'D:\BOOTCAMP\2_Price prediction\Project2_ml_price\Data\train.csv')

#STEP 2  : Now we need to create the DataBase name  as well as  Connection Name ( AAP kuch bhi naam de skte ho database and coonection name ka it is totaly upto us)
DATABASE ="Machine_Learning"
COLLECTION_NAME = "DATASET"

#------------------------------------------------------------------------------------------------------------
#AUR WE CAN USE THE MODULAR CODING TO READ THE DATA FROM TRAIN .CSV

if __name__ == "__main__":  #entry point 
    # step : first of all call the current working directory 
    ROOT_DIR =os.getcwd()


    DATA_FILE_PATH =  os.path.join(ROOT_DIR ,"Data" ,"train.csv")  
    FILE_PATH = os.path.join(ROOT_DIR , DATA_FILE_PATH)

    write_schema_yaml(csv_file = DATA_FILE_PATH)
     #Now read the dataset first 
    df =pd.read_csv(DATA_FILE_PATH)

    #print shape
    print(f"Rows and Columns of our data: {df.shape}")

    json_records = json.loads(df.to_json(orient ="records"))
    print(json_records[0])
    # orient that i m going to define our complete records

# next  we  arre goint to call oour MongoDB clients
    # Establish a connection to MongoDB
    client = pymongo.MongoClient(uri) 
    db =client[DATABASE]
    collection =db[COLLECTION_NAME]


    #Insert the JSOn records inti the collection 
    collection.insert_many(json_records)

    # close the MOngoDb connection 
    client.close()













    # reset_index( must done )
    df.reset_index(drop=True ,inplace =True)
    #______N___O___T___E__________
## STEP 4   : whenever we are going to upload the data over mongodb Atlas we need to upload data in KEY & VALUE pair .we can say in a json format ::::

    # df.T (data transpose) --> df.T.to_json().values() --> and apart from that we can covert that into complete list .so list of 
    # json dot load. so we are goiing  to "loads"  our entire data


#STEP 5    #Convert the csv to json file (to_json()) for that we define json_record variable
    # df.T.to_json()
    json_record =list(json.loads(df.T.to_json()).values())

    # I am going to print first json record 
    print(json_record[0])

    #After that we have to insert  our all data whaetever the data we hve  into our mongo database 
    #we have mulitple record so in this case we ve to called CLIENT()
    # and here we have to pass our DATABASE NAME  and COLLECTION NAME after that we
    # are going to  insert our "complete records"

    client[DATABASE][COLLECTION_NAME].insert_many([json_record])

    #insert the complete data 


