# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 10:35:47 2018

@author: ebolger2
"""

import glob, os
import pandas as pd

def folderSearch(pathname,fileExt = "*.csv",debug = False):
    '''
        This function is used to Search for all Files in a Directory
        With a certain File extension. 
        
        Embedded in this function is a Directory Path fix which will 
        replace all back slashes (\) with a Double back slash as the
        backshash is a special charter and cannot be handled like a
        standard charterector.
    '''
    #Create empty Arrays to store File Names and Full Directories
    csvFileNames = []
    csvFileDir = []
    
    if debug == True:
        print('file ext:',fileExt) # For debug purposes only
    
    #NB: Important Step, Replace all '\' with a double '\\'
    pathname = pathname.replace('\\','\\\\')
    
    if debug == True:
        print('The path named being used is ',pathname)
        
    os.chdir(pathname)
    
    for file in glob.glob(fileExt):
        csvFileDir.append(pathname+ '\\' + file)
        csvFileNames.append(file)
    return (csvFileNames,csvFileDir)

def csvRead(fileName,debug = False, sep = str(',')):
    '''
    This function is used to load in the data file all at once in a matrix 
    object. 
    
    '''
    
    df = pd.read_csv(fileName, sep )#generate data frame
    
    if df.empty == False:
        size = df.shape
        headers = df.columns
        if debug == True:
            print('--------Debug info:Start--------')
            print('Is this dataframe empty? ',df.empty)
            print('The imported DataFrame has',size[0],'number of rows & ',size[1],'number of Columns')
            print('The Headers in the file are:\n',headers)
            print('--------Debug info:End--------')
            '''
            This works however is considerably slower then .shape property
            https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe 
            
            print('Number of columns',len(CSV_Data.columns))
            print('Number of Rows',len(CSV_Data.index))
            '''
    else:
        print('Error')
            

    return (headers,df,size)


# In[409]:


def findHeader(fileName,debug = False, sep = str(',')):
    '''
        This Function is used to locate the row in the file which is empty.
    '''
    found = False
    n_rows = 0
    while found == False or n_rows > 1000:
        n_rows = n_rows +20
        dfh = pd.read_csv(fileName, sep,nrows = n_rows,header = None)

        for i,row in dfh.iterrows():
            # first column
            if row.isnull().all():
                found = True
                if debug == True:
                    print('The Head is located on the ',i,'Row.')
                
                break
        if debug == True:
            print('Empty Row found ? ',found)
        headerPos = 1 + i
    
    return(headerPos)


# In[410]:


def csvReadPD(fileName,debug = False, sep = str(',')):
    '''
    This function is used to load in the data file all at once in a matrix 
    object. 
    
    '''
    
    startPoint = findHeader(fileName,debug)

    df = pd.read_csv(fileName, sep,skiprows = startPoint)#generate data frame
    
    if df.empty == False:
        '''
            This works however is considerably slower then .shape property
            https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe 
            
            print('Number of columns',len(CSV_Data.columns))
            print('Number of Rows',len(CSV_Data.index))
        '''
        size = df.shape
        headers = df.columns
        if debug == True:
            print('--------Debug info:Start--------')
            print('Is this dataframe empty? ',df.empty)
            print('The imported DataFrame has',size[0],'number of rows & ',size[1],'number of Columns')
            print('The Headers in the file are:\n',headers)
            print('--------Debug info:End--------')
            
            print(df)
            
    else:
        print('Error')
            

    return (headers,df,size)