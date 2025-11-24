from .models import Config, State, EnvironmentModel
from .phy_utils import compute_rssi
import logging
from .logger import default_logger
from .environment import LORA_SIMULATION_ENVIRONMENTS

class LoraSimulation():
  def __init__(
      self, logger: logging.Logger = default_logger, 
      env_model: EnvironmentModel = LORA_SIMULATION_ENVIRONMENTS['open_field']
    ):
    self.config: Config = None
    self.logger = logger
    self.env_model = env_model

  def set_config(self, config: Config) -> None:
    self.config = config

  def get_config(self) -> Config:
    return self.config
  
  def ping(self) -> State:
    freq = self.config.get('FQ') * 10e6
    tx_power_dbm = self.config.get('TP')

    rssi = compute_rssi(
      distance_m=self.env_model.distance_m,
      freq_hz=freq,
      d0=1,
      path_loss_exponent=self.env_model.path_loss_exponent,
      tx_power_dbm=tx_power_dbm,
      shadow_sigma_db=self.env_model.shadow_sigma_db
    )

    return {
      'bytes_per_second': 611.0,
      'chunks_count': 1.0,
      'delay': 151.0,
      'rssi': rssi,
      'snr': 7.25,
      'time_over_air': 36.0,
      'attempt': 2
    }