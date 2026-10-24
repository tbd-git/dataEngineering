Run the following commands to set up your environment:
Databricks CLI:
winget search databricks
winget install Databricks.DatabricksCLI

databricks auth login --host <workspace_url>

pip install langchain langgraph databricks-sdk databricks-langchain mlflow langgraph-checkpoint-postgres pydantic databricks-connect\

AWS CLI:
 After installing the AWS CLI, configure it with your credentials:
run with "aws login" command and follow the prompts to enter your AWS Access Key ID, Secret Access Key, and default region.