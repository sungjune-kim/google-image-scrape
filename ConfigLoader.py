#!/usr/bin/env python
# coding: utf-8

import os
import yaml

config_fp = os.path.join(os.path.dirname(__file__),'config.yml')
config = yaml.load(open(config_fp,'r'))

config_driver = config['driver']
config_save = config['save']