from .utils import path_loss, compute_rssi
import random
import numpy as np

def test_path_loss():
  assert path_loss(
    distance_m=1,
    pl_d0=1.0,
    d0=32.4,
    n=2.7
  ) == 1

  assert path_loss(
    distance_m=100,
    pl_d0=32.4,
    d0=1.0,
    n=2.7
  ) == 86.4

  assert path_loss(
    distance_m=100,
    pl_d0=32.4,
    d0=1.0,
    n=4
  ) == 112.4

  assert path_loss(
    distance_m=100,
    pl_d0=10,
    d0=1.0,
    n=4
  ) == 90

def test_compute_rssi():
  random.seed(1)
  np.random.seed(1)
  assert compute_rssi(500, 868e6, 1, 2, 10, 2) == -72.28413092270193