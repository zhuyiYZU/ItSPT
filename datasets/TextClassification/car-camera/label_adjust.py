read_path1 = 'car_train.csv'
read_path2 = 'camera_test.csv'

f_1 = open("adjust_train.csv", 'w', encoding='utf-8')
with open(read_path1, 'r', encoding='utf-8') as t:
    for ii, text in enumerate(t):
        text = text.split(',')
        label = text[0]
        text = ' '.join(text[1:])
        if label == '"0"':
            f_1.write(label + ',' + text)

f_1 = open("adjust_train.csv", 'a', encoding='utf-8')
with open(read_path1, 'r', encoding='utf-8') as t:
    for ii, text in enumerate(t):
        text = text.split(',')
        label = text[0]
        text = ' '.join(text[1:])
        if label == '"1"':
            f_1.write(label + ',' + text)

f_2 = open("adjust_test.csv", 'w', encoding='utf-8')
with open(read_path2, 'r', encoding='utf-8') as t:
    for ii, text in enumerate(t):
        text = text.split(',')
        label = text[0]
        text = ' '.join(text[1:])
        if label == '"0"':
            f_2.write(label + ',' + text)

f_2 = open("adjust_test.csv", 'a', encoding='utf-8')
with open(read_path2, 'r', encoding='utf-8') as t:
    for ii, text in enumerate(t):
        text = text.split(',')
        label = text[0]
        text = ' '.join(text[1:])
        if label == '"1"':
            f_2.write(label + ',' + text)
