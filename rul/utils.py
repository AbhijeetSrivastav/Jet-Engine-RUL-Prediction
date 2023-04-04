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
    

def write_yaml_file(file_path: str, data: dict) -> None:
    """
    Writes any data to yaml format
    ----------------------------------------------------
    input:
    - `file_path`: output file name
    - `data`: dictionary to be wrote as yaml
    -----------------------------------------------------
    return: `None`
    """

    try:
        # Making directory to store YAML file
        file_dir = os.path.dirname(file_path)
        os.makedirs(file_dir, exist_ok=True)

        # Write YAML file
        with open(file_path, "w") as file:
            yaml.dump(data, file)
    except Exception as e:
        raise RULException(e, sys)


def save_object(file_path: str, obj: object) -> None:
    """
    Save given object to specified location
    --------------------------------------------------------
    input:
    -  `file_path`: path where to save object
    - `obj`: object to save
    ---------------------------------------------------------
    return: `None`
    """

    try:
        # Making directory to store object file
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Save object file
        logging.info(f"Saving the object file")
        with open(file_path, "wb") as obj_file:
            dill.dump(obj, obj_file)
    
    except Exception as e:
        raise RULException(e, sys)
    

def load_object(file_path: str) -> object:
    """
    Load specified object
    --------------------------------------------------
    input:
    - `file_path`: path where object is
    --------------------------------------------------
    return: `None`
    """

    try:
        # Checking if file path exist or not
        if not os.path.exists(file_path):
            raise Exception("File path: {file_path} doesn't exist")
        
        # Load object file
        logging.info(f"Loading object file")
        with open(file_path, "rb") as obj_file:
            return dill.load(obj_file)
    
    except Exception as e:
        raise RULException(e, sys)
        
