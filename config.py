import os

from env_reader import read_env

env = read_env()

ICON_FILE = os.path.realpath(env['ICON_FILE'])
