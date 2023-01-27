#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 10:28:06 2023

Module plot1D

Includes new functions to 

- plot curves on inverse-logarithmic x-axis (extremes). Improved from plot1DInvLog
- add shadings

@author: bfildier
"""

#---- Modules ----#

import matplotlib.pyplot as plt
import numpy as np
from math import log10,ceil
from matplotlib.patches import Polygon
from matplotlib.colors import LogNorm

#---- Functions ----#

#-- Inverse logarithmic axes to display extremes with correct ticks
#
# The trick here is to duplicate the axis and rescale the background frame
# so that the data, already correctly sampled on the transformed axis, can be displayed
# independently from the figure frame
#
# Example : start with the setting the figure and duplicate y axis
#
# fig,ax = plt.subplots(figsize=(6,4.5))
# ax_show = ax.twiny()


#-- create inverse-log frame

def setXaxisIL(ax,ranks):
    
    # define axes values
    x = np.flipud(1./(1-ranks/100.))
    Nx = len(x)
    # display empty data
    h = ax.plot(x,np.full((Nx,),np.nan))
    ax.set_xscale('log')
    # invert direction
    ax.invert_xaxis()
    
    # axis position
    ax.xaxis.set_ticks_position('bottom')

    # set xticks
    xtick_pos = np.mod(np.log10(np.round(x,5)),1) == 0
    xticks = x[xtick_pos]
    xticklabels = np.array(ranks[xtick_pos],dtype=str)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels)
    
def setYaxisIL(ax,ranks):
    
    # define axes values
    y = np.flipud(1./(1-ranks/100.))
    Ny = len(y)
    # display empty data
    h = ax.plot(np.full((Ny,),np.nan),y)
    ax.set_yscale('log')
    # invert direction
    ax.invert_yaxis()
    
    # axis position
    ax.yaxis.set_ticks_position('left')

    # set xticks
    ytick_pos = np.mod(np.log10(np.round(y,5)),1) == 0
    yticks = y[ytick_pos]
    yticklabels = np.array(ranks[ytick_pos],dtype=str)
    ax.set_yticks(yticks)
    ax.set_yticklabels(yticklabels)
    
def showData(ax,values,axisIL='x',**kwargs):
    """Show data as it is, regardless of preset frame and ticks"""

    if axisIL == 'x':
        
        dum_x = np.linspace(0,1,len(values))
        # show
        h = ax.plot(dum_x,values,**kwargs)
        # be careful that the x bounds are precisely the same as the background frame
        ax.margins(x=0)
        # remove ticks
        ax.set_xticks([])
        
        return h

    elif axisIL == 'y':
        
        dum_y = np.linspace(0,1,len(values))
        # show
        h = ax.plot(values,dum_y,**kwargs)
        # be careful that the y bounds are precisely the same as the background frame
        ax.margins(y=0)
        # remove ticks
        ax.set_yticks([])

        return h
    
def addXHatch(ax,x,i_xlim,color='gray',hatch='//',
    alpha=1,fill=False,**kwargs):
    """Add vertical shading"""

    dum_x = np.linspace(0,1,len(x))
    
    ax.add_patch(Polygon([[dum_x[i_xlim[0]], ax.get_ylim()[0]],\
                          [dum_x[i_xlim[1]], ax.get_ylim()[0]],\
                          [dum_x[i_xlim[1]], ax.get_ylim()[1]],\
                          [dum_x[i_xlim[0]], ax.get_ylim()[1]]],\
                          closed=True, fill=fill, hatch=hatch,linewidth=0,
                          color=color,alpha=alpha,**kwargs))
    
def addYHatch(ax,y,i_ylim,color='gray',hatch='//',
    alpha=1,fill=False,**kwargs):
    """Add horizontal shading"""

    dum_y = np.linspace(0,1,len(y))
    
    ax.add_patch(Polygon([[ax.get_xlim()[0],dum_y[i_ylim[0]]],\
                          [ax.get_xlim()[0],dum_y[i_ylim[1]]],\
                          [ax.get_xlim()[1],dum_y[i_ylim[1]]],\
                          [ax.get_xlim()[1],dum_y[i_ylim[0]]]],\
                          closed=True, fill=fill, hatch=hatch,linewidth=0,
                          color=color,alpha=alpha,**kwargs))
