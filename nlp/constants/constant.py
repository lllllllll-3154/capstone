#储存常数

from pathlib import Path

#DIR
HOME_DIR = Path.home() #C:\Users\Use'r
NLP_DATA_DIR = Path("F:\\hku\\capstone\\pythonProject\\nlp") #文件储存位置,总目录
#if not NLP_DATA_DIR.is_dir(): #判断是否是一个存在的dir
    #raise Exception("Please modify PROJECT_DATA_DIR in constants to a valid directory")



#RAW DATA
CSV_DATA_DIR = NLP_DATA_DIR / "data" # csv文件目录
DEM = CSV_DATA_DIR / "Demographics.csv"
ICD = CSV_DATA_DIR / "ICD.csv"
INP = CSV_DATA_DIR / "INP_MED.csv"
LAB = CSV_DATA_DIR / "LABS.csv"
OUT = CSV_DATA_DIR / "OUT_MED.csv"
VIT = CSV_DATA_DIR / "Vitals.csv"
ALL = CSV_DATA_DIR / "all.csv"
#全部的CSV文件
RAW_CSV_DATA = [
    DEM,
    ICD,
    INP,
    LAB,
    OUT,
    VIT,
    ALL
]

LABELS = CSV_DATA_DIR / "Labels.csv"

# Mappings
MAPPINGS_DIR = NLP_DATA_DIR / "mappings"
IDX_2_ACC = MAPPINGS_DIR / "idx_2_acc_stanford.pkl"
IDX_2_SPLIT = MAPPINGS_DIR / "idx_2_split_stanford.pkl"
ACC_2_TYPE = MAPPINGS_DIR / "acc_2_type.pkl"
ACC_2_LABEL = MAPPINGS_DIR / "acc_2_label.pkl"


# Parsed data  #处理后的data
PARSED_DATA_DIR = NLP_DATA_DIR / "parsed_data"
ALL_DIR = PARSED_DATA_DIR / "All"
DEMOGRAPHICS_DIR = PARSED_DATA_DIR / "Demographics"
ICD_DIR = PARSED_DATA_DIR / "ICD"
INP_MED_DIR = PARSED_DATA_DIR / "INP_MED"
OUT_MED_DIR = PARSED_DATA_DIR / "OUT_MED"
LABS_DIR = PARSED_DATA_DIR / "LABS"
VITALS_DIR = PARSED_DATA_DIR / "Vitals"
VISION_DIR = PARSED_DATA_DIR / "Vision"
PARSED_EMR_DATA = [
    ALL_DIR,
    DEMOGRAPHICS_DIR,
    ICD_DIR,
    INP_MED_DIR,
    OUT_MED_DIR,
    LABS_DIR,
    VITALS_DIR,
]
PARSED_EMR_DICT = {
    "All": ALL_DIR,
    "Demographics": DEMOGRAPHICS_DIR,
    "ICD": ICD_DIR,
    "INP_MED": INP_MED_DIR,
    "OUT_MED": OUT_MED_DIR,
    "LABS": LABS_DIR,
    "Vitals": VITALS_DIR,
    "Vision": VISION_DIR,
}

# Logging
LOG_DIR = NLP_DATA_DIR / 'logs'
CKPT_DIR = NLP_DATA_DIR / 'ckpt'
RESULTS_DIR = NLP_DATA_DIR / 'results'

# Column names
ACCESSION_COL = "idx"
PROBS_COL = "probs"
LABELS_COL = "labels"


