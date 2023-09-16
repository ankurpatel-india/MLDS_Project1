from src.MLDS.logger import logging
from src.MLDS.exception import CustomException
import sys
from src.MLDS.components.data_ingestion import DataIngestion
from src.MLDS.components.data_ingestion import DataIngestionConfig
if __name__=="__main__":
    logging.info("The exectution has started.") 
    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custome Exceptions")
        raise CustomException(e,sys)                                                    