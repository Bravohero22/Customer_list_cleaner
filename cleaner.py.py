import csv
import pandas as pd 

def load_data(filename):
    df = pd.read_csv(filename)
    return df

# df = load_data("customers.csv")
# print(df)

def clean_data(df):
    df["name"] = df["name"].str.strip()   # remove extra spaces around tex
    df["email"] = df["email"].str.strip()
    df["city"] = df["city"].str.strip()

    df["name"] = df["name"].str.title()    # John Doe style capitals
    df["city"] = df["city"].str.title()    
    df["email"] = df["email"].str.lower()  # all lowercase

    df = df.drop_duplicates()              # remove repeated rows
    df = df.dropna(subset=["name", "email"])  # remove rows missing name or email

    return df 

def save_data(df, filename):
    df.to_csv("clean_customers.csv", index=False)  # save the result
    # index=False stops pandas from adding an extra numbering column to the saved file.
    return df 


df = load_data("customers.csv")
rows_before = len(df)
clean_df = clean_data(df)
rows_after = len(clean_df)
rows_removed = rows_before - rows_after
total_amount = clean_df["amount"].sum()
save_data(clean_df, "clean_customers.csv")

print(clean_df)
print(f"Rows before: {rows_before}")
print(f"Rows after: {rows_after}")
print(f"Rows removed: {rows_removed}")
print(f"Total amount: {total_amount}")

