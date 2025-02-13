**We chose AWS DMS over other ETL tools like AWS Glue or AWS Data Pipeline because:**

✅ Real-Time CDC Support – AWS DMS provides low-latency Change Data Capture (CDC), making it ideal for continuously syncing MySQL (binlog) and MongoDB (oplog) 
changes to S3.
✅ Minimal Overhead – Unlike AWS Glue, which requires ETL transformations, AWS DMS performs direct migrations without extra processing, making it faster and 
cost-effective for this use case.
✅ Automated Schema Conversion – DMS automatically handles schema mapping, reducing manual effort in migrations.
✅ No-Code Managed Service – Unlike AWS Data Pipeline, which requires more manual setup, AWS DMS is a fully managed service with built-in fault tolerance and 
monitoring.

**Taking care of Large dataset migration using AWS DMS?**
Use Parallel Full Load & CDC (Change Data Capture) Efficiently
✔ Enable Parallel Load:

Use multiple replication tasks instead of a single task to distribute load.
Increase table loading threads (MaxFullLoadSubTasks).
✔ Optimize CDC:

Reduce LOB handling (Limited LOB mode for better performance).
Use Log-Based CDC instead of query-based CDC.

**Common issues faced during DMS Migration?**
**High Latency in CDC (Change Data Capture)**
Issue: CDC replication lag increases (CDCLatencySource, CDCLatencyTarget).
Fix:

Increase replication instance size (r5.xlarge or higher).
Enable parallel apply (ParallelApplyThreads) for faster writes.

**Full Load Stuck or Slow**
Issue: Full load is extremely slow or hangs.
Fix:

Increase MaxFullLoadSubTasks to load multiple tables in parallel.
Disable indexes & constraints on the target database during migration.
Use AWS S3 as an intermediate storage for large datasets.

 **Limitations in AWS DMS**

Dropping columns, renaming tables, or changing primary keys are NOT supported automatically.
DMS only captures schema changes if the target supports it (e.g., RDS, Aurora).
We need to perform this manually
