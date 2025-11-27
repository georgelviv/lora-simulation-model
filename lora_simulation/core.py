from .models import Config, State, EnvironmentModel
from .utils import (
  lora_rssi_hata_chip, lora_snr_chip, lora_log,
  lora_delay_ms, chunks_count, lora_time_on_air_ms
)
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
    self.logger.info(lora_log("CONFIG_SYNC", config))
    self.config = config

  def get_config(self) -> Config:
    return self.config
  
  def ping(self) -> State:
    freq = self.config.get('FQ') * 10e6
    tx_power_dbm = self.config.get('TP')
    sf = self.config.get('SF')
    bw = self.config.get('BW') * 10e3
    cr = self.config.get('CR')
    ih = self.config.get('IH')
    pl = self.config.get('PL')

    payload_size = 10

    rssi_chip = lora_rssi_hata_chip(
      distance_m=self.env_model.distance_m,
      freq_hz=freq,
      tx_power_dbm=tx_power_dbm,
      shadow_sigma_db=self.env_model.shadow_sigma_db,
      hb_m=self.env_model.hb_m,
      hm_m=self.env_model.hm_m,
      area=self.env_model.area_type,
      sf=sf
    )

    snr_chip = lora_snr_chip(
      rssi_dbm=rssi_chip,
      bw_hz=bw,
      area=self.env_model.area_type,
      sigma_noise_db=self.env_model.sigma_noise_db
    )

    delay = lora_delay_ms(
      sf=sf,
      bw_hz=bw,
      payload_bytes=payload_size,
      cr=cr
    )

    state: State = {
      'BPS': 611.0,
      'CHC': chunks_count(payload_size, ih, pl),
      'DELAY': delay,
      'RSSI': rssi_chip,
      'SNR': snr_chip,
      'TOA': lora_time_on_air_ms(sf, bw, payload_size, cr, pl),
      'ATT': 1
    }

    self.logger.info(lora_log("PING", state))

    return state