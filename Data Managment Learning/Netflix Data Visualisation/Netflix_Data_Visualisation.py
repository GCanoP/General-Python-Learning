"""
=======================================================================================================
NETFLIX DATA VISUALISATION
author : Gerardo Cano Perea.
date : March 05, 2021.
=======================================================================================================
"""
# Relevant Packages.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# ==================================== Importing Dataset ==============================================
df = pd.read_csv('netflix_titles.csv')

# ==================================== Missing Data. ==================================================
# Graphic and Analytic NaN values.
print(df.isna().sum())
sns.heatmap(df.isna(), cmap = 'cividis')

# Drop director and cast columns cause too many nan values.
df.drop(['director', 'cast'], axis = 1, inplace = True)

# In case of country / rating columns, we can replace nan values for a default value.
df['country'].replace(np.nan, 'United States', inplace = True)
df['rating'].replace(np.nan, 'TV-MA', inplace = True)

# We have released year, thus date_added is not needed for the analysis.
df.drop(['date_added'], axis = 1, inplace = True)

# Value Counts for Variables.
df['rating'].value_counts()
df['listed_in'].value_counts()

# Check data without missing values.
df.isna().sum()

# ============================= Data Visualisation ====================================================
# Looking the Number of Movies and TV shows.
ax = sns.countplot(x = 'type', data = df)
ax.set_title('Movies / TV Series')
ax.set_ylabel('Counter')
ax.set_xlabel('Type')

# Looking the Number of Rating Media.
ax = sns.countplot(x = 'rating', data = df)
ax.set_title('Rating Media')
ax.set_ylabel('Counter')
ax.set_xlabel('Rating Types')

# Number of Media Released per Year.
ax = sns.countplot(x = 'release_year', data = df)
ax.set_title('Media Released per Year')
ax.set_ylabel('Counter')
ax.set_xlabel('Years')

# Counting Movies and Series Classified per Rating.
ax = sns.countplot(x = 'rating', data = df, hue = 'type')
ax.set_title('Movies / TV Series per Rating')
ax.set_ylabel('Counter')
ax.set_xlabel('Rating Classification')

# Distribution of Top 10 Media.
import plotly.express as px
top_rated = df[0:10]
fig = px.sunburst(top_rated, path = ['country'])
fig.show()

# Plotting the WordCloud.
from wordcloud import WordCloud
plt.subplots(figsize = (25, 15))
wordcloud = WordCloud(background_color = 'Black',
                      width = 1920, height = 1080,).generate(''.join(df.title))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()




