"Predictor for RUL package"


import sys
import os
from glob import glob
from typing import Optional
from rul.exception import RULException
from rul.logger import logging
from rul.entity.config_entity import TRANSFORMER_OBJECT_FILE_NAME, MODEL_FILE_NAME


class ModelResolver:
    """
    Model Resolver 
    -----------------------------------------------------------------------------------------------------------------------------------------------------
    LATEST SAVED named methods are for the directory or objects which have been created when pipeline is started to produce new model.
    LATEST named methods are for the directory or object which have been created when pipeline was previously ran to produce model. 
    ------------------------------------------------------------------------------------------------------------------------------------------------------
    input:
     - `model_registry`: directory containing all sub directories which contain the models trained and their transformers till now in  artifacts of model training component
     - `model_dir_name`: directory name containing models which is in (model_registry -> subdir -> model)
     - `transformer_dir_name`: directory name containing models which is in (model_registry -> subdir -> transformer_dir_name)
     - `target_encoder_dir_name`: directory name containing models which is in (model_registry -> subdir -> target_encoder_dir_name)
    -------------------------------------------------------------------------------------------------------------------------------------------------------
    return: `None`
    """ 

    def __init__(self, model_registry: str = "saved_models", transformer_dir_name="transformer", model_dir_name="model") -> None:
        try:
            self.model_registry = model_registry
            os.makedirs(self.model_registry, exist_ok=True)

            self.transformer_dir_name = transformer_dir_name

            self.model_dir_name = model_dir_name

        except Exception as e:
            raise RULException(e, sys)
    
    def get_latest_dir_path(self) -> Optional[str]:
        """
        Returns latest model directory path if their any
        -------------------------------------------------
        input:
        - `None`
        -------------------------------------------------
        return: `None` or `latest_dir_path`
        """

        try:
            # Creating list of all the sub directories in the model_registry folder of model training artifact
            dir_names = os.listdir(self.model_registry)

            # If no sub directory that means no saved model object
            if len(dir_names) == 0:
                return None
            
            # Convert str name of subdir to int for all subdirs
            dir_names = list(map(int, dir_names))

            # Get the latest one as we saved subdirs as named by date time format
            latest_dir_name = max(dir_names)

            # Get absolute path to our latest subdir
            latest_dir_path = os.path.join(self.model_registry, f"{latest_dir_name}")

            return latest_dir_path
        
        except Exception as e:
            raise RULException(e, sys)
