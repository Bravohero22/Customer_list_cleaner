# Customer List Cleaner

A Python script that takes a messy customer list (CSV), cleans it with pandas, and saves a tidy file plus a short summary. It was built as a practice freelance ticket.

## The problem

> My customer list is a mess. Some names have extra spaces or wrong capitals, some rows are repeated, and some are missing a name or email. Please clean it up and send me a tidy file, plus a short summary of what you changed.

## What it does

1. Loads `customers.csv`
2. Removes extra spaces from name, email and city
3. Fixes capitals: names and cities in Title Case, emails in lowercase
4. Removes duplicate rows (after cleaning, so `  john doe ` and `John Doe` count as the same person)
5. Removes rows that are missing a name or an email
6. Saves the result to `clean_customers.csv`
7. Prints a summary of what changed

## Project structure

```
customer-list-cleaner/
    cleaner.py             # the script
    customers.csv          # sample messy data
    clean_customers.csv    # cleaned output
    README.md
```

## How to run

1. Install [Python 3](https://www.python.org/downloads/)
2. Install pandas:
   ```
   python -m pip install pandas
   ```
3. Run:
   ```
   python cleaner.py
   ```

## Sample output

```
Rows before: 7
Rows after: 3
Rows removed: 4
Total amount: 10000
```

Before (`customers.csv`):

```
name,email,city,amount
  john doe ,JOHN@MAIL.COM,lagos,5000
Mary Ade,mary@mail.com,ABUJA,3000
john doe,john@mail.com,Lagos,5000
Chidi Okeke,,Enugu,4500
mary ade,mary@mail.com,Abuja,3000
Bola Tunde,bola@mail.com,  lagos  ,2000
,ken@mail.com,Kano,1500
```

After (`clean_customers.csv`):

```
name,email,city,amount
John Doe,john@mail.com,Lagos,5000
Mary Ade,mary@mail.com,Abuja,3000
Bola Tunde,bola@mail.com,Lagos,2000
```

## How the code is organized

| Function | Job |
|---|---|
| `load_data(filename)` | Reads the CSV into a table |
| `clean_data(df)` | Strips spaces, fixes capitals, removes duplicates and incomplete rows |
| `save_data(df, filename)` | Saves the cleaned table to a CSV |

## What I learned

- Loading and saving CSV files with pandas
- Cleaning text columns with `.str.strip()`, `.str.title()` and `.str.lower()`
- Why the order matters: clean first, then remove duplicates
- Removing incomplete rows with `dropna`
- Installing and using a third-party module with `pip`

## Possible improvements

- Take the file names from the command line
- Report which rows were removed and why
- Support Excel files as well as CSV

## Note

All data in this repo is made-up sample data.
