"Data Transformation Component"

import os
import sys
from typing import Optional
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
from rul.entity import config_entity
from rul.entity import artifact_entity
from rul.config import TARGET_COLUMN
from rul.exception import RULException
from rul.logger import logging
from rul import utils


class DataTransformation:
    """
    Data Transformation Component
    -----------------------------------------------------------------
    input:
    - `data_transformation_config`: Data Transformation Configuration
    - `data_ingestion_artifact`: Data Ingestion Artifact
    -----------------------------------------------------------------
    return: Data Transformation Artifact
    """

    def __init__(self, data_transformation_config: config_entity.DataTransformationConfig, data_ingestion_artifact: artifact_entity.DataIngestionArtifact) -> None:
        try:
            self.data_transformation_config = data_transformation_config

            self.data_ingestion_artifact = data_ingestion_artifact
        
        except Exception as e:
            raise RULException(e, sys)
        
    @classmethod
    def get_data_transformer_object(cls) -> Pipeline:
        """
        Creates a pipeline based on experimentation done during EDA
        -------------------------------------------------------------
        input:
        - 'None`
        -------------------------------------------------------------
        return: `None`
        """

        try:
            simple_imputer = SimpleImputer(strategy="constant", fill_value=0)

            min_max_scaler = MinMaxScaler()

            logging.info(f"Creating transformation object")
            pipeline = Pipeline(steps=[
                ("Imputer", simple_imputer),
                ("Min Max Scaler", min_max_scaler)
            ])

            return pipeline
        
        except Exception as e:
            raise RULException(e, sys)
    
    def add_RUL_feature(df: pd.DataFrame) -> pd.DataFrame:
        """"
        Adds target feature RUL to the dataframe
        ---------------------------------------------
        input:
        -  `df`: dataframe in which to add RUL
        ----------------------------------------------
        return: `pd.Dataframe`
        """

        try:
            train_grouped_by_unit = df.groupby(by='unit_number') 

            max_time_cycles = train_grouped_by_unit['time_cycles'].max() 

            merged = df.merge(max_time_cycles.to_frame(name='max_time_cycle'), left_on='unit_number',right_index=True)

            merged["RUL"] = merged["max_time_cycle"] - merged['time_cycles']

            merged = merged.drop("max_time_cycle", axis=1) 

            return merged
        
        except Exception as e:
            raise RULException(e, sys)

    def initiate_data_transformation(self) -> artifact_entity.DataTransformationArtifact:
        """
        Initiates Data Transformation Component
        ----------------------------------------------
        input:
        - `None`
        -----------------------------------------------
        return: Data Transformation Artifact
        """

        # Reading train file
        logging.info(f"Reading train file")
        train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)

        # Reading test file 
        logging.info(f"Reading test file")
        test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

        # Adding RUL feature to train and test dataFrame
