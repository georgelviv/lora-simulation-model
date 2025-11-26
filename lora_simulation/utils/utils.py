from ..models import Config, State

def lora_log(command: str, cfg: Config | State) -> str:
  return  command + ";" + ",".join(f"{k}={v}" for k, v in cfg.items())
  