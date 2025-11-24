import math
import numpy as np
import random

def pl_d0_friis(freq_hz: float, d0: float = 1.0) -> float:
  """
  Computes path loss PL(d0) at the reference distance using Friis equation.
  PL(d0) = 20 log10(4π d0 / λ)
  λ = c / f
  """
  c = 3e8
  wavelength = c / freq_hz
  return 20 * math.log10(4 * math.pi * d0 / wavelength)

def path_loss(
  distance_m: float, # distance
  pl_d0: float, # loss at 1 meter
  d0: float, # reference distance
  n: float, #  path loss exponent
) -> float:
  if distance_m < d0:
    distance_m = d0

  pl = pl_d0 + 10 * n * math.log10(distance_m / d0)
  return pl

def shadowing(sigma_db: float) -> float:
  return random.gauss(0, sigma_db)

def rayleigh_fading_db() -> float:
  r = np.random.rayleigh(1.0)
  fading_db = 20 * math.log10(r)
  return fading_db

def compute_rssi(
  distance_m: float,
  freq_hz: float,
  d0: float,
  n: float,
  tx_power_dbm: float,
  shadow_sigma_db: float
) -> float:
    
  pl_d0 = pl_d0_friis(freq_hz, d0)
  pl = path_loss(distance_m, pl_d0, d0, n)
  sh = shadowing(shadow_sigma_db)
  ff = rayleigh_fading_db()
  rssi = tx_power_dbm - pl + sh + ff

  return rssi