from collections import namedtuple


DataIngestionArtifact = namedtuple("DataIngestionArtifact",
["raw_data_file_path","is_ingested","message"])


DataValidationArtifact = namedtuple("DataValidationArtifact",
["validate_csv_path","is_validated","message"])

DataTransformationArtifact = namedtuple("DataTransformationArtifact",
["is_transformed", "message", "transformed_train_file_path","transformed_test_file_path","preprocessed_object_file_path"])