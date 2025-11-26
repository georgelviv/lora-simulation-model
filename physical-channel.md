
# Physical Channel

## RSSI

```latex
RSSI=Ptx​−PL(d)+S+F
```
Where:
- Ptx - transmit power
- PL - Path loss
- S - shadowing
- F - Fast Fading

### Path Loss
Path loss represents the large-scale, deterministic attenuation of a radio signal as it propagates through space. It mainly depends on distance and the environment. Path loss defines the average received power without considering random effects such as obstacles or multipath reflections.

```latex
PL(d) = PL(d_0) + 10n\log_{10}\left(\frac{d}{d_0}\right)
```

Where:
- PL(d): path loss at distance 
- PL(d0): loss at reference distance d0
- n: path loss exponent
- d0 - reference distance (often 1 m)
- d - distance between Tx and Rx

#### Path Loss Exponent
- Free space - `2.0`
- Rural area - `2.2 - 2.4`
- Suburban - `2.4 - 2.7`
- Urban - `2.7 - 4.0`
- Industrial - `4.0 - 7.0`

#### Friis Free-Space Path Loss
Friis Free-Space Path Loss (FSPL) describes the theoretical attenuation of a radio signal propagating in ideal free space without obstacles, reflections, or absorption.
It provides the reference starting point for more realistic propagation models such as log-distance, shadowing, and fading.
 
Higher frequency → shorter wavelength → more loss.

```Latex
PL(d_0) = 20 \log_{10}\left( \frac{4 \pi d_0}{\lambda} \right)
\lambda = \frac{c}{f}
```

### Shadowing (Slow Fading)
Shadowing models slow, random variations of the received signal caused by large obstacles such as buildings, walls, or trees. It changes over tens or hundreds of meters and causes the signal level to fluctuate around the average path loss.

```Latex
PL_{\text{shadow}}(d) = PL(d) + X_{\sigma}
X_{\sigma} \sim \mathcal{N}(0, \sigma^2)
```

#### Sigma
- No obstacles (open field) - `0 - 1 dB`
- Light outdoor clutter (trees, cars) - `1 - 3 dB`
- Suburban - `3 - 5 dB`
- Urban - `5 - 8 dB`
- Indoor environment - `4 - 12 dB`
- Industrial - `8 - 14 dB`


Where:
- X_{sigma}  : Gaussian random variable (shadowing term)
- 

### Fast Fading (Multipath Fading)
Fast fading represents rapid fluctuations of the signal caused by multipath propagation. Multiple reflected waves interfere constructively or destructively, causing the received power to vary dramatically over very short distances (centimeters).

```Latex
F = 20 \log_{10}(R)
R \sim \text{Rayleigh}(\sigma)
```

Where:
- F: fast fading term in dB
- R: Rayleigh-distributed amplitude
- σ: scale parameter of the Rayleigh distribution

## SNR

```latex
SNR = RSSI – NoiseFloor
NoiseFloor = -174 + 10*log10(BW_Hz) + NF
```

Where:
- NF - Noise Figure
- BW_Hz - bandwidth in Hz