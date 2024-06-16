import pandas as pd 

nato_df=pd.read_csv("./nato_phonetic_alphabet.csv")
print(nato_df.head())

# Iter Rows returns a tuple(index,row).
nato_alphabet_dict={row["letter"]:row["code"] for (index,row) in nato_df.iterrows()}
print(nato_alphabet_dict)

program_is_running=True

while program_is_running:
    user_input=str(input("Enter a Word: ")).upper()
    if user_input=="EXIT":
        program_is_running=False
        print("Exiting Program.")
    else:
        user_nato_list=[nato_alphabet_dict[key] for key in user_input]
        print(user_nato_list)

# Test Code:
# nato_alphabet_dict={index:row for (index,row) in nato_df.iterrows()}
# print(nato_alphabet_dict)
