from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')
messages = df['message'].tolist()
words = [word.lower() for message in messages for word in str(message).split()]
wordcloud = WordCloud(collocations=False, height=1000, width=1000, colormap='pink').generate(' '.join(words))
plt.imshow(wordcloud)
plt.show()
wordcloud.to_file('wordcloud.png')
