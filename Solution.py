import pandas as pd

df = pd.read_csv('/Users/Karl/Documents/audible_uncleaned.csv')

#Remove all text before and including ':' from the author and narrator columns

df["author"] = df["author"].str.replace(r"^.*?:", "", regex=True)

df["narrator"] = df["narrator"].str.replace(r"^.*?:", "", regex=True)

#Seperate names using capital letters as break points

df["author"] = df["author"].str.findall(r'[A-Z][^A-Z]*').str.join(" ")

df["narrator"] = df["narrator"].str.findall(r'[A-Z][^A-Z]*').str.join(" ")

#Remove text from the time column and convert hours and minutes to minutes

df["time"] = (
    df["time"].str.extract(r"(\d+)\s*(?:h|hr|hrs|hour|hours)", expand=False)
        .astype(float).fillna(0) * 60
    +
    df["time"].str.extract(r"(\d+)\s*(?:m|min|mins|minute|minutes)", expand=False)
        .astype(float).fillna(0)
).astype(int)

#Rename time and releasedate columns to time_mins and release_date

df.rename(columns={"time": "time_mins"}, inplace=True)

df.rename(columns={"releasedate": "release_date"}, inplace=True)

#Remove text from stars column and split ratings into its own column

df[["stars", "ratings"]] = df["stars"].str.extract(
    r"(\d+(?:\.\d+)?)\s*out of\s*\d+\s*stars\s*(\d+)\s*ratings"
)

df["stars"] = df["stars"].astype(float)
df["ratings"] = df["ratings"].astype('Int64')


df.to_csv('/Users/Karl/Documents/audible_cleaned_1.csv', index=False)

#Reorder columns in the csv so that the new ratings column follows the stars column 

cols = df.columns.tolist()

cols.remove('ratings')

price_idx = cols.index('price')

cols.insert(price_idx, 'ratings')

df=df[cols]

df.to_csv('/Users/Karl/Documents/audible_cleaned_1.csv', index=False)


 
name                                            author            narrator      time_mins   release_date   language  stars  ratings   price  
0   Geronimo Stilton 11 & 12                    Geronimo Stilton    Bill Lobely        140        04-08-08      English    5.0     34.0  468.00  
1   The Burning Maze                            Rick Riordan        Robbie Daymond     788        01-05-18      English    4.5     41.0  820.00   
2   The Deep End                                Jeff Kinney         Dan Russell        123        06-11-20      English    4.5     38.0  410.00   
3   Daughter of the Deep                        Rick Riordan        Soneela Nankani    676        05-10-21      English    4.5     12.0  615.00  
4   The Lightning Thief: Percy Jackson, Book 1  Rick Riordan        Jesse Bernstein    600        13-01-10      English    4.5    181.0  820.00 

         
   
   
