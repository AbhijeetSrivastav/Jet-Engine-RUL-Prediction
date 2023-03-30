"Configuration for RUL package"


import os
import json
import pymongo
import pandas as pd
from dataclasses import dataclass


@dataclass
class EnvironmentVariable:
    """
    Fetch environment variables from .env file
    """

    mongo_db_url: str = os.getenv("MONGO_DB_URL")



# instance of environment variable
env_var = EnvironmentVariable()

# creating MongoDb client
mongo_client  = pymongo.MongoClient(env_var.mongo_db_url)

# declaring the target column
TARGET_COLUMN = "class"