"""
Values for minecraft data
"""

import yaml
from logger import logger

with open('packet.yml', 'rb') as packet_stream:
    packet = yaml.load(packet_stream, Loader=yaml.CLoader)

with open('state.yml', 'rb') as state_stream:
    state = yaml.load(state_stream, Loader=yaml.CLoader)
