"Model Pusher Component"


import sys
from rul.entity import config_entity
from rul.entity import artifact_entity
from rul.predictor import ModelResolver
from rul.exception import RULException
from rul.logger import logging
from rul import utils


class ModelPusher:
    """
    Model Pusher Component
    ---------------------------------------------------------------
    input:
    - `model_pusher_config`: Model Pusher Configuration
    - `data_transformation_artifact`: Data Transformation Artifact
    - `model_trainer_artifact`: Model Trainer Artifact
    """

    def __init__(self, model_pusher_config: config_entity.ModelPusherConfig, data_transformation_artifact: artifact_entity.DataTransformationArtifact, model_trainer_artifact: artifact_entity.ModelTrainerArtifact) -> None:
        try:
            self.model_pusher_config = model_pusher_config

            self.data_transformation_artifact = data_transformation_artifact

            self.model_trainer_artifact = model_trainer_artifact

            # Initializing Model Resolver
            self.model_resolver = ModelResolver(model_registry=self.model_pusher_config.saved_model_dir)
        
        except Exception as e:
            raise RULException(e, sys)

    def initiate_model_pusher(self) -> artifact_entity.ModelPusherArtifact:
        try:
            # => For model_pusher directory
            # Load Transformer and Model Object
            logging.info(f"Loading transformer object")
            transformer = utils.load_object(file_path=self.data_transformation_artifact.transformer_object_path)

            logging.info(f"Loading model object")
            model = utils.load_object(file_path=self.model_trainer_artifact.model_path)

            # Save Model, Transformer to model pusher directory in artifacts
            logging.info(f"Saving model, transformer object model pusher directory as artifacts")
            utils.save_object(file_path=self.model_pusher_config.pusher_transformer_path, obj=transformer)

            utils.save_object(file_path=self.model_pusher_config.pusher_model_path, obj=model)

            
            # => For saved_model directory
            # Fetch path of latest Model, Transformer 
            logging.info(f"Fetching path of latest model, transformer object")
            transformer_path = self.model_resolver.get_latest_save_transformer_path()

            model_path = self.model_resolver.get_latest_save_model_path()

            # Save latest Model, Transformer to saved_model directory
            logging.info(f"Saving model, transformer object save_models directory")
            utils.save_object(file_path=transformer_path, obj=transformer)

            utils.save_object(file_path=model_path, obj=model)

            # Prepare artifacts
            logging.info(f"Preparing Pusher artifacts")
            model_pusher_artifact = artifact_entity.ModelPusherArtifact(pusher_model_dir=self.model_pusher_config.pusher_model_dir,
                                                                        saved_model_dir=self.model_pusher_config.saved_model_dir
                                                                        )
            
        except Exception as e:
            raise RULException(e, sys)
