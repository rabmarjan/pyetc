import numpy as np
import pandas as pd
import rpy2.robjects.packages as packages
import rpy2.robjects.lib.ggplot2 as ggplot2
import rpy2.robjects as ro
R = ro.r
datasets = packages.importr('datasets')
mtcars = packages.data(datasets).fetch('mtcars')['mtcars']
gp = ggplot2.ggplot(mtcars)
pp = (gp
      + ggplot2.aes_string(x='wt', y='mpg')
      + ggplot2.geom_point(ggplot2.aes_string(colour='qsec'))
      + ggplot2.scale_colour_gradient(low="yellow", high="red")
      + ggplot2.geom_smooth(method='auto')
      + ggplot2.labs(title="mtcars", x='wt', y='mpg'))

pp.plot()
R("dev.copy(png,'/home/rose/Desktop/out.png')")
print("output")