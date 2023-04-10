"Batch Prediction Pipeline"


import sys
import os
from datetime import datetime
import pandas as pd
import numpy as np
from rul.logger import logging
from rul.exception import RULException
from rul import utils
from rul.predictor import ModelResolver
from rul.components.data_transformation import DataTransformation as DT


PREDICTION_DIR = "prediction"


def start_batch_prediction(input_file_path):
    """
    Predicts output for batch of data points
    -----------------------------------------------------------------
    input:
    - `input_file_path`: file to make prediction on (Assuming that input file has same shape as base file and has not only just input features but both input features and target feature--- we can alter this function for only input feature file only)
    -----------------------------------------------------------------
    return: `prediction_file_path`
    """

    try:
        # Making prediction directory
        logging.info(f"Creating prediction directory if not exist")
        os.makedirs(PREDICTION_DIR, exist_ok=True)

        # Loading Model resolver
        logging.info(f"Creating instance of model resolver class")
        model_resolver = ModelResolver(model_registry="saved_models")

        # Loading dataset on which we want to make predictions (in batch)
        logging.info(f"Loading dataset on which to predict")
        df = pd.read_csv(input_file_path)

        # Replacing na with Nan
        logging.info(f"Replacing Na with NAN")
        df.replace({"na": np.NAN}, inplace=True)

        # Loading latest transformer object
        logging.info(f"Loading latest transformer object")
        transformer = utils.load_object(file_path=model_resolver.get_latest_transformer_path())

        # Load latest Model object
        logging.info(f"Loading latest model object")
        model = utils.load_object(file_path=model_resolver.get_latest_model_path())

        # Add RUL feature
        logging.info(f"Adding RUL feature to dataframe")
        df = DT.add_RUL_feature(DT, df=df)

        # Dropping irrelevant  features
        logging.info(f"Proceeding to drop irrelevant index, setting and constant sensor features")
        index_names = ["unit_number", "time_cycles"]
        setting_names = ["setting_1", "setting_2", "setting_3"]
        constant_sensors = ["s_1", "s_5",'s_6', "s_10", "s_16", "s_18", "s_19"]

        drop_labels = index_names + setting_names + constant_sensors

        df.drop(columns=drop_labels, inplace=True)

        # Transforming df to array
        logging.info(f"Transforming dataframe to numpy array")
        df_arr = transformer.transform(df)

        # Extracting input feature
        logging.info(f"Extracting input features from dataframe")
        input_features = df_arr[:,:-1]

        # Predict using the model
        logging.info(f"Making predictions on input features")
        prediction = model.predict(input_features)

        # Reshaping prediction array
        logging.info(f"Reshaping prediction numpy array")
        prediction = prediction.reshape((20631, 1))

        # Converting input feature and prediction array to dataframe
        logging.info(f"Converting input_feature and prediction array to dataframe")
        input_features = pd.DataFrame(input_features)
        prediction = pd.DataFrame(prediction)

        # Merging input_feature and prediction dataframe
        logging.info(f"Merging input_feature and prediction dataframe as output dataframe")
        output = pd.concat([input_features, prediction], axis=1)

        # Inverse transforming every features of output dataframe
        logging.info(f"Inverse transforming every feature of output dataframe to get original data in array form")
        output = transformer.inverse_transform(output)

        # Converting output array to dataframe and adding column header
        logging.info(f"Converting output numpy array to dataframe and adding headers")
        output = pd.DataFrame(output, 
                              columns=['s_2', 's_3', 's_4', 's_7', 's_8', 's_9',
                                        's_11', 's_12', 's_13', 's_14', 's_15', 
                                        's_17', 's_20', 's_21', 'RUL'
                                        ]
                            )

        # Save prediction file
        logging.info(f"Saving output file containing prediction and input features")

        prediction_file_name = os.path.basename(input_file_path).replace(".csv", f"{datetime.now().strftime('%m%d%Y__%H%M%S')}.csv")

        prediction_file_path = os.path.join(PREDICTION_DIR, prediction_file_name)

        output.to_csv(prediction_file_path, index=False, header=True)

        return prediction_file_path
    
    except Exception as e:
        raise RULException(e, sys)