"""
This is a boilerplate pipeline
generated using Kedro 0.18.1
"""

import logging
from typing import Dict, Tuple

import numpy as np
import pandas as pd

from pyspark.sql import DataFrame, types
from pyspark.ml.pipeline import Pipeline
from pyspark.ml.feature import VectorAssembler, OneHotEncoder, StringIndexer
from pyspark.ml.classification import RandomForestClassifier

def select_cols(df: DataFrame, params: Dict ):
    columns_of_interest = params['columns_of_interest']
    return df.select(columns_of_interest).na.drop()

def feature_engineering():
    pass

def make_pyspark_pipeline():
    pass

def split_data():
    pass