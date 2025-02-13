Apache Parquet is a columnar storage format optimized for analytics workloads. It efficiently stores large datasets with compression, encoding, and schema 
evolution support, making it ideal for big data processing.

**Parquet File Architecture
Parquet follows a hierarchical structure:
**
**File**
The entire data is stored in a single Parquet file.

**Row Groups**

A file is divided into multiple row groups, each containing multiple rows.
Each row group is processed independently, allowing parallel reads.

**Column Chunks**

Inside a row group, data is stored column-wise instead of row-wise.
Columnar storage allows efficient compression and fast column-based queries.

**Pages**

Each column chunk is further divided into pages.
Pages store actual data and metadata (e.g., encoding and dictionary compression).

**Advantages of Parquet**
✔ Columnar Storage → Faster queries on selected columns.
✔ Efficient Compression → Uses encoding (e.g., Snappy, Gzip) to reduce file size.
✔ Schema Evolution → Supports adding/removing columns dynamically.
✔ Optimized for Big Data → Works well with Spark, Hive, AWS Athena, Redshift, and Dremio.
