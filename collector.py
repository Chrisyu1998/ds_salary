import glassdoor_scraper as gsimport pandas as pdpath = "/Users/cyt/Downloads/ds_salary/chromedriver"df = gs.get_jobs('software engineer',500,False,path,30)df.to_csv('glassdoor_jobs.csv',index = False)