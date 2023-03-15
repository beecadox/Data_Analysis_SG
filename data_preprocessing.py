import pandas as pd
import numpy as np 
from scipy import stats
import os

DATASET_FOLDER = 'data'
RAW_DATASET_FILE = 'assignment_rev2.csv'
PREPROCESSED_DATASET_FILE = 'assignment_preprocessed.csv'
Z_SCORE_THRESHOLD = 3  # define a threshold for z-score

def delete_outliers_zscore(dataset):
    outliers_list = []
    
    # loop through each numeric column leaving out id columns
    for col in dataset[dataset.columns.difference(['id', 'agent_id'])].select_dtypes(include=np.number):
        # calculate z-score for each value in the column
        z = np.abs(stats.zscore(dataset[col]))
        # identify outliers based on the threshold
        outliers = np.where(z > Z_SCORE_THRESHOLD)
        outliers_list+=list(outliers[0])
    
    dataset = dataset.drop(outliers_list, axis=0)
    dataset = dataset.reset_index(drop=True)
    return dataset

def delete_outliers_percentiles(dataset):
    q1 = dataset.quantile(0.25)
    q3 = dataset.quantile(0.75)
    iqr = q3 - q1
    dataset = dataset[~((dataset < (q1 - 1.5 * iqr)) | (dataset > (q3 + 1.5 * iqr))).any(axis=1)]
    
def delete_null(dataset):
    columns = dataset.columns
    null_percentage = dataset.isnull().sum() / len(dataset) * 100
    # create a list of columns with more than 80% null values
    columns_to_drop = null_percentage[null_percentage > 80].index.tolist()
    # drop the columns with more than 80% null values
    dataset = dataset.drop(columns_to_drop, axis=1)
    '''
    drop rows where data is missing from specific columns.
    ['id', 'ranking_score', 'agent_id', 'geography_name', 'sq_meters', 'price', 'year_of_construction', 'floor', 'subtype', 'rooms', 'no_of_wc', 'ad_type', 'living_rooms', 'kitchens', 'balcony_area']
    '''
    dataset = dataset.dropna(subset=columns[0:10].append(columns[13:18]))
    dataset = dataset.reset_index(drop=True)
    return dataset
    
def preprocess():
    dataset = pd.read_csv(os.path.join(DATASET_FOLDER, RAW_DATASET_FILE))
    dataset = delete_outliers_zscore(delete_null(dataset))
    dataset.drop_duplicates(subsest=dataset.columns.difference(['id', 'agent_id']))
    

