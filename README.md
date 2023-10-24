# snow_tracker

Snow tracker for Tahoe

Project Title:
Tahoe Snow Tracker

Authors:
Jesse Ge & Brian Lam

Project Description (5 Sentences):
Snowboarding and skiing is a hobby shared by many people throughout the Bay Area. However, snow conditions are not always ideal. Some find it difficult to set aside vacation days for their next snow day, so our project will attempt to gather snow level data from previous years in Tahoe, and put together a collective average snow level for that day. Using this data, we will be able to determine what the snow level will be for that day using the average of previous years.

Project Outline/Plan:
Interface Plan:
Everything can still change, but for our interface we're planning to make it simple. We want the user to be able to select the dates, so we may make a calendar type of interface, where the user can see the predicted snowfall on each day. Once they click on the day, it could show data from previous years.

Data Collection and Storage Plan:
For our data collection, we'll use an online API in order to get data from previous years. For the data, we plan to use https://www.nohrsc.noaa.gov/ 's GIS Data Sets, specifically: Snow Information on Skiing Locations; it provides a .gz file, which we will read.
As for storing the data, we will be transferring it to our own .txt file, where we can format it however we like, and search for specific days easily.

Data Analysis and Visualization Plan
A .gitignore file and a license
