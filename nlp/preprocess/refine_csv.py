import pandas as pd

import pickle
import pandas as pd
import os
import sys
from pathlib import Path
sys.path.append('F:\\hku\\capstone\\pythonProject\\nlp')
from constants import *


demograph = pd.read_csv(DEM)
#对年龄分箱
bins = [0,10,20,30,40,50,60,70,80,90,110]
label_list = [0,1,2,3,4,5,6,7,8,9]
age_bins =pd.cut(demograph["current_age_yrs"],bins,labels=label_list)
demograph["current_age_yrs"] = age_bins

demograph.to_csv(DEM)
