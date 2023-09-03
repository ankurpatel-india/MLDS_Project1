from src.MLDS.logger import logging
from src.MLDS.exception import CustomException
import sys

if __name__=="__main__":
    logging.info("The exectution has started.") 
    try:
        a=1/0
    except Exception as e:
        logging.info("Custome Exceptions")
        raise CustomException(e,sys)                                                    