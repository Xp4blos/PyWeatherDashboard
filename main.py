from services.openweather_api import get_weather
import time
from services.dashboard import render_dashboard
from services.postgresql_db import save_weather_to_postgresql, manage_db, get_latest_weather


manage_db()
# ok render_dashboard("lisbon1.xlsx")
print(get_latest_weather())

# while True:
#       weather = get_weather()
#       print(weather)
#       save_weather_to_postgresql(weather)
#       time.sleep(10)