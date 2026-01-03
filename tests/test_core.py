import random
import numpy as np
import pytest
from lora_simulation_model import Config, LORA_SIMULATION_ENVIRONMENTS, LoraSimulationModel, State

@pytest.mark.asyncio
async def test_lora_simulation():
  random.seed(1)
  np.random.seed(1)

  lora_sim = LoraSimulationModel(env_model=LORA_SIMULATION_ENVIRONMENTS['open_field'])
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
  await lora_sim.config_sync(
    1, 
    lora_config
  )

  cfg = await lora_sim.config_get()
  assert cfg == lora_config

  state = await lora_sim.ping(1)

  assert state == {
    'BPS': 31.847,
    'CHC': 1.0,
    'DELAY': 840.7,
    'RSSI': -66.613,
    'SNR': 10.25,
    'TOA': 314,
    'ATT': 1,
    'ETX': 1, 
    'RTOA': 379.536
  }