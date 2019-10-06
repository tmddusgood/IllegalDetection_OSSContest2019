import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import pickle
import os

class model_application:
    def __init__(self,newData):
        self.dataform = '.\\Dataset\\dataset_form.csv'
        self.dataset = '.\\Dataset\\prototype_final_shuffle_dataset(50000)_real.csv'
        self.newdata =newData
        self.model_tokenizer = 'tokenizer.word_index_original_new_100000'
        self.model_nlp = '.\\Model\\illegal_nlp_model_new_100000.h5'
        self.model_tokenizer_path = '.\\Model\\' + self.model_tokenizer
        self.max_num_words = 100000
        self.max_len = 2720 # 한 본문 당 길이는 2720으로 맞춘다(padding 할 때 쓴다).
        self.tokenizer = Tokenizer(num_words=self.max_num_words)  # 객체를 먼저 만들고

    def split(self,_input_X_data):
        tmp = []
        for _test_list in _input_X_data[:]:
            _test_list = _test_list.split()
            tmp.append(_test_list)
        return tmp


    # 각각의 본문이 리스트 형태로 바뀌어있고, 검사 후 none_exist에는 존재하지 않는 단어만 들어간다.
    def none_inspection(self,_tmp_X_data, _tokenizer):
        tmp2 = []
        for list in _tmp_X_data:
            tmp = []
            for item in list:
                try:
                    _tokenizer.word_index[item]
                    # 새로 넣은 본문의 단어들이 내가 가진 인덱스에 있는지 확인
                except:
                    tmp.append(item)
            tmp2.append(tmp)
        return tmp2


    def delete_none(self,_tmp_X_data, _none_exist):
        count = 0
        tmp = []
        for list in _tmp_X_data[:]:
            for item in _none_exist[count][:]:
                list.remove(item)
            list = " ".join(list)
            tmp.append(list)
            count = count + 1
        return tmp

    def read_data(self, form):
        if form == 'csv':
            _data = pd.read_csv(self.newdata, encoding='utf-8')
            _data = _data.astype(str)
            return _data
        elif form == 'url':
            _data = pd.read_csv(self.dataform, encoding='utf-8')
            _data = _data.astype(str)
            return _data

    def check_tokenizer(self):
        if not os.path.isfile(self.model_tokenizer_path):
            print(self.model_tokenizer + " DOESN'T exist")
            data = pd.read_csv(self.dataset, encoding='utf-8')
            data = data.astype(str)
            X_data = data['body']
            # y_data = data['classification']

            print(data.isnull().values.any())
            print(data.info)
            self.tokenizer.fit_on_texts(X_data)  # X의 각 행에 토큰화를 수행
            with open(self.model_tokenizer, 'wb') as f:
                print('SAVING TOKENIZER')
                pickle.dump(self.tokenizer, f)
            return self.tokenizer
        else:
            print(self.model_tokenizer + ' EXISTS')
            with open(self.model_tokenizer_path, 'rb') as f:
                print('LOADING TOKENIZER')
                _tokenizer = pickle.load(f)
            return _tokenizer

    def data_processing(self,_data, _tokenizer):
        input_X_data = _data['body']
        converted_input_X_data = input_X_data
        tmp_X_data = self.split(converted_input_X_data)
        none_exist = self.none_inspection(tmp_X_data, _tokenizer)
        tmp_X_data = self.delete_none(tmp_X_data, none_exist)
        for i in range(0, len(input_X_data)):
            input_X_data[i] = tmp_X_data[i]
        sequences = _tokenizer.texts_to_sequences(input_X_data)
        sequences_X_data = sequences
        _final_X_data = pad_sequences(sequences_X_data, maxlen=self.max_len)
        return _final_X_data


    def load_prediction(self, _final_X_data):
        _percentage = []
        model = load_model(self.model_nlp)
        _predictions = model.predict_classes(_final_X_data, verbose=2)
        _probability = model.predict_proba(_final_X_data, verbose=2)
        for number in _probability:
            _percentage.append(float(number) * 100)

        return _predictions, _percentage


if __name__ == '__main__':
    model = model_application()
    tokenizer = model.check_tokenizer()
    data = model.read_data('csv')
    final_X_data = model.data_processing(data, tokenizer)

    predictions, percentage = model.load_prediction(final_X_data)

    for i in range(0,len(predictions)):
        print(predictions[i], percentage[i])