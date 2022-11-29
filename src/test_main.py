import unittest
import os
import sys
from pyspark.sql import SparkSession
from transformations.data_cleansing import DataCleansing

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
class TestDataCleansing(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.spark = SparkSession.builder \
            .appName('UNITTEST_CLEANSING') \
            .getOrCreate()
        cls.df_orig = cls.spark.read.format('csv').option('delimiter', ';').option('header', False).load('input_data.csv', multiLine=True)
        cls.df_to_list = cls.df_orig.collect()

    def test_cleanse_df(self):
        '''I am checking a number of asserts with the 
        result of the cleanse_address method. I first 
        wannt to check that both the extracted housenumber
        and streetname are in the original address string.
        I also want to test that street and housenumber
        concatenated have the same length as the original
        address (means no information got lost'''
        data_cleanser = DataCleansing()
        dataframe_cleansed = data_cleanser.cleanse_address(self.df_orig)
        dataframe_coll = dataframe_cleansed.collect()
        for a, b in zip(dataframe_coll, self.df_to_list):
            self.assertIn(a['street'], b['_c0'])
            self.assertIn(a['housenumber'], b['_c0'])
            self.assertLessEqual(len(a['street'] + ' ' + a['housenumber']), len(b['_c0']))

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()


if __name__ == '__main__':
    unittest.main()