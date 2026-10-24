# from databricks.sdk import WorkspaceClient
# w = WorkspaceClient()
# print(w.current_user.me().user_name)
# print(len(list(w.jobs.list(limit=5))), "jobs visible")

# ---if already installed, you can check the version of the Databricks CLI by running:
from databricks.connect import DatabricksSession
spark = DatabricksSession.builder.getOrCreate()
print(spark.range(3).collect())