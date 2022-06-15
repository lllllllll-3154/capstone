import numpy as np
import pickle
import os
import sys
sys.path.append(os.getcwd()) #添加搜索import的路径

from torch.utils.data import Dataset, DataLoader
from constants import *

class EMRDataset(Dataset):

    def __init__(self,data_type:str,label_path:str,split:str):
        self.data_path = PARSED_EMR_DICT[data_type] / f"{data_type}_{split}.pkl"