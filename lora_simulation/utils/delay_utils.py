DELAY_COEF_500 = {
  12: (684, 15.67),
  11: (338, 8.45),
  10: (183, 4.64),
  9:  (100, 2.54),
  8:  (59,  1.43),
  7:  (30,  0.83),
  6:  (60,  0.59),
}

def lora_delay_ms(
  sf: int,
  bw_hz: float,
  payload_bytes: int,
  cr: int = 8,
):
  base_delay, per_byte = DELAY_COEF_500[sf]

  if bw_hz == 250_000:
    bw_scale = 2.2
  elif bw_hz == 125_000:
    bw_scale = 4.4
  else:
    bw_scale = 1.0

  cr_scale = cr / 8.0

  delay = (base_delay + per_byte * payload_bytes) * bw_scale * cr_scale

  return round(delay, 2)
