# mpatlotlib 
import numpy as np
import matplotlib as mpl
from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

def prettyplot():
    '''
    Some settings to make pretty plots
    '''
    params = {
            'text.usetex': True,
            'text.latex.preamble': [r"\usepackage[T1]{fontenc}", r"\usepackage{cmbright}"], 
            'text.dvipnghack': False, 
            'xtick.major.size': 10,
            'xtick.major.width': 2.5
            ,'ytick.major.size': 10
            ,'ytick.major.width': 2.5
            ,'ytick.minor.size': 3
            ,'ytick.minor.width': 1.5
            ,'xtick.minor.size': 3
            ,'xtick.minor.width': 1.5
            ,'xtick.major.pad': 12
            ,'ytick.major.pad': 12
            ,'xtick.labelsize': 'large'
            ,'ytick.labelsize': 'large'
            ,'axes.linewidth': 2.5, 
            'axes.xmargin': 1,
            'font.family': 'monospace',
            'font.monospace': [u'Courier New'],
            'font.size': 16
            ,'legend.frameon': False
            ,'legend.markerscale': 5.0
            }
    mpl.rcParams.update(params)
    '''
    # Use Latex
    mpl.rcParams['text.usetex']=True
    mpl.rcParams['text.latex.preamble']=[r"\usepackage[T1]{fontenc}",
    r"\usepackage{cmbright}",]
    # Set Major tick size and width
    mpl.rcParams['xtick.major.size']=10
    mpl.rcParams['xtick.major.width']=2.5
    mpl.rcParams['ytick.major.size']=10
    mpl.rcParams['ytick.major.width']=2.5
    # Set minor tick size and wdith
    mpl.rcParams['ytick.minor.size']=3
    mpl.rcParams['ytick.minor.width']=1.5
    mpl.rcParams['xtick.minor.size']=3
    mpl.rcParams['xtick.minor.width']=1.5
    # Set space between axes and tick label
    mpl.rcParams['xtick.major.pad']=12
    mpl.rcParams['ytick.major.pad']=12
    mpl.rcParams['xtick.labelsize']='large'
    mpl.rcParams['ytick.labelsize']='large'
    mpl.rcParams['axes.linewidth']=2.5

    mpl.rcParams['font.family']='monospace'
    mpl.rcParams['font.monospace']='Courier'
    mpl.rcParams['font.weight']=800
    mpl.rcParams['font.size']=16
    # legend settings
    mpl.rcParams['legend.frameon']=False
    mpl.rcParams['legend.markerscale']=5.0
    mpl.rcParams['axes.xmargin']=1
    '''

def prettycolors(): 
    # Tableau20 colors 
    pretty_colors = [(89, 89, 89), (31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),  
            (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),  
            (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),  
            (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),  
            (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]  
  
    # Scale the RGB values to the [0, 1] range
    for i in range(len(pretty_colors)):  
        r, g, b = pretty_colors[i]  
        pretty_colors[i] = (r / 255., g / 255., b / 255.)  
    return pretty_colors 

def quick_hist(arr, nbin=None, range=None, normed=None): 
    '''
    Calculate quick histogram of given array
    '''
    prettyplot()
    pretty_colors = prettycolors()

    if nbin is None: 
        arr_width = arr.max() - arr.min()
        if arr_width/100. < 0.05*np.min(arr):
            nbin = int(np.rint(arr_width/(0.05*np.min(arr))))
        else:
            nbin = 100
    if range is None: 
        range = [arr.min(), arr.max()]
    if normed is None:
        normed = False

    arr_dist, arr_bin_edges = np.histogram( arr, range = range,  bins = nbin, normed = normed )
    arr_bin_mid = 0.5 * (arr_bin_edges[:-1] + arr_bin_edges[1:])
    
    return [arr_bin_mid, arr_dist]

def png2pdf(png_filename): 
    ''' Convert png file to pdf 
    '''
    pdf_filename = png_filename.replace('.png', '.pdf')

    convert_cmd = ' '.join(['convert', png_filename, pdf_filename])
    
    subprocess.call(convert_cmd.split())
    return None 
