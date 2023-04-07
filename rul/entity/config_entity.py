"Contain all the configuration of the components and pipelines"


import os
import sys
from datetime import datetime
from rul.exception import RULException
from rul.logger import logging


# Defining relevant file names
FILE_NAME = "rul.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"
TRANSFORMER_OBJECT_FILE_NAME = "transformer.pkl"
TARGET_ENCODER_FILE_OBJECT_NAME = "target_encoder.pkl"
MODEL_FILE_NAME = "model.pkl"


class TrainingPipelineConfig:
    """
    Configuration for Training Pipeline
    ------------------------------------
    return: `None`
    """

    def __init__(self) -> None:
        try:
            self.artifact_dir = os.path.join(os.getcwd(), "artifact", f"{datetime.now().strftime('%m%d%Y_%H%M%S')}")
        except Exception as e:
            raise RULException(e, sys)
        

class DataIngestionConfig:
    """
    Configuration for Data Ingestion Component
    -----------------------------------------------------------------
    input:
    - `training_pipeline_config`: configuration of training pipeline
    -----------------------------------------------------------------
    return: dictionary of everything defined in constructor
    """

    def __init__(self, training_pipeline_config: TrainingPipelineConfig) -> dict:
        try:
            self.database_name = "rul"
            self.collection_name = "rul_collect"

            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir, "data_ingestion")

            self.feature_store_file_path = os.path.join(self.data_ingestion_dir, "feature_store", FILE_NAME)

            self.train_file_path = os.path.join(self.data_ingestion_dir, "dataset", TRAIN_FILE_NAME)

            self.test_file_path = os.path.join(self.data_ingestion_dir, "dataset", TEST_FILE_NAME)

            self.test_size = 0.2

        except Exception as e:
            raise RULException(e, sys)
        
        def to_dict(self)->dict:
            try:
                return self.___dict__
            except Exception as e:
                raise RULException(e, sys)
            

class DataValidationConfig:
    """
    Configuration for Data Validation Component
    -----------------------------------------------------------------
    input:
    - `training_pipeline_config`: configuration of training pipeline
    -----------------------------------------------------------------
    return: `None`
    """

    def __init__(self, training_pipeline_config: TrainingPipelineConfig) -> None:
        try:
            self.data_validation_dir  = os.path.join(training_pipeline_config.artifact_dir, "data_validation")

            self.report_file_path = os.path.join(self.data_validation_dir, "report")

            self.missing_value_threshold = 0.2

            self.base_file_path = os.path.join("rul.csv")

        except Exception as e:
            raise RULException(e, sys)
        

class DataTransformationConfig:
    """
    Configuration for Data Transformation Component
    ------------------------------------------------------------------
    input:
    - `training_pipeline_config`: configuration of training pipeline
    ------------------------------------------------------------------
    return: `None`
    """

    def __init__(self, training_pipeline_config: TrainingPipelineConfig) -> None:
        try:
            self.data_transformation_dir = os.path.join(training_pipeline_config.artifact_dir, "data_transformation")

            self.data_transformer_object_path = os.path.join(self.data_transformation_dir, "transformer")

            self.data_transformed_train_path = os.path.join(self.data_transformation_dir, "transformed", TRAIN_FILE_NAME)

            self.data_transformed_test_path = os.path.join(self.data_transformation_dir, "transformed", TEST_FILE_NAME)

        except Exception as e:
            raise RULException(e, sys)
        

class ModelTrainerConfig:
    """
    Configuration for Model Component
    -----------------------------------------------------------------
    input:
    - `training_pipeline_config`: configuration of training pipeline
    -----------------------------------------------------------------
    return: `None`
    """

    def __init__(self,trainer_pipeline_config: TrainingPipelineConfig) -> None:
        try:
            self.model_trainer_dir = os.path.join(trainer_pipeline_config.artifact_dir, "model_trainer")

            self.model_path = os.path.join(self.model_trainer_dir, "model", MODEL_FILE_NAME)

            self.expected_score = 0.6

            self.overfitting_threshold = 0.5
            
        except Exception as e:
            raise RULException(e, sys)
        

class ModelEvaluationConfig:
    """
    Configuration for Model Evaluation Component
    -----------------------------------------------------------------
    input:
    - `training_pipeline_config`: configuration of training pipeline
    -----------------------------------------------------------------
    return: `None`
    """

    def __init__(self) -> None:
        try:
            self.change_threshold = 0.01
            
        except Exception as e:
            raise RULException(e, sys)