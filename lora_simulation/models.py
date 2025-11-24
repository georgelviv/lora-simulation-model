from typing import TypedDict
from dataclasses import dataclass

class State(TypedDict):
  DELAY: float
  RSSI: float
  SNR: float
  TOA: float
  BPS: float
  CHC: float
  ATT: float

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
  distance_m: float  
  description: str = "" 