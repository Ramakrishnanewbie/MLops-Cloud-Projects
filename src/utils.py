import pandas as pd
from src.logger import logging 
from sklearn.model_selection import train_test_split



def read_dataset():
    logging.info("dataset is being read")
    df=pd.read_csv('notebook/data/stud.csv')

    return df

def train_test_split_dataset(df):
    train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

    return train_set,test_set