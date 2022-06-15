import pickle
import pandas as pd
import os
import sys
from pathlib import Path
sys.path.append('F:\\hku\\capstone\\pythonProject\\nlp')
from constants import *


def create_dataset(input_file:str, out_dir:str):
    '''
    save features into train val test dataset with pickle file
    :param input_file: path to the raw features file(csv)
    :param out_dir:path to the parsed dataset (pkl)
    '''
    #更改当前工作路径到nlp文件夹
    os.chdir(NLP_DATA_DIR)
    #mapping
    # mapping
    idx_2_split = pickle.load(open(IDX_2_SPLIT, "rb"))
    #idx_2_acc = pickle.load(open(IDX_2_ACC, "rb"))

    # read in features
    df = pd.read_csv(input_file) #dataframe

    # remove zero variance 去掉只有同一个值的列
    df = df.loc[:,df.apply(pd.Series.nunique) != 1]
    df = df.set_index(ACCESSION_COL)

    #normalization
    df = df.apply(lambda x: (x - x.mean())/(x.std()))

    # convert to dictionary
    feature_dict = df.T.to_dict("list")
    #格式为 890:[...]

    # split data
    feature_dict = {k:v for k,v in feature_dict.items() if k in idx_2_split}
    train = {k:v for k,v in feature_dict.items() \
             if idx_2_split[k]["split"] == "train"}
    val = {k:v for k,v in feature_dict.items() \
             if idx_2_split[k]["split"] == "val"}
    test = {k:v for k,v in feature_dict.items() \
             if idx_2_split[k]["split"] == "test"}


    # create save directory
    feature_type = str(input_file).split(".")[0].split("\\")[-1]
    out_dir = os.path.join(out_dir, feature_type)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # save to pickle
    pickle.dump(train, open(f"{out_dir}/{feature_type}_train.pkl","wb"))
    pickle.dump(val, open(f"{out_dir}/{feature_type}_val.pkl","wb"))
    pickle.dump(test, open(f"{out_dir}/{feature_type}_test.pkl","wb"))






if __name__ == "__main__":

    for raw_data in RAW_CSV_DATA: #file path
        create_dataset(raw_data,PARSED_DATA_DIR)