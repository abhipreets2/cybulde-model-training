from pydantic.dataclasses import dataclass
from hydra.core.config_store import ConfigStore
from typing import Optional

from cybulde.config_schemas.infrastructure import infrastructure_schema

@dataclass
class Config:
    infrastructure: infrastructure_schema.InfrastructureConfig = infrastructure_schema.InfrastructureConfig()
    docker_image: Optional[str] = None 



def setup_config() -> None:
    infrastructure_schema.setup_config()
    cs = ConfigStore.instance()
    cs.store(name="config_schema", node=Config)
