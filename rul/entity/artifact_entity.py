"Contain all the artifacts of the components and pipelines"


from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    """
    Artifact for Data Ingestion component
    -----------------------------------------------------------------------------
    return:
    `feature_store_file_path`: path of feature store of data ingestion component
    `train_file_path`: path of train file created by Data Ingestion component
    `test_file_path`: path of test file created by Data Ingestion component
    """
    feature_store_file_path: str
    train_file_path: str
    test_file_path: str


@dataclass
class DataValidationArtifact:
    """
    Artifact for Data Validation component
    --------------------------------------------------------------
    return:
    - `report_file_path`: path of the validation report
    """
    report_file_path: str