import pickle
import pandas as pd
import os
import sys
from pathlib import Path
sys.path.append('F:\\hku\\capstone\\pythonProject\\nlp')
from constants import *

def create_acc_2_label(input_file:str,output_file):
    os.chdir(NLP_DATA_DIR)

    df = pd.read_csv(input_file)

    df = df[["label","idx"]]
    df = df.set_index("idx")

    df = df.T.to_dict()



    pickle.dump(df, open(output_file, "wb"))


if __name__ == "__main__":
    create_acc_2_label(LABELS,ACC_2_LABEL)

