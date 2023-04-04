"Data Transformation Component"

import os
import sys
from typing import Optional
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
from rul.entity import config_entity
from rul.entity import artifact_entity
from rul.config import TARGET_COLUMN
from rul.exception import RULException
from rul.logger import logging
from rul import utils


class DataTransformation:
    """
    Data Transformation Component
    -----------------------------------------------------------------
    input:
    - `data_transformation_config`: Data Transformation Configuration
    - `data_ingestion_artifact`: Data Ingestion Artifact
    -----------------------------------------------------------------
    return: Data Transformation Artifact
    """

    def __init__(self, data_transformation_config: config_entity.DataTransformationConfig, data_ingestion_artifact: artifact_entity.DataIngestionArtifact) -> None:
        try:
            self.data_transformation_config = data_transformation_config

            self.data_ingestion_artifact = data_ingestion_artifact
        
        except Exception as e:
            raise RULException(e, sys)