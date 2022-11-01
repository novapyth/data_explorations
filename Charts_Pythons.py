#!/usr/bin/env python
# coding: utf-8

# # Pie charts using matplotlib

# In[1]:


import matplotlib.pyplot as plt


# In[23]:


# Data
labels = ["G1", "G2", "G3", "G4", "G5"]
value = [12, 22, 16, 38, 12]

# Pie chart
fig, ax = plt.subplots()
ax.pie(value, labels = labels)
plt.show()


# In[24]:


# Data
labels = ["G1", "G2", "G3", "G4", "G5"]
value = [0.1, 0.2, 0.1, 0.2, 0.1]

# Pie chart
fig, ax = plt.subplots()
ax.pie(value, labels = labels, normalize = False)
plt.show()


# # Clockwise pie chart
# 
# As stated before, the pie chart will be created by default counterclockwise. To set a clockwise direction set the argument counterclock as False.

# In[25]:


# Data
labels = ["G1", "G2", "G3", "G4", "G5"]
value = [12, 22, 16, 38, 12]

# Pie chart
fig, ax = plt.subplots()
ax.pie(value, labels = labels, counterclock = False)
plt.show()


# # Start angle
# 
# The pie will rotate counterclockwise from the X-axis by default. You can change the start angle with startangle. As an example, if you set this argument to 90 the first slice will start to rotate counterclokwise perpendicular to the X-axis.

# In[26]:


# Data G1-G5 at  at start angle 90
labels = ["G1", "G2", "G3", "G4", "G5"]
value = [12, 22, 16, 38, 12]

# Pie chart
fig, ax = plt.subplots()
ax.pie(value, labels = labels, startangle = 90)
plt.show()


# In[27]:


# Data A1-A5 at start angle 70
labels = ["A1", "A2", "A3", "A4", "A5"]
value = [110, 220, 160, 390, 140]

# Pie chart
fig, ax = plt.subplots()
ax.pie(value, labels = labels, startangle = 70)
plt.show()


# In[28]:


# Data A1-A5 at start angle 45
labels = ["A1", "A2", "A3", "A4", "A5"]
value = [110, 220, 160, 390, 140]

# Pie chart
fig, ax = plt.subplots()
ax.pie(value, labels = labels, startangle = 70)
plt.show()


# # Explode
# 
# Note that you can also explode (offset) one or some slices of the pie passing an array of the length of the data to explode.

# In[29]:


# Data, once explode
labels = ["G1", "G2", "G3", "G4", "G5"]
value = [12, 22, 16, 38, 12]
explode = [0, 0, 0, 0.1, 0]

# Pie chart
fig, ax = plt.subplots()
ax.pie(value, labels = labels, explode = explode)
plt.show()


# In[30]:


# Data,twice explode
labels = ["G1", "G2", "G3", "G4", "G5"]
value = [12, 22, 16, 38, 12]
explode = [0, 0, 0.1, 0.1, 0]

# Pie chart
fig, ax = plt.subplots()
ax.pie(value, labels = labels, explode = explode)
plt.show()


# # Add a shadow
# 
# The pie function also allows adding a shadow to the pie setting the shadow argument to True.

# In[31]:


# Data
labels = ["G1", "G2", "G3", "G4", "G5"]
value = [112, 212, 161, 318, 192]

# Pie chart
fig, ax = plt.subplots()
ax.pie(value, labels = labels, shadow = True)
plt.show()


# # Add the frame of the plot
# 
# You might have noticed that the default pie doesn’t display the typical frame of the charts created with matplotlib. In case you want to add it you can set frame = True.

# In[21]:


# Data
labels = ["G1", "G2", "G3", "G4", "G5"]
value = [12, 22, 16, 38, 12]

# Pie chart
fig, ax = plt.subplots()
ax.pie(value, labels = labels, frame = True)
plt.show()


# # Pie chart labels

# # Percentage labels distance to the origin
# 
# Note that you can customize the distance of these labels from the origin and display them instead of the group labels. The default value is 0.6.

# In[20]:


# Data
labels = ["G1", "G2", "G3", "G4", "G5"]
value = [12, 22, 16, 38, 12]

# Pie chart
fig, ax = plt.subplots()
ax.pie(value, autopct = '%1.1f%%', pctdistance = 1.1)
plt.show()


# In[19]:


labels = ["A1", "A2", "A3", "A4", "A5"]
value = [110, 220, 160, 390, 140]

# Pie chart
fig, ax = plt.subplots()
ax.pie(value, autopct = '%1.1f%%', pctdistance = 1.1)
plt.show()


# # Group labels distance to the origin
# 
# In addition, you can also modify the default distance (1.1 for a slice of radius 1) of the group labels with labeldistance.

# In[34]:


labels = ["A1", "A2", "A3", "A4", "A5"]
value = [110, 220, 160, 390, 140]

# Pie chart
fig, ax = plt.subplots()
ax.pie(value, autopct = '%1.1f%%', pctdistance = 0.7)
ax.pie(value, labels = labels, labeldistance = 1.0)
plt.show()


# # Labels rotation
# 
# Finally, it is also possible to rotate the group labels to the angle of the corresponding slice setting rotatelabels as True.

# In[36]:


labels = ["A1", "A2", "A3", "A4", "A5"]
value = [110, 220, 160, 390, 140]

# Pie chart
fig, ax = plt.subplots()
ax.pie(value, autopct = '%1.1f%%', pctdistance = 0.7)
ax.pie(value, labels = labels, labeldistance = 1.1, rotatelabels = True)
plt.show()


# In[37]:


labels = ["A1", "A2", "A3", "A4", "A5"]
value = [110, 220, 160, 390, 140]
# Pie chart
fig, ax = plt.subplots()
ax.pie(value, autopct = '%1.1f%%', pctdistance = 0.7, labels = labels, labeldistance = 1.1, rotatelabels = True)
plt.show()


# # Pie chart colors
# The colors argument allows customizing the fill color for each slice. You can input an array of ordered colors to change the color for each category.

# In[38]:


labels = ["A1", "A2", "A3", "A4", "A5"]
value = [110, 220, 160, 390, 140]
colors = ["#B9DDF1", "#9FCAE6", "#73A4CA", "#497AA7", "#2E5B88"]

# Pie chart
fig, ax = plt.subplots()
ax.pie(value, labels = labels, colors = colors)
plt.show() 


# In[39]:


labels = ["A1", "A2", "A3", "A4", "A5"]
value = [110, 220, 160, 390, 140]
colors = ["#B9DDF1", "#9FCAE6", "#73A4CA", "#497AA7", "#2E5B88"]

# Pie chart
fig, ax = plt.subplots()
ax.pie(value, labels = labels, colors = colors,
      wedgeprops = {"linewidth": 1, "edgecolor": "white"})
plt.show() 


# In[42]:


labels = ["A1", "A2", "A3", "A4", "A5"]
value = [110, 220, 160, 390, 140]
colors = ["#B9DDF1", "#9FCAE6", "#73A4CA", "#497AA7", "#2E5B88"]

# Pie chart
fig, ax = plt.subplots()
ax.pie(value,  autopct = '%1.1f%%', pctdistance = 0.7, 
       labels = labels, colors = colors, labeldistance = 1.1, rotatelabels = True,
      wedgeprops = {"linewidth": 1, "edgecolor": "white"})
plt.show() 


# # References:
#     # 1. https://python-charts.com/part-whole/pie-chart-matplotlib/
#     # 2. https://matplotlib.org/

# In[ ]:




