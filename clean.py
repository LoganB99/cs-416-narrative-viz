import pandas as pd

df = pd.read_csv('~/Downloads/TMDB_movie_dataset_v11.csv')

df.drop(columns=['imdb_id', 'spoken_languages', 'production_countries', 'production_companies', 'runtime', 'adult', 'backdrop_path', 'homepage', 'overview', 'tagline', 'original_title', 'original_language', 'status', 'poster_path'], inplace=True)
df['keywords'] = df['keywords'].fillna('')
df['contains_superhero'] = df['keywords'].apply(lambda x: 1 if 'superhero' in x else 0)

df.drop(columns=['keywords'], inplace=True)

df.dropna(inplace=True)

df.drop_duplicates(inplace=True)

df = df.map(lambda x: x.replace('\u2028', '').replace('\u2029', '') if isinstance(x, str) else x)

# Convert release_date to year
df['release_date'] = pd.to_datetime(df['release_date']).dt.year

# drop movies before 2000
df = df[df['release_date'] >= 2000]

# Replace the existing 'id' column with a new calculated id
df['id'] = range(1, len(df) + 1)

df.reset_index(drop=True, inplace=True)
print(df.columns)
print(df.head())


df.to_csv('~/Downloads/TMDB_movie_dataset_v11_clean.csv', index=False)
