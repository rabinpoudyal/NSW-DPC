from pyspark.sql import SparkSession
import logging


from dpc import version

# define the version before the other imports since these need it
__version__ = version.__version__

spark = SparkSession.builder.appName("dpc").getOrCreate()


logging.getLogger(__name__).addHandler(logging.NullHandler())