import json
from dataclasses import dataclass
import dataclasses
import os

FILE_LOC = '/home/app/config/config.json'


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


@dataclass
class Config(object):
    service_config: dict
    local_service_config: dict
    external_ip: str
    user_name: str


class ServiceConfig(object):
    def __init__(self):
        self.services = None
        with open(FILE_LOC, 'r') as f:
            data = json.load(f)
            self.services = Config(**data)

    def _save(self):
        with open(FILE_LOC, 'w') as f:
            jsonstr = json.dumps(self.services, cls=EnhancedJSONEncoder)
            f.write(jsonstr)

    def save_service(self, name, instance):
        self.services.service_config[name] = instance
        self._save()

    def save_local_service(self, name, instance):
        self.services.local_service_config[name] = instance
        self._save()

    def save_external_ip(self, ip):
        self.services.external_ip = ip
        self._save()

    def save_user_name(self, user_name):
        self.services.user_name = user_name
        self._save()


sc = ServiceConfig()
