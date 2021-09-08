import pandas as pd
import numpy as np

csv = pd.read_csv('data/dirty/sales_1521.csv', 
                    low_memory=False)
csv2 = pd.read_csv('data/dirty/round4.csv')

df = pd.DataFrame(csv)
df2 = pd.DataFrame(csv2)

def clean_date(row):
    parts = row['SoldDate'].split(' ')
    return parts[0]

def get_branch(row):
    parts = row['BranchNumberAndBranchNameOfCustomer'].split(' ')
    return parts[0]

df['SoldDate'] = df.apply(lambda row: clean_date(row), axis = 1)
df['Branch'] = df.apply(lambda row: get_branch(row), axis = 1)
df['SoldDateYear'] = pd.to_datetime(df['SoldDateFormatted'], format='%m/%d/%Y').dt.year
df = df[[
    'CustomerFirstNameLastNameOrCompany',
    'CustomerNumber',
    'SoldDateFormatted',
    'SoldDateYear',
    'City',
    'State',
    'Address',
    'TotalPrice',
    'ProgramSize',
    'ProgramCode',
    'EmployeeName',
    'ProgramId',
    'Branch'
]]

df_invoice = df[[
    'CustomerNumber',
    'ProgramCode',
    'Address'
]]

df['InvoiceNumber'] = pd.Series((hash(tuple(row)) for _, row in df_invoice.iterrows()))


df = df.loc[~((pd.to_numeric(pd.DatetimeIndex(pd.to_datetime(df['SoldDateFormatted'], format='%m/%d/%Y')).year) <= 2020) & (df['Branch']=='MV'))]

df2 = df2[[
    'City',
    'ServiceId',
    'ServiceSize',
    'ServicePrice'
]]


df.to_csv('data/clean/sales_1521.csv')
df2.to_csv('data/clean/top_dress.csv')
