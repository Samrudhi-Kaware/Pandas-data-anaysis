import pandas as pd
import numpy as np
# ML Processing in details
# operations
# - selection
# - indexing
# - slicing
# - filtering
# -> data wrongling
#   - data cleaning
#   - data transformation
#   - deduplication
#   -> data enrichment
#     - adding new columns
#     - binning
#     - aggregation (query, groupby, mean, min, max)
#     - re-sampling

def function1():
    df = pd.read_csv('customers.csv')
    print(df.columns)
    # selection
    #print(df['Age'])
    #print(f"type of Age = {type(df['Age'])}")
    #selecting 2 columns
    #print(df[['Age', 'Income']])
    #categorial to numeric
    #print(df.Age.unique())
    #print(df.Gender.value_counts())
#function1()

def function2():
    df = pd.read_csv('customers.csv')
    # loc
    # print(df['Age'])
    # print(df.loc[0, 'Age'])
    #select col: age gender , row is 0
    #print(df.loc[0, ['Age', 'Gender']])
    print(df.loc[10:21, ['CustomerID', 'Gender', 'Age', 'Income', 'Score']])
# function2()


def function3():
    df = pd.read_csv('Wine.csv')
    print(df.columns)
    # iloc used when we have multiple columns uca fetch over using col index
    print(df.columns)
    # iloc
    # print(df.iloc[0, 0])
    print(df.iloc[10:20, 2:5])
# function3()


def function4():
    df = pd.read_csv('customers.csv')
    print(df.columns)
    # slicing
    # print(df[10:20])
    print(df.loc[10:20, ['Age', 'Gender']])
    # print(df.iloc[10:20, 1:3])
    # print(df[['Gender', 'Age']][10:20])
#function4()

def function5():
    df = pd.read_csv('customers.csv')
    print(df.columns)
    # filtering
    #print(df.Age > 30)
    #print(df[df.Age > 30])
    print(df[(df.Income > 50) & (df.Age > 30)])
    print(df[(df.Income > 50) | (df.Age > 30)])
function5()