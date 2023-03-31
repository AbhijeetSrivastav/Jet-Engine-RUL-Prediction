"Training Pipeline"


import sys
import os
from rul.logger import logging
from rul.exception import RULException
from rul.entity import config_entity
from rul.components.data_ingestion import DataIngestion



def start_training_pipeline():
    try:
        # Import training pipeline configuration
        logging.info(f"Loading Training Pipeline COnfiguration")
        training_pipeline_config = config_entity.TrainingPipelineConfig()

        # Data Ingestion
        logging.info(f"-----------------Initiating Data Ingestion-----------------")
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config = training_pipeline_config)

        data_ingestion = DataIngestion(data_ingestion_config = data_ingestion_config)

        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

    except Exception as e:
        raise RULException(e, sys)