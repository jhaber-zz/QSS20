#!/usr/bin/env python
# coding: utf-8

# ## Course schedule
# 
# Here is the current week-by-week schedule 📅 . We may adjust as we go along. To get started, we're going to create the calendar of weeks for the course programmatically rather than manually!
# 
# The course will be offered in two distinct sessions, which will each follow the same schedule and have common deadlines for problem sets. To make things simpler:
# 
# - 3A/Section 01: Monday-Wednesday schedule
# - 6A/Section 02: Monday-Thursday schedule; the Thursday content will correspond to Section 01's Wednesday content

# In[1]:


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
start_date = pd.to_datetime("2022-01-05")
end_date = pd.to_datetime("2022-03-08")
st_alldates = pd.date_range(start_date, end_date)

## subset to days in that range equal to Tuesday or Thursday
st_mw_3A = st_alldates[st_alldates.day_name().isin(['Monday', 'Wednesday'])]
st_mt_6A = st_alldates[st_alldates.day_name().isin(['Monday', 'Thursday'])]

## create data frame with that information
st_dates_3A = [re.sub("2022\\-", "", str(day.date())) for day in st_mw_3A] 
st_dates_6A = [re.sub("2022\\-", "", str(day.date())) for day in st_mt_6A] 
course_sched = pd.DataFrame({'dow_3A': st_mw_3A.day_name(),
                             'dow_6A': st_mt_6A.day_name(),
                             'date_3A': st_dates_3A,
                            'date_6A': st_dates_6A})
course_sched['Dates_3Asection'] = course_sched.dow_3A.astype(str) + " " + \
            course_sched.date_3A.astype(str) 
course_sched['Dates_6Asection'] = course_sched.dow_6A.astype(str) + " " + \
            course_sched.date_6A.astype(str)

course_sched_display = course_sched[['Dates_3Asection', 
                                     'Dates_6Asection']].copy()

## display the resulting date sequence
display(course_sched_display)

## next block of code creates the
## actual content; can click "show"
## to see the underlying code


# In[2]:


## create the actual content

### list of concepts
concepts = ["Course intro. and checking software setup",
             "Python pandas: aggregation, joins, lambda and user-defined functions",
            "Python pandas: aggregation, joins, lambda and user-defined functions (continued)",
             "MLK day (no class)",
            "Workflow basics: command line/jhub, Github workflow",
            "Intro to merging",
            "Regex",
            "Probabilistic matching",
            "Text as data: part one",
            "Text as data: part two",
            "Text as data: part two (continued)",
            "APIs (part 1)",
             "APIs (twitter)",
             "Supervised machine learning",
             "SQL",
            "Interactive data viz. or web scraping (if time)",
             "Final project work session",
             "Final presentations"]

## check that concepts match number of weeks
assert len(course_sched_display.Dates_3Asection) == len(concepts)
assert len(course_sched_display.Dates_6Asection) == len(concepts)



## combine
course_sched_concepts = pd.DataFrame({'Week_3A': course_sched_display.Dates_3Asection,
                                      'Week_6A': course_sched_display.Dates_6Asection,
                                     'Concepts': concepts})

df = course_sched_concepts.copy()

print(df)


# In[3]:


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

topics_trunc = [df[col] ==  "Python pandas: aggregation, joins, lambda and user-defined functions",
               df[col] == "Intro to merging",
               df[col] == "Probabilistic matching",
               df[col] == "Supervised machine learning"]
datacamp_modules_trunc = ["Data manipulation with Pandas",
                          "Joining data with pandas",
                         "Regular expressions for pattern matching",
                         "Supervised Learning with scikit-learn"]

df["DataCamp module(s) (if any)"] = np.select(topics_trunc, 
                                     datacamp_modules_trunc, 
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


# In[11]:


date_col = "Week_3A"
due_dates = [df[date_col] == "Wednesday 01-12",
            df[date_col] == "Wednesday 01-26",
             df[date_col] == "Wednesday 02-09",
             df[date_col] == "Wednesday 02-23",
            df[date_col] == "Monday 03-07"]
assig = ["Problem set one (due Sunday 01-16)",
         "Problem set two (due Friday 01-28)",
        "Final project milestone 1 (due Wednesday 02-09);<br>Problem set three (due Friday 02-11)",
         "Problem set four (due Friday 02-25);<br>Final project milestone 2 (due Sunday 02-27) ",
        "Problem set five (due Friday 03-11);<br>Final project presentation (paper due on Monday 03-14)"]


df["Due (11:59 PM EST unless otherwise specified)"] = np.select(due_dates,
                     assig,
                     default = "")


# In[12]:


HTML(df.to_html(index=False, escape = False))

