#!/usr/bin/env python
# coding: utf-8

# In[52]:


#1 ВАРИАНТ 2
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("titanic_train.csv", sep = ",")


# In[15]:


#2 Представьте данные в виде таблицы. Посмотрите на первые 5 строк.
df.head()


# In[18]:


#3 Выведите на экран основную информацию (info) о наборе данных и признаках
df.info()


# In[30]:


#4 Выведите на экран данные о самой молодой женщине, находящемся на борту
df["Sex"] =="female"
df["Age"].min()


# In[36]:


#5 Выведите распределение переменной Pclass по всем классам (социально-экономический статус) и это же распределение, только для женщин по отдельности. Сколько было женщин 1-го класса?
df["Pclass"].value_counts()


# In[37]:


#5 
df[(df["Pclass"] == 1 ) & (df["Sex"] == "female")]


# In[38]:


#6 Сколько женщин до 50 лет погибли при крушении?
df[(df["Survived"] == 0 ) & (df["Age"] < 51)]


# In[43]:


#7 Подсчитать средний возраст мужчин вышивших при крушении
df[df["Sex"] == "male"] ["Age"].mean()


# In[44]:


#8 Постройте попарные зависимости признаков Age, Fare, Pclass, Sex, SibSp, Parch, Embarked и Survived. (метод scatter_matrix Pandas или pairplot Seaborn).
sns.set_theme(style="darkgrid")
sns.pairplot(df[["Age", "Fare", "Pclass", "Sex", "SibSp", "Parch", "Embarked", "Survived"]])


# In[45]:


#9 Каково соотношение погибших и выживших в зависимости от пола? Отобразите c помощью Seaborn.countplot c аргументом hue.
sns.countplot(x="Survived", hue="Sex", data = df)


# In[46]:


#10 Как плата за билет (Fare) зависит от класса каюты (Pclass)? Постройте boxplot.
sns.set_theme(style="darkgrid")
sns.boxplot (data = df, y ="Fare", x="Pclass")


# In[51]:


#11 Постройте график рассеяния на осях Age и Fare. Cиним отметьте пассажиров, которые не выжили (Survived = 0) и красным — выживших (Survived = 1).
plt.xlabel("Age")
plt.ylabel("Fare")

plt.scatter (df["Age"], df["Fare"] ,  c = df["Survived"], cmap = "bwr");
handles, labels = scatter.legend_elements()
labels = ['Not Survived', 'Survived']
plt.legend(handles, labels)
plt.show()


# In[ ]:





# In[ ]:




