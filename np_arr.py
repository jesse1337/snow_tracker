import numpy as np
import matplotlib.pyplot as plt
import json

months_tb = ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"]
months = np.array(months_tb)
# print("months")

# snowfall
snowfall_path = 'monthly_snow_averages.json'
with open(snowfall_path, 'r') as f:
    data = json.load(f)

snowfall_arr = list(data.values())
snowfall = np.array(snowfall_arr)

# print(snowfall)

# snowy days
days_path = 'monthly_snow_days.json'
with open(days_path, 'r') as f:
    data2 = json.load(f)

snowdays_arr = list(data2.values())
snowdays = np.array(snowdays_arr)

# print(snowdays_arr)

# graph


def plot_snowfall():
    plt.figure(figsize=(16, 9))
    plt.plot(months, snowfall, label="Average Snowfall")
    plt.xlabel("Months")
    plt.ylabel("Snowfall (cm)")
    plt.title("Average Monthly Snowfall(2015-Present)")
    plt.grid(True)
    plt.savefig("static/images/snowfall.png")


def plot_snowdays():
    plt.figure(figsize=(16, 9))
    plt.xlabel("Months")
    plt.ylabel("Snowy days")
    plt.title("Average Number of Snowy Days Per Month(2015-Present)")
    plt.plot(months, snowdays, label="Average Snowy Days")
    plt.grid(True)
    plt.savefig("static/images/snow_days.png")


# plot_snowdays()


def yearly_data(file):
    delimiter = "\t"
    f = open(file)
    lines = f.read()
    f.close()
    lines = lines.split("\n")
    data3 = []
    for line in lines:
        data3.append(line.split(delimiter))
    print("Ran")
    data3 = data3[1:]
    years = []
    jan = []
    feb = []
    mar = []
    apr = []
    may = []
    jun = []
    jul = []
    aug = []
    sep = []
    oct = []
    nov = []
    dec = []
    for i in range(len(data3) - 1):  # len = 24
        # print(len(data3))
        # print(data3[i])
        years.append(float(data3[i][0]))
        jan_data = data3[i][1]
        jan.append(float(jan_data[:-1]))
        # print(jan_data)

        feb_data = data3[i][2]
        feb.append(float(feb_data[:-1]))

        mar_data = data3[i][3]
        mar.append(float(mar_data[:-1]))

        apr_data = data3[i][4]
        apr.append(float(apr_data[:-1]))

        may_data = data3[i][5]
        may.append(float(may_data[:-1]))

        jun_data = data3[i][6]
        jun.append(float(jun_data[:-1]))

        jul_data = data3[i][7]
        jul.append(float(jul_data[:-1]))

        aug_data = data3[i][8]
        aug.append(float(aug_data[:-1]))

        sep_data = data3[i][9]
        sep.append(float(sep_data[:-1]))

        oct_data = data3[i][10]
        oct.append(float(oct_data[:-1]))

        nov_data = data3[i][11]
        nov.append(float(nov_data[:-1]))

        dec_data = data3[i][12]
        dec.append(float(dec_data[:-1]))

    jan = np.array(jan)
    feb = np.array(feb)
    mar = np.array(mar)
    apr = np.array(apr)
    may = np.array(may)
    jun = np.array(jun)
    jul = np.array(jul)
    aug = np.array(aug)
    sep = np.array(sep)
    oct = np.array(oct)
    nov = np.array(nov)
    dec = np.array(dec)

    # set up years
    years_raw = range(2000, 2023)

    years = years - np.min(years)  # normalize

    # now get the slope for each month
    jan_x, jan_int = np.polyfit(years, jan, 1)
    feb_x, feb_int = (np.polyfit(years, feb, 1))
    mar_x, mar_int = (np.polyfit(years, mar, 1))
    apr_x, apr_int = (np.polyfit(years, apr, 1))
    may_x, may_int = (np.polyfit(years, may, 1))
    jun_x, jun_int = (np.polyfit(years, jun, 1))
    jul_x, jul_int = (np.polyfit(years, jul, 1))
    aug_x, aug_int = (np.polyfit(years, aug, 1))
    sep_x, sep_int = (np.polyfit(years, sep, 1))
    oct_x, oct_int = (np.polyfit(years, oct, 1))
    nov_x, nov_int = (np.polyfit(years, nov, 1))
    dec_x, dec_int = (np.polyfit(years, dec, 1))

    # GET the mean of each month
    jan_m = np.mean(jan)
    feb_m = np.mean(feb)
    mar_m = np.mean(mar)
    apr_m = np.mean(apr)
    may_m = np.mean(may)
    jun_m = np.mean(jun)
    jul_m = np.mean(jul)
    aug_m = np.mean(aug)
    sep_m = np.mean(sep)
    oct_m = np.mean(oct)
    nov_m = np.mean(nov)
    dec_m = np.mean(dec)
    print(years)
    print(years_raw)

    plt.figure(figsize=(16, 9))
    plt.xlabel("Years")
    plt.ylabel("Snowfall")
    plt.title("Snowfall of January")
    plt.plot(years, jan, label="Snowfall (in)")
    jan_trend = jan_x * years + jan_int
    jan_trend_lab = round(np.polyfit(years, jan, 1)[0], 3)
    plt.xticks(ticks=years, labels=years_raw, rotation=45)
    plt.plot(years, jan_trend, linewidth=2,
             label=f"Snowfall trend: {jan_trend_lab}")
    plt.axhline(jan_m, color='r', linestyle='--', label=f"Mean: {jan_m}")
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.savefig("static/images/Jan")

    plt.figure(figsize=(16, 9))
    plt.xlabel("Years")
    plt.ylabel("Snowfall")
    plt.title("Snowfall of February")
    plt.plot(years, feb, label="Snowfall (in)")
    feb_trend = feb_x * years + feb_int
    feb_trend_lab = round(np.polyfit(years, feb, 1)[0], 3)
    plt.xticks(ticks=years, labels=years_raw, rotation=45)
    plt.plot(years, feb_trend, linewidth=2,
             label=f"Snowfall trend:{feb_trend_lab}")
    plt.axhline(feb_m, color='r', linestyle='--', label=f"Mean: {feb_m}")
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.savefig("static/images/Feb")

    plt.figure(figsize=(16, 9))
    plt.xlabel("Years")
    plt.ylabel("Snowfall")
    plt.title("Snowfall of March")
    plt.plot(years, mar, label="Snowfall (in)")
    march_trend = mar_x * years + mar_int
    march_trend_lab = round(np.polyfit(years, mar, 1)[0], 3)
    plt.xticks(ticks=years, labels=years_raw, rotation=45)
    plt.plot(years, march_trend, linewidth=2,
             label=f"Snowfall trend:{march_trend_lab}")
    plt.axhline(mar_m, color='r', linestyle='--', label=f"Mean: {mar_m}")
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.savefig("static/images/Mar")

    plt.figure(figsize=(16, 9))
    plt.xlabel("Years")
    plt.ylabel("Snowfall")
    plt.title("Snowfall of April")
    plt.plot(years, apr, label="Snowfall (in)")
    apr_trend = apr_x * years + apr_int
    apr_trend_lab = round(np.polyfit(years, apr, 1)[0], 3)
    plt.xticks(ticks=years, labels=years_raw, rotation=45)
    plt.plot(years, apr_trend, linewidth=2,
             label=f"Snowfall trend:{apr_trend_lab}")
    plt.axhline(apr_m, color='r', linestyle='--', label=f"Mean: {apr_m}")
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.savefig("static/images/Apr")

    plt.figure(figsize=(16, 9))
    plt.xlabel("Years")
    plt.ylabel("Snowfall")
    plt.title("Snowfall of May")
    plt.plot(years, may, label="Snowfall (in)")
    may_trend = may_x * years + may_int
    may_trend_lab = round(np.polyfit(years, may, 1)[0], 3)
    plt.xticks(ticks=years, labels=years_raw, rotation=45)
    plt.plot(years, may_trend, linewidth=2,
             label=f"Snowfall trend:{may_trend_lab}")
    plt.axhline(may_m, color='r', linestyle='--', label=f"Mean: {may_m}")
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.savefig("static/images/May")

    plt.figure(figsize=(16, 9))
    plt.xlabel("Years")
    plt.ylabel("Snowfall")
    plt.title("Snowfall of June")
    plt.plot(years, jun, label="Snowfall (in)")
    jun_trend = jun_x * years + jun_int
    jun_trend_lab = round(np.polyfit(years, jun, 1)[0], 3)
    plt.xticks(ticks=years, labels=years_raw, rotation=45)
    plt.plot(years, jun_trend, linewidth=2,
             label=f"Snowfall trend:{jun_trend_lab}")
    plt.axhline(jun_m, color='r', linestyle='--', label=f"Mean: {jun_m}")
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.savefig("static/images/Jun")

    plt.figure(figsize=(16, 9))
    plt.xlabel("Years")
    plt.ylabel("Snowfall")
    plt.title("Snowfall of July")
    plt.plot(years, jul, label="Snowfall (in)")
    jul_trend = jul_x * years + jul_int
    jul_trend_lab = round(np.polyfit(years, jul, 1)[0], 3)
    plt.xticks(ticks=years, labels=years_raw, rotation=45)
    plt.plot(years, jul_trend, linewidth=2,
             label=f"Snowfall trend:{jul_trend_lab}")
    plt.axhline(jul_m, color='r', linestyle='--', label=f"Mean: {jul_m}")
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.savefig("static/images/Jul")

    plt.figure(figsize=(16, 9))
    plt.xlabel("Years")
    plt.ylabel("Snowfall")
    plt.title("Snowfall of August")
    plt.plot(years, aug, label="Snowfall (in)")
    aug_trend = aug_x * years + aug_int
    aug_trend_lab = round(np.polyfit(years, aug, 1)[0], 3)
    plt.xticks(ticks=years, labels=years_raw, rotation=45)
    plt.plot(years, aug_trend, linewidth=2,
             label=f"Snowfall trend:{aug_trend_lab}")
    plt.axhline(aug_m, color='r', linestyle='--', label=f"Mean: {aug_m}")
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.savefig("static/images/Aug")

    plt.figure(figsize=(16, 9))
    plt.xlabel("Years")
    plt.ylabel("Snowfall")
    plt.title("Snowfall of September")
    plt.plot(years, sep, label="Snowfall (in)")
    sep_trend = sep_x * years + sep_int
    sep_trend_lab = round(np.polyfit(years, sep, 1)[0], 3)
    plt.xticks(ticks=years, labels=years_raw, rotation=45)
    plt.plot(years, sep_trend, linewidth=2,
             label=f"Snowfall trend:{sep_trend_lab}")
    plt.axhline(sep_m, color='r', linestyle='--', label=f"Mean: {sep_m}")
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.savefig("static/images/Sep")

    plt.figure(figsize=(16, 9))
    plt.xlabel("Years")
    plt.ylabel("Snowfall")
    plt.title("Snowfall of October")
    plt.plot(years, oct, label="Snowfall (in)")
    oct_trend = oct_x * years + oct_int
    oct_trend_lab = round(np.polyfit(years, oct, 1)[0], 3)
    plt.xticks(ticks=years, labels=years_raw, rotation=45)
    plt.plot(years, oct_trend, linewidth=2,
             label=f"Snowfall trend:{oct_trend_lab}")
    plt.axhline(oct_m, color='r', linestyle='--', label=f"Mean: {oct_m}")
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.savefig("static/images/Oct")

    plt.figure(figsize=(16, 9))
    plt.xlabel("Years")
    plt.ylabel("Snowfall")
    plt.title("Snowfall of November")
    plt.plot(years, nov, label="Snowfall (in)")
    nov_trend = nov_x * years + nov_int
    nov_trend_lab = round(np.polyfit(years, nov, 1)[0], 3)
    plt.xticks(ticks=years, labels=years_raw, rotation=45)
    plt.plot(years, nov_trend, linewidth=2,
             label=f"Snowfall trend:{nov_trend_lab}")
    plt.axhline(nov_m, color='r', linestyle='--', label=f"Mean: {nov_m}")
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.savefig("static/images/Nov")

    plt.figure(figsize=(16, 9))
    plt.xlabel("Years")
    plt.ylabel("Snowfall")
    plt.title("Snowfall of December")
    plt.plot(years, dec, label="Snowfall (in)")
    dec_trend = dec_x * years + dec_int
    dec_trend_lab = round(np.polyfit(years, dec, 1)[0], 3)
    plt.xticks(ticks=years, labels=years_raw, rotation=45)
    plt.plot(years, dec_trend, linewidth=2,
             label=f"Snowfall trend:{dec_trend_lab}")
    plt.axhline(dec_m, color='r', linestyle='--', label=f"Mean: {dec_m}")
    plt.grid(True)
    plt.legend(loc="upper left")
    plt.savefig("static/images/Dec")


yearly_data("yearly_month_snowfall.txt")
plot_snowfall()
plot_snowdays()
