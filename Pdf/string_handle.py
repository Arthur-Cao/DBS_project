#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 12:28:47 2018

@author: Cris
"""
from AzureTextAnalytics import azure_api
from pdf2text import pdf2text
from split_5k import split_5k

#total_string = pdf2text("case study.pdf")
#intersected_string = split_5k(total_string,5000)
#print(azure_api2(intersected_string))

def generate_keyword (rawfile,s='keyPhrases'):
    total_string = pdf2text(rawfile)
    intersected_string = split_5k(total_string,5000)
    azure_result = azure_api(intersected_string, s)  #will call API and return a dict
    return azure_result

def generate_sentiment (rawfile,s='sentiment'):
    total_string = pdf2text(rawfile)
    intersected_string = split_5k(total_string,5000)
    azure_result = azure_api(intersected_string, s)  #will call API and return a dict
    return azure_result

def generate_entity (rawfile,s='entities'):
    total_string = pdf2text(rawfile)
    intersected_string = split_5k(total_string,5000)
    azure_result = azure_api(intersected_string, s)  #will call API and return a dict
    return azure_result
