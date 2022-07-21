## Course schedule

Here is the current week-by-week schedule 📅 . We may adjust as we go along. To get started, we're going to create the calendar of weeks for the course programmatically rather than manually!

The course will be offered in two distinct sessions, which will each follow the same schedule.


## import modules
import pandas as pd
import re
import numpy as np


## tell python to display output and print multiple objects
from IPython.display import display, HTML
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

## create range b/t start and end date
## of course 
start_date = pd.to_datetime("2022-01-04")
end_date = pd.to_datetime("2022-03-08")
st_alldates = pd.date_range(start_date, end_date)

## subset to days in that range equal to Tuesday or Thursday
st_tuth = st_alldates[st_alldates.day_name().isin(['Tuesday', 'Thursday'])]

## create data frame with that information
st_dates = [re.sub("2022\\-", "", str(day.date())) for day in st_tuth] 
course_sched = pd.DataFrame({'dow': st_tuth.day_name(), 'st_tuth': st_dates})
course_sched['date_toprint'] = course_sched.dow.astype(str) + " " + \
            course_sched.st_tuth.astype(str) 
course_sched = course_sched['date_toprint']

## display the resulting date sequence
display(course_sched)

## next block of code creates the
## actual content; can click "show"
## to see the underlying code

## create the actual content

### list of concepts
concepts = ["Course intro. and checking software setup",
             "Workflow basics: command line, Github workflow, basic LaTeX syntax, pre-analysis plans",
            "Workflow basics (continued)",
             "Python pandas review: aggregation, joins, lambda and user-defined functions",
            "Python pandas review: aggregation, joins, lambda and user-defined functions",
                        "Problem set one work session",
            "Intro to merging",
            "Regex",
            "Probabilistic matching: part one",
            "Probabilistic matching: part two",
             "Text as data: part one",
            "Text as data: part two",
            "Problem set two work session and intro to APIs",
             "APIs continued",
             "APIs continued; SQL part one",
             "SQL part two",
            "Final project work session",
             "Scraping + final project work session",
             "Final presentations"]

len(course_sched)
len(concepts)
## combine
course_sched_concepts = pd.DataFrame({'Week': course_sched,
                                     'Concepts': concepts})

df = course_sched_concepts.copy()

print(df)

## add datacamp modules conditionally
col = "Concepts"

### older code on more exhaustive modules
# topics  = [df[col] == "Python basic data wrangling: data structures (vectors; lists; dataframes; matrices), control flow, and loops", 
#                df[col] == "Python basic data wrangling: basic regular expressions and text mining",
#                df[col] ==  "Python basic data wrangling: combining data (row binds, column binds, joins); aggregation",
#                df[col] == "Review of visualization: ggplot; plotnine",
#                df[col] == "Python: writing your own functions",
#                df[col] == "Python: text data using nltk and gensim",
#                df[col] ==  "SQL: reading data from a database and basic SQL (postgres) syntax",
#                df[col] == "SQL: more advanced SQL syntax (subqueries; window functions)",
#                df[col] == "Python: reading data from APIs and basic web scraping"]
# datacamp_modules = ["Python basics; python lists; Pandas: extracting and transforming data; Intermediate python for data science (loops)",
#                    "First three modules of regular expressions in Python",
#                    "Merging DataFrames with Pandas",
#                    "Introduction to Data Visualization with ggplot2",
#                    "Python data science toolbox (Part one): user-written functions, default args, lambda functions and error handling",
#                    "Natural language processing fundamentals in Python",
#                    "Introduction to databases in Python",
#                    "Intermediate SQL",
#                    "Importing JSON data and working with APIs; Importing data from the Internet"]

topics_trunc = [df[col] ==  "Workflow basics (continued)",
               df[col] == "Merging (continued) and PSET 1 review"]
datacamp_modules_trunc = ["Data manipulation with Pandas",
                         "Regular expressions for pattern matching"]

df["DataCamp module(s) (if any)"] = np.select(topics_trunc, 
                                     datacamp_modules_trunc, 
                                     default = "")


date_col = "Week"
due_dates = [df[date_col] == "Tuesday 04-20",
            df[date_col] == "Tuesday 04-27",
            df[date_col] == "Thursday 05-13",
             df[date_col] == "Tuesday 05-18",
             df[date_col] == "Thursday 05-20",
            df[date_col] == "Tuesday 06-01"]
assig = ["Problem set one",
        "Final project step 1",
        "Problem set two: part one",
        "Problem set two: part two",
        "Final project step 2 (due Sunday 05.23 at 11:59 PM EST)",
        "Slides for final presentation (due Tuesday 06.01 at 5 PM EST)"]


df["Due (11:59 PM EST unless otherwise specified)"] = np.select(due_dates,
                     assig,
                     default = "")

## add slides or tutorial link
# df['Link to slides or tutorial'] = np.select([df["Concepts"] == "Course intro. and checking software setup",
#                                              df["Concepts"] == "Workflow basics: command line, Github workflow, basic LaTeX syntax, pre-analysis plans"],
#                                             ["https://github.com/rebeccajohnson88/qss20_slides_activities/blob/main/slides/qss20_s21_class1.pdf",
#                                             "https://github.com/rebeccajohnson88/qss20_slides_activities/blob/main/slides/qss20_s21_class2.pdf"],
#                                             default = "")

# df['Link to slides or tutorial'] = np.where(df['Link to slides or tutorial'] != "",
#                         '<a target="_blank" href=' + df['Link to slides or tutorial'] + '><div>' + "Link" + '</div></a>',
#                         "")

# df['Link to activity (blank)'] = np.select([df["Concepts"] == "Workflow basics: command line, Github workflow, basic LaTeX syntax, pre-analysis plans"],
#                                             ["https://github.com/rebeccajohnson88/qss20_slides_activities/blob/main/activities/00_latex_output_examples.ipynb"],
#                                             default = "")

# df['Link to activity (blank)'] = np.where(df['Link to activity (blank)'] != "",
#                         '<a target="_blank" href=' + df['Link to activity (blank)'] + '><div>' + "Link" + '</div></a>',
#                         "")


HTML(df.to_html(index=False, escape = False))

