"Model Evaluation Component"


import sys
import pandas as pd
from sklearn.metrics import r2_score
from rul.entity import config_entity
from rul.entity import artifact_entity
from rul.exception import RULException
from rul.logger import logging
from rul.predictor import ModelResolver


class ModelEvaluation:
    """
    Model Evaluation Component
    -----------------------------------------------------------------
    input:
    - `model_evaluation_config`: Model Evaluation Configuration
    - `data_ingestion_artifact`: Data Ingestion Artifact
    - `data_transformation_artifact`: Data Transformation Artifact
    - `model_trainer_artifact`: Model Trainer Artifact
    """

    def __init__(self, model_evaluation_config: config_entity.ModelEvaluationConfig, data_ingestion_artifact: artifact_entity.DataIngestionArtifact, data_transformation_artifact: artifact_entity.DataTransformationArtifact, model_trainer_artifact: artifact_entity.ModelTrainerArtifact) -> None:
        try:
            self.model_evaluation_config = model_evaluation_config
            
            self.data_ingestion_artifact = data_ingestion_artifact
            
            self.data_transformation_artifact = data_transformation_artifact

            self.model_trainer_artifact = model_trainer_artifact

            # Initiating model resolver
            logging.info(f"Initiating Model Resolver")
            self.model_resolver = ModelResolver()
            
        except Exception as e:
            raise RULException(e, sys)