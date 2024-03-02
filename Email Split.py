import csv
import re

# Load the text data
with open(r'C:\Users\aksha\Downloads\archive (4)\fradulent_emails.csv.txt' , 'r') as file:
    data = file.read()

# Define a function to extract fields from the text
def extract_field(label, text):
    match = re.search(f"{label}: (.+?)(?=\n\w+:|$)", text, re.DOTALL)
    return match.group(1).strip() if match else ''

# Parse the data into a list of dictionaries
parsed_data = []
email_entries = re.split(r'(?=\nFrom r )', data)
for entry in email_entries:
    email_dict = {
        'Return-Path': extract_field('Return-Path', entry),
        'From': extract_field('From', entry),
        'Message-Id': extract_field('Message-Id', entry),
        'Date': extract_field('Date', entry),
        'Subject': extract_field('Subject', entry),
        'Content': extract_field('Content-Type', entry),  # Adjust as needed
    }
    parsed_data.append(email_dict)

# Write the parsed data to a CSV file
output_csv_file = r'C:\Users\aksha\Desktop\output.csv'
fieldnames = ['Return-Path', 'From', 'Message-Id', 'Date', 'Subject', 'Content']
with open(output_csv_file, 'w', newline='') as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(parsed_data)
