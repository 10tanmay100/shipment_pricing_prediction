from collections import namedtuple

DataIngestionConfig=namedtuple("DataIngestionConfig",
["raw_data_dir"])

#DataValidationConfig
DataValidationConfig = namedtuple("DataValidationConfig", ["raw_data_path"])

#DataTransformationConfig
DataTransformationConfig=namedtuple("DataTransformationConfig",
["transformed_train_dir","transformed_test_dir","preprocessed_object_folder_path",
"preprocessed_object_file_path"])



#datapipelineconfig
TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])