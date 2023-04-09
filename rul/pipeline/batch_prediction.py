"Batch Prediction Pipeline"


import sys
import os
from datetime import datetime
import pandas as pd
import numpy as np
from rul.logger import logging
from rul.exception import RULException
from rul.utils import load_object
from rul.predictor import ModelResolver


PREDICTION_DIR = "prediction"


def start_batch_prediction(input_file_path):...