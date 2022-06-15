import pandas as pd
import numpy as np

# Labels

labels = pd.read_csv("nlp/data/Labels.csv")
labels = labels[[ 'idx', 'label', 'pe_type', 'split']]

demograph = pd.read_csv("nlp/data/Demographics.csv")
#对年龄分箱
bins = [0,10,20,30,40,50,60,70,80,90,110]
label_list = [0,1,2,3,4,5,6,7,8,9]
age_bins =pd.cut(demograph["current_age_yrs"],bins,labels=label_list)
demograph["age"] = age_bins
#选取指定列
demograph = demograph[['Male', 'Asian', 'Black',
       'Native American', 'Other', 'Pacific Islander', 'Unknown_race', 'White',
       'SMOKER_Y', 'idx','age']]

vitals = pd.read_csv("nlp/data/Vitals.csv")
vitals = vitals[["SBP","DBP","height_inch","weight_kg","bmi","tempf","spO2","pulse","idx"]]



#df_join
pd.merge(labels,demograph,how="left",on="idx")


print(" ")

'''
ICD = pd.read_csv("nlp/ICD.csv")
inp = pd.read_csv("nlp/INP_MED.csv")
labs = pd.read_csv("nlp/LABS.csv")
outp = pd.read_csv("nlp/OUT_MED.csv")

'''