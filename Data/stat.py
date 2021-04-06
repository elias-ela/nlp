import sys
import numpy as np
from itertools import chain
from matplotlib import pyplot as plt


def read_data(loc_):
    data = list()
    with open(loc_, encoding='utf-8') as fp:
        for line in fp:
            text = line.strip()
            data.append(text)
    return data


if __name__ == '__main__':
    for filename in sys.argv[1:]:
        train_text = read_data(filename)
        data_len = list(map(lambda x: len(x.split()), train_text))

        print(f'\n{"Stat Information":*^50}\n')
        print(f'File name: {filename:>39}')
        print(f'Total Number of Sentence: {len(train_text):=24,d}')
        print(f'Total Number of Tokens: {np.sum(data_len):=26,d}')
        print(f'Total Number of unique words: {len(set(chain(train_text))):=20,d}')
        print(f'Median words: {np.median(data_len):=36,.2f}')
        print(f'Mean words: {np.mean(data_len):=38,.2f}')
        print(f'Max words: {np.max(data_len):=39,d}')
        print(f'Min words: {np.min(data_len):=39,d}')
        print(f'Std words: {np.std(data_len):=39,.2f}')

        plt.plot(data_len)
        plt.show()
