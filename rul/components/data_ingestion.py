"Data Ingestion Component"


import os
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from rul.entity import config_entity
from rul.entity import artifact_entity
from rul.exception import RULException
from rul.logger import logging
from rul import utils


class DataIngestion:
    """
    Data Ingestion Component
    --------------------------------------------------------
    input:
    - `data_ingestion_config`: Data Ingestion Configuration
    --------------------------------------------------------
    return: Data Ingestion Artifact
    """

    def __init__(self, data_ingestion_config: config_entity.DataIngestionConfig) -> None:
        try:
            logging.info("Collecting Data Ingestion Configuration")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise RULException(e, sys)
        
    def initiate_data_ingestion(self)->artifact_entity.DataIngestionArtifact:
        try:
            # Collecting MongoDB collection as dataframe
            logging.info(f"Exporting MongoDB collection to dataframe")
            df: pd.DataFrame = utils.get_collection_as_dataframe(database_name=self.data_ingestion_config.database_name, collection_name=self.data_ingestion_config.collection_name)

            # Replace na with Nan
            logging.info(f"Replacing na values with NAN values")
            df.replace(to_replace="na", value=np.NAN, inplace=True)

            # Creating feature store
            logging.info(f"Creating feature directory if not exist")
            feature_store_dir = os.path.dirname(self.data_ingestion_config.feature_store_file_path)
            os.makedirs(feature_store_dir, exist_ok=True)

            # Saving dataframe as csv to feature store
            logging.info(f"Saving feature to feature directory")
            df.to_csv(path_or_buf=self.data_ingestion_config.feature_store_file_path, index=False, header=True)

            # Creating dataset directory
            logging.info(f"Creating dataset director y if not exist")
            dataset_dir = os.path.dirname(self.data_ingestion_config.train_file_path)

            # Splitting dataset into train and test set
            logging.info(f"Performing Train Test Split")
            train_df, test_df = train_test_split(df, test_size=self.data_ingestion_config.test_size, random_state=42)

            # Save train and test dataframe to dataset directory
            logging.info(f"Saving Train Set to dataset directory")
            train_df.to_csv(path_or_buf=self.data_ingestion_config.train_file_path, index=False, header=True)

            logging.info(f"Saving Test Set to dataset directory")
            test_df.to_csv(path_or_buf=self.data_ingestion_config.test_file_path, index=False, header=True)

            # Prepare artifacts
            logging.info(f"Preparing Data Ingestion Artifacts")
            data_ingestion_artifact = artifact_entity.DataIngestionArtifact(
                feature_store_file_path = self.data_ingestion_config.feature_store_file_path,
                train_file_path = self.data_ingestion_config.train_file_path,
                test_file_path = self.data_ingestion_config.test_file_path
            )

            return data_ingestion_artifact

        except Exception as e:
            raise RULException(e, sys)