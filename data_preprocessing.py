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
    
    dataset.drop(outliers_list, axis=0, inplace = True)
    dataset.reset_index(drop=True, inplace = True)
    return dataset

def delete_outliers_percentiles(self):
    q1 = self.dataset.quantile(0.25)
    q3 = self.dataset.quantile(0.75)
    iqr = q3 - q1
    dataset = dataset[~((dataset < (q1 - 1.5 * iqr)) | (dataset > (q3 + 1.5 * iqr))).any(axis=1)]
    
def delete_null(dataset):
    columns = dataset.columns
    null_percentage = dataset.isnull().sum() / len(dataset) * 100
    # create a list of columns with more than 80% null values
    columns_to_drop = null_percentage[null_percentage > 80].index.tolist()
    # drop the columns with more than 80% null values
    dataset.drop(columns_to_drop, axis=1, inplace = True)
    '''
    drop rows where data is missing from specific columns.
    ['id', 'ranking_score', 'agent_id', 'geography_name', 'sq_meters', 'price', 'year_of_construction', 'floor', 'subtype', 'rooms', 'no_of_wc', 'ad_type', 'living_rooms', 'kitchens', 'balcony_area']
    '''
    dataset.dropna(subset=columns[0:10].append(columns[13:18]), inplace = True)
    dataset.reset_index(drop=True, inplace = True)
    return dataset

def add_decade_and_pricepersqm_columns(dataset):
    dataset['price_per_sqm'] = dataset['price'].div(dataset['sq_meters']).round(2)
    dataset['decade'] = dataset['year_of_construction'] - (dataset['year_of_construction']%10)
    return dataset
    
def drop_duplicates_and_corrupt_entries(dataset):
    dataset.drop_duplicates(subset=dataset.columns.difference(['id', 'agent_id']), inplace = True)
    dataset = dataset[(dataset['price'] > 1000) & (dataset['sq_meters'] != 1)].copy()
    dataset.drop_duplicates(subset=dataset[['subtype', 'price', 'sq_meters', 'geography_name', 'floor', 'rooms', 'price_per_sqm', 'decade']], keep='last', inplace=True)
    dataset = dataset[dataset['price_per_sqm'] != 16666.67].copy()
    return dataset

def replace_na_and_boolean(dataset):
    unique_counts = dataset.nunique()
    # Filter columns based on number of unique values in this case 2
    cols_with_x_unique_vals = unique_counts[unique_counts == 2].index.tolist()
    dataset.fillna(value=-1, inplace=True)
    dataset[cols_with_x_unique_vals] = dataset[cols_with_x_unique_vals].astype(int)
    return dataset 

def preprocess_and_save(dataset):
    dataset = add_decade_and_pricepersqm_columns(dataset)
    dataset = delete_null(dataset)
    dataset = delete_outliers_zscore(dataset)
    dataset = replace_na_and_boolean(dataset)
    dataset = drop_duplicates_and_corrupt_entries(dataset)
    
    dataset.to_csv(os.path.join(DATASET_FOLDER, PREPROCESSED_DATASET_FILE), index=False)
    return dataset

dataset = pd.read_csv(os.path.join(DATASET_FOLDER, RAW_DATASET_FILE))
preprocessed_dataset = preprocess_and_save(dataset)
