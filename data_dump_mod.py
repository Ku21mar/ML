import pandas as pd
import pymongo
import json
from schema import write_schema_yaml


# Mongodb connection uri 

uri =  "mongodb+srv://Abhishek11:<Abhishek123>@cluster0.t4mqlop.mongodb.net/?retryWrites=true&w=majority"


# I need a data so let me create one of the variable called DATA_FILE_PATH\
##----------------------------- READING THE DATA WITH URL PATH DIRECTLY  _______________________________-0---------_-0----0--0-0-0--0-0-0--0-0-0-0-0-0-0-0-0-0-0-0-
DATA_FILE_PATH = (r'D:\BOOTCAMP\2_Price prediction\Project2_ml_price\Data\train.csv')
DATABASE = "Machine_learning"
COLLECTION_NAME ="DATASET"


if __name__ =="__main__":
    #Read data from the CSV file into a pandas Dataframe 

    df =pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns :{df.shape}")


    #convert the dataframe to a list of dictionary (JSON records)

    json_records = json.loads(df.to_json(orient ="records"))
    print(json_records[0])


    #Estiablish a cinnection  to mongodb

    client =pymongo.MongoClient(uri)

    #Access the desired database and collection 

    db =client[DATABASE]
    collection =db[COLLECTION_NAME]
    
    #Inser the JSON records into the collection 
    collection.insert_many(json_records)

    #close then mongodb colllection 
    client.close()


    
