"Utility function for RUL package"


import os
import sys
import yaml
import dill
import numpy as np
import pandas as pd
from rul.config import mongo_client
from rul.logger import logging
from rul.exception import RULException


def get_collection_as_dataframe(database_name:str, collection_name:str)->pd.DataFrame:
    """
    Collects a MongoDB database collection and returns a dataframe of it
    ---------------------------------------------------------------------
    input:
    - `database_name`: Name of the database
    - `collection_name`: Name of the collection of the database
    ----------------------------------------------------------------------
    return: Pandas Dataframe of the collection of the database
    """

    try:
        # Reading data from database
        logging.info(f"Converting collection: {collection_name} from MongoDB : {database_name} into Data Frame")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))

        logging.info(f"Dataframe shape: {df.shape}")

        # Dropping the default id column if any
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id")
            df = df.drop("_id", axis=1)

        
        logging.info(f"Dataframe shape: {df.shape}")

        return df
    
    except Exception as e:
        raise RULException(e, sys)
    

def convert_columns_float(df: pd.DataFrame, exclude_columns: list) -> pd.DataFrame:
    """
    Converts columns of given data frame into float
    ------------------------------------------------------------------
    input:
    - `df`: source dataframe to process
    - `exclude_columns`: columns to exclude from the source dataframe
    ------------------------------------------------------------------
    return: `pd.DataFrame`
    """

    try:
        for column in df.columns:
            if column not in exclude_columns:
                df[column] = df[column].astype("float")
        
        return df
    except Exception as e:
        raise RULException(e, sys)