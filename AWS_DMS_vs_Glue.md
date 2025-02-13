**We chose AWS DMS over other ETL tools like AWS Glue or AWS Data Pipeline because:**

✅ Real-Time CDC Support – AWS DMS provides low-latency Change Data Capture (CDC), making it ideal for continuously syncing MySQL (binlog) and MongoDB (oplog) 
changes to S3.
✅ Minimal Overhead – Unlike AWS Glue, which requires ETL transformations, AWS DMS performs direct migrations without extra processing, making it faster and 
cost-effective for this use case.
✅ Automated Schema Conversion – DMS automatically handles schema mapping, reducing manual effort in migrations.
✅ No-Code Managed Service – Unlike AWS Data Pipeline, which requires more manual setup, AWS DMS is a fully managed service with built-in fault tolerance and 
monitoring.
