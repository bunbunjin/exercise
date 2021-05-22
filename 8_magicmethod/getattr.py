import json


class Config:
    def __init__(self, filename):
        self.config = json.load(open(filename))

    def __getattr__(self, name):
        if name in self.config:
            return self.config[name]
        raise AttributeError()


conf = Config('config.json')
print(conf.url)
print(conf.name)
