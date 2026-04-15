from services.openweather_api import get_weather
import time
from services.dashboard import render_dashboard


render_dashboard("lisbon1.xlsx")




# while True:
#     weather = get_weather()
#     print(weather)
#     time.sleep(10)