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
import numpy as np
from bokeh.models import ColumnDataSource, HoverTool


def plot():
    """
    Returns the plot of circles and squares glyphs. 
    
    """

    # Create a blank figure with labels

    p = figure(
        plot_width=600,
        plot_height=600,
        title="Example Glyphs",
        x_axis_label="X",
        y_axis_label="Y",
    )

    # Example data
    squares_x = [1, 3, 4, 5, 8]
    squares_y = [8, 7, 3, 1, 10]
    circles_x = [9, 12, 4, 3, 15]
    circles_y = [8, 4, 11, 6, 10]

    # Add squares glyph
    p.square(squares_x, squares_y, size=12, color="navy", alpha=0.6)
    # Add circle glyph
    p.circle(circles_x, circles_y, size=12, color="red", alpha=0.6)
    return show(p)


def make_flight_delays_dataframe(flights):
    """
    Returns the delays of flights as a dataframe, including the number of.
    """

    flights["arr_delay"].describe()  # returns a list of stats like mean, std etc...

    # will make a histogram - bohek doesn't support it, will make it with bars
    # create data for he bars
    # arr_host: the number of data points in each specified bin (number of 'delays'/flights)
    # edges: the interval number: [-60, +120]
    arr_hist, edges = np.histogram(
        flights["arr_delay"],
        bins=int(180 / 5),  # bins are the intervals of the histogram - in 5min slots
        range=[-60, 120],
    )

    # put info in a df
    delays = pd.DataFrame(
        {"arr_delay": arr_hist, "left": edges[:-1], "right": edges[1:]}
    )
    return delays


def flight_delays_plot(delays):
    """
    Returns the plot of the flight delays.
    """

    # create the blank point
    p = figure(
        plot_height=600,
        plot_width=600,
        title="Histogram of Arrival Delays",
        x_axis_label="Delay (min)",
        y_axis_label="Number of Flights",
    )

    # add a quad glyph
    p.quad(
        bottom=0,
        top=delays["arr_delay"],
        left=delays["left"],
        right=delays["right"],
        fill_color="red",
        line_color="black",
    )

    return p

# add intercativity
# need to change the dataframe to ColumnDataSource - data will be held in a dict    
def add_interactivity(p, delays):
    """

    Parameters
    ----------
    p : figure.
    delays : dataframe.

    Adds interactivity in the p figure.

    """
    
    # convert dataframe to column data source
    src = ColumnDataSource(delays)
    src.data.keys() # show keys
    
    # add a quad glyph with source
    p.quad(source=src, bottom=0, top='arr_delay', left='left', right='right',
           fill_color='red', line_color='black')
    
    # reference attributes of the graph, (such as x or y) using ‘$’
    # and specific fields in our source using ‘@
    # here are both:
    #h = HoverTool(tooltips = [('Delay Interval Left ', '@left'),
    #                     ('(x,y)', '($x, $y)')])
    return p


flights_plot = plot()
# read the data
flights = pd.read_csv("flights.csv", index_col=0)
delays = make_flight_delays_dataframe(flights)
p = flight_delays_plot(delays)
show(p)
show(add_interactivity(p, delays))
# def main():
#     # p = plot()


# if __name__ == "__main__":
#     main()
