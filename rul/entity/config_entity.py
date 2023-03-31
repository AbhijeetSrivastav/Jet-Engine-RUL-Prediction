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
        

