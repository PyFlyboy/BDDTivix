from configparser import ConfigParser


def read_conf(key):
    config = ConfigParser()
    config.read(".\\Config\\conf.ini")
    return config.get(key)
