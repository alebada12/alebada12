# https://buildmedia.readthedocs.org/media/pdf/pyowm/latest/pyowm.pdf
# pyowm doc, for some reason my API key was invalid
from pyowm.utils import timestamps
from pyowm.owm import OWM
owm = OWM('83d51e0f1034279915ae8a3ccb361bdb')
mgr = owm.weather_manager()
daily_forecaster = mgr.forecast_at_place('Toledo,US','daily')
tomorrow = timestamps.tomorrow()
weather = daily_forecaster.get_weather_at(tomorrow)

# I had nothing but errors with this assignment