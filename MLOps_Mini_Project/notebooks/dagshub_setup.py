import mlflow
import dagshub


mlflow.set_tracking_uri("https://dagshub.com/preeti.sahay5182/MLOps-_Mini_Project.mlflow")
dagshub.init(repo_owner='preeti.sahay5182', repo_name='MLOps-_Mini_Project', mlflow=True)

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)