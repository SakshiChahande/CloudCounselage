#!/usr/bin/env python
# coding: utf-8

# # Cloud Counselage Live Project : Data Science
# ## Data Science : Visualization
# ### Sakshi Chahande

# In[1]:


import numpy as np
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages


# In[2]:

path=input("Enter path of dataset: ")
#path= r"C:\Users\saksh\Desktop\DS_DATESET.csv"
df=pd.read_csv(path)
df=pd.DataFrame(df)
df.head(5)
df2=df


# In[3]:


df.isnull().sum()


# In[4]:


df=df.drop('Certifications/Achievement/ Research papers',axis=1)
df=df.drop('Link to updated Resume (Google/ One Drive link preferred)',axis=1)
df=df.drop('link to Linkedin profile',axis=1)
df.head()


# In[5]:


df['Have you worked core Java']=df['Have you worked core Java'].replace({'No': 0, 'Yes': 1})
df['Have you worked on MySQL or Oracle database']=df['Have you worked on MySQL or Oracle database'].replace({'No': 0, 'Yes': 1})
df['Have you studied OOP Concepts']=df['Have you studied OOP Concepts'].replace({'No': 0, 'Yes': 1})
df['Label']=df['Label'].replace({'ineligible': 0, 'eligible': 1})
df.head(10)


# In[6]:


#Q 2a. Plot number of students who applied for different technologies
dfTech=df['Areas of interest'].value_counts()
dfTech=pd.DataFrame(dfTech)


# In[7]:


dfTech.rename(columns={'Areas of interest':'Count'},inplace=True)


# In[8]:


dfTech = dfTech.rename_axis('Technology').reset_index()
dfTech.head()


# In[9]:


import matplotlib
import matplotlib.pyplot as plt


# In[10]:


plt.cla()


# In[11]:
with PdfPages('visualization-output.pdf') as pdf:

    fig1=plt.figure(figsize=(20,8))
    ax = fig1.add_axes([0,0,1,1])
    ax.barh(dfTech['Technology'],dfTech['Count'], align='center',color='#f2a5e0')
    plt.ylabel('Technology')
    plt.xlabel('Number of students')
    ax.set_yticklabels(dfTech['Technology'])
    plt.title('Q2.a. Number of students who applied for different technologies')
    for i, v in enumerate(dfTech['Count']):
        ax.text(v + 3, i + .25, str(v), color='black',fontsize='12',va='center')
    #plt.show()

    pdf.savefig(fig1,bbox_inches='tight')
    plt.close()

# In[12]:


    #Q2b The number of students applied for Data Science who knew 'Python' and who didn’t.
    
    dfDataScience=pd.DataFrame(df.loc[df['Areas of interest']=='Data Science '])
    dfDataScience.head()


# In[13]:


    total_lang_count=dfDataScience.count()['First Name']
    python_count=dfDataScience[dfDataScience['Programming Language Known other than Java (one major)']=='Python'].count()['Programming Language Known other than Java (one major)']
    #print("Total Languages: ",total_lang_count)
    not_python=total_lang_count-python_count
    #print("Python count: ", python_count)
    #print("Not Python Count:", not_python)


# In[14]:


    plt.cla()


# In[15]:



    fig = plt.figure(figsize=(20,8))
    ax = fig.add_axes([0,0,1,1])
    ax.set_title("Q2.b. Data Science Students who know Python")
    ax.bar(['Knows Python','Does not know Python'],[python_count,not_python],width=0.5,color=['#ff8080','#34b1eb'])
    for p in ax.patches:
        ax.annotate(np.round(p.get_height(),decimals=2),(p.get_x()+p.get_width()/2., p.get_height()),
                    ha='center',
                    va='center',
                    xytext=(0, 10),
                    textcoords='offset points',
                    fontsize = 12)

    #plt.show()

    pdf.savefig(fig,bbox_inches='tight')
    plt.close()


# In[16]:


# Q2 c
    dfInterest=df["How Did You Hear About This Internship?"].value_counts()
    dfInterest=pd.DataFrame(dfInterest)
    dfInterest.rename(columns={'How Did You Hear About This Internship?':'Count'},inplace=True)
    dfInterest.head()


# In[17]:


    plt.cla()


# In[18]:

    fig30=plt.figure(figsize=(20,8))
    dfInterest.plot.pie(y='Count',legend=None,autopct='%1.2f%%')
    plt.ylabel=None
    plt.xlabel=None
    plt.title('Q2.c. The different ways students learned about this program.')
    #plt.show()
    pdf.savefig(bbox_inches='tight')
    plt.close()

# In[19]:


    # Q2d Students who are in the fourth year and have a CGPA greater than 8.0.
    df['Which-year are you studying in?'].value_counts()
    dfY4=pd.DataFrame(df.loc[df['Which-year are you studying in?']=='Fourth-year'])


    # In[20]:


    plt.cla()


    # In[21]:


    greater_than_8=dfY4[dfY4['CGPA/ percentage']>=8.00].count()['CGPA/ percentage']
    less_than_8=dfY4[dfY4['CGPA/ percentage']<8.00].count()['CGPA/ percentage']


    fig3=plt.figure(figsize=(20,8))
    ax = fig3.add_axes([0,0,1,1])
    ax.set_title('Q2.d. Fourth year students with CGPA greater than or less than 8.0')
    ax.pie([greater_than_8,less_than_8],labels=['Greater than or equal to 8.0', 'Less than 8.0'],autopct='%1.2f%%',explode=[0,0.1],colors=['#5bc0de','#d9534f'])
    #plt.show()

    pdf.savefig(fig3,bbox_inches='tight')
    plt.close()


# In[22]:


    # Q 2e Students who applied for Digital Marketing with verbal and written communication score greater than 8.
    dfDM=df['Areas of interest']
    dfDM=pd.DataFrame(df.loc[df['Areas of interest']=='Digital Marketing '])
    dfDM.rename(columns={'Rate your written communication skills [1-10]':'Written','Rate your verbal communication skills [1-10]':'Verbal'},inplace=True)
    #print("Digital Marketing students :",dfDM.count()['First Name'])


# In[23]:


    written_count=dfDM[dfDM['Written']>=8].count()['CGPA/ percentage']
    verbal_count=dfDM[dfDM['Verbal']>=8].count()['CGPA/ percentage']
    written_verbal_count=dfDM[(dfDM['Written']>=8) & (dfDM['Verbal']>=8)].count()['CGPA/ percentage']
    #print("written: ",written_count)
    #print("verbal: ",verbal_count)
    #print("both: ",written_verbal_count)


# In[24]:


    plt.cla()


# In[25]:



    fig4=plt.figure(figsize=(10,8))
    ax = fig4.add_axes([0,0,1,1])
    ax.bar(['Written','Verbal','Both'],[written_count,verbal_count,written_verbal_count],color=['#2af5aa','#d9eb34','#eb3489'])
    for p in ax.patches:
            ax.annotate(np.round(p.get_height(),decimals=2),(p.get_x()+p.get_width()/2., p.get_height()),
                    ha='center',
                    va='center',
                    xytext=(0, 10),
                    textcoords='offset points',
                    fontsize = 12)

    ax.set_title('Q2.e. Communication Skills Rating of Digital Marketing Students ')
    #plt.show()
    pdf.savefig(bbox_inches='tight')
    plt.close()


# In[26]:


    # Year-wise and area of study wise classification of students.
    dfYearMajor=pd.DataFrame(df['Which-year are you studying in?'])
    dfYearMajor.replace({'First-year':'1st Year','Second-year':'2nd Year','Third-year':'3rd Year','Fourth-year':'4th Year'},inplace=True)
    dfYearMajor=dfYearMajor.join(df['Major/Area of Study'])
    dfYearMajor=dfYearMajor.join(df['State'])
    dfYearMajor.rename(columns={'Which-year are you studying in?':'Year','Major/Area of Study':'Major'},inplace=True)
    dfYearMajor.head()


# In[27]:


    dfYearMajor=dfYearMajor.groupby(["Year","Major"],as_index=False)['State'].count()


# In[28]:


    dfYearMajor.rename(columns={'State':'Count'},inplace=True)
    dfYearMajor.head(20)
    dfYearMajor.set_index(['Year'])


# In[29]:


    dfYearMajor=dfYearMajor.set_index(['Year','Major'],drop=True).unstack('Major')


# In[30]:


    dfYearMajor


# In[31]:


    plt.cla()


# In[32]:


    fig6=plt.figure(figsize=(20,8))
    ax=fig6.add_axes([0,0,1,1])
    ax=dfYearMajor.plot(kind='bar',width=0.8,color=['#8f0686','#0f068f','#068a8f'],fontsize=14)
    ax.set_title('Q2.f. Year and Major wise classification of Students',fontsize=16)
    ax.set_facecolor('white')
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5),fontsize=14)
    ax.get_yaxis().set_visible(False)
    for p in ax.patches:
            ax.annotate(np.round(p.get_height(),decimals=2),(p.get_x()+p.get_width()/2., p.get_height()),
                    ha='center',
                    va='center',
                    xytext=(0, 10),
                    textcoords='offset points',
                    fontsize = 14, fontweight='bold')



    #plt.show()
    pdf.savefig(bbox_inches='tight')
    plt.close()


# In[33]:


    # Q2f City and college wise classification of students
    dfCityCollege=df[['College name','City','State']]
    dfCityCollege.head()


# In[34]:


    dfCityCollege=dfCityCollege.groupby(["City","College name"],as_index=False)['State'].count()
    dfCityCollege.rename(columns={'State':'Count'},inplace=True)
    dfCityCollege.set_index(['City'])
    dfCityCollege.head()


# In[35]:


    dfCityCollege1=dfCityCollege.set_index(['City','College name'],drop=True)
    dfCityCollege1.head()


# In[36]:


    plt.cla()


# In[37]:



    fig7=plt.figure(figsize=(20,8))
    ax=fig7.add_axes([0,0,1,1])
    ax=dfCityCollege1.plot(kind='barh',width=0.8,color=['maroon'],fontsize=14)
    ax.set_title('Q2.g. No. of students in a college',fontsize=16)
    ax.set_facecolor('white')
    ax.invert_yaxis()
    #ax.legend(loc='center left', bbox_to_anchor=(1, 0.5),fontsize=14)
    ax.get_yaxis().set_visible(True)
    for i, v in enumerate(dfCityCollege['Count']):
        ax.text(v + 3,i + .25, str(v), color='black',fontsize='12',va='center')
    #plt.show()
    pdf.savefig(bbox_inches='tight')
    plt.close()


# In[38]:


    city_names=(dfCityCollege['City'].unique())
#print(city_names)


# In[39]:


    dfKolhapur=pd.DataFrame(dfCityCollege.loc[dfCityCollege['City']=='Kolhapur'])
    dfMumbai=pd.DataFrame(dfCityCollege.loc[dfCityCollege['City']=='Mumbai'])
    dfNaviMumbai=pd.DataFrame(dfCityCollege.loc[dfCityCollege['City']=='NaviMumbai'])
    dfPune=pd.DataFrame(dfCityCollege.loc[dfCityCollege['City']=='Pune'])
    dfSangli=pd.DataFrame(dfCityCollege.loc[dfCityCollege['City']=='Sangli'])
    dfSolapur=pd.DataFrame(dfCityCollege.loc[dfCityCollege['City']=='Solapur'])


# In[40]:


    city_count=[dfKolhapur.sum()['Count'],dfMumbai.sum()['Count'],dfNaviMumbai.sum()['Count'],dfPune.sum()['Count'],dfSangli.sum()['Count'],dfSolapur.sum()['Count']]
    city_count


# In[41]:


    plt.cla()


# In[42]:



    fig8=plt.figure(figsize=(20,8))
    ax=fig8.add_axes([0,0,1,1])
    plt.title('Q2.i.Number of students in a city')
    ax.bar(city_names,city_count,color='orange')
    for p in ax.patches:
            ax.annotate(np.round(p.get_height(),decimals=2), 
                    (p.get_x()+p.get_width()/2., p.get_height()),
                    ha='center',
                    va='center', 
                    xytext=(0, 10),
                    textcoords='offset points',
                    fontsize = 12)

    #plt.show()
    pdf.savefig(fig8,bbox_inches='tight')
    plt.close()


# In[43]:


    plt.cla()


# In[44]:



    fig9,ax=plt.subplots(3,2,figsize=(20,8))
    ax[0,0].pie(dfKolhapur['Count'],labels=dfKolhapur['College name'],autopct='%1.2f%%',textprops={'size': 'smaller'})
    ax[0,0].set_title('Kolhapur')
    ax[0,1].pie(dfMumbai['Count'],labels=dfMumbai['College name'],autopct='%1.2f%%',textprops={'size': 'smaller'})
    ax[0,1].set_title('Mumbai')
    ax[1,0].pie(dfNaviMumbai['Count'],labels=dfNaviMumbai['College name'],autopct='%1.2f%%',textprops={'size': 'smaller'})
    ax[1,0].set_title('Navi Mumbai')
    ax[1,1].pie(dfPune['Count'],labels=dfPune['College name'],autopct='%1.2f%%',textprops={'size': 'smaller'})
    ax[1,1].set_title('Pune')
    ax[2,0].pie(dfSangli['Count'],labels=dfSangli['College name'],autopct='%1.2f%%',textprops={'size': 'smaller'})
    ax[2,0].set_title('Sangli')
    ax[2,1].pie(dfSolapur['Count'],labels=dfSolapur['College name'],autopct='%1.2f%%',textprops={'size': 'smaller'})
    ax[2,1].set_title('Solapur')

    #plt.show()
    pdf.savefig(fig9,bbox_inches='tight')
    plt.close()


# In[45]:


    # Plot the relationship between the CGPA and the target variable
    dfCGPA_Target=df[['CGPA/ percentage','Label']]
    dfCGPA_Target=dfCGPA_Target.rename(columns={'CGPA/ percentage':'CGPA'})


    # In[46]:


    plt.cla()


# In[47]:



    #where 0 is ineligible and 1 is eligible
    import seaborn as sns
    sns.set(color_codes=True)
    sns.lmplot(x="CGPA", y="Label",hue='Label',data=dfCGPA_Target)
    pdf.savefig(bbox_inches='tight')
    plt.close()


# In[48]:


    #Plot the relationship between the Area of Interest and the target variable
    dfArea_Target=df[['Areas of interest','Label','State']]
    dfArea_Target=dfArea_Target.groupby(["Areas of interest","Label"],as_index=False)['State'].count()
    dfArea_Target.rename(columns={'State':'Count'},inplace=True)


# In[49]:


    plt.cla()


# In[50]:





    ax=sns.relplot(x="Areas of interest", y="Count",hue='Label',data=dfArea_Target)
    ax.set_xticklabels(rotation=90)
    pdf.savefig(bbox_inches='tight')
    plt.close()


    # In[51]:


    plt.cla()


# In[52]:



    df_elligible=dfArea_Target.loc[dfArea_Target['Label'] == 1]
    df_inelligible=dfArea_Target.loc[dfArea_Target['Label'] == 0]
    Labels = df_elligible["Areas of interest"].tolist()
    elligible_count=df_elligible["Count"].tolist()
    inelligible_count=df_inelligible["Count"].tolist()
    
    fig20=plt.figure(figsize=(20,8))
    ax=fig20.add_axes([0,0,1,1])
    dfx = pd.DataFrame({'Elligible': elligible_count,
                   'Inelligible': inelligible_count}, index=Labels)
    ax = dfx.plot.bar(rot=90,color=['#a83232','#8332a8'])

    pdf.savefig(bbox_inches='tight')
    plt.close()


# In[53]:


    #Plot the relationship between the year of study, major, and the target variable.
    dfYSMT=df2[['Which-year are you studying in?','Major/Area of Study','Label','State']]
    dfYSMT=dfYSMT.rename(columns={'Which-year are you studying in?':'Year of Study','Major/Area of Study':'Major','State':'Count'})
    dfYSMT.replace({'First-year':'1st Year','Second-year':'2nd Year','Third-year':'3rd Year','Fourth-year':'4th Year',1:'Eligible',0:'Ineligible'},inplace=True)
    dfYSMT


# In[54]:


    dfYSMT=dfYSMT.groupby(["Year of Study","Major","Label"],as_index=False)['Count'].count()


    # In[55]:


    dfYSMT.head()


    # In[56]:


    dfYSMT=dfYSMT.set_index(['Year of Study','Major','Label'],drop=True).unstack('Major','Label')
    dfYSMT


    # In[57]:


    plt.cla()


# In[58]:



    fig14=plt.figure(figsize=(20,8))
    ax=fig14.add_axes([0,0,1,1])
    ax=dfYSMT.plot(kind='bar',width=0.8,color=['#ffd470','#b8ff70','#70ffc3'],fontsize=14)
    ax.set_title('Q2. j. Year and Major wise Eligibilty of Students',fontsize=16)
    ax.set_facecolor('white')
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5),fontsize=14)
    ax.get_yaxis().set_visible(False)
    for p in ax.patches:
            ax.annotate(np.round(p.get_height(),decimals=2), 
                    (p.get_x()+p.get_width()/2., p.get_height()), 
                    ha='center', 
                    va='center', 
                    xytext=(0, 10), 
                    textcoords='offset points',
                    fontsize = 10, fontweight='bold')

    #plt.show()
    pdf.savefig(bbox_inches='tight')
    plt.close()

