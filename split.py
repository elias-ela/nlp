def file_to_array(file_path):
    with open(file_path, 'r') as reader:
        return reader.readlines()


def array_to_file(array_object, filename):
    with open(filename, 'w') as writer:
        writer.writelines(array_object)


def split(first_file, second_file):
    from sklearn.model_selection import train_test_split
    first_train, first_test, second_train, second_test = train_test_split(
        file_to_array(first_file), file_to_array(second_file))
    return [[first_train, first_test], [second_train, second_test]]


if __name__ == '__main__':
    import sys
    first_file, second_file = sys.argv[1], sys.argv[2]
    value = split(first_file, second_file)
    array_to_file(value[0][0], f'{first_file.split(".")[0]}-train.txt')
    array_to_file(value[0][1], f'{first_file.split(".")[0]}-test.txt')
    array_to_file(value[1][0], f'{second_file.split(".")[0]}-train.txt')
    array_to_file(value[1][1], f'{second_file.split(".")[0]}-test.txt')
