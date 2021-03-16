import requests
from datetime import datetime
import tkinter as tk
import config as cg

# api key, url and designated city
api_key = cg.api_key
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = cg.city_name
full_url = base_url + "q=" + city_name + "&appid=" + api_key

base_zip_url = "http://api.openweathermap.org/data/2.5/weather?"
zip_name = cg.zip_code
full_zip_irl = base_zip_url + "zip=" + str(zip_name) + "&appid=" + api_key

"""
Updates the text for the labels in the main display.
Does this by collecting info from datetime and openweathermap api

Args:
    root: the root window, used to repeat process
    tempLabel: label for temperature
    clothesLabel: label for clothing recommendation
    timeLabel: label for the current time
    dateLabel: label for the current date
    
Returns:
    n/a
"""


def update(root, tempLabel, clothesLabel, timeLabel, dateLabel, weatherLabel):
    # determines weather to display 24 hour clock
    if cg.militaryTime:
        timeLabel['text'] = datetime.now().strftime("%H:%M")
    # displays 12 hour clock
    else:
        # determines weather or not to display am or pm
        if (datetime.now().hour / 12) < 1:
            period = "am"
        else:
            period = "pm"
        # determines number of hour shown
        # because midnight is am and noon is pm, must be calculated separate from am/pm
        if datetime.now().hour <= 12:
            timeLabel['text'] = datetime.now().strftime("%H:%M") + period
        else:
            timeLabel['text'] = str(datetime.now().hour - 12) + ":" + str(datetime.now().minute) + period

    # displays date
    dateLabel['text'] = datetime.now().strftime("%A %B %d, %Y\n")

    # obtain json from api
    if cg.basedOnZip:
        response = requests.get(full_zip_irl)
    else:
        response = requests.get(full_url)
    x = response.json()

    # carries out if api called properly
    if x["cod"] != "404":

        y = x["main"]

        # obtain current temp from json in kelvin
        current_temperature = y["temp"]
        # calculate Fahrenheit from kelvin
        fahrenheit = ((current_temperature - 273.15) * 1.8) + 32

        # set temperature label text
        if cg.fahrenheit:
            tempLabel['text'] = "{:.1f}".format(fahrenheit)
        else:
            tempLabel['text'] = "{:.1f}".format(current_temperature - 273.15)

        # set clothing recommendation based on obtained temperature
        if fahrenheit > 100:
            clothesLabel["text"] = "It's HOT! Wear a tank top and drink lots of water!\n"
        elif 100 >= fahrenheit > 75:
            clothesLabel["text"] = "Its pretty hot outside. Shorts weather!\n"
        elif 75 >= fahrenheit > 50:
            clothesLabel["text"] = "Its a comfortable temperature out. Pants and a T-shirt will do.\n"
        elif 50 >= fahrenheit > 32:
            clothesLabel["text"] = "It's a bit cold out. Wear long sleeves!\n"
        else:
            clothesLabel["text"] = "Its freezing out there! Wear as much layers as possible!\n"

        y = x["weather"][0]

        desc = y["description"]

        weatherLabel["text"] = desc

    # returns error when city is not found
    else:
        tempLabel['text'] = "City not found"
        clothesLabel['text'] = "Check your config file"

    # rerun this function every second
    root.after(1000, update, root, tempLabel, clothesLabel, timeLabel, dateLabel, weatherLabel)


"""
Main function for the program.
Contains initialization of window and labels.
"""


def main():
    # create window and frame for labels
    root = tk.Tk()
    root.attributes('-fullscreen', cg.fullscreen)
    root.geometry("750x750")
    frame = tk.Frame(root)

    # create labels
    timeLabel = tk.Label(frame,
                         anchor=tk.CENTER,
                         justify=tk.CENTER,
                         font=("Courier", 60))
    dateLabel = tk.Label(frame,
                         anchor=tk.CENTER,
                         justify=tk.CENTER,
                         font=("Courier", 12))
    tempLabel = tk.Label(frame,
                         anchor=tk.CENTER,
                         justify=tk.CENTER,
                         font=("Courier", 60))
    clothesLabel = tk.Label(frame,
                            anchor=tk.CENTER,
                            justify=tk.CENTER,
                            font=("Courier", 12))
    weatherLabel = tk.Label(frame,
                            anchor=tk.CENTER,
                            justify=tk.CENTER,
                            font=("Courier", 12))

    # pack labels/frame
    timeLabel.pack(fill="x")
    dateLabel.pack(fill="x")
    tempLabel.pack(fill="x")
    clothesLabel.pack(fill="x")
    weatherLabel.pack(fill="x")
    frame.pack(expand=1)

    # run fist instance of update
    update(root, tempLabel, clothesLabel, timeLabel, dateLabel, weatherLabel)

    root.mainloop()


if __name__ == "__main__":
    main()
