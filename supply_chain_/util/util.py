import yaml
from supply_chain_.exception import supply_chain_exception
import pandas as pd
import numpy as np
import sys


def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise supply_chain_exception(e,sys) from e


def pandas_factory(colnames, rows):
    return pd.DataFrame(rows, columns=colnames)