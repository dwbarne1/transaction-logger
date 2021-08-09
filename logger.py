import csv
import os


def log_transactions(structure):
    """This function accepts a data structure containing all
    transactions made during the execution of the application
    and writes the entire data structure to a csv file."""
    if not os.path.isfile('transactions.csv'):
        with open('transactions.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(structure[0])
    with open('transactions.csv', 'a', newline='') as file:
        write_data = csv.writer(file)
        write_data.writerows(structure[1:])
    return None


def format_money(amount):
    """This function accepts a decimal value and formats it as a
    dollar amount adding a dollar sign, commas, and 2 decimal places."""
    amount = '${:,.2f}'.format(amount)
    return amount
