"Script to dump CSV dataset into MongoDB database"


import pymongo
import pandas as pd
import numpy as np
import json 
import os
from dotenv import load_dotenv


# Load .env file
load_dotenv()


DATA_FILE_PATH = "./CMaps/train_FD001.txt"
DATABASE_NAME = "rul"
COLLECTION_NAME = "rul_collect"
MongoDB_Password = os.environ.get("MONGODB_KEY")


if __name__ == "__main__":
    
    # Connecting to MongoDB client
    client = pymongo.MongoClient(f"mongodb+srv://abhijeetsrivastav292:{MongoDB_Password}@cluster0.wbjve5i.mongodb.net/?retryWrites=true&w=majority")

     # Reading the txt Dataset with specified rows and columns
    index_names = ["unit_number", "time_cycles"]
    setting_names = ["setting_1", "setting_2", "setting_3"]
    sensor_names = ["s_{}".format(i+1) for i in range(0, 21)]
    col_names = index_names + setting_names + sensor_names

    df = pd.read_csv(DATA_FILE_PATH, sep='\s+', header=None, index_col=False, names=col_names)
    print(f"Rows: {df.shape[0]} Columns: {df.shape[1]}")

    # Dropping the default index of the data frame
    df.reset_index(drop=True, inplace=True)

    # Convert data frame to json 
    json_record = list(json.loads(df.T.to_json()).values())

    # Dump the json record to MongoDB database
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)