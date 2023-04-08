"Model Evaluation Component"


import sys
import pandas as pd
from sklearn.metrics import r2_score
from rul.entity import config_entity
from rul.entity import artifact_entity
from rul.exception import RULException
from rul.logger import logging
from rul.predictor import ModelResolver
from rul import utils


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
        
    def initiate_model_evaluation(self) -> artifact_entity.ModelEvaluationArtifact:
        """
        Initiate MOdel Evaluation Artifact
        -----------------------------------------
        input:
        - `None`
        ------------------------------------------
        return: Model Evaluation Artifact
        """

        try:
            # --------FOR LATEST MODEL (ALREADY DEPLOYED ONE)--------
            logging.info(f"Fetching path of latest model, transformer")

            # latest model directory path
            latest_dir_path = self.model_resolver.get_latest_dir_path()

            # => Case I: If their is no model accept the current trained model (model trained in this pipeline run)
            if  latest_dir_path == None:
                model_eval_artifact = artifact_entity.ModelEvaluationArtifact(is_model_accepted=True, improved_accuracy=None)

                return model_eval_artifact
            

            # =>CASE II: If their are previously saved model then compare it to current trained model

            # Fetching the path of latest model, transformer (Already deployed ones)
            latest_transformer_path = self.model_resolver.get_latest_transformer_path()

            latest_model_path = self.model_resolver.get_latest_model_path()

            # Loading the latest model, transformer (Already deployed ones)
            logging.info(f"Loading latest model, transformer objects")
            transformer = utils.load_object(file_path=latest_transformer_path)

            model = utils.load_object(file_path=latest_model_path)


            # --------FOR LATEST SAVED MODEL (MODEL SAVED IN THIS RUN OF PIPELINE)----------------
            logging.info(f"Fetching path of current model, transformer")
            current_transformer_path = self.data_transformation_artifact.transformer_object_path

            current_model_path = self.model_trainer_artifact.model_path

            # Loading current model, transformer and target encoder object
            logging.info(f"Loading current model, transformer")
            current_transformer = utils.load_object(file_path=current_transformer_path)

            current_model = utils.load_object(file_path=current_model_path)


            # --------Evaluation--------
            
            # Loading test dataFrame
            logging.info(f"Loading test dataframe")
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            # Splitting test dataframe in target and input feature
            logging.info(f"Splitting test dataframe in target and input feature")
            y_true = test_df[:,-1]

            # ** Accuracy using latest model(already deployed one)
            logging.info(f"Calculating accuracy for latest model(already deployed one)")
            input_feature_name = list(transformer.feature_names_in_)

            input_arr = transformer.transform(test_df[input_feature_name])

            y_pred = model.predict(input_arr)

            latest_model_score = r2_score(y_true=y_true, y_pred=y_pred)


            # ** Accuracy using the current model(model saved in this run of pipeline)
            logging.info(f"Calculating accuracy for latest saved model(current trained model)")
            input_feature_name = list(current_transformer.feature_names_in_)

            input_arr = current_transformer.transform(test_df[input_feature_name])

            y_pred = current_model.predict(input_arr)

            current_model_score = r2_score(y_true=y_true, y_pred=y_pred)


            # ** Comparing models
            logging.info(f"Comparing accuracy of latest(already deployed one) and current model(model saved in this run of pipeline)")
            if current_model_score <= latest_model_score:
                raise Exception("Current trained model(model saved in this pipeline) is not better than previous model(already deployed one)")
            

            logging.info(f"Latest model accuracy:: {latest_model_score}, Current model accuracy:: {current_model_score}")

            # Calculating accuracy score diff
            diff = current_model_score - latest_model_score


            # Preparing artifact
            logging.info(f"Preparing Model Evaluation artifacts")
            model_eval_artifact = artifact_entity.ModelEvaluationArtifact(is_model_accepted=True, improved_accuracy=diff)
        
            return model_eval_artifact


        except Exception as e:
            raise RULException(e, sys)
        

