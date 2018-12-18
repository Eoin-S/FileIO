# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 12:11:59 2018

@author: ebolger2
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='adi_FileIO',  
     version='0.1',
     scripts=['adi_FileIO'] ,
     author="Eoin Bolger",
     author_email="eoin.bolger21@gmail.com",
     description="This package contains File IO functions",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/javatechy/dokr",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )