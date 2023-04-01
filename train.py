"Execution of Training Pipeline"


from rul.pipeline.training_pipeline import start_training_pipeline
from rul.logger import logging


if __name__ == "__main__":
    try:
        logging.info(f"-----------------Initiating Training Pipeline-----------------")
        start_training_pipeline()
    except Exception as e:
        print(e)