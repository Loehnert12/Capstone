import pandas as pd
import numpy as np
import matplotlib as plot
import openpyxl

# Converted the bowl data excel sheet into a csv file.
bowl_sheet = pd.read_excel(r'C:\Users\danie\OneDrive\Desktop\SavvyCoders\Capstone\Project\collegefootballbowl.xlsx')
bowl_sheet.to_csv(r'C:\Users\danie\OneDrive\Desktop\SavvyCoders\Capstone\Project\collegefootballbowl.csv')

# Grabbed basic info of the csv file
bowl_sheet = pd.read_csv(r'C:\Users\danie\OneDrive\Desktop\SavvyCoders\Capstone\Project\collegefootballbowl.csv')
bowl_sheet.info()
bowl_sheet

# Printed the total bowl game average.
print('Average Bowl Attendance: ', round(bowl_sheet['attendance'].mean(), 2))

# Specified down to only the winner/loser of the bowl game and what the attendance was at that game.
bowl_sheet1 = bowl_sheet[['winner_tie', 'attendance']]
bowl_sheet2 = bowl_sheet[['loser_tie', 'attendance']]

# Different data cleaning methods
print(bowl_sheet1.head())
print(bowl_sheet1.info())
bowl_sheet1.describe()

# Sorted the winner in alphabetical order. Saved the new data into a new excel sheet.
bowl_sheet1.sort_values('winner_tie', ascending= True)
# bowl_sheet1.to_excel(r'C:\Users\danie\OneDrive\Desktop\SavvyCoders\Capstone Data\College Football Data\Winner_attendance.xlsx')

# Got the top 20 teams who won and how many wins total.
bowl_sheet1['winner_tie'].value_counts().head(20)

# Sorted the loser in alphabetical order. Saved the new data into a new excel sheet.
bowl_sheet2.sort_values('loser_tie', ascending= True)
bowl_sheet2.to_excel(r'C:\Users\danie\OneDrive\Desktop\SavvyCoders\Capstone Data\College Football Data\Loser_attendance.xlsx')

# Converted data.
Bowl_sheet3 = pd.read_excel(r'C:\Users\danie\OneDrive\Desktop\SavvyCoders\Capstone Data\College Football Data\Winner_attendance.xlsx')
Bowl_sheet3.to_csv(r'C:\Users\danie\OneDrive\Desktop\SavvyCoders\Capstone Data\College Football Data\Winner_attendance.csv')
Bowl_sheet3.fillna(49487, inplace = True)
Bowl_sheet3.to_excel(r'C:\Users\danie\OneDrive\Desktop\SavvyCoders\Capstone Data\College Football Data\Winner_attendance.xlsx')

# Converted data.
Bowl_sheet4 = pd.read_excel(r'C:\Users\danie\OneDrive\Desktop\SavvyCoders\Capstone Data\College Football Data\Loser_attendance.xlsx')
Bowl_sheet4.to_csv(r'C:\Users\danie\OneDrive\Desktop\SavvyCoders\Capstone Data\College Football Data\Loser_attendance.csv')
Bowl_sheet4.fillna(49487, inplace = True)
Bowl_sheet4.to_excel(r'C:\Users\danie\OneDrive\Desktop\SavvyCoders\Capstone Data\College Football Data\Loser_attendance.xlsx')

# Used SQL to show bowl games from 1980-2022.
# Read the csv into a dataframe so I can organize it.
bowl_sheet1980 = pd.read_csv(r'C:\Users\danie\OneDrive\Desktop\SavvyCoders\Capstone\Project\1980_Bowl_Games.csv')
bowl_sheet1980_1 = bowl_sheet1980[['winner_tie', 'attendance']]

