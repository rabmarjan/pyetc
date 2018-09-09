import rpy2.robjects as robjects
import numpy as np
import pandas as pd

r=robjects.r

x = r.source("/home/rose/Desktop/MIS/read_excel_file.R")
#y = pd.DataFrame(x)
print(x)