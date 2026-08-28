import requests
import time
url = "https://timeapi.io/api/v1/time/current/zone?timezone=asia%2Fkolkata"




while True:
    response = requests.get(url)
    data = response.json()
    print(f"time right now {data['time']}")
  

    time.sleep(1)