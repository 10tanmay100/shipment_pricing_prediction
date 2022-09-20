
from supply_chain_.config.configuration import Configuration
from supply_chain_.pipeline.pipeline import Pipeline
def run():
    p=Configuration
    # print(p.get_data_validation_config())
    pipe=Pipeline(p)
    return pipe.run_pipeline()

run()
