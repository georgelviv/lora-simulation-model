import random
import numpy as np
from lora_simulation import Config, LORA_SIMULATION_ENVIRONMENTS, LoraSimulation

def test_lora_simulation():
  random.seed(1)
  np.random.seed(1)

  lora_sim = LoraSimulation(env_model=LORA_SIMULATION_ENVIRONMENTS['open_field'])
  lora_config: Config = {
    "SF": 12,
    "FQ": 878,
    "BW": 500.0,
    "CR": 8.0,
    "TP": 20,
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
    'BPS': 611.0,
    'CHC': 1.0,
    'DELAY': 840.7,
    'RSSI': -66.61333507831323,
    'SNR': 10.75,
    'TOA': 36.0,
    'ATT': 1
  }