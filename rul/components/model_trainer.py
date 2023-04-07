"Model Trainer Component"


import os
import sys
from typing import Optional
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from rul.entity import config_entity
from rul.entity import artifact_entity
from rul.logger import logging
from rul.exception import RULException
from rul import utils


class ModelTrainer:
    """
    Model Trainer Component
    ---------------------------------------------------------------
    input:
    - `model_trainer_config`: Model Trainer Configuration
    - `data_transformation_artifact`: Data Transformation Artifact
    ----------------------------------------------------------------
    return: Model Trainer Artifact
    """

    def __init__(self, model_trainer_config: config_entity.ModelTrainerConfig, data_transformation_artifact: artifact_entity.DataTransformationArtifact) -> None:
        try:
            self.model_trainer_config = model_trainer_config

            self.data_transformation_artifact = data_transformation_artifact

        except Exception as e:
            raise RULException(e, sys)
    
    def train_model(self, x: np.array, y: np.array) -> RandomForestRegressor:
        """
        Creates a Random Forest Regressor which was selected as the best model during experimentation
        -------------------------------------------------------------------------------------------------
        input:
        - `x`: input feature array
        - `y`: target feature array
        ---------------------------------------------------------------------------------------------------
        return: `RandomForestRegressor`
        """

        try:
            logging.info(f"Creating instance of RandomForestRegressor")
            rfr = RandomForestRegressor(
                                        criterion="poisson", max_features="sqrt",
                                        ccp_alpha=0.0, n_estimators=100
                                        )
            
            logging.info(f"Fitting the RandomForestRegressor model")
            rfr.fit(x, y)

            return rfr
        
        except Exception as e:
            raise RULException(e, sys)