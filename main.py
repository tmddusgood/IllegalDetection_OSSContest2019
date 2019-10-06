from Preprocessing.input_preprocessing_text import *
from Model.model_application import *
from ImageClassification import ocr_prediction
import argparse


def main(csvPath):
     pre_input = input_preprocessing()
     html_text = pre_input.get_text()
     # html_text = string
     kor_bag = pre_input.extractkor(str(html_text))
     split_kor = pre_input.splitkor_kornouns(kor_bag)
     joined_kor = pre_input.length_join(split_kor)
     print(joined_kor)

     model = model_application(csvPath)
     tokenizer = model.check_tokenizer()
     data = model.read_data('url')
     data['body'][0] = " ".join(joined_kor)
     print(data)

     final_X_data = model.data_processing(data, tokenizer)
     predictions, percentage = model.load_prediction(final_X_data)

     for i in range(0, len(predictions)):
          print(predictions[i], percentage[i])

     result = {'classification': predictions, 'probability': percentage}
     df = pd.DataFrame(data)

     writer = pd.ExcelWriter('result.xlsx', engine='xlsxwriter')
     df.to_excel(writer, sheet_name='Sheet1')
     writer.close()

if __name__=="__main__":
     parser = argparse.ArgumentParser()
     parser.add_argument(
          '--csv_path',
          type=str,
          default='.\\Dataset\\pure_new_dataset.csv',
          help='Path to load csv'
     )
     args = parser.parse_args()
     csv_path=args.csv_path
     main(csv_path)