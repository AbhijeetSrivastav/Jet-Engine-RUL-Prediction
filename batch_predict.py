"Execution of Batch Prediction Pipeline"


from rul.pipeline.batch_prediction import start_batch_prediction
from rul.logger import logging


FILE_PATH_FOR_BATCH_PREDICTION = "rul.csv"

if __name__ == "__main__":
    try:
        logging.info(f"------------------Initiating Batch Prediction------------------")
        start_batch_prediction(input_file_path=FILE_PATH_FOR_BATCH_PREDICTION)

    except Exception as e:
        print(e)