from omegaconf import OmegaConf
from hydra.utils import instantiate
import os

from cybulde.utils.config_utils import get_config
from cybulde.utils.utils import get_logger
from cybulde.config_schemas.config_schema import Config
from cybulde.utils.mlflow_utils import activate_mlflow

import torch
from cybulde.utils.torch_utils import get_local_rank

@get_config(config_path="../configs", config_name="config")
def entrypoint(config: Config) -> None:
    os.environ["HYDRA_FULL_ERROR"] = "1"
    logger = get_logger(__file__)
    with activate_mlflow(
            experiment_name=config.infrastructure.mlflow.experiment_name,
            run_id=config.infrastructure.mlflow.run_id,
            run_name=config.infrastructure.mlflow.run_name
            ) as run:
        run_id = run.info.run_id
        experiment_id = run.info.experiment_id
        artifact_uri = run.info.artifact_uri

    config.infrastructure.mlflow.run_id = run_id
    config.infrastructure.mlflow.experiment_id = experiment_id
    config.infrastructure.mlflow.artifact_uri = artifact_uri

    print(OmegaConf.to_yaml(config))

    assert config.infrastructure.mlflow.run_id is not None, "Run ID has not been set"
    
    backend = "gloo"
    if torch.cuda.is_available():
        torch.cuda.set_device(f"cuda:{get_local_rank()}")
        backend = "nccl"
    print(backend)
    torch.distributed.init_process_group(backend=backend)

    #Add tasks
    #instance_group_creator = instantiate(config.infrastructure.instance_group_creator)
    #instance_ids = instance_group_creator.launch_instance_group()
if __name__ == "__main__":
    entrypoint()
