import csv
from typing import List, Optional, Set, Text, Tuple, Type, Any
import itertools
from pathlib import Path


class SparkCSVLoader:
    '''
        A class to load CSV files into Spark DataFrames
    '''
    def __init__(self, spark: SparkSession, logger: Logger, config: Dict[str, Any]):
        self.spark = spark
        self.logger = logger
        self.config = config

    def load(self, path: str, schema: StructType, **options) -> DataFrame:
        '''
        Load a CSV file into a Spark DataFrame
        '''
        return self.spark.read.csv(path, schema=schema, **options)