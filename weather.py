#! /usr/bin/env python3
# Group name: Weather App
# Authors:   Nicholas Vuong , Luciano Gibertoni
# Emails:  nicholasvuong123@csu.fullerton.edu , lgibertoni@csu.fullerton.edu
# Institution:   California State University Fullerton

import python_weather
import asyncio
import sys

async def getweather(location):
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)

    # fetch a weather forecast from a city
    weather = await client.find(location)

    # returns the current day's forecast temperature (int)
    print("Current temperature is {}.".format(weather.current.temperature))

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    await client.close()

if __name__ == "__main__":
    location = sys.argv[1]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather(location))
