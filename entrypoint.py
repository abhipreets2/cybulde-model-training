
from omegaconf import OmegaConf

from cybulde.utils.config_utils import get_config
from cybulde.utils.utils import get_logger
from cybulde.config_schemas.config_schema import Config

@get_config(config_path="../configs", config_name="config")
def entrypoint(config: Config) -> None:
    logger = get_logger(__file__)
    print(OmegaConf.to_yaml(config))



if __name__ == "__main__":
    entrypoint()
