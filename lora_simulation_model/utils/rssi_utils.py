import math
import random
from ..models import AreaType

def hata_mobile_correction(f_mhz: float, hm_m: float, large_city: bool) -> float:
  if large_city:
    return 3.2 * (math.log10(11.75 * hm_m))**2 - 4.97
  return (1.1 * math.log10(f_mhz) - 0.7) * hm_m - (1.56 * math.log10(f_mhz) - 0.8)

def path_loss_hata_lora(
  distance_m: float,
  freq_hz: float,
  hb_m: float,
  hm_m: float,
  area: AreaType
) -> float:
    f_mhz = freq_hz / 1e6
    d_km = max(distance_m / 1000.0, 0.01)

    large_city = area == AreaType.LARGE_URBAN
    a_hm = hata_mobile_correction(f_mhz, hm_m, large_city)

    pl = (
        46.3
        + 33.9 * math.log10(f_mhz)
        - 13.82 * math.log10(hb_m)
        - a_hm
        + (44.9 - 6.55 * math.log10(hb_m)) * math.log10(d_km)
    )

    if area == AreaType.SUBURBAN:
        pl -= 2 * (math.log10(f_mhz / 28))**2 - 5.4
    elif area == AreaType.RURAL:
        pl -= (
            4.78 * (math.log10(f_mhz))**2
            - 18.33 * math.log10(f_mhz)
            + 40.94
        )

    return pl

def compute_rssi_hata_lora(
  distance_m: float,
  freq_hz: float,
  tx_power_dbm: float,
  shadow_sigma_db: float,
  hb_m: float,
  hm_m: float,
  area: AreaType
) -> float:
  pl = path_loss_hata_lora(
    distance_m,
    freq_hz,
    hb_m,
    hm_m,
    area,
  )

  shadowing = random.gauss(0.0, shadow_sigma_db)

  return tx_power_dbm - pl + shadowing

def lora_rssi_hata_chip(
  distance_m: float,
  freq_hz: float,
  tx_power_dbm: float,
  shadow_sigma_db: float,
  hb_m: float,
  hm_m: float,
  area: AreaType
) -> float:
  rssi = compute_rssi_hata_lora(
    distance_m,
    freq_hz,
    tx_power_dbm,
    shadow_sigma_db,
    hb_m,
    hm_m,
    area,
  )

  chip_noise = random.uniform(-0.8, 0.8)

  return round(rssi + chip_noise, 2)
