# -------------------------------------- IMPORT SECTION ---------------------------------------------#
import pandas as pd

# ----------------------------------------- METHODS -------------------------------------------------#
def replace_element(my_list, old_value, new_value):
        for n, i in enumerate(my_list):
            if i == old_value:
                my_list[n] = new_value
        return my_list

# ------------------------------------ IMPORT DATAFRAMES --------------------------------------------#

osszes_df = pd.read_excel('osszes.xlsx', index_col=0)
ugyfel_df = pd.read_excel('ugyfel.xlsx', index_col=0)
diszpecser_df = pd.read_excel('diszpecser.xlsx', index_col=0)

osszes_df.head(10)
ugyfel_df.head(10)
diszpecser_df.head(10)

# -------------------------------------- PROCESS TEXTS ----------------------------------------------#
# ------------------------------ MAKE TWO LIST - TEXT, TARGET ---------------------------------------#

ugyfelList = ugyfel_df['All'].tolist()
ugyfelList
ugyfelList[0]

diszpecserList = diszpecser_df['All'].tolist()
diszpecserList

texts = ugyfelList + diszpecserList
texts
len(texts)

ugyfelTargetList = ugyfel_df['erzelem'].tolist()
diszpecserTargetList = diszpecser_df['erzelem'].tolist() 

toDistinct = ['N\t\t\t', 'E ', 'N ', 'NN', ' N', 'N\t', 'N0']
expected = ['N', 'E', 'N', 'N', 'N', 'N', 'N']

for i in range(0, len(toDistinct)):
    diszpecserTargetList = replace_element(diszpecserTargetList, toDistinct[i], expected[i])
    ugyfelTargetList = replace_element(ugyfelTargetList, toDistinct[i], expected[i])

target = ugyfelTargetList + diszpecserTargetList
