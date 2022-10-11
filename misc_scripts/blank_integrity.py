"""Checks to see if blank columns are consistent per country
  Note: Run in parent directory!"""
import csv
from owid_covid_schema import owid_schema

def main():
  with open ('./owid-covid-data.csv', 'r') as file:
    csvreader = csv.reader(file)
    lastrow = owid_schema
    for row in csvreader:
      for idx, val in enumerate(row):
        if row[idx] != '' or lastrow[idx] != '': continue
        if lastrow[2] != row[2]: continue
        if row[idx] != lastrow[idx]:
          print('Inconsistent blank data!')
          print(lastrow[idx])
          print(row[idx])
      lastrow = row
  
if __name__ == "__main__":
  main()