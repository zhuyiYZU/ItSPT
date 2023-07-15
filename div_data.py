# 划分数据集newsgroups6（100train，100val）
read_path = 'newsgroups6_test0.csv'
m = 0
n = 0

with open(read_path, 'r', encoding='utf-8') as f:
    for ii, text in enumerate(f):
        text = text.split(',')
        label = text[0]
        if label == '"1"':
            m += 1
        else:
            n += 1
print(m, n)
k = 0
j = m
for i in range(1, 11):
    save_path = "newsgroups6_train" + str(i) + ".csv"
    f_w = open(save_path, 'w', encoding='utf-8')
    print('----------')
    with open(read_path, 'r', encoding='utf-8') as f:
        for ii, text in enumerate(f):
            text = text.split(',')
            label = text[0]
            text = ' '.join(text[1:]).replace('\n', '')
            if k+100 <= m:
                if k <= ii < k+100:    #train1
                    f_w.write(label + ',' + text + '\n')
            elif m-k < 100:
                if k <= ii < m or 0 <= ii < 100-m+k:
                    f_w.write(label + ',' + text + '\n')

            if j+100 <= m+n:
                if j <= ii < j+100:   #train1
                    f_w.write(label + ',' + text + '\n')
            elif m+n-j < 100:
                if j <= ii < m+n or m <= ii < j + 100 - n:
                    f_w.write(label + ',' + text + '\n')
    if k+100 <= m:
        print("train{}:{}-{}".format(i, k, k + 100))
    elif m - k < 100:
        print("train{}:{}-{},{}-{}".format(i, k, m, 0, 100-m+k))

    if j + 100 <= m + n:
        print("train{}:{}-{}".format(i, j, j + 100))
    elif m + n - j < 100:
        print("train{}:{}-{},{}-{}".format(i, j, m + n, m, j + 100 - n))

    k += 100
    if k > m:
        k = k-m
    j += 100
    if j > m+n:
        j = j-n

# 1003 1036
# ----------
# train1:0-100
# train1:1003-1103
# ----------
# train2:100-200
# train2:1103-1203
# ----------
# train3:200-300
# train3:1203-1303
# ----------
# train4:300-400
# train4:1303-1403
# ----------
# train5:400-500
# train5:1403-1503
# ----------
# train6:500-600
# train6:1503-1603
# ----------
# train7:600-700
# train7:1603-1703
# ----------
# train8:700-800
# train8:1703-1803
# ----------
# train9:800-900
# train9:1803-1903
# ----------
# train10:900-1000
# train10:1903-2003




