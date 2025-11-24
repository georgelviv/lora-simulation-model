from .models import EnvironmentModel

ENVIRONMENTS = {
  "open_field": EnvironmentModel(
    name="open_field",
    path_loss_exponent=2.0,
    shadow_sigma_db=1.0,
    description="Clear line-of-sight, almost no obstructions."
  ),
  "suburban": EnvironmentModel(
    name="suburban",
    path_loss_exponent=2.5,
    shadow_sigma_db=3.0,
    description="Light obstacles, trees, small buildings."
  ),
  "urban": EnvironmentModel(
    name="urban",
    path_loss_exponent=2.9,
    shadow_sigma_db=6.0,
    description="City area with buildings and partial obstructions."
  ),
  "dense_urban": EnvironmentModel(
    name="dense_urban",
    path_loss_exponent=3.5,
    shadow_sigma_db=10.0,
    description="Dense buildings, non-line-of-sight."
  ),
  "indoor": EnvironmentModel(
    name="indoor",
    path_loss_exponent=4.0,
    shadow_sigma_db=8.0,
    description="Office or indoor environment with walls."
  ),
  "industrial": EnvironmentModel(
    name="industrial",
    path_loss_exponent=5.0,
    shadow_sigma_db=12.0,
    description="Heavy metal/industrial environment with strong attenuation."
  ),
}
