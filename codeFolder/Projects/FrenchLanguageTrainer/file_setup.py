import pandas as pd 

try:
    french_df=pd.read_csv("/home/msokhi99/Desktop/py_programming/Day31/words_to_learn.csv")
except:
    french_df=pd.read_csv("/home/msokhi99/Desktop/py_programming/Day31/french_words.csv")