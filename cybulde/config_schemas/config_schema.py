from pydantic.dataclasses import dataclass
from hydra.core.config_store import ConfigStore

@dataclass
class Config:
    test: int = 123

def setup_config() -> None:

    cs = ConfigStore.instance()
    cs.store(name="config_schema", node=Config)
