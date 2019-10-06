from Preprocessing.input_preprocessing_text import *
from Model.model_application import *
from ImageClassification import ocr_prediction
import cv2
pre_input = input_preprocessing()
html_text = pre_input.get_text()
# html_text = string
kor_bag = pre_input.extractkor(str(html_text))
split_kor = pre_input.splitkor_kornouns(kor_bag)
# image join needed

result=ocr_prediction.start("./ImageClassification/test.jpg")
# replace the path with variables

img_kor_bag = pre_input.extractkor(str(result))
img_split_kor = pre_input.splitkor_kornouns(img_kor_bag)
combine_img_text = split_kor + img_split_kor
joined_kor = pre_input.length_join(combine_img_text)
print(joined_kor)

model = model_application()
tokenizer = model.check_tokenizer()
data = model.read_data('url')
data['body'][0] = " ".join(joined_kor)
print(data)

final_X_data = model.data_processing(data, tokenizer)
predictions, percentage = model.load_prediction(final_X_data)

for i in range(0, len(predictions)):
     print(predictions[i], percentage[i])
