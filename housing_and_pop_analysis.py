#!/usr/bin/env python
# coding: utf-8

# In[77]:


"""Allows user to pick a csv file and perform histogram analysis
on plots and variables in each data set"""
import sys
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Importing each
housing_df = pd.read_csv("Housing.csv")
pop_df = pd.read_csv("PopChange.csv")


# In[78]:


def analyze_pop_column(pop_input):
    """Displays all the data for each column"""
    print("The statistics are as follows:")
    print("Count =", pop_df[pop_input].sum())  # I assume count is the total population
    print("Mean =", pop_df[pop_input].mean())
    print("Standard Deviation =", pop_df[pop_input].std())
    print("Min =", pop_df[pop_input].min())
    print("Max =", pop_df[pop_input].max())
    print("Displaying histogram.")

    # Code to display histogram
    hist_data = np.array(pop_df[pop_input])
    fig, ax = plt.subplots(figsize=(10, 7))
    if pop_input == "Pop Apr 1" or pop_input == "Pop Jul 1":
        ax.hist(hist_data, bins=[0, 25000, 50000, 75000, 100000, 250000])
    if pop_input == "Change Pop":
        ax.hist(hist_data, bins=[0, 50, 100, 250, 500, 1000, 2000, 3000, 4000, 5000])
    plt.show()


# In[79]:


def analyze_pop_data():
    """This will run if the user chooses to analyze population data"""
    pop_input = input("Which column would you like to analyze?\n"
                      "a. Pop Apr 1\n"
                      "b. Pop Jul 1\n"
                      "c. Change Pop\n"
                      "d. Exit\n")

    if pop_input == "a":
        analyze_pop_column("Pop Apr 1")
        analyze_pop_data()
    if pop_input == "b":
        analyze_pop_column("Pop Jul 1")
        analyze_pop_data()
    if pop_input == "c":
        analyze_pop_column("Change Pop")
        analyze_pop_data()
    if pop_input == "d":
        pop_input2 = input(print("Select the data you'd like to analyze:\n"
                                 "1. Population Data\n"
                                 "2. Housing Data\n"
                                 "3. Exit\n"))
        if pop_input2 == "1":
            analyze_pop_data()
        if pop_input2 == "2":
            analyze_housing_data()
        if pop_input2 == "3":
            sys.exit()
    else:
        print("Please enter a, b, c, or d.")
        analyze_pop_data()


# In[80]:


def analyze_housing_column(housing_input):
    """Displays all the data for each column"""
    print("The statistics are as follows:")
    print("Count =", housing_df[housing_input].sum())  # I assume count is the total
    print("Mean =", housing_df[housing_input].mean())
    print("Standard Deviation =", housing_df[housing_input].std())
    print("Min =", housing_df[housing_input].min())
    print("Max =", housing_df[housing_input].max())
    print("Displaying histogram.")

    # Code to display histogram
    hist_data = np.array(housing_df[housing_input])
    fig, ax = plt.subplots(figsize=(10, 7))
    if housing_input == "AGE":
        ax.hist(hist_data, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    if housing_input == "BEDRMS":
        ax.hist(hist_data, bins=[0, 1, 2, 3, 4, 5, 6, 7])
    if housing_input == "BUILT":
        ax.hist(hist_data, bins=[1900, 1915, 1930, 1945, 1960, 1975, 1990, 2005, 2020, 2035])
    if housing_input == "ROOMS":
        ax.hist(hist_data, bins=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    if housing_input == "UTILITY":
        ax.hist(hist_data, bins=[0, 25, 50, 75, 100, 150, 200, 250, 500, 750, 1000, 1200])
    plt.show()


# In[81]:


def analyze_housing_data():
    """This will run if the user chooses to analyze housing data"""
    housing_input = input("Which column would you like to analyze?\n"
                          "a. Age\n"
                          "b. Bedrooms\n"
                          "c. Built\n"
                          "d. Rooms\n"
                          "e. Utility\n"
                          "f. Exit\n")

    if housing_input == "a":
        analyze_housing_column("AGE")
        analyze_housing_data()
    if housing_input == "b":
        analyze_housing_column("BEDRMS")
        analyze_housing_data()
    if housing_input == "c":
        analyze_housing_column("BUILT")
        analyze_housing_data()
    if housing_input == "d":
        analyze_housing_column("ROOMS")
        analyze_housing_data()
    if housing_input == "e":
        analyze_housing_column("UTILITY")
        analyze_housing_data()
    if housing_input == "f":
        housing_input2 = input(print("Select the data you'd like to analyze:\n"
                                     "1. Population Data\n"
                                     "2. Housing Data\n"
                                     "3. Exit\n"))
        if housing_input2 == "1":
            analyze_pop_data()
        if housing_input2 == "2":
            analyze_housing_data()
        if housing_input2 == "3":
            sys.exit()
    else:
        print("Please enter a letter a-f.")
        analyze_housing_data()


# In[76]:


# Main Menu
print("****************Python Data Analysis App****************")
main_input = input("Select data you'd like to analyze:\n"
                   "1. Population Data\n"
                   "2. Housing Data\n"
                   "3. Exit\n")
while main_input != "3":
    if main_input == "1":
        analyze_pop_data()
    elif main_input == "2":
        analyze_housing_data()
    else:
        main_input = input("Please enter a valid number 1-3.\n")

# In[ ]:
