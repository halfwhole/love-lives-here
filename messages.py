from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

WORDCLOUD_PIC = 'wordcloud.png'
LOVE_IS_LOVE_PIC = 'love-is-love.png'

def create_wordcloud(messages):
    words = [word.lower() for msg in messages for word in str(msg).split()]
    wordcloud = WordCloud(collocations=False, height=1000, width=1000, colormap='pink').generate(' '.join(words))
    plt.imshow(wordcloud)
    plt.show()
    wordcloud.to_file(WORDCLOUD_PIC)

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

    test = [msg for msg in messages if 'love is love is love is love is love is love' in str(msg).lower()]
    print(test)

    labels = ['love', 'is love', 'is love', 'is love', 'is love', 'is love', 'is love', 'is love', 'is love', 'is love', 'is love']
    num_messages = [a, b, c, d, e, f, g, h, i, j, k]

    x = np.arange(len(labels))
    width = 0.8  # the width of the bars

    fig, ax = plt.subplots(figsize=(8, 5))
    rects = ax.bar(x, num_messages, width)

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


if __name__ == '__main__':
    df = pd.read_csv('data.csv')
    messages = [str(msg) for msg in df['message']]
    # create_wordcloud(messages)
    love_is_love(messages)
