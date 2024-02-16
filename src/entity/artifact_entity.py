# coming from config_entity ----->> artifact entity
# Artifact entity -- with the help of artifact entity we can store our output and we can generate and we can store under the artifact directory 



#step 1: import the dataclass
from dataclasses import dataclass

#step2: next we are going to create the class for our DataIngestionArtifact 
@dataclass
class DataIngestionartifact:

    #step3 : In this class we have to define two thing 
    #   1: train_file_path
    #   2: test_file_path 
    # so that wr can store under our directory 
    train_file_path : str   #train_file_path so whatever the data store under train directory those are in the "string format "
    test_file_path :str



    #someway that we can create for data transformation and model trainning