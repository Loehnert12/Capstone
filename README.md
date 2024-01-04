# Does Fan Attendance Effect the Win/Loss Ratio of Bowl Eligible College Football Teams?
Author: Daniel Loehnert
# Overview
This is a capstone project for Savvy Coders where I found out if college football teams win or lose more bowl games in front of a higher fan attendance? Using data analytics and different visualization methods, we are able to see how teams have performed since 1902-2022, but more specifically how the top 20 most winning teams have performed since 1980-2022. Fan attendance plays a huge role in how a team performs. Football teams might not be as focused, they might not be able to hear if the crowd is too loud, or they might thrive and play extremely well. What we can see from this project is the historical data of how well a college football team has performed in post season bowl games.
# Objectives
1. Determine the top 20 bowl eligible teams from 1980-2022.
2. Gather the average fan attendance when that team has won, the average attendance when they have lost, how many games that team has won and lost, and then their win/loss ratio.
# Data Sources
The data source that I found for this was from Kaggle.com that you can access [here](https://www.kaggle.com/datasets/mattop/college-football-bowl-games-1902-2022). This data set had everything I needed in order to answer my questions, but it did need to be cleaned up and reorganized.
# Methods
### Python
- Started cleaning the .csv file by taking care of any null values.
- I got the overall average attendance and used that number for any null values in the attendance column.
- I then converted the new table that I had into an Excel file.
### Excel
- Deleted any cloumns that I was not going to use.
- Organized that sheet alphabetically based on the winning team column.
### SQL
- Sorted bowl game dates from 1980-2022
- Pulled the top 20 teams
- Saved that new file into a new Excel file
- Pulled the average attendance the teams that won, and then the teams that lost.
### Tableau
- Created multiple different graphs and charts to show the difference in average fan attendance for wins and losses of every team.
---
### Data Processing Steps
- Python: Data cleaning and extraction of relevant information from datasets.
- Excel: Pivot tables, graphs, merging data together and got the top 20 teams' ratios.
- SQL: Got specific queries as needed.
- Tableau: Visual representation and exploration of college football win/loss record during bowl season between 1980-2022.

## Analysis
### Note: Please visit my [Tableau Account](https://public.tableau.com/app/profile/daniel.loehnert/viz/CapstoneFinal_17025168054460/Story1) to interact woth the graphs from this project.
- After narrowing down the top 20 teams with the most amount of wins, I was able to create a chart to visualize the fan attendance when a team won, and when they lost. You can see in the below graph that a mojority of the top 20 teams have a higher fan average when they win a bowl game. However, there are a handful of teams that have a higher fan average when they have lost games.
![Alt text](<Bar Graph.PNG>)
- You can see the plot chart below shows some outlier teams who have won the most games, but do not have the average fan attendance that everyone else does. And we have some othe routliers that have the highest fan average, but not as many wins as some others.
![Alt text](<Plot Chart.PNG>)
- This tree map below is a great representation of how many games a team has won vs lost and the average fan attendance by color.
![Alt text](<Tree Map.PNG>)
## Conclusion
The data collected, cleaned, narrowed down, and visually represented shows that a majority of college football teams win more games with a higher average fan attendance. There are some teams that have a higher fan attendance when they lose as well. Everyone knows that there are many other factors that play into whether a football team wins or loses, but this data shows specific teams that perform well in front of more people. 
## Next Steps 
There are a lot of other factors that come into play when looking at how a team performs in bowl games. The next steps in this project could be working on narrowing down the location of the bowl games compared to the winning teams home field. This could correlate a lot with how well fans travel for that team. That information could come in handy for colleges looking at which bowl games they get invited to and how well they have performed in the past when traveling that distance.
## Repository Structure
├── Documents
│   ├── Capstone_Project.ipynb
│   ├── Project Objectives.txt
│   ├── README.md
├── Project
|   ├── CSV Files
|   ├── Excel Files
|   ├── Images
|   ├── Python Files
|   ├── SQL Files
├── README.md
