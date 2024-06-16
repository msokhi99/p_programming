with open("./guest_names.txt",mode="r") as guest_name_file:
    list_of_names=guest_name_file.readlines()

with open("./initial_letter.txt",mode="r") as initial_letter_file:
    contents=initial_letter_file.read()

for names in list_of_names:
    updated_contents=contents.replace("[name]",names.strip())
    with open(f"{names.strip()}.txt",mode="w") as new_file:
        new_file.write(updated_contents)
