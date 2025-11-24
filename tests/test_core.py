import random
import numpy as np
from lora_simulation import LoraSimulation
from lora_simulation import Config

def test_lora_simulation():
  random.seed(1)
  np.random.seed(1)

  lora_sim = LoraSimulation()
  lora_config: Config = {
    "SF": 8.0,
    "FQ": 878,
    "BW": 125.0,
    "CR": 8.0,
    "TP": 10.0,
    "IH": 0.0,
    "HS": 10.0,
    "PL": 10.0,
    "CL": 45.0,
    "RT": 1.0
  }
  lora_sim.set_config(
    lora_config
  )

  assert lora_sim.get_config() == lora_config

  assert lora_sim.ping() == {
    'bytes_per_second': 611.0,
    'chunks_count': 1.0,
    'delay': 151.0,
    'rssi': -73.67181149044961,
    'snr': 7.25,
    'time_over_air': 36.0,
    'attempt': 2
  }