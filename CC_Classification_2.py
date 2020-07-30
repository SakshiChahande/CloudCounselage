#!/usr/bin/env python
# coding: utf-8

# # Cloud Counselage Live Project 
# ## Sakshi Chahande
# ### Classification: Identify the best binary classifier to classify data into “eligible/1” and “not eligible/0”

# In[1]:


import numpy as np
import pandas as pd
path=input("Enter the document ")
#path= r"C:\Users\saksh\Desktop\DS_DATESET.csv"
df=pd.read_csv(path)
df=pd.DataFrame(df)
df.head(5)


# In[2]:


#3. Identify the best binary classifier to classify data into “eligible/1” and “not eligible/0”.
import sklearn
from sklearn import preprocessing


# In[3]:


dfNew=df
columns=dfNew.columns.tolist()
#print(columns)


# In[4]:


dfNew=dfNew.rename(columns={'DOB [DD/MM/YYYY]':'DOB','Major/Area of Study':'Major','Which-year are you studying in?':'Year',
                      'CGPA/ percentage':'CGPA','Have you worked core Java':'Java',
                      'Programming Language Known other than Java (one major)':'Language',
                      'Have you worked on MySQL or Oracle database':'Database',
                      'Have you studied OOP Concepts':'OOP','Rate your written communication skills [1-10]':'Written',
                      'Rate your verbal communication skills [1-10]':'Verbal','How Did You Hear About This Internship?':'Internship Info'
                     })


# In[5]:


dfNew=dfNew.drop('Certifications/Achievement/ Research papers',axis=1)
dfNew=dfNew.drop('Link to updated Resume (Google/ One Drive link preferred)',axis=1)
dfNew=dfNew.drop('link to Linkedin profile',axis=1)


# In[6]:


dfNew['Java']=dfNew['Java'].replace({'No': 0, 'Yes': 1})
dfNew['Database']=dfNew['Database'].replace({'No': 0, 'Yes': 1})
dfNew['OOP']=dfNew['OOP'].replace({'No': 0, 'Yes': 1})
dfNew['Label']=dfNew['Label'].replace({'ineligible': 0, 'eligible': 1})
dfNew


# In[7]:


degree = pd.get_dummies(dfNew['Degree'],drop_first = True)
major = pd.get_dummies(dfNew['Major'])
year = pd.get_dummies(dfNew['Year'],drop_first = True)
area = pd.get_dummies(dfNew['Areas of interest'],drop_first = True)
language = pd.get_dummies(dfNew['Language'],drop_first = True)


# In[8]:


dfNew=pd.concat([dfNew,degree,major,year,area,language],axis = 1)
dfNew


# In[9]:



from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
dfNew = dfNew.apply(LabelEncoder().fit_transform)


# In[10]:


dfNew.head()


# In[11]:


#print(dfNew.columns.to_list())


# In[12]:


dfNew.drop(['First Name','Last Name','City',
 'State', 'Areas of interest','Major','Degree','Year',
 'Zip Code',
 'DOB','Email Address',
 'Contact Number',
 'Emergency Contact Number',
 'College name',
 'University Name'],axis = 1, inplace = True)


# In[13]:


#print(dfNew.columns.to_list())


# In[14]:


dfNew.head()


# In[15]:


from sklearn.model_selection import train_test_split
Y=dfNew['Label']
X=dfNew[['Age', 'Gender', 'Course Type', 'CGPA', 
          'Expected Graduation-year', 'Current Employment Status', 'Java', 'Language', 
          'Database', 'OOP', 'Written', 'Verbal', 'Internship Info', 'B.Tech', 'Computer Engineering', 
          'Electrical Engineering', 'Electronics and Telecommunication', 'Fourth-year', 
          'Second-year', 'Third-year', 'Big Data ', 'Blockchain ', 'Cloud Computing ', 
          'Cyber Security ', 'Data Science ', 'DevOps ', 'Digital Marketing ', 'Information Security',
          'IoT ', 'Machine Learning', 'Mobility', 'Python ', 'QMS/Testing ', 'RPA ', 'Web Development ',
         'C', 'C#', 'C++', 'HTML/CSS', 'JavaScript', 'PHP', 'Python']]


# In[17]:


X_train,X_test,y_train,y_test = train_test_split(X,Y,random_state = 1)
X_train.head()


# ## Random Forest Classifier

# In[18]:


from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators = 500,max_depth=2,random_state=42,)
rf.fit(X_train,y_train)


# In[20]:


from sklearn.metrics import f1_score,accuracy_score,confusion_matrix,r2_score,classification_report
import itertools
y_pred = rf.predict(X_test)
score = accuracy_score(y_test,y_pred)
f1 = f1_score(y_test,y_pred)
print(f1)


# In[21]:


#print(confusion_matrix(y_test,y_pred))


# In[22]:


#print(classification_report(y_test,y_pred))


# In[24]:


#import matplotlib.pyplot as plt
#import seaborn as sns
#plt.figure(figsize = (10, 10))
#sns.heatmap(dfNew.corr());
#plt.show()

