import pandas as pd
import pymongo
import json
# from pymongo.mongo_client import MongoClient

# uri = "mongodb+srv://kumar21:qwerty123456@cluster0.vbh9imy.mongodb.net/?retryWrites=true&w=majority"
client = "mongodb+srv://kumar21:qwerty123456@cluster0.vbh9imy.mongodb.net/?retryWrites=true&w=majority"




DATA_FILE_PATH = (r'D:\BOOTCAMP\2_Price prediction\Project2_ml_price\Data\train.csv')
DATABASE ="machine_learning"
COLLECTION_NAME = "DATASET"

if __name__ =="__main__":
    #read the dataset
    df =pd.read_csv(DATA_FILE_PATH)

    #print shape
    print(f"Rows and Columns of our data: {df.shape}")

    # reset_index
    df.reset_index(drop=True ,inplace =True)

    #Convert the csv to json file (to_json())
    json_record =list(json.loads(df.T.to_json()).values())

    # print first json
    print(json_record[0])

    #we have to insert  our all data into our mongo database 
    #we have mulitple record so in this case we ve to called CLIENT()
    # and here we have to pass our DATABASE and COLLECTION NAME after that we
    # are going to  insert our complete records

    client[DATABASE][COLLECTION_NAME].insert_many(json_record)

    # url[DATABASE][COLLECTION_NAME].insert_many(json_record)
















# # Create a new client and connect to the server
# client = MongoClient(uri)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)