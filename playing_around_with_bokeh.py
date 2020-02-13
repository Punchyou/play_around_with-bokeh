#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 10:57:01 2020

@author: punchubu1804
"""
# tutorial from https://towardsdatascience.com/data-visualization-with-bokeh-in-python-part-one-getting-started-a11655a467d4
# bokeh basics.
from bokeh.plotting import figure
from bokeh.io import show
import pandas as pd


def plot():
    """
    Returns the plot of circles and squares glyphs. 
    
    """
    
    # Create a blank figure with labels

    p = figure(plot_width = 600, plot_height = 600, title = 'Example Glyphs',
    x_axis_label = 'X', y_axis_label = 'Y')
    
    # Example data
    squares_x = [1, 3, 4, 5, 8]
    squares_y = [8, 7, 3, 1, 10]
    circles_x = [9, 12, 4, 3, 15]
    circles_y = [8, 4, 11, 6, 10]
    
    # Add squares glyph
    p.square(squares_x, squares_y, size=12, color='navy', alpha=0.6)
    # Add circle glyph
    p.circle(circles_x, circles_y, size=12, color='red', alpha=0.6)
    return show(p)


def make_flight_delays_dataframe():
    """
    Returns the delays of flights as a dataframe, including the number of.
    """
    
    # read the data
    flights = pd.read_csv('flights.csv', index_col=0)
    flights['arr_delay'].describe() # returns a list of stats like mean, std etc...
    
    # will make a histogram - bohek doesn't support it, will make it with bars
    # create data for he bars
    # arr_host: the number of data points in each specified bin (number of 'delays')
    # edges: the interval number: [-60, +120]
    arr_hist, edges = np.histogram(flights['arr_delay'],
                                           bins= int(180/5), # bins are the intervals of the histogram - in 5min slots
                                           range = [-60, 120]) 
    
    # put info in a df
    delays = pd.DataFrame({'arr_delay': arr_hist,
                           'left': edges[:-1],
                           'rights': edges[1:]})

def delays_plot():
    """
    Returns the plot of the flight delays.
    """
    
    
def main():
    #p = plot()
    flights = flights_plot()

    
if __name__ == "__main__":
    main()
