from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

WORDCLOUD_PIC = 'wordcloud.png'
LOVE_IS_LOVE_PIC = 'love-is-love.png'
SENTIMENT_HISTOGRAM_PIC = 'sentiment-histogram.png'

## Creates wordcloud of messages
def create_wordcloud(messages):
    words = [word.lower() for msg in messages for word in str(msg).split()]
    wordcloud = WordCloud(collocations=False, height=1000, width=1000, colormap='pink').generate(' '.join(words))
    plt.imshow(wordcloud)
    plt.show()
    wordcloud.to_file(WORDCLOUD_PIC)


## Creates bar chart of love is love is love is love...
def love_is_love(messages):
    def get_count(phrase): # case-insensitive
        return len([msg for msg in messages if phrase in str(msg).lower()])

    a = get_count('love')
    b = get_count('love is love')
    c = get_count('love is love is love')
    d = get_count('love is love is love is love')
    e = get_count('love is love is love is love is love')
    f = get_count('love is love is love is love is love is love')
    g = get_count('love is love is love is love is love is love is love')
    h = get_count('love is love is love is love is love is love is love is love')
    i = get_count('love is love is love is love is love is love is love is love is love')
    j = get_count('love is love is love is love is love is love is love is love is love is love')
    k = get_count('love is love is love is love is love is love is love is love is love is love is love')

    labels = ['love', 'is love', 'is love', 'is love', 'is love', 'is love', 'is love', 'is love', 'is love', 'is love', 'is love']
    num_messages = [a, b, c, d, e, f, g, h, i, j, k]

    x = np.arange(len(labels))

    fig, ax = plt.subplots(figsize=(8, 5))
    rects = ax.bar(x, num_messages, 0.8) # 0.8 is the bar width

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Number of messages containing phrase')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    # Attach a text label above each bar in rects, displaying its height
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords='offset points',
                    ha='center', va='bottom')

    fig.tight_layout()
    plt.savefig(LOVE_IS_LOVE_PIC)


## Creates a histogram and gives the statistics for a sentiment analysis of messages
def analyse_sentiments(messages):
    analyser = SentimentIntensityAnalyzer()
    sentiments = [{ 'message': msg, 'score': analyser.polarity_scores(msg)['compound']} for msg in messages]
    sentiments = sorted(sentiments, key=lambda msg: msg['score'])

    df = pd.DataFrame(sentiments)
    hist = df.hist(grid=False, bins=20)
    for ax in hist.flatten():
        ax.set_title(None)
        ax.set_ylabel('Number of messages')
        ax.set_xlabel('Sentiment score')

    plt.savefig(SENTIMENT_HISTOGRAM_PIC)

    mean = df['score'].mean()
    std = df['score'].std()
    print('Mean: %.3f' % mean)               # 0.658
    print('Standard Deviation: %.3f' % std)  # 0.335

    bads     = [sentiment for sentiment in sentiments if sentiment['score'] < -0.5]
    neutrals = [sentiment for sentiment in sentiments if sentiment['score'] == 0]
    goods    = [sentiment for sentiment in sentiments if sentiment['score'] > 0.5]
    bad_sample = random.sample(bads, k=5)
    neutral_sample = random.sample(neutrals, k=5)
    good_sample = random.sample(goods, k=5)
    for sample in [bad_sample, neutral_sample, good_sample]:
        for sentiment in sample:
            print('%.3f:\t%s' % (sentiment['score'], sentiment['message']))

    # Mean: 0.658
    # Standard Deviation: 0.335
    # -0.566:	I can't believe thousand years of evolution and human species still couldn't get love right!
    # -0.557:	there will come a time where we won’t have to be shamed
    # -0.539:	Yishunites will climb over the wall to fight homophobia!!!
    # -0.674:	Shout-out to every single person I've come out to so far, for never giving me a bad coming out experience ever
    # -0.670:	May all hatred harboring, narrow-minded bigots be gone!
    # 0.000:	Hello
    # 0.000:	SHOUTOUT FROM HOUGANG!!!!! ❤️❤️❤️❤️
    # 0.000:	someday we'll find our pot of gold at the rainbow's end
    # 0.000:	We stand with the LGBTQ community!
    # 0.000:	#loveislove
    # 0.856:	Freedom to love
    # 0.972:	We will get there ❤️🧡💛💚💙💜
    # 0.599:	We all deserve to be loved for who we are
    # 0.918:	we are all here to support you!!! love is love
    # 0.791:	Hoping that eventually, my wife and I will have the freedom to own a home in Singapore together as equal partners under the law.

if __name__ == '__main__':
    df = pd.read_csv('data.csv')
    messages = [str(msg) for msg in df['message']]

    # create_wordcloud(messages)
    # love_is_love(messages)
    # analyse_sentiments(messages)
