"Training Pipeline"


import sys
import os
from rul.logger import logging
from rul.exception import RULException
from rul.entity import config_entity
from rul.components.data_ingestion import DataIngestion
from rul.components.data_validation import DataValidation
from rul.components.data_transformation import DataTransformation



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

        # Data Validation 
        logging.info(f"-----------------Initiating Data Validation-----------------")
        data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)

        data_validation = DataValidation(data_validation_config=data_validation_config, data_ingestion_artifact=data_ingestion_artifact)

        data_validation_artifact = data_validation.initiate_data_validation()

        # Data Transformation
        logging.info(f"-----------------Initiating Data Transformation-----------------")
        data_transformation_config = config_entity.DataTransformationConfig(training_pipeline_config=training_pipeline_config)

        data_transformation = DataTransformation(data_transformation_config=data_transformation_config, data_ingestion_artifact=data_ingestion_artifact)

        data_transformation_artifact = data_transformation.initiate_data_transformation()

    except Exception as e:
        raise RULException(e, sys)