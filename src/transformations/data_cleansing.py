from pyspark.sql.functions import col, expr, size, udf, when, concat
from pyspark.sql.types import StringType
from transformations.helper_functions import (
    get_street,
    get_housenumber,
)

class DataCleansing:
    def __init__(self) -> None:
        self.get_street_udf = udf(lambda address: get_street(address), StringType())
        self.get_housenumber_udf = udf(lambda address, numbers: get_housenumber(address, numbers), StringType())


    def cleanse_address(self, dataframe):
        '''this method takes an dataframe without headers
        as argument. It first extracts all substrings
        containing digits from the dataframe column by checking
        a number of regex patterns. If there is only 1 substring
        with digits, I assume that this is the housenumber.
        If there are more substrings with digits, I apply a udf that
        determines which digit substring belongs to the streetname.
        A 2nd udf identifies the housenumber by substracting the
        identified streetnumber from col(digits)'''
        dataframe = dataframe \
            .withColumnRenamed('_c0', 'orig_string') \
            .withColumn('digits', expr(r"regexp_extract_all(orig_string, '\\d+\\s\\w$|\\d+\\s\\w\\s|\\d+\\s\\w\\s|\\d+\\w+|\\d+\\w|\\d+\\s\\w\\s|\\d+', 0)")) \
            .withColumn('digits_count', size(col('digits'))) \
            .withColumn('street', when(col('digits_count') == 1,
                expr(r"regexp_extract(orig_string, '^\\D+(?=[,.:-])|^\\D+(?=\\s)|(?<=\\s)\\D+', 0)")).otherwise(
                    concat(self.get_street_udf(
                            col('orig_string'),
                            ))
                )
            ) \
            .withColumn('housenumber', when(col('digits_count') == 1, col('digits')[0]).otherwise(
                self.get_housenumber_udf(
                    col('street'),
                    col('digits'),
                )
            )) \


        dataframe = dataframe.select(
            'street',
            'housenumber',
        )
        return dataframe