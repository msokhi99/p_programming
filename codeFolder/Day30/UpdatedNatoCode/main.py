import pandas as pd 

nato_df=pd.read_csv("/home/msokhi99/Desktop/py_programming/Day30/UpdatedNatoCode/nato_phonetic_alphabet.csv")

alphabet_list={row["letter"]:row["code"] for (index,row) in nato_df.iterrows()}

user_input=str(input("Enter a name: ")).upper()
while True:
    try:
        converted_name=[alphabet_list[char] for char in user_input]
    except KeyError as error_message:
        print(f"{error_message} is not a key in the dictionary.\nPlease do not enter any numbers.")
        user_input=str(input("Enter a name: ")).upper()
    else:
        print(f"The converted name is: {converted_name}")
        break
