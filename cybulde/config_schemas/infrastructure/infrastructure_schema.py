from pydantic.dataclasses import dataclass
from hydra.core.config_store import ConfigStore
from omegaconf import SI

from cybulde.config_schemas.infrastructure.instance_group_creator_schema import InstanceGroupCreatorConfig
from typing import Optional

@dataclass
class MLFlowConfig:
    mlflow_external_tracking_uri: str = SI("${oc.env:MLFLOW_TRACKING_URI,localhost:6101}")
    mlflow_internal_tracking_uri: str = SI("${oc.env:MLFLOW_INTERNAL_TRACKING_URI,localhost:6101}")
    experiment_name: str = "default"
    run_name: Optional[str] = "none"
    run_id: Optional[str] = None
    experiment_id: Optional[str] = None
    experiment_url: str = SI("${.mlflow_external_tracking_uri}/#/experiments/${.experiment_id}/runs/${.run_id}")
    artifact_uri: Optional[str] = None 

@dataclass
class InfrastructureConfig:
    project_id: str = "cybulde-427611"
    zone: str = "asia-south1-a"
    mlflow: MLFlowConfig = MLFlowConfig()
    instance_group_creator: InstanceGroupCreatorConfig = InstanceGroupCreatorConfig()
    etcd_ip: Optional[str] = "123"

def setup_config() -> None:
    cs = ConfigStore.instance()
    cs.store(
        name="infrastructure_schema",
        group="infrastructure",
        node=InfrastructureConfig,
    )