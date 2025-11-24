from typing import TypedDict
from dataclasses import dataclass

class State(TypedDict):
  delay: int
  rssi: int
  snr: float
  time_over_air: int
  bytes_per_second: int
  chunks_count: int

class Config(TypedDict):
  SF: int
  FQ: int
  BW: int
  CR: int
  TP: int
  IH: int
  HS: int
  PL: int
  CL: int
  RT: int

@dataclass
class EnvironmentModel:
  name: str
  path_loss_exponent: float
  shadow_sigma_db: float
  description: str = ""   