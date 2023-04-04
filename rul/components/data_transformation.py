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

        try:
            # Reading train file
            logging.info(f"Reading train file")
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)

            # Reading test file 
            logging.info(f"Reading test file")
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            # Adding RUL feature to train dataFrame
            logging.info(f"Adding RUL to train dataFrame")
            train_df = self.add_RUL_feature(train_df)
            
            # Adding RUL feature to test dataFrame
            logging.info(f"Adding RUL to test dataFrame")
            test_df = self.add_RUL_feature(test_df)

            # Defining irrelevant features aka: index, setting and constant sensor 
            logging.info(f"Proceeding to drop irrelevant index, setting and constant sensor features")
            index_names = ["unit_number", "time_cycles"]
            setting_names = ["setting_1", "setting_2", "setting_3"]
            constant_sensors = ["s_1", "s_5",'s_6', "s_10", "s_16", "s_18", "s_19"]

            drop_labels = index_names + setting_names + constant_sensors

            # Dropping irrelevant features from train dataFrame
            logging.info(f"Dropping irrelevant features from train dataFrame")
            train_df.drop(columns=drop_labels, inplace=True)
            
            # Dropping irrelevant features from test dataFrame
            logging.info(f"Dropping irrelevant features from test dataFrame")
            test_df.drop(columns=drop_labels, inplace=True) 

            # Fetching and Fitting transformation pipeline
            logging.info(f"Fetching transformation object, creating and fitting transformation pipeline")
            transformation_pipeline = DataTransformation.get_data_transformer_object()
            transformation_pipeline.fit(train_df)

            # Transforming train dataFrame
            logging.info(f"Transforming train dataFrame")
            train_arr = transformation_pipeline.transform(train_df)

            # Transforming train dataFrame
            logging.info(f"Transforming test dataFrame")
            test_arr = transformation_pipeline.transform(test_df)

            # Saving train array as artifact
            logging.info(f"Saving train array as artifact")
            utils.save_numpy_array_data(file_path=self.data_transformation_config.data_transformed_train_path, array=train_arr)

            # Saving test array as artifact
            logging.info(f"Saving test array as artifact")
            utils.save_numpy_array_data(file_path=self.data_transformation_config.data_transformed_test_path, array=test_arr)

            # Saving transformer object
            utils.save_object(file_path=self.data_transformation_config.data_transformer_object_path, obj=transformation_pipeline)

            # Preparing artifact
            logging.info(f"Preparing Data Transformation Artifact")
            data_transformation_artifact = artifact_entity.DataTransformationArtifact(
                                                                        transformer_object_path=self.data_transformation_config.data_transformer_object_path,
                                                                        transformed_train_path=self.data_transformation_config.data_transformed_train_path,
                                                                        transformed_test_path=self.data_transformation_config.data_transformed_test_path
                                                                        )
            
            return data_transformation_artifact

        except Exception as e:
            raise RULException(e, sys)