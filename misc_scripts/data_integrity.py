"""Checks to see what percentage of rows/countries contain data
  Note: Run in parent directory!"""
import csv
import numpy as np
from owid_covid_schema import owid_schema

def main():
  with open ('./owid-covid-data.csv', 'r') as file:
    csvreader = csv.reader(file)
    countrycount = 0
    rowcount = 0
    row_cols = list(range(36))
    country_cols = list(range(36))

    #Reset with each new country
    lastrowcountry = ''
    countryrowcount = 0
    binary_cols = list(range(36))
    for row in csvreader:
      rowcount += 1
      #If is same country
      if lastrowcountry == row[2]: 
        countryrowcount += 1
        lastrowcountry = row[2]
        continue
      #Is new country

      #Update Country, Row Tally for previous country
      new_tally = update_tallies(country_cols, row_cols, binary_cols, countryrowcount)
      country_cols = new_tally[0]
      row_cols = new_tally[1]
      #Reset per country vals
      countryrowcount = 1
      countrycount+=1

      #Check for blank columns
      for idx, val in enumerate(row):
        if val != '':
          binary_cols[idx] = 1
          continue
        binary_cols[idx] = 0
        
      lastrowcountry = row[2]

    #print values
    for idx, val in enumerate(row_cols):
      perc = val/rowcount
      numrows = round(perc * rowcount)
      perc = round(perc, 4)
      print(f'{owid_schema[idx]}: {perc} ({numrows})')
    #TODO: validate country_cols
    print(country_cols)
    print(countrycount)
        

def update_tallies(country_col, row_col, binary_col, countryrowcount):
  ary1 = np.array(country_col)
  ary2 = np.array(row_col)
  aryb = np.array(binary_col)
  new_country_col = np.add(ary1, aryb)
  aryb = aryb * countryrowcount
  new_row_col = np.add(ary2, aryb)
  return (new_country_col, new_row_col)
        
  
if __name__ == "__main__":
  main()