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
        
    def initiate_model_trainer(self) -> artifact_entity.ModelTrainerArtifact:
        """
        Initiate Model Trainer Component
        -------------------------------------
        input: `None`
        -------------------------------------
        return: Model Trainer Artifact
        """

        try:
            # Load Train array
            logging.info(f"Reading train array")
            train_arr = utils.load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_train_path)

            # Load Test array
            logging.info(f"Reading test array")
            test_arr = utils.load_numpy_array_data(file_path=self.data_transformation_artifact.transformed_test_path)

            # Split train array in input and target array
            logging.info(f"Splitting train array in input and target feature array")
            x_train, y_train = train_arr[:,:-1], train_arr[:,-1]

            # Split test array in input and target array
            logging.info(f"Splitting train array in input and target feature array")
            x_test,y_test = test_arr[:,:-1], test_arr[:,-1]

            # Calling model trainer method
            logging.info(f"Calling the Model Trainer method")
            model = self.train_model(x=x_train, y=y_train)

            # Predict the value of target using model for train array
            logging.info(f"Predicting the value of target feature for train array")
            y_hat_train = model.predict(x_train)

            # Calculate  r2 score for train array
            logging.info(f"Calculating r2 score for train array")
            r2_score_train = r2_score(y_true=y_train, y_pred=y_hat_train)

            # Predict the value of target using model for test array
            logging.info(f"Predicting the value of target feature for test array")
            y_hat_test = model.predict(x_test)

            # Calculate  r2 score for test array
            logging.info(f"Calculating r2 score for train array")
            r2_score_test = r2_score(y_true=y_test, y_pred=y_hat_test)


            # Check for underfitting
            logging.info(f"Checking Model is Underfitting or not")
            if r2_score_test < self.model_trainer_config.expected_score:
                logging.info(f"Model is Underfitting ! Expected Score:: {self.model_trainer_config.expected_score} Achieved Score:: {r2_score_test}")

                raise Exception(f"Model is Underfitting ! Expected Score:: {self.model_trainer_config.expected_score} Achieved Score:: {r2_score_test}")
            
            logging.info(f"Model is not Underfitting")


            # Check for overfitting
            logging.info(f"Checking Model is Overfitting or not")

            logging.info(f"Calculating r2 score test and train score difference")
            diff = abs(r2_score_train - r2_score_test)

            if diff > self.model_trainer_config.overfitting_threshold:
                logging.info(f"Model is Overfitting! Expected Threshold:: {self.model_trainer_config.overfitting_threshold} Diff of train and test score:: {diff}")

                raise Exception(f"Model is Overfitting! Expected Threshold:: {self.model_trainer_config.overfitting_threshold} Diff of train and test score:: {diff}")

            logging.info(f"Model is not Overfitting")


            # Save the trained model object
            logging.info(f"Saving the model object")
            utils.save_object(file_path=self.model_trainer_config.model_path, obj=model)

            # Prepare the artifact
            logging.info(f"Preparing Model Trainer artifacts")
            model_trainer_artifact  = artifact_entity.ModelTrainerArtifact(model_path=self.model_trainer_config.model_path, 
            r2_train_score=r2_score_train, r2_test_score=r2_score_test)

            return model_trainer_artifact

        except Exception as e:
            raise RULException(e, sys)