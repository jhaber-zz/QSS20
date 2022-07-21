#!/usr/bin/env python
# coding: utf-8

# # Evaluation and grading
# 
# ## Summary and grading policy
# 
# You will have four cumulative late days for assignments, that can be apportioned as you see fit between the different problem sets. Late days cannot be used for the final project or final presentation. If you run over and have not submitted the pset by the following class, I ask that you not attend class as not to see the answers. There will be a deduction of 10 percentage points for each late day after you have used your allowed late days.
# 
# Grades may be curved if there are no students receiving A's on the non-curved grading scale. 

# In[1]:


## import modules
import pandas as pd

from IPython.display import display, HTML

grade_summary = pd.DataFrame({'Assignments':
                ["Datacamp modules",
                  "Five problem sets",
                  "Final project",
                  "Team player/participation"],
                'Percentage':
                [5, 
                  50,
                  35,
                  10],
                'Deadlines':
                ["Throughout",
                  "Throughout (see course schedule and Canvas)",
                  "Presentation: Monday March 07; Short report: Monday March 14 (both sections)",
                  "Throughout"]}) 

HTML(grade_summary.to_html(index=False))


# ## Details
# 
# ### Datacamp modules to support programming topics (5% of grade)
# 
# The DataCamp modules are mainly to support your work on the problem sets and final project by giving you additional practice prior to our in-class activities. As a result, they will be graded on a "complete" and "incomplete" basis, regardless of how many points you received on the assignment itself. This means that you shouldn't get stuck partway through, since you can always ask to be shown the answer with a points deduction. Conversely, if the concepts are review, these should be very quick to complete, but if you'd prefer to skip, you can talk to me and I will reapportion the 5\% to your second problem set.
# 
# ### Five problem sets (10-20% of grade, each; 50% total)
# 
# DataCamp provides a very smooth introduction to programming, in the sense that they provide you with example code that gets you ~80\% of the way to the solution, with you needing to apply that code to reach the other ~20\%. 
# 
# In contrast, the problems sets will assess your ability to apply the concepts to data that is substantially messier, and problems that are substantially more difficult, than the ones in the DataCamp modules. More details on the problem sets will be provided the week before each is released,  but roughly, the workflow will be:
# 
# - Accessing the problem set and data via Canvas (pset one) or GitHub and/or jhub (psets two - five)
# - Working to produce the following outputs for each problem set:
#   - A raw .ipynb (or .Rmd file) with the code for the pset
#   - A compiled pdf that displays that code, as well as the answers to the written questions. These written questions will involve using some Latex syntax for equations and formatting.
#   - When applicable (e.g., part of the pset is run in script form), a supporting .py or .R file
#   
# The problem sets will be graded on both accuracy and programming style. For instance, by our second problem set, you will have learned to write functions. The problem set will be designed to test those concepts and if you revert, for instance, to writing repeated code that could be replaced with a function, points will be deducted even if that inefficient code arrives at the correct answer. 
# 
# Your lowest problem set grade of the five will be dropped.
# 
# ### Final project (35% of grade)
# 
# - I will randomly assign groups of 3-4 a few meetings in to the quarter. I've found that this is more effective than letting you choose your own groups for teaching you how to collaborate on technical projects with people who you may not always see eye to eye with!
# - I'll be releasing instructions on Canvas for two preliminary project milestones 
# - Each group will work on a project that integrates the concepts we are covering into an applied data science project. The end product will be a github repository that contains:
# 
#   - The raw source data you used for the project. This will include portions of the data I provide to all groups and external data sources you bring to the project.
#   - A pre-analysis plan where you pre-commit to certain analyses with the data: this will be especially important for the other group to be able to replicate your work.
#   - A README for the repository that, for each file, describes in detail:
#     - Inputs to the file: e.g., raw data; a file containing credentials needed to access an API/
#     - What the file does: describe major transformations.
#     - Output: if the file produces any outputs (e.g., a cleaned dataset; a figure or graph).
#   - A set of code files that transform that data into a form usable to answer the question you have posed in your descriptive research proposal.
#   - Final output: 
#     1. A 10-minute presentation, written in Beamer (presented in class on the dates listed above).
#     2. A report written in the computer science-style conference proceedings (10 pages; will share a template; due **Monday March 14th**).
# 
# 
# ### Team player/participation (10% of grade)
# 
# Data science is a highly collaborative activity in the real world and you should think of your classmates as resources rather than as competition. This part of your grade will reflect:
# 
# - Participation in class and help making the class interactive
# - Participation in coding activities in class in small groups
# - Contributions to your group's final project 
# - Helping classmates on Slack: for this, we will be using a `#problemset` channel in our class Slack for you to ask questions about roadblocks you encounter with the DataCamp activities or on the problem sets. While I will be answering questions within a window of 24 hours, I encourage you to help each other and answer each other's questions. 
# 
