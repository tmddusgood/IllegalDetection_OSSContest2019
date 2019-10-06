import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from tqdm import tqdm
import itertools
from konlpy.tag import Kkma
import re

class input_preprocessing:
    def __init__(self):
        self.textfile = 'url_text.txt'
        self.kkma = Kkma()

    def get_text(self):
        # 복사 붙여넣기로 넣을 수 없어서 텍스트파일에 넣고 가져옴
        # 나중에는 그냥 string 받아서 시작하면 된다.

        with open('.\\Dataset\\' + self.textfile, 'rb') as f:
            tmp = f.read().decode('utf-8')
        return tmp

    def extractkor(self, _s):
        try:
            hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
            result = hangul.sub('', _s)
            # print(result)
            result2 = result.split(' ')
            result2 = [item for item in result2 if item != ' ']
            result2 = [item for item in result2 if item != ""''""]
            return result2
        except Exception as error:
            # print("error!",error)
            return 1

    def splitkor_kornouns(self, _list):
        _temp_korbag = []
        try:
            # for item in tqdm(_list, ascii= True, desc='명사 추출'):
            for item in _list:
                tempstr = str(item)
                tplist = self.kkma.nouns(tempstr)
                # print(tplist)
                _temp_korbag.append(tplist)
        except Exception as error:
            print("for문 에러", error)
        _temp_korbag = list(itertools.chain(*_temp_korbag))
        return _temp_korbag

    def length_join(self, _bodytext):
        junk = []
        for word in _bodytext:
            if len(word) < 2:
                junk.append(word)
        for word2 in junk:
            try:
                _bodytext.remove(word2)
            except:
                pass
        _bodytext = [" ".join(_bodytext)]
        return _bodytext

#
# if __name__ == '__main__':
#     pre_input = input_preprocessing()
#
#     html_text = pre_input.get_text()
#     kor_bag = pre_input.extractkor(str(html_text))
#     split_kor = pre_input.splitkor_kornouns(kor_bag)
#     joined_kor = pre_input.length_join(split_kor)
#     print(joined_kor)
