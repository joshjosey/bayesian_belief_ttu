"""
The process data module contains functions to process specific data sets
"""
import pandas as pd


def process_lung_data(path_to_data):
    """
    Function to load in & format data from the Lung_Cancer_Data.csv file

    Input: 
        path_to_data: the file path (ex. './data/Lung_Cancer_Data.csv')

    Output:
        data: a pandas dataframe formatted to work with pgmpy estimators
    """
    #use pandas to read the CSV file into a dataframe
    df = pd.read_csv(path_to_data)

    #remove unnecessary columns
    df = df.drop(columns=['index', 'Patient Id'])  # Remove unnecessary columns

    #rename columns to make the names consistent (if needed, can also change column names in the data file)
    df = df.rename(columns={'Alcohol use': 'Alcohol Use'})

    #example of how to manipulate columns if needed, converts the age column to a binary column
    df = df.rename(columns={'Age': 'Over 50'})
    df['Over 50'] = df['Over 50'].apply(lambda l: 0 if l < 50 else 1)

    #conver the level column from strings to integer data
    df['Level'] = df['Level'].apply(lambda l: 0 if l == "Low" else 1 if l == "Medium" else 2)

    # Create a subset of the attributes for testing
    data = df[['Coughing of Blood', 'Air Pollution', 'Alcohol Use', 'Smoking', 'Fatigue', 'Frequent Cold', 'Dry Cough', 'Level', 'Chest Pain']]
    
    #return the processed data set
    return data