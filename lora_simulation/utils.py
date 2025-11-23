import math

def path_loss(
  distance_m: float, # distance
  freq_hz: float, # frequency
  pl_d0: float, # loss at 1 meter
  d0: float, # reference distance
  n: float, #  path loss exponent
) -> float:
  if distance_m < d0:
    distance_m = d0

  pl = pl_d0 + 10 * n * math.log10(distance_m / d0)
  return pl