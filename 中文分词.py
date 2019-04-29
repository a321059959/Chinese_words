import time
max_len = 0
words = []
text = '我们是共产主义的接班人'
dic = ('我们', '是', '共产主义', '的', '接班', '人', '你', '我', '社会', '主义')

for key in dic:
    if max_len < len(key):
        max_len = len(key)
        
# print(max_len)
while len(text) > 0:
    word_len = max_len
    
    for i in range(0, max_len):
        word = text[0: word_len]
        print(word, '开始匹配...')
        time.sleep(1)
        if word not in dic:
            word_len -= 1
            word = None
        else:
            text = text[word_len:]
            print('%s\b匹配成功!' % word)
            words.append(word)
            print('正在添加到分词词组...')

            time.sleep(1)
            print('添加成功！')
            word = None
print('\n\n\n')
print('分词后的词组为：')
print(words)