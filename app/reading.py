# encoding=utf-8

import random
import re
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
        self.__parag_list = re.split(r'\n\n|\r\n|\r|\n', self.__source_str)
        self.__parags()


    def __parags(self):
        __parag_num = 1
        for parag in self.__parag_list:
            tmp_list = re.findall(r'[a-zA-Z0-9\-\,\s\\\"]+\.', parag)
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
    r1 = '"To paraphrase 18th-century statesman Edmund Burke, \u201call that is needed for the triumph of a misguided cause is that good people do nothing.\u201d One such cause now seeks to end biomedical research because of the theory that animals have rights ruling out their use in research. Scientists need to respond forcefully to animal rights advocates, whose arguments are confusing the public and thereby threatening advances in health knowledge and care. Leaders of the animal rights movement target biomedical research because it depends on public funding, and few people understand the process of health care research. Hearing allegations of cruelty to animals in research settings, many are perplexed that anyone would deliberately harm an animal.\n\n\u3000\u3000For example, a grandmotherly woman staffing an animal rights booth at a recent street fair was distributing a brochure that encouraged readers not to use anything that comes from or is tested in animals\u2014no meat, no fur, no medicines. Asked if she opposed immunizations, she wanted to know if vaccines come from animal research. When assured that they do, she replied, \u201cThen I would have to say yes.\u201d Asked what will happen when epidemics return, she said, \u201cDon\u2019t worry, scientists will find some way of using computers.\u201d Such well-meaning people just don\u2019t understand.", '
    a = ReadingProcess(r1)
    print a.parags()

if __name__ == '__main__':
    main()

# def process_word(sentence):
#     tmp = re.match(r'[a-zA-Z]*-?’?[a-zA-Z]+|,|:|\.|\d+|"', sentence)
#     print tmp
