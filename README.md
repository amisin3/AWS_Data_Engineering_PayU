# AWS Data Engineering Project at PayU
**Related Articles**
https://techblog.lazypay.in/big-data-bigger-savings-a-million-dollar-success-story-95fb141431a7
https://techblog.lazypay.in/unlock-the-power-of-airflow-external-task-sensor-for-any-cron-schedules-b42c34b09fd7
https://techblog.lazypay.in/revolutionizing-statement-generation-at-lazypay-227c9332eb1d

# In PayU the ETL structure
# Extract -
Different Databases sources like SQL, NoSQL, File based system, Different clouds, Kafka using
AWS DMS we used for extracting the data from SQL(MySQL) and NoSQL(MongoDB)
Initially there was full_load and after that we were using CDC(change data capture)
For CDC - MySQL(Binary Log), MongoDB(OpLog)
For monitoring we were using the AWS DMS Console
Using Terraform in AWS DMS
AWS DMS CDC Frequency is around 5 seconds default. Once the data was available in transient-bucket(bronze
layer) using AWS DMS (Full_Load+CDC) (Realtime Sync) (No transformations was performed).

**Summary**
**Source Databases** - SQL (MySQL), NoSQL (MongoDB)
**Migration Engine** - AWS DMS (Full_Load + CDC (binary log, oplog)) written in Terraform
**Target Databases** - AWS S3 (Transient_bucket or Bronze Layer)
**Fault Tolerance** - AWS DMS, S3 takes care by using checksum
**Syncing of Data** - Realtime
**Throughput** - 
**Challenges faced** - Mentioned in the AWS DMS
**Cost for migrating one tables** - 
**Format of targeted files** - Parquet

# Transform -
Later we had an Airflow job which used to extract the data from the transient_bucket. We used pyspark for
performing transformation and then dumping the data to AWS trusted_bucket. This was near-realtime data
because we don't sync the transient_data in realtime we run different airflow jobs for bringing the data
on a frequency of daily and hourly. Our trusted-bucket was the silver layer where we performed most of the
transformations and cleaning. Here we also provided the access to read the trusted-bucket data using AWS
Athena which gets created by Airflow in runtime. Since this are just S3 files we faced the issue related
to the duplicate records because we are performing append. We use another Service named Apache Huidi for
performing deduplication on the records which was intermediate layer between AWS S3 and AWS Athena. So
whenever someone used to run a query on AWS Athena they used to get non-duplicate records.
Later we also had another layer of transformations where we performed business logic directly on the
trusted_bucket and store the results in the consumer bucket for this also we used Airflow jobs and spark
for scheduling and transformations.
# Load -




