## CASE STUDY DATASET CREATION ##

## This company previously ran a marketing campagin for a product they offer. 
## They want to do it again, but be more strageic
## Which customers should they target for communications? (segmentation)
## Which customers are most likely to purchase the product? (explore or modeling)
## What recommendations do you have for marketing strategies? (synthethize)

import numpy as np
import pandas as pd

file_dir = 'case-study/marketing-bank/data/'
df = pd.read_csv(file_dir + 'bank-additional-full.csv', sep=';')

# make the binarize the response
df['deposit'] = np.where(df.y == 'yes', 1, 0)

# drop duration
drop_cols = [
  'duration',
  'y',
  'emp.var.rate',
  'cons.price.idx',
  'cons.conf.idx',
  'euribor3m',
  'nr.employed'
]
df = df.drop(drop_cols, axis=1)

# modernize the contact methods
contact_mapping = {
  'contact': {
    'cellular': 'app',
    'unknown': 'email',
    'telephone': 'push'
  }
}
df = df.replace(contact_mapping)

# update education
education_mapping = {
  'education': {
    'basic.4y': 'other',
    'basic.6y': 'other',
    'basic.9y': 'other',
    'high.school': 'high school',
    'illiterate': 'other',
    'professional.course': 'graduate/professional',
    'university.degree': 'undergraduate',
  }
}
df = df.replace(education_mapping)

# re-code jobs
job_mapping = {
  'job': {
    'admin.': 'other',
    'entrepreneur': 'business',
    'management': 'education',
    'blue-collar': 'trade',
    'housemaid': 'retail',
    'technician': 'technology'
  }
}
df = df.replace(job_mapping)

# create NAs for days since last campaign
df['pdays'] = np.where(df['pdays'] == 999, np.nan, df[col])
    
# rename columns
df = df.rename(columns={
  'contact': 'channel',
  'campaign': 'cur_campaign_cnt',
  'previous': 'prev_campaign_cnt',
  'poutcome': 'prev_campaign_outcome',
  'pdays': 'prev_campaign_days'
  })

# save data
df.to_csv(file_dir + 'bac_bank_marketing.csv', index=False)

