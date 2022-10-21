#--------------------------------------------------------------------------#
#                  This code contains small useful functions               # 
#--------------------------------------------------------------------------#

# imports ------------------------------------------------------------------
import pandas as pd
import numpy as np
from datetime import datetime
from ast import literal_eval

# function definitions -----------------------------------------------------
def get_user_input():
    """get user input for topic to search"""
    user_input = input("Enter key words: ")
    return user_input

def format_user_input(user_input):
    """re-formats user input for API queries"""
    lower_user_input = user_input.lower()
    search_query = lower_user_input.replace(" ", "%20")
    return search_query
    
def convert_to_datetime(string):
    if string == 'no data':
        datetimeobj = 'no data'
    else:
        datetimeobj = datetime.strptime(string,"%Y-%m-%d")
    return datetimeobj

def load_from_csv(data_path):
    """Loads a csv file and converts STR representation of list to a LIST
       Why? Because when a df is saved to csv, the list of key_words are converted into STR
       Attention: the csv file must have a "key_words" column """
    df = pd.read_csv(data_path)
    df["key_words"] = df["key_words"].apply(literal_eval)
    return df

def flatten_list(list_to_flatten):
    flat_list = []
    for sublist in list_to_flatten:
        for e in sublist:
            flat_list.append(e)
    return flat_list

def clean_google_authors(df):
    authors_list = []
    for element in df.authors:
        authors_ = element.strip('et al.').split(',')
        authors = [authors_[1] + ' ' + authors_[0]]
        for i in range(2, len(authors_)):
            authors.append(authors_[i])
        authors_list.append(authors)
    return authors_list