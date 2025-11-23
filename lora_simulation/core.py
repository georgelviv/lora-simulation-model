from .models import Config, State

class LoraSimulation():
  def __init__(self, distance):
    self.config: Config = None
    self.distance = distance

  def set_config(self, config: Config) -> None:
    self.config = config

  def get_config(self) -> Config:
    return self.config
  
  def ping(self) -> State:
    return {
      'bytes_per_second': 611.0,
      'chunks_count': 1.0,
      'delay': 151.0,
      'rssi': -32.0,
      'snr': 7.25,
      'time_over_air': 36.0,
      'attempt': 2
    }