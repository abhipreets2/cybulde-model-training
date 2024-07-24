from omegaconf import OmegaConf
from hydra.utils import instantiate
import os

from cybulde.utils.config_utils import get_config
from cybulde.utils.utils import get_logger
from cybulde.config_schemas.config_schema import Config


@get_config(config_path="../configs", config_name="config")
def entrypoint(config: Config) -> None:
    os.environ["HYDRA_FULL_ERROR"] = "1"
    logger = get_logger(__file__)
    print(OmegaConf.to_yaml(config))
    
    #instance_group_creator = instantiate(config.infrastructure.instance_group_creator)
    #instance_ids = instance_group_creator.launch_instance_group()
if __name__ == "__main__":
    entrypoint()
