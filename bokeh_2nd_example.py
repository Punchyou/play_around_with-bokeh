#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:00:56 2020

@author: punchubu1804
"""
from bokeh.plotting import figure, output_file, show, ColumnDataSource
import pandas as pd


def cars_plot(df):
    """

    Parameters
    ----------
    df : dataframe.

    Returns
    -------
    p cars plot.

    """    
    
    # create ColumnDataSource from dataframe
    source = ColumnDataSource(pd)   
    
    
    # car list
    car_list = source.data['Car'].to_list()
    
    # figure
    p = figure(
        y_range=car,
        plot_width=800,
        plot_height=600,
        title='Cars Horsepower',
        x_axis_label='Horsepower',
        y_axis_label='Cars',
        # set the tools
        tools='pan, box_select, zoom_in, zoom_out, save, reset',
        source=source
        )
    
    # use bokeh horizontal bar glyphs
    p.hbar(
        y='Car',
        right='Horsepower',
        left=0,
        height=0.4,
        color='navy',
        fill_alpha=0.5 # opacity
        )
    
    return p

# read csv file
df = pd.read_csv('cars.csv')

show(cars_plot(df))