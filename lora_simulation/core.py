from .models import Config, State, EnvironmentModel
from .utils import compute_rssi
import logging

class LoraSimulation():
  def __init__(self, logger: logging.Logger, env_model: EnvironmentModel):
    self.config: Config = None
    self.logger = logger
    self.env_model = env_model

  def set_config(self, config: Config) -> None:
    self.config = config

  def get_config(self) -> Config:
    return self.config
  
  def ping(self) -> State:
    freq = self.config.get('FQ')

    self.logger.info(freq)

    # compute_rssi(
    #   distance_m=self.distance_m,
    #   freq_hz=freq
    # )

    return {
      'bytes_per_second': 611.0,
      'chunks_count': 1.0,
      'delay': 151.0,
      'rssi': -32.0,
      'snr': 7.25,
      'time_over_air': 36.0,
      'attempt': 2
    }