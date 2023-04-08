"Training Pipeline"


import sys
import os
from rul.logger import logging
from rul.exception import RULException
from rul.entity import config_entity
from rul.components.data_ingestion import DataIngestion
from rul.components.data_validation import DataValidation
from rul.components.data_transformation import DataTransformation
from rul.components.model_trainer import ModelTrainer
from rul.components.model_evaluation import ModelEvaluation


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

        # Model Trainer
        logging.info(f"-----------------Initiating Model Trainer-----------------")
        model_trainer_config = config_entity.ModelTrainerConfig(training_pipeline_config=training_pipeline_config)

        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)

        model_trainer_artifact = model_trainer.initiate_model_trainer()

        # Model Evaluation
        logging.info(f"-----------------Initiating Model Evaluation-----------------")
        model_evaluation_config = config_entity.ModelEvaluationConfig(training_pipeline_config=training_pipeline_config)

        model_evaluation = ModelEvaluation(model_evaluation_config=model_evaluation_config, data_ingestion_artifact=data_ingestion_artifact, data_transformation_artifact=data_transformation_artifact, model_trainer_artifact=model_trainer_artifact)

        model_evaluation_artifact = model_evaluation.initiate_model_evaluation()

    except Exception as e:
        raise RULException(e, sys)