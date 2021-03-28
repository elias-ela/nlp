import sys

if __name__ == '__main__':
    for filename in sys.argv[1:]:
        with open(filename, 'r', encoding='utf-8') as reader:
            file_reader = reader.read()

        print(f'\n{"Stat Information":*^50}\n')
        print(f'File name: {filename:>39}')
        print(f'Number of Sentence: {len(file_reader.splitlines()):=30,d}')
        print(f'Number of Tokens: {len(file_reader.split()):=32,d}')
        print(f'Number of unique words: {len(set(file_reader.split())):=26,d}')
        print(f'{"":*^50}')
