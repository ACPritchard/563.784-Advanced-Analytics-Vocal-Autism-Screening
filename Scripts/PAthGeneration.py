
# coding: utf-8

# In[1]:


import numpy as np
import os
from pathlib import Path


# In[11]:


rootDir = Path("F:/AdvancedDataAnalysisData/Lanna_speech_database_children/Data/Data/Patients/")


# In[5]:


for path in rootDir.iterdir():
    print(path)


# In[12]:


for root, dirs, files in os.walk(rootDir):
    for file in files:
        if file.endswith(".wav"):
            command = "SMILExtract_Release -C F:\AdvancedDataAnalysisData\opensmile-2.3.0\config\emobase2010.conf -I "+ os.path.join(root, file) +" -O F:\AdvancedDataAnalysisData\TestOut.csv"
            #print(os.path.join(root, file))
            print(command)

