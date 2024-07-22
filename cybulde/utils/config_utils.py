import hydra
import yaml
import logging

from hydra.types import TaskFunction
from omegaconf import DictConfig, OmegaConf

from typing import Any, Optional

from cybulde.config_schemas import config_schema

def get_config(
    config_path: str, config_name: str, to_object: bool = True, return_dict_config: bool = False
) -> TaskFunction:
    setup_config()
    setup_logger()

    def main_decorator(task_function: TaskFunction) -> Any:
        @hydra.main(config_path=config_path, config_name=config_name, version_base=None)
        def decorated_main(dict_config: Optional[DictConfig] = None) -> Any:
            if to_object:
                config = OmegaConf.to_object(dict_config)

            if not return_dict_config:
                assert to_object
                return task_function(config)
            return task_function(dict_config)

        return decorated_main

    return main_decorator


def setup_config() -> None:
    config_schema.setup_config()


def setup_logger() -> None:
    with open("./cybulde/configs/hydra/job_logging/custom.yaml", "r") as stream:
        config = yaml.load(stream, Loader=yaml.FullLoader)
    logging.config.dictConfig(config)
