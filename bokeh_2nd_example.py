#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:00:56 2020

@author: punchubu1804
"""
from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.models.glyphs import ImageURL
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
    source = ColumnDataSource(df)   
    
    
    # car list
    car_list = source.data['Car'].tolist()
    
    # figure
    p = figure(
        y_range=car_list,
        plot_width=800,
        plot_height=600,
        title='Cars Horsepower',
        x_axis_label='Horsepower',
        y_axis_label='Cars',
        # set the tools
        tools='pan, box_select, zoom_in, zoom_out, save, reset',
        )
    
    # use bokeh horizontal bar glyphs
    p.hbar(
        y='Car',
        right='Horsepower',
        left=0,
        height=0.4,
        color='navy',
        fill_alpha=0.5, # opacity
        source=source
        )
    
    # Add tooltips with ColumnDataSoure
    # mouse hover over
    hover = HoverTool()
    hover2 = HoverTool()
    # dict of tuples (name, field) or a raw html text in """ """
    # an image will be shown when hove over
    # access the data with @ (field names associated with the ColumnDataSource columns), <string> defines important text, 
    hover.tooltips = """
    <div>
      <h3>@Car</h3>
      <div><strong>Price: </strong>@Price</div>
      <div><strong>HP: </strong>@Horsepower</div>
      <div><img src="@Image" alt="Car Image" width="200" /></div>
    </div>
    """
    p.add_tools(hover)
    
    # second hover tool
    # hover2.tooltips=[
    #     ('Image', '@Image'),
    #     ('Horsepower', '@Horsepower'),
    #     ('Price', '@Price'),
    #     ]
    # p.add_tools(hover2)
    
    
    return p

# read csv file
df = pd.read_csv('cars.csv')

show(cars_plot(df))