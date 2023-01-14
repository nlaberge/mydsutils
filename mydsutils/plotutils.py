#!/usr/bin/env python

# Inspired by Sam Way's samplotlib
import numpy as np
from matplotlib import rcParams
import matplotlib.pyplot as plt
import textwrap


# Constants
SINGLE_FIG_SIZE = (6,4)
BAR_WIDTH = 0.6
TICK_SIZE = 15
XLABEL_PAD = 10
LABEL_SIZE = 14
TITLE_SIZE = 16
LEGEND_SIZE = 12
LINE_WIDTH = 2
LIGHT_COLOR = '0.8'
LIGHT_COLOR_V = np.array([float(LIGHT_COLOR) for i in range(3)])
DARK_COLOR = '0.4'
DARK_COLOR_V = np.array([float(DARK_COLOR) for i in range(3)])
ALMOST_BLACK = '0.125'
ALMOST_BLACK_V = np.array([float(ALMOST_BLACK) for i in range(3)])
ACCENT_COLOR_1 = np.array([255., 145., 48.]) / 255.


# Configuration

#rcParams['text.usetex'] = True #Let TeX do the typsetting
# rcParams['pdf.use14corefonts'] = True
# rcParams['ps.useafm'] = True
#rcParams['text.latex.preamble'] = [r'\usepackage{sansmath}', r'\sansmath'] #Force sans-serif math mode (for axes labels)
# rcParams['font.family'] = 'sans-serif' # ... for regular text
# rcParams['font.sans-serif'] = ['Helvetica Neue', 'HelveticaNeue', 'Helvetica'] #, Avant Garde, Computer Modern Sans serif' # Choose a nice font here
# rcParams['pdf.fonttype'] = 42
# rcParams['ps.fonttype'] = 42
rcParams['text.color'] = ALMOST_BLACK
rcParams['axes.unicode_minus'] = False

rcParams['xtick.major.pad'] = '8'
rcParams['axes.edgecolor']  = ALMOST_BLACK
rcParams['axes.labelcolor'] = ALMOST_BLACK
rcParams['lines.color']     = ALMOST_BLACK
rcParams['xtick.color']     = ALMOST_BLACK
rcParams['ytick.color']     = ALMOST_BLACK
rcParams['text.color']      = ALMOST_BLACK
rcParams['lines.solid_capstyle'] = 'butt'

MPL_MARKERS = ['o','s','v','p','*','D','^','P','d',]

def hide_spines(ax):
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)



def get_rainbow_colors(num_categories):
    '''
    returns categorical colors
    max num categories: 10
    '''
    import palettable.cartocolors.qualitative as colors
    return colors.get_map(f'Prism_{num_categories}').mpl_colors
    
def savefig(path):
    plt.savefig(path,bbox_inches='tight')

def legend_no_duplicates(**kwargs):
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(),**kwargs)

def wrap(text, width):
    return textwrap.fill(text,width)

def plot_dumbell(ax, x1,y1,x2,y2,kw_scatter1 = {},kw_scatter2 = {},kw_plot = {}):
    ax.plot([x1,x2],[y1,y2],**kw_plot)
    ax.scatter(x1,y1, **kw_scatter1)
    ax.scatter(x2,y2, **kw_scatter2)

def arrow_label(ax, x,y,dx,dy,text, kw_text = {}):
    ax.annotate(text, xy=(x, y), xytext=(dx,dy), 
            textcoords='offset points', ha='center', va='bottom',**kw_text,
            # bbox=dict(boxstyle='round,pad=0.2', fc='white', alpha=0.3),
            arrowprops=dict(arrowstyle='->', #connectionstyle='arc3,rad=0.5', 
                            color='black'))