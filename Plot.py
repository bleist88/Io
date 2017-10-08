
from    __future__  import absolute_import
from    __future__  import division
from    __future__  import print_function
from    __future__  import unicode_literals

from   .__imports__ import *

##  ========================================================================  ##

def smart_figure( figure, aspect="auto" ):

    figure.tight_layout()

    for i in range( len(figure.axes) ):

        figure.axes[i].minorticks_on()

        figure.axes[i].tick_params(
            axis        = "both",
            which       = "major",
            #direction   = "inout",
            length      = 12,
            width       = 1.2,
        )

        figure.axes[i].tick_params(
            axis        = "both",
            which       = "minor",
            #direction   = "inout",
            length      = 7,
            width       = 1.2,
        )

        figure.axes[i].set_aspect( aspect )
