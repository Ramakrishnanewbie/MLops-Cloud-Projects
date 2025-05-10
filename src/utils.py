import pandas as pd
from src.logger import logging 
from sklearn.model_selection import train_test_split
from src.exception import CustomException
import sys
import os
import dill

def read_dataset():
    logging.info("dataset is being read")
    df=pd.read_csv('notebook/data/stud.csv')

    return df

def train_test_split_dataset(df):
    train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

    return train_set,test_set


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)