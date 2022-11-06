import os
import kopf
import kubernetes
import yaml

CRD_NAME = "easy-faas.serverless"
CRD_VERSION = "v1"
KIND = "functions"

@kopf.on.create(CRD_NAME, CRD_VERSION, KIND)
def create(name, spec, namespace, logger, **kwargs):
    logger.info(f"Function {name} is created")


