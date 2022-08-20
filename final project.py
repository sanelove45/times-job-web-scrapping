#!/usr/bin/env python
# coding: utf-8

# In[34]:


#------------------WEB SCRAPING PROJECT----------------------#

base_url='https://www.timesjobs.com/candidate/job-search.html?from=submit&searchType=Home_Search&luceneResultSize=25&postWeek=60&cboPresFuncArea=35&pDate=Y&sequence='
    
                                                     # this is a main url of website for scrapping data.

common_url='&startPage=1'                            # this is common page url.

all_urls=[]

for item in range(1,41):
    all_urls.append(base_url+str(item)+common_url) 

    #print(all_urls)                # fetched 40 links of page, one page has 25 jobs (40*25=1000).
    
import requests                  # requests useed for extract data from website.
from bs4 import BeautifulSoup    # beatifulsoup to understand HTML code for python.


all_fetched_data=[]                  # list created for store list of dictionary data.

for url in all_urls:
    source_data=requests.get(url).text           # data from website.
    #print(source_data)
        
    soup_data=BeautifulSoup(source_data,'lxml')   # converted data from python to beautifulsoup.
    #print(soup_data)
        
    all_pages_data=soup_data.find_all('li',class_='clearfix job-bx wht-shd-bx')     # tags of HTML which contain job detail
    #print(all_pages_data)

    for item in all_pages_data:

        job_title=item.find('h2').text                                      # fetched job_title,
        #job_title=job_title.lstrip()

        company_name=item.find('h3',class_='joblist-comp-name').text        # fetched job_company_name,
        companyname=company_name.lstrip().split()[0]
        #print(companyname)

        experience=item.find('li').text                                      # fetched job_experience, 
        experience1=experience.replace('card_travel','')
        #print(experience1)

        location=item.find('span').text                                      # fetched job_loaction,
        location1=location.lstrip()
        #print(location1)

        job_discription=item.find('ul',class_='list-job-dtl clearfix').text   # fetched job_description,
        jobdescription=job_discription.splitlines()[3:4]                     
        jobdescription=','.join(jobdescription)
        #print(jobdescription)

        key_skill=item.find('span',class_='srp-skills').text         # fetched job_key_skill,
        keyskill=key_skill.lstrip().splitlines()[0:1]               
        keyskill=(','.join(keyskill))
        #print(keyskill)

        job_link=item.find('a')['href']              # fetched job_details_link,
        #print(job_link) 
        
        dict1={
            'Job Title': job_title,
            'Company Name': companyname,
            'Experience': experience1,
            'Location': location1,
            'Job Description': jobdescription,
            'Key Skills': keyskill,
            'Job Detail Link': job_link
        }
            
        #print(dict1)
            
        all_fetched_data.append(dict1)
            
        print(all_fetched_data)


# In[42]:


pip install pandas


# In[43]:


pip install xlrd


# In[44]:


import pandas as pd


# In[45]:


df1=pd.DataFrame(all_fetched_data)


# In[46]:


df1


# In[47]:


df1.to_excel('web-scrapping-project.xlsx')           # exporting data to excel sheet


# In[ ]:




