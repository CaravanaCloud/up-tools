from dynaconf import Dynaconf
import logging

_settings = None
def settings():
    global _settings
    if not _settings:
        _settings = Dynaconf(
                envvar_prefix="UP",
                load_dotenv=True,) 
    return _settings

def get_log_level():
    level_name = settings().get("log_level", "INFO")
    level = logging.getLevelName(level_name)
    return level


