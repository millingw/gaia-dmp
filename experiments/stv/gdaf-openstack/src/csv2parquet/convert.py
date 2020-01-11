import pyspark
from pyspark.sql.types import *

from  pyspark.sql import SparkSession
from pyspark.sql import *
from pyspark.sql import SQLContext
from pyspark.conf import SparkConf
import time
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession

sc = SparkContext.getOrCreate()
spark = SparkSession(sc)


start = time.time()
print("-- [Staring conversion] --")


## Defining a Schema

gaia_schema = StructType([
    StructField("solution_id", LongType(), True),        
    StructField("designation", StringType(), True),
    StructField("source_id", LongType(), True),
    StructField("random_index", LongType(), True),
    StructField("ref_epoch", DoubleType(), True),
    StructField("ra", DoubleType(), True),
    StructField("ra_error", DoubleType(), True),
    StructField("dec", DoubleType(), True),
    StructField("dec_error", DoubleType(), True),
    StructField("parallax", DoubleType(), True),
    StructField("parallax_error", DoubleType(), True),
    StructField("parallax_over_error", FloatType(), True),
    StructField("pmra", DoubleType(), True),
    StructField("pmra_error", DoubleType(), True),
    StructField("pmdec", DoubleType(), True),
    StructField("pmdec_error", DoubleType(), True),
    StructField("ra_dec_corr", FloatType(), True),
    StructField("ra_parallax_corr", FloatType(), True),
    StructField("ra_pmra_corr", FloatType(), True),
    StructField("ra_pmdec_corr", FloatType(), True),
    StructField("dec_parallax_corr", FloatType(), True),
    StructField("dec_pmra_corr", FloatType(), True),
    StructField("dec_pmdec_corr", FloatType(), True),
    StructField("parallax_pmra_corr", FloatType(), True),
    StructField("parallax_pmdec_corr", FloatType(), True),
    StructField("pmra_pmdec_corr", FloatType(), True),
    StructField("astrometric_n_obs_al", IntegerType(), True),
    StructField("astrometric_n_obs_ac", IntegerType(), True),
    StructField("astrometric_n_good_obs_al", IntegerType(), True),
    StructField("astrometric_n_bad_obs_al", IntegerType(), True),
    StructField("astrometric_gof_al", FloatType(), True),
    StructField("astrometric_chi2_al", FloatType(), True),
    StructField("astrometric_excess_noise", DoubleType(), True),
    StructField("astrometric_excess_noise_sig", DoubleType(), True),
    StructField("astrometric_params_solved", ShortType(), True),
    StructField("astrometric_primary_flag", BooleanType(), True),
    StructField("astrometric_weight_al", FloatType(), True),
    StructField("astrometric_pseudo_colour", DoubleType(), True),
    StructField("astrometric_pseudo_colour_error", DoubleType(), True),
    StructField("mean_varpi_factor_al", FloatType(), True),
    StructField("astrometric_matched_observations", DoubleType(), True),
    StructField("visibility_periods_used", ShortType(), True),
    StructField("astrometric_sigma5d_max", FloatType(), True),
    StructField("frame_rotator_object_type", IntegerType(), True),
    StructField("matched_observations", ShortType(), True),
    StructField("duplicated_source", BooleanType(), True),
    StructField("phot_g_n_obs", IntegerType(), True),
    StructField("phot_g_mean_flux", DoubleType(), True),
    StructField("phot_g_mean_flux_error", DoubleType(), True),
    StructField("phot_g_mean_flux_over_error", FloatType(), True),
    StructField("phot_g_mean_mag", FloatType(), True),
    StructField("phot_bp_n_obs", IntegerType(), True),
    StructField("phot_bp_mean_flux", DoubleType(), True),
    StructField("phot_bp_mean_flux_error", DoubleType(), True),
    StructField("phot_bp_mean_flux_over_error", FloatType(), True),
    StructField("phot_bp_mean_mag", FloatType(), True),
    StructField("phot_rp_n_obs", IntegerType(), True),
    StructField("phot_rp_mean_flux", DoubleType(), True),
    StructField("phot_rp_mean_flux_error", DoubleType(), True),
    StructField("phot_rp_mean_flux_over_error", FloatType(), True),
    StructField("phot_rp_mean_mag", FloatType(), True),
    StructField("phot_bp_rp_excess_factor", FloatType(), True),
    StructField("phot_proc_mode", ShortType(), True),
    StructField("bp_rp", FloatType(), True),
    StructField("bp_g", FloatType(), True),
    StructField("g_rp", FloatType(), True),
    StructField("radial_velocity", DoubleType(), True),
    StructField("radial_velocity_error", DoubleType(), True),
    StructField("rv_nb_transits", IntegerType(), True),
    StructField("rv_template_teff", FloatType(), True),
    StructField("rv_template_logg", FloatType(), True),
    StructField("rv_template_fe_h", FloatType(), True),
    StructField("phot_variable_flag", StringType(), True),
    StructField("l", DoubleType(), True),
    StructField("b", DoubleType(), True),
    StructField("ecl_lon", DoubleType(), True),
    StructField("ecl_lat", DoubleType(), True),
    StructField("priam_flags", LongType(), True),
    StructField("teff_val", FloatType(), True),
    StructField("teff_percentile_lower", FloatType(), True),
    StructField("teff_percentile_upper", FloatType(), True),
    StructField("a_g_val", FloatType(), True),
    StructField("a_g_percentile_lower", FloatType(), True),
    StructField("a_g_percentile_upper", FloatType(), True),
    StructField("e_bp_min_rp_val", FloatType(), True),
    StructField("e_bp_min_rp_percentile_lower", FloatType(), True),
    StructField("e_bp_min_rp_percentile_upper", FloatType(), True),
    StructField("flame_flags", LongType(), True),
    StructField("radius_val", FloatType(), True),
    StructField("radius_percentile_lower", FloatType(), True),
    StructField("radius_percentile_upper", FloatType(), True),
    StructField("lum_val", FloatType(), True),
    StructField("lum_percentile_lower", FloatType(), True),
    StructField("lum_percentile_upper", FloatType(), True)

])

df = spark.read.csv("hdfs:/hadoop/gaia/csv/gdr2/gaia_source/*.csv.gz", header=True, schema=gaia_schema, mode="FAILFAST")
df.show()
df.printSchema()
df.write.parquet('hdfs:/hadoop/gaia/parquet/gdr2/gaia_source/')


end = time.time()
print("-- [Ended conversion] --")
print(str(end - start) + " seconds taken" )

sc.stop()

