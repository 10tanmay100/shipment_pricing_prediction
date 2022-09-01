from collections import namedtuple

DataIngestionConfig=namedtuple("DataIngestionConfig",
["raw_data_dir","ingested_train_dir","ingested_test_dir"])

#DataValidationConfig
DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path","report_file_path","report_page_file_path"])





#datapipelineconfig
TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])