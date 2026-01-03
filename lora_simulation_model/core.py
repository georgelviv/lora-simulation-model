from .models import Config, State, EnvironmentModel
from .utils import (
  lora_rssi_hata_chip, compute_snr, lora_log,
  lora_delay_ms, chunks_count, lora_time_on_air_ms,
  bytes_per_second, rtoa_ms
)
import logging
from .logger import default_logger
from .environment import LORA_SIMULATION_ENVIRONMENTS

class LoraSimulationModel():

  def __init__(
      self, logger: logging.Logger = default_logger, 
      env_model: EnvironmentModel = LORA_SIMULATION_ENVIRONMENTS['open_field']
    ):
    self.config: Config = None
    self.logger = logger
    self.env_model = env_model

  async def start(self):
    pass

  async def stop(self):
    pass

  async def config_sync(self, id: int, params: Config) -> bool:
    self.logger.info(lora_log("CONFIG_SYNC", params))
    self.config = params
    return True

  async def config_get(self) -> Config:
    return self.config
  
  async def ping(self, id: int) -> State:
    freq = self.config.get('FQ') * 10e6
    tx_power_dbm = self.config.get('TP')
    sf = self.config.get('SF')
    bw = self.config.get('BW') * 1000
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
      area=self.env_model.area_type
    )

    # snr_chip = lora_snr_chip(
    #   rssi_dbm=rssi_chip,
    #   bw_hz=bw,
    #   area=self.env_model.area_type,
    #   sigma_noise_db=self.env_model.sigma_noise_db
    # )

    snr_chip = compute_snr(
      rssi_dbm=rssi_chip,
      sf=sf,
      bw_hz=bw
    )

    delay = lora_delay_ms(
      sf=sf,
      bw_hz=bw,
      payload_bytes=payload_size,
      cr=cr
    )

    toa = lora_time_on_air_ms(sf, bw, payload_size, cr, pl)
    rtoa = rtoa_ms(toa_ms=toa, sf=sf, bw_hz=bw)

    state: State = {
      'BPS': bytes_per_second(payload_size, toa),
      'CHC': chunks_count(payload_size, ih, pl),
      'DELAY': delay,
      'RSSI': rssi_chip,
      'SNR': snr_chip,
      'RTOA': rtoa,
      'TOA': toa,
      'ETX': 1,
      'ATT': 1
    }

    state = { key: round(value, 3) if isinstance(value, (float, int)) else value for key, value in state.items() }

    self.logger.info(lora_log("PING", state))

    return state
