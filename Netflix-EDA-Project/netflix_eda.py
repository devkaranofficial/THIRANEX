import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------
# Load Dataset
# ----------------------------------------

df = pd.read_csv("netflix_titles.csv")

print("=" * 60)
print("NETFLIX EDA PROJECT")
print("=" * 60)

# ----------------------------------------
# Dataset Information
# ----------------------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# ----------------------------------------
# Data Cleaning
# ----------------------------------------

df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])

# Convert date column safely
df['date_added'] = pd.to_datetime(
    df['date_added'],
    format='mixed',
    errors='coerce'
)

# Create new columns
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# ----------------------------------------
# Basic Statistics
# ----------------------------------------

print("\nDataset Info:")
df.info()

print("\nStatistical Summary:")
print(df.describe(include='object'))

# ----------------------------------------
# Set Plot Style
# ----------------------------------------

sns.set_style("whitegrid")

# ========================================
# Chart 1: Movies vs TV Shows
# ========================================

plt.figure(figsize=(8, 5))

sns.countplot(
    x='type',
    data=df
)

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("1_movies_vs_tvshows.png")
plt.show()

# ========================================
# Chart 2: Top 10 Countries
# ========================================

country_df = df[df['country'] != 'Unknown']

top_countries = country_df['country'].value_counts().head(10)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=top_countries.values,
    y=top_countries.index
)

plt.title("Top 10 Content Producing Countries")
plt.xlabel("Number of Titles")
plt.ylabel("Country")

plt.tight_layout()
plt.savefig("2_top_countries.png")
plt.show()

# ========================================
# Chart 3: Ratings Distribution
# ========================================

valid_ratings = [
    'TV-MA', 'TV-14', 'TV-PG', 'R',
    'PG-13', 'TV-Y7', 'TV-Y',
    'PG', 'TV-G', 'NR',
    'G', 'TV-Y7-FV', 'NC-17', 'UR'
]

ratings_df = df[df['rating'].isin(valid_ratings)]

plt.figure(figsize=(10, 6))

sns.countplot(
    y='rating',
    data=ratings_df,
    order=ratings_df['rating'].value_counts().index
)

plt.title("Netflix Ratings Distribution")
plt.xlabel("Count")
plt.ylabel("Rating")

plt.tight_layout()
plt.savefig("3_ratings_distribution.png")
plt.show()

# ========================================
# Chart 4: Release Year Trend
# ========================================

release_year = (
    df['release_year']
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(12, 6))

plt.plot(
    release_year.index,
    release_year.values,
    marker='o'
)

plt.title("Netflix Content Release Trend")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.tight_layout()
plt.savefig("4_release_year_trend.png")
plt.show()

# ========================================
# Chart 5: Content Added Per Year
# ========================================

content_added = (
    df['year_added']
    .value_counts()
    .sort_index()
)

plt.figure(figsize=(12, 6))

plt.plot(
    content_added.index,
    content_added.values,
    marker='o'
)

plt.title("Content Added to Netflix Per Year")
plt.xlabel("Year Added")
plt.ylabel("Titles Added")

plt.tight_layout()
plt.savefig("5_content_added_per_year.png")
plt.show()

# ========================================
# Chart 6: Top 10 Directors
# ========================================

directors = (
    df[df['director'] != 'Unknown']['director']
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=directors.values,
    y=directors.index
)

plt.title("Top 10 Directors on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Director")

plt.tight_layout()
plt.savefig("6_top_directors.png")
plt.show()

# ========================================
# Chart 7: Correlation Heatmap
# ========================================

numeric_df = df[
    ['release_year', 'year_added', 'month_added']
]

plt.figure(figsize=(8, 5))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("7_correlation_heatmap.png")
plt.show()

# ========================================
# Key Insights
# ========================================

print("\n" + "=" * 60)
print("KEY INSIGHTS")
print("=" * 60)

print("""
1. Movies dominate Netflix content compared to TV Shows.

2. United States is the largest contributor of Netflix titles.

3. India is among the top content-producing countries.

4. TV-MA is the most common content rating.

5. Netflix experienced significant growth after 2015.

6. Content additions peaked around 2019–2020.

7. Netflix has rapidly expanded its global content library.

8. A small group of directors contribute multiple titles.
""")

print("\nEDA PROJECT COMPLETED SUCCESSFULLY")
