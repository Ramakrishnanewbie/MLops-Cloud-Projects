import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import *
from data_transformation import *

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test.csv')
    raw_data_path=os.path.join('artifacts','raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()#ingestion_config will have all the three paths we defined above and each of the path variable above will be a sub variable in it

    
    def initiate_data_ingestion(self):
        # if in database create data read using client in utils.py
        logging.info('Entered the data ingestion method or component')
        try:
            df=read_dataset()
            logging.info('dataset has been read as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info('Train Test Split initiated')

            train_set,test_set = train_test_split_dataset(df)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('ingestion of the data is completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,

            )
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=='__main__' :
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    data_transformation=DataTransformation()
    data_transformation.initiate_data_transformation(train_data_path,test_data_path)