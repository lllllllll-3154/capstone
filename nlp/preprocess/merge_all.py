import pandas as pd

import pickle
import pandas as pd
import os
import sys
from pathlib import Path
sys.path.append('F:\\hku\\capstone\\pythonProject\\nlp')
from constants import *

def main(output_path:str):
    os.chdir(NLP_DATA_DIR)
    df = pd.read_csv(LABELS)
    df = df[["idx"]]
    for raw_data in RAW_CSV_DATA:
        new_df = pd.read_csv(raw_data)
        df = pd.merge(df,new_df,how="left",on="idx")

    output_path = os.path.join(output_path,"all.csv")
    df.to_csv(output_path,index=False)



if __name__ == "__main__":
    main(CSV_DATA_DIR)



