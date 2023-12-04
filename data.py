# c0b015941064404da9a224932230212
import requests
import json
import calendar
import numpy as np


def data_json(file_name, data):
    """Save data to a JSON file."""
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)


api_key = 'c0b015941064404da9a224932230212'
url = "https://api.worldweatheronline.com/premium/v1/ski.ashx"

msnowfall = {month: [] for month in range(1, 13)}

initial_year = 2015  # start of API recording
year = 2022  # last complete year
days_snowed = 0
for year in range(initial_year, year + 1):
    total_snow = {year: {month: [] for month in range(
        1, 13)} for year in range(initial_year, year + 1)}

    for month in range(1, 13):
        # Not all months have the same number of days
        month_days = calendar.monthrange(year, month)[1]

        # Loop through the month
        for day in range(1, month_days + 1):
            params = {
                'key': api_key,
                'q': '38.93, -119.98',
                'format': 'json',
                'date': f'{year}-{month:02d}-{day:02d}'
            }

            response = requests.get(url, params=params)
            # If no error:
            if response.status_code == 200:
                data = response.json()
                # We want the "snowfall_cm" data section in the API
                snowfall_cm = data['data']['weather'][0].get(
                    'totalSnowfall_cm', '0.0')
                total_snow[year][month].append(float(snowfall_cm))

                # Print the totalSnowfall_cm for the day
                # print(f"Snowfall on {year}-{month:02d}-{day:02d}: {snowfall_cm} cm")
            else:
                print(
                    f"Error fetching data for {year}-{month:02d}-{day:02d}: {response.status_code}")

    # Get the average snowfall per month
    monthly_snowfall_avg = {}
    for month, snowfalls in msnowfall.items():

        # Values 0 are also accepted
        snow_amt = [snowfall for snowfall in snowfalls if snowfall >= 0]
        days_snowed += 1

        if snow_amt:
            avg = sum(snow_amt) / len(snow_amt)
            monthly_snowfall_avg[month] = avg
        else:
            monthly_snowfall_avg[month] = 0

        print(
            f"Average snowfall for month {month}: {monthly_snowfall_avg[month]:.2f} cm")

data_json('total_snow.json', total_snow)
# print(days_snowed)
