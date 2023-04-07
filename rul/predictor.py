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

    def get_latest_model_path(self):
        """
        Returns latest model path form the latest model subdir from model_registry
        ---------------------------------------------------------------------------------
        input:
        - `None`
        ----------------------------------------------------------------------------------
        return: `latest_model_path`
        """

        try:
            latest_dir_path = self.get_latest_dir_path()

            # If no model in the path
            if latest_dir_path is None:
                logging.info(f"Model is not available!")
                raise Exception(f"Model is not available!")
            
            latest_model_path = os.path.join(latest_dir_path, self.model_dir_name, MODEL_FILE_NAME)

            return latest_model_path
        
        except Exception as e:
            raise RULException(e, sys)
        
    def get_latest_transformer_path(self):
        """
        Returns latest transformer path form the latest transformer subdir from model_registry
        ---------------------------------------------------------------------------------------------
        input:
        - `None`
        ---------------------------------------------------------------------------------------------
        return: `latest_transformer_path`
        """

        try:
            latest_dir_path = self.get_latest_dir_path()

            # If no transformer in path
            if latest_dir_path is None:
                logging.info(f"Transformer is not available!")
                raise Exception(f"Transformer is not available!")
            
            latest_transformer_path = os.path.join(latest_dir_path, self.transformer_dir_name, TRANSFORMER_OBJECT_FILE_NAME)

            return latest_transformer_path
        
        except Exception as e:
            raise RULException(e, sys)
        
        ##########################################################################

    def get_latest_save_dir_path(self)->Optional[str]:
        """
        Returns latest saved model directory path if their any
        ---------------------------------------------------------
        input:
         - `None`
        ---------------------------------------------------------
        return: `None` or `latest_save_dir_path`
        """
        try:
            latest_dir_path = self.get_latest_dir_path()

            # If no latest directory
            if latest_dir_path is None:
                logging.info(f"No latest saved model registry found!")
                return os.path.join(self.model_registry,f"{0}")
            
            # Number name of the latest saved model sub directory
            latest_dir_num = int(os.path.basename(self.get_latest_dir_path()))


            latest_save_dir_path = os.path.join(self.model_registry, f"{latest_dir_num+1}")

            return latest_save_dir_path

        except Exception as e:
            raise RULException(e, sys)     
    
    def get_latest_save_model_path(self):
        """
        Returns latest saved model path from the latest saved model subdir from model_registry
        ---------------------------------------------------------------------------------------
        input:
         - `None`
        ----------------------------------------------------------------------------------------
         return: `latest_save_model_path`
        """
        try:
            latest_save_dir_path = self.get_latest_save_dir_path()

            latest_save_model_path = os.path.join(latest_save_dir_path, self.model_dir_name,MODEL_FILE_NAME)

            return latest_save_model_path

        except Exception as e:
            raise RULException(e, sys)
    
    def get_latest_save_transformer_path(self):
        """
        Returns latest saved transformer path from the latest saved transformer subdir from model_registry
        ---------------------------------------------------------------------------------------------------
        input:
         - `None`
        ---------------------------------------------------------------------------------------------------
         return: `latest_save_transformer_path`
        """
        try:
            latest_save_dir_path = self.get_latest_save_dir_path()

            latest_save_transformer_path = os.path.join(latest_save_dir_path, self.transformer_dir_name,TRANSFORMER_OBJECT_FILE_NAME)

            return latest_save_transformer_path

        except Exception as e:
            raise RULException(e, sys)
