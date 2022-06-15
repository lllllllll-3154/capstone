import pickle
import pandas as pd
import os
import sys
from pathlib import Path
sys.path.append('F:\\hku\\capstone\\pythonProject\\nlp')
from constants import *

def create_mappings(input_file:str,output_file:str):
    '''
    create mapping pkl file
    :param input_file: 
    :param output_dir: 
    '''

    os.chdir(NLP_DATA_DIR)

    df = pd.read_csv(input_file)

    df = df[["split","idx"]]
    df = df.set_index("idx")

    df = df.T.to_dict()



    pickle.dump(df, open(output_file, "wb"))


if __name__ == "__main__":
    create_mappings(LABELS,IDX_2_SPLIT)


