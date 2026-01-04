import os
from src.data_science_project import logger
import pandas as pd

from src.data_science_project.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema_keys = self.config.all_schema.keys()
            all_schema = self.config.all_schema
            for col in all_cols:
                if col not in all_schema_keys:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    if data[col].dtype==all_schema[col]:
                        validation_status = True
                    else:
                        validation_status = False
                        logger.info(f'Schema contain the dtpye mismatch for col : {col}')
                        with open(self.config.STATUS_FILE, 'w') as f:
                            f.write(f"Validation status: {validation_status}")
                        break
                        
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            if validation_status:
                logger.info(f'All the schemas are matched')
            else:
                logger.info(f'All the schemas are not matched')
            # import pdb;pdb.set_trace()
            return validation_status

        except Exception as e:
            raise e

    

