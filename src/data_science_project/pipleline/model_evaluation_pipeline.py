import mlflow
import fix_ssl
from src.data_science_project.config.configuration import ConfigurationManager
from src.data_science_project.components.model_evaluation import ModelEvaluation
import os
fix_ssl.apply_ssl_fix()
# Set BEFORE importing mlflow
os.environ['MLFLOW_TRACKING_INSECURE_TLS'] = 'true'
mlflow.set_tracking_uri("https://dagshub.com/MadarwalaHussain/datascienceproject.mlflow")
os.environ['REQUESTS_CA_BUNDLE'] = ''  # Disable for requests library


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.log_into_mlflow()


        except Exception as e:
            raise e
