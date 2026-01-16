"""
Standard setup for interactive work
By David Palmer, dmopalmer@gmail.com

Heavily oriented towards astronomy, satellites, and other science.
Make it your own.
```
from mylab import *
```
"""
from copy import copy as _copy
from .mytools import *

from pathlib import Path

# Set up matplotlib
try:
    import matplotlib as mpl
    from mpl_toolkits.mplot3d import Axes3D
    # mpl.use('QtAgg')
    import matplotlib.pyplot as plt
    # Copy /Users/palmer/anaconda/envs/dmplab/lib/python3.6/site-packages/matplotlib/mpl-data/matplotlibrc
    # Use ~/.matplotlib/matplotlibrc (osx) or ~/.config/matplotlib/matplotlibrc  (linux) to make changes like default window size
    plt.rcParams['hist.bins'] = 'auto' # 1-d histogram only
    cmap_gray = _copy(plt.get_cmap('gray'))
    cmap_gray.set_bad('#000000ff')
    cmap_lognorm = mpl.colors.LogNorm(vmin=0.5)
    _ion = plt.ion()
except ImportError:
    pass

try:
    import numpy as np
except ImportError:
    pass

try:
    import scipy as sp
except ImportError:
    pass

# Polars instead of pandas
try:
    import polars as pl
except:
    pass
    
try:
    import astropy as ap
    from astropy.io import fits
    from astropy import units
    from astropy import constants
except ImportError:
    pass


# Pick one resolution of the datetiem/datetime.datetime confusion
from datetime import datetime
import datetime as dt

try:
    try:
        utc = datetime.timezone.utc
    except:
        from pytz import utc
    from dateutil.parser import parse as parsedate
except ImportError:
    pass

try:
    import skyfield
    import skyfield.api as sfapi
    import os.path
    skyfield.load = sfapi.Loader(os.path.expanduser("~/.config/skyfield"))
    skyfield.ts_builtin = skyfield.load.timescale(builtin=True)
except ImportError:
    pass


# Make Jupyter Notebook show edge-to-edge
# https://stackoverflow.com/questions/15411967/how-can-i-check-if-code-is-executed-in-the-ipython-notebook
# https://www.linkedin.com/pulse/top-5-usability-tips-jupyter-notebooks-apoorv-kashyap
# https://stackoverflow.com/questions/21971449/how-do-i-increase-the-cell-width-of-the-jupyter-ipython-notebook-in-my-browser

try:
    import os
    if os.path.basename(os.environ['_']).startswith('jupyter'):
        plt.rcParams['figure.figsize'] = [8, 5]  # smaller plots default within notebook
        import IPython.core.display
        IPython.core.display.display(IPython.core.display.HTML(
            "<style>.container {width:99% !important;}</style>"
        ))

        try:
            # Pixiedust
            # pixiedisplay(pandas.DataFrame) is cool
            # %%pixie_debugger is awesome
            # Can also do %debug in the cell after the error.   How does that work?
            # Or in python3.7, put a breakpoint() call in the code
            import pixiedust
            from pixiedust.display.app import display as pixiedisplay
        except ImportError:
            pass
except:
    pass



"""
Simplest cut/paste that you can just stick in your file and edit down:


from pathlib import Path
import datetime

from dateutil.parser import parse as parsedate, isoparser, isoparse

import numpy as np
import scipy as sp
import astropy as ap
from astropy.io import fits
from astropy import units
from astropy import constants

# Plotting
from copy import copy as _copy
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
mpl.use('QtAgg')
import matplotlib.pyplot as plt
plt.rcParams['hist.bins'] = 'auto' # 1-d histogram only
cmap_gray = _copy(plt.get_cmap('gray'))
cmap_gray.set_bad('#000000ff')
cmap_lognorm = mpl.colors.LogNorm(vmin=0.5)

"""
