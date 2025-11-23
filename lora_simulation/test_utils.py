from .utils import path_loss

def test_estimate_tx_current():
    assert path_loss(
      distance_m=1,
      freq_hz=868e6,
      pl_d0=1.0,
      d0=32.4,
      n=2.7
    ) == 1

    assert path_loss(
      distance_m=100,
      freq_hz=868e6,
      pl_d0=32.4,
      d0=1.0,
      n=2.7
    ) == 86.4

    assert path_loss(
      distance_m=100,
      freq_hz=868e6,
      pl_d0=32.4,
      d0=1.0,
      n=4
    ) == 112.4

    assert path_loss(
      distance_m=100,
      freq_hz=900e6,
      pl_d0=10,
      d0=1.0,
      n=4
    ) == 90