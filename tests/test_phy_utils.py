from lora_simulation.utils import (
  path_loss, compute_rssi, lora_snr_chip,
  lora_delay_ms, chunks_count, lora_time_on_air_ms,
  bytes_per_second
)
from lora_simulation.models import AreaType
import random
import numpy as np

def test_path_loss():
  assert path_loss(
    distance_m=1,
    pl_d0=1.0,
    d0=32.4,
    path_loss_exponent=2.7
  ) == 1

  assert path_loss(
    distance_m=100,
    pl_d0=32.4,
    d0=1.0,
    path_loss_exponent=2.7
  ) == 86.4

  assert path_loss(
    distance_m=100,
    pl_d0=32.4,
    d0=1.0,
    path_loss_exponent=4
  ) == 112.4

  assert path_loss(
    distance_m=100,
    pl_d0=10,
    d0=1.0,
    path_loss_exponent=4
  ) == 90

def test_compute_rssi():
  random.seed(1)
  np.random.seed(1)
  assert compute_rssi(500, 868e6, 1, 2, 10, 2) == -72.28413092270193


def test_lora_snr_chip():
  random.seed(1)
  np.random.seed(1)

  assert lora_snr_chip(-66, 500e3, AreaType.LARGE_URBAN, 2.0) == 10.5
  assert lora_snr_chip(-80, 500e3, AreaType.LARGE_URBAN, 2.0) == 9.5
  assert lora_snr_chip(-80, 1250e3, AreaType.LARGE_URBAN, 2.0) == 7.25
  assert lora_snr_chip(-80, 1250e3, AreaType.LARGE_URBAN, 2.0) == 5.5

def test_lora_delay_ms():
  assert lora_delay_ms(10, 500e3, 1000, 8) == 4823.0
  assert lora_delay_ms(10, 500e3, 10, 8) == 229.4

def test_chunks_count():
  assert chunks_count(10) == 1
  assert chunks_count(1000) == 5
  assert chunks_count(1000, True, 100) == 10


def test_lora_time_on_air_ms():
  assert lora_time_on_air_ms(12, 500e3, 10) == 314
  assert lora_time_on_air_ms(12, 500e3, 1024) == 13749
  assert lora_time_on_air_ms(12, 125e3, 1024) == 54996.0
  assert lora_time_on_air_ms(6, 125e3, 1024) == 1708

def test_bytes_per_second():
  assert bytes_per_second(1000, 1) == 1
  assert bytes_per_second(100, 1) == 0.1