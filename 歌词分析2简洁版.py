# -*- coding:utf-8 -*-
import os
import json
import jieba.analyse
from PIL import Image, ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def read_content(content_path):
    content = ''
    for f in os.listdir(content_path):
        file_fullpath = os.path.join(content_path, f)
        if os.path.isfile(file_fullpath):
            print('loading {}'.format(file_fullpath))
            content += open(file_fullpath, 'r').read()
            content += '\n'
    print('done loading')
    return content
content = read_content('E:\\Song\\lyrics\\yuanyajie')
result = jieba.analyse.textrank(content, topK=1000, withWeight=True)
keywords = dict()
for i in result:
    keywords[i[0]] = i[1]
dcp = json.dumps(keywords)
wangyang = dcp.decode("unicode-escape")
print (wangyang)

image = Image.open('E:\\Song\\image\\yuanyawei.jpg') #tony_src.png
graph = np.array(image)

wc = WordCloud(font_path='C:/Windows/Fonts/STXINGKA.TTF',
    background_color='white', max_words=1000, mask=graph)
wc.generate_from_frequencies(keywords)
image_color = ImageColorGenerator(graph)

plt.imshow(wc)
plt.imshow(wc.recolor(color_func=image_color))
plt.axis("off")
plt.show()