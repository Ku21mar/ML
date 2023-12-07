## import necessary library 
import pandas as pd
import pymongo
import json
# from pymongo.mongo_client import MongoClient




uri =  "mongodb+srv://Abhishek11:Abhishek123@cluster0.t4mqlop.mongodb.net/?retryWrites=true&w=majority"


# I need a data so let me create one of the variable called DATA_FILE_PATH
DATA_FILE_PATH = r'D:\BOOTCAMP\2_Price prediction\Project2_ml_price\Data\train.csv'

#STEP 2  : Now we need to create the DataBase name  as well as  Connection Name ( AAP kuch bhi naam de skte ho database and coonection name ka it is totaly upto us)
DATABASE ="machine_learning"
COLLECTION_NAME = "DATASET"

# STEP 3:  Now I m going the define next Entry Point 

if __name__ =="__main__":
    #Now read the dataset first 
    df =pd.read_csv(DATA_FILE_PATH)

    #print shape
    print(f"Rows and Columns : {df.shape}")

    # reset_index( must done )
    # df.reset_index(drop=True ,inplace =True)
    #______N___O___T___E__________
## STEP 4   : whenever we are going to upload the data over mongodb Atlas we need to upload data in KEY & VALUE pair .we can say in a json format ::::

    # df.T (data transpose) --> df.T.to_json().values() --> and apart from that we can covert that into complete list .so list of 
    # json dot load. so we are goiing  to "loads"  our entire data


#STEP 5    #Convert the csv to json file (to_json()) for that we define json_record variable
    # df.T.to_json()
    # json_record =list(json.loads(df.T.to_json()).values())

    # # I am going to print first json record 
    # print(json_record[0])

    json_records = json.loads(df.to_json(orient ="records"))
    print(json_records[0])
    # orient that i m going to define our complete records

# next  we  arre goint to call oour MongoDB clients
    # Establish a connection to MongoDB
    client = pymongo.MongoClient(uri) # here we ve created a variabke to establish connection our MongoDb cooncetion 

# now we r going to call this CLIENT  variable here to create our databsase name :: client[DATABASE] and under this db we r going to create our  collection name 
    
    
    # Access the desired databased and collection
## firdt e are going to set out mongodb creditnail
    # under this creditnal ((client = pymongo.MongoClient(uri))) under this databased(db)
    db =client[DATABASE]
    collection =db[COLLECTION_NAME]


    #Insert the JSOn records inti the collection 
    collection.insert_many(json_records)

    # close the MOngoDb connection 
    client.close()

## INSER_MANY- means we are going to insert many records ( here we are going to insert json records )



#first we are going to set our complete MongoDb url creditnal after that under this particukar creditidnal we are going to create database and then we are going to create a collection name
# 
# client = pymongo.MongoClient(uri) 

    # Access the desired databased and collection
    # db =client[DATABASE]
    # collection =db[COLLECTION_NAME] 





    ##########__________________________________________________###################3
    """after uloafding complete dta so in thie wat like in a company what you will get a ata so ur client told u
    our data are avialable over mongodb.first of all u need to fect hte entire data in ur local system 
    and then you can perform a complete pipeline operation 
    data injection .data transformation etect like whatever the pipeline we can impleiment 
    each and everything 
    1 --  Fetch the entire data into our local system 
    
    
    Now we are going to go fect thre entire data from mongoDB into our local system """

## NEXT STEEEPppppppp

    """_____________NOtE____________"""

    """jo hmare creditinal wo data_dump1 file me ha.let say if i m pushing this file over the gitub so any member they can access my complete creditinal
    where this particular(url) link"""

    """ Now I m going to do I m going to create the  dot(.env) env file and in this particular env file first of all i will create a 3 variable 
    __ Username 
    __password
    __clusterlevel"""

    """based upon this on i ill put it down our comlete creditinal information under this .env file 
     __ Username = 
    __password= 
    __clusterlevel = 
    now i m goint o push this partivaular data over github in thhus case that wr can add this partiaular do env file under the our .gitignore folder so that whenever
    wheb we can push that over github this partcular 
    data it will get ignore this particaular file mainly"""