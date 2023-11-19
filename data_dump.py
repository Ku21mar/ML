
## import necessary library 
import pandas as pd
import pymongo
import json
# from pymongo.mongo_client import MongoClient



# uri = "mongodb+srv://kumar21:qwerty123456@cluster0.vbh9imy.mongodb.net/?retryWrites=true&w=majority"
client =  "mongodb+srv://Abhishek11:<Abhishek123>@cluster0.t4mqlop.mongodb.net/?retryWrites=true&w=majority"


# I need a data so let me create one of the variable called DATA_FILE_PATH
DATA_FILE_PATH = (r'D:\BOOTCAMP\2_Price prediction\Project2_ml_price\Data\train.csv')

#STEP 2  : Now we need to create the DataBase name  as well as  Connection Name ( AAP kuch bhi naam de skte ho database and coonection name ka it is totaly upto us)
DATABASE ="machine_learning"
COLLECTION_NAME = "DATASET"

# STEP 3:  Now I m going the define next Entry Point 

if __name__ =="__main__":
    #Now read the dataset first 
    df =pd.read_csv(DATA_FILE_PATH)

    #print shape
    print(f"Rows and Columns of our data: {df.shape}")

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

    # url[DATABASE][COLLECTION_NAME].insert_many(json_record)

## INSER_MANY- means we are going to insert many records ( here we are going to insert json records )














# # Create a new client and connect to the server
# client = MongoClient(uri)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)