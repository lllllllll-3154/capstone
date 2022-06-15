import pickle
import pandas as pd
import os
import sys
from pathlib import Path
sys.path.append('F:\\hku\\capstone\\pythonProject\\nlp')
from constants import *


def main(in_dir:str):
    """Remove subsegmental cases from parsed data
    Args:
        in_dir (str): input directory of the parsed data
    """
    os.chdir(NLP_DATA_DIR)

    # mapping
    mapping = pickle.load(open(ACC_2_TYPE, "rb"))

    # read in parsed files
    study = str(in_dir).split("\\")[-1]
    train = pickle.load(open(os.path.join(in_dir, study + "_train.pkl"), "rb"))
    val = pickle.load(open(os.path.join(in_dir, study + "_val.pkl"), "rb"))
    test = pickle.load(open(os.path.join(in_dir, study + "_test.pkl"), "rb"))

    # filter out subsegmental cases
    train = {k:v for k,v in train.items() if mapping[k]["pe_type"] != "subsegmental"}
    val = {k:v for k,v in val.items() if mapping[k]["pe_type"] != "subsegmental"}
    test = {k:v for k,v in test.items() if mapping[k]["pe_type"] != "subsegmental"}

    # create save directory
    out_dir = os.path.join(in_dir, study+ "_no_subseg")
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # save to pickle
    pickle.dump(train, open(f"{out_dir}/{study}_train.pkl","wb"))
    pickle.dump(val, open(f"{out_dir}/{study}_val.pkl","wb"))
    pickle.dump(test, open(f"{out_dir}/{study}_test.pkl","wb"))


if __name__ == "__main__":

    for parsed_data in PARSED_EMR_DATA:
        main(parsed_data)