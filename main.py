import requests
import json
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=db44c6f777a7466a9dc122009241711&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
print(w)
speak.Speak(f"The current weather in {city} is {w} degrees")