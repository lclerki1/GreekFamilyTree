
# coding: utf-8

# In[1]:

import lineage_module as lm
import pandas as pd


# In[2]:

df = pd.read_csv("ASK_zeta_lineage.csv")
df.fillna("", inplace=True)


# In[4]:

dfc = pd.read_csv("family_colors.csv")
dfc.fillna("", inplace=True)


# In[6]:

lm.generate_family_trees_withColors(df, dfc, output_loc='lineage/')


# In[ ]:



