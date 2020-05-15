#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 10:39:35 2020

@author: cyt
"""

import pandas as pd

df = pd.read_csv("glassdoor_jobs.csv")

#create min, max, avg_salary
salary = df["Salary Estimate"].apply(lambda x: x.split('(')[0])
noK = salary.apply(lambda x: x.replace('K','').replace('$',''))
df["min_salary"] = noK.apply(lambda x: x.split('-')[0])
df["max_salary"] = noK.apply(lambda x: x.split('-')[1])

df['min_salary'] = pd.to_numeric(df['min_salary'])
df['max_salary'] = pd.to_numeric(df['max_salary'])
df["avg_salary"] = (df.min_salary + df.max_salary)/2


# clean company name
df.columns
df['Company Name'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

# clean state
df["job_st"] = df['Location'].apply(lambda x: 1 if ',' in x.lower() else 0)
df['job_state'] = df.apply(lambda x: x['Location'].split(',')[1] if x['job_st'] > 0 else x['Location'], axis = 1)
df['job_state'] = df.apply(lambda x: ' VA' if x['Location'] == 'Virginia' else x['job_state'], axis =1)
df['job_state'] = df.apply(lambda x: ' WI' if x['Location'] == 'Wisconsin' else x['job_state'], axis =1)
df['job_state'] = df.apply(lambda x: ' CA' if x['Location'] == 'California' else x['job_state'], axis =1)
df = df[df['job_state'] != 'Remote']
df = df[df['job_state'] != 'United States']
df['head_state'] = df.apply(lambda x: x['Headquarters'].split(',')[1] if x['Headquarters'] != '-1' else x['Headquarters'], axis =1)
df["same_state"] = df.apply(lambda x:  1 if x.head_state == x.job_state else 0 , axis = 1)

#clean age
df['age (2020)'] = df['Founded'].apply(lambda x: x if x == -1 else 2020-x)

# clean description
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['java_yn'] = df['Job Description'].apply(lambda x: 1 if 'java' in x.lower() else 0)
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['api_yn'] = df['Job Description'].apply(lambda x: 1 if 'api' in x.lower() else 0)

#title
def job_title(title):
    if 'data' in title.lower():
        return 'database'
    elif 'technical' in title.lower() or 'IT' in title:
        return 'technical'
    elif 'web' in title.lower():
        return 'front_end'
    elif 'software' in title.lower():
        return 'software'
    else:
        return 'others'
    
df['job_simple'] = df['Job Title'].apply(job_title)

def seniority(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'lead' in title.lower() or 'master' in title.lower():
        return 'senior'
    elif 'junior' in title.lower() or 'jr' in title.lower():
        return 'junior'
    else:
        return 'na'

df['seniority'] = df['Job Title'].apply(seniority)
df.seniority.value_counts()    

df['desc_len'] = df['Job Description'].apply(lambda x: len(x))
df['Competitors'] = df['Competitors'].apply(lambda x: len(x.split(',')) if x != '-1' else 0)
df['Company'] = df['Company Name'].apply(lambda x: x.replace('\n',''))




