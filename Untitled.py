
# coding: utf-8

# In[ ]:


for variable in object:
    statements


# In[6]:


lst = [1,2,3,4]
for element in lst:
    print(element, end=" ")


# In[7]:


dic = {'459':'gayatri', '235':'jogi'}


# In[8]:


for key in dic:
    print(key)


# In[10]:


for key in dic:
    print(dic[key])


# In[12]:


for value in dic.values():
    print(value)


# In[13]:


for key in dic:
    print(key, dic[key])


# In[14]:


range(0, 100)


# In[16]:


for i in range(100):
    print(i, end=" ")


# In[17]:


for i in range(2,10):
    print(i,end=" ")


# In[18]:


for i in range(2,50,2):
    print(i,end=" ")


# In[19]:


for i in range(2,70,5):
    print(i,end=" ")


# In[23]:


for i in range(1,-100,-1):
    print(i,end=" ")


# In[24]:


lst = [1, 2, 3, 4, 5, 6, 7]


# In[30]:


key = 3
for i in lst:
    if i == key:
        print("element found")
        break
print("element not found")


# In[34]:


key = 8
flag = 0
for i in lst:
    if i == key:
        flag = 1
        break
if flag == 1:
    print("element found")
else:
    print("element not found")


# In[36]:


lst = [1,2,3,4,5]
key = 7
key in lst


# In[38]:


lst = [1,2,3,4,5]
key = 4
key in lst


# In[40]:


type(range(100))


# In[41]:


lst = list(range(100))


# In[42]:


print(lst, end=" ")

