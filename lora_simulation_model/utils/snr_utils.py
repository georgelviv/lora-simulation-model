import math

G_SF = {
    6: 0.0,
    7: 2.2565851920,
    8: 3.5673078273,
    9: 3.9262238744,
    10: 3.8311772339,
    11: 2.6879371816,
    12: 2.2690226187,
}

B0 = 73.2218241505
B1 = 0.2351399215          # * RSSI_dBm
B2 = -8.7495916402         # * log10(BW_Hz)

def compute_snr(rssi_dbm: float, sf: int, bw_hz: float) -> float:
    return B0 + B1 * rssi_dbm + B2 * math.log10(bw_hz) + G_SF.get(sf, 0.0)
