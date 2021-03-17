# Daily Display
Displays useful daily info, such as time and weather. Intended for use with a raspberry pi as an always-on bedside display.

This project uses OpenWeather API. Please visit https://openweathermap.org/api and generate a free key for the current weather data API. The API key can be set by editing the config.py file included in the process. This file also sets the desired city for weather collection, whether the temperature is shown as farenheit or celcius, and various other settings.

### Installation
This project was designed for:
* Raspberry Pi 3 Model B
* Raspberry Pi OS
* Python 3.8.5

```
$ cd /path/to/project/
$ git clone https://github.com/kable5/dailyDisplay.git
$ cd dailyDisplay
$ pip3 install -r requirements.txt
$ pip3 install -e
```

### TODO
- [ ] Display icon for weather conditions
- [ ] Display Calendar and Tasks through Google API
- [ ] C++ branch (may not be necessary but good for experience)
- [ ] Improve graphical design
- [ ] More wholistic and in-depth testing and error handling
