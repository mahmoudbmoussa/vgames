import pandas as pd


path_books="Books_Data_Clean.xlsx" #path books file
path_games = "vgsales.xlsx" #path games file


def CleanSpecialChars(path,column_name):
    df = pd.read_excel(path)
    clean_df = df[~df[column_name].str.contains(r'[^\x00-\x7F]', na=False)]
    print(clean_df["Name"])
    clean_df.to_excel(path, index=False)
    
#CleanSpecialChars(path_books,"Book Names") #delete special characters in books file
#CleanSpecialChars(path_games,"Name") #delete special characters in vsg file