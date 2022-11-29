import os
import sys

from pyspark.sql import SparkSession

from transformations.data_cleansing import DataCleansing

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# create Spark Session
try:
    spark = SparkSession.builder\
                .appName('MORITZ-CHALLENGE') \
                .config('spark.local.dir', 'u02/spark-temp') \
                .getOrCreate()
    print('Spark Session successfully created')
except Exception as e:
    print('failed to create Spark Session')
    print(e)
    sys.exit()


# load data into a dataframe
dataframe = spark.read.format('csv').option('delimiter', ';').option('header', False).load('input_data.csv', multiLine=True)


# transform data and store it in a new dataframe
try:
    cleansedDf = DataCleansing().cleanse_address(dataframe)
    print('transformation of data successful')
except Exception as e:
    print('failed to transform data')
    print(e)
    sys.exit()

cleansedDf.show()
cleansedDf.coalesce(1).write.format('json').save('addresses_cleansed')
