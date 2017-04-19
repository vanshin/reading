# encoding=utf-8

import re
import random
from datetime import datetime

class ReadingProcess(object):

    def __init__(self, source_str):
        self.__source_str = source_str

        # 段落列表
        self.__parag_list = []

        # 用来存放段落，格式为：
        # {段落号: 段落句子列表, parag_number: 段落句子数量}
        self.__parag_dict = {}


        self.__sentence_list = []
        self.__sentence_dict = {}
        self.__process_str()


    def __process_str(self):

        # 得到段落
        self.__parag_list = re.split(r'\n|\r\n|\r', self.__source_str)
        self.__parags()


    def __parags(self):
        __parag_num = 1
        for parag in self.__parag_list:
            tmp_list = re.split(r'\.|\?', parag)
            self.__parag_dict[__parag_num] = tmp_list
            self.__parag_dict['parag_' + str(__parag_num)] = len(tmp_list)
            self.__parag_dict['count'] = __parag_num
            __parag_num += 1

    def __sentences(self):
        pass


    def parags(self):
        """ 返回包含句子的段落字典 """
        return self.__parag_dict

    def parag_count(self):
        """ 返回文章的段落数量 """
        return len(self.__parag_list)

def get_random():
    number = random.randint(000000, 999999)
    date = int(datetime.now().strftime('%M%S%f')) // 1000
    random_number = date + number
    return random_number


def main():
    a = Reading(r1)
    print a.parags()

if __name__ == '__main__':
    main()

# def process_word(sentence):
#     tmp = re.match(r'[a-zA-Z]*-?’?[a-zA-Z]+|,|:|\.|\d+|"', sentence)
#     print tmp
