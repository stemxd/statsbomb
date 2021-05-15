# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

X = 120
Y = 80

match_id_req = 69301

file_name = str(match_id_req)+'.json'

with open(''+file_name) as data_file:
    data = json.load(data_file)
    
from pandas.io.json import json_normalize
df = json_normalize(data, sep = "_").assign(match_id = file_name[:])
