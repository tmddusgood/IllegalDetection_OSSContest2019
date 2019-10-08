# Illegal Sports Gambling Filtering by Keras NLP + InceptionV3 Classification

텍스트처리를 피하기 위해서 이미지에 글을 쓰는 도박 사텍스트를 인식 및 추출 후 다른 텍스트와 함께 자연어처리를 수행합니다.

Input URL 혹은 Input CSV 목록에 대해서 높은 정확도의 Prediction 결과를 줄 수 있습니다.

# 처리과정

![file123](https://user-images.githubusercontent.com/39071543/66269559-b6b2a980-e884-11e9-8038-1bf792acb6ca.PNG)  

- 이미지 처리  

1. url의  페이지를 OpenCV를 사용하여 텍스트 주위의 영역을  박스로 표시합니다  
2. 박스 내의 이미지를 텍스트와 텍스트가 아닌 것으로 분류합니다.  
3. 텍스트를 머신러닝을 이용하여 글자를 인식합니다.  
4. 추출된 텍스트를 일반 텍스트와 취합합니다.  

- 텍스트 처리  

1. 일반 텍스트와 이미지로부터 추출된 텍스트로부터 한글만 추출합니다.  
2. 추출된 한글로부터 명사만 추출합니다.  
3. 2글자 이하의 단어는 제외합니다.  
4. 추출된 단어들을 인덱싱합니다.  
5. 단어들을 분석 모델에 입력하여 불법 사이트인지의 여부를 판정한 뒤, 결과를 출력합니다.

# 개발 환경 및 설치 방법

## Tessract 5.0-alpha  

[Tesseract 5.0-alpha](https://github.com/UB-Mannheim/tesseract/wiki)- 사용자의 운영체제 버전   

- 설치 파일 경로는  C:\Program Files (x86)\Tesseract-OCR   또는 C:\Program Files\Tesseract-OCR  (코드에는 예외처리 O)
- Path 설정  
- TESSDATA_PREFIX 설정

# 모듈 설치  

## Tensorflow, Opencv, Keras

- gpu는 사용할 경우에만 설치
- 다른 모듈의 경우 Requirements.txt 참조

```
pip install tensorflow==1.12  
pip install tensorflow-gpu==1.12  
pip install opencv-contrib-python
pip install keras==2.3.0
pip install keras-gpu==2.3.0
pip install pytesseract
pip install h5py
```

## Konlpy  

- Java 1.7+ 설치
- JAVA_HOME 설정 (환경 변수)
- JPype1 (>=0.5.7)을 다운로드 후 설치 (아래 링크에서 버전 별 선택)
- Window에서는 Mecab() 지원 X
- 참고: https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype

```
pip install -upgrade pip
EX) pip install JPype1-0.5.7-cp[your_version]-none-win_amd64.whl
pip install konlpy
```

# Run

- 새로운 데이터를 .csv 형태로 입력받아서 분류

```
default: \Dataset 폴더의 pure_new_dataset.csv 을 input으로 분류 결과를 results.csv로 제시
python main.py

your data: 새로운 input 데이터셋의 분류 결과를 return 해줍니다.
python main.py --csv_path=[your new dataset]
```

- .csv should be following (example: \Dataset\dataset_form.csv)

| Classification           | Body         |
| ------------------------ | ------------ |
| (Random Number Except 0) | (Bodytext_1) |
| (Random Number Except 0) | (Bodytext_2) |

# Details  

- 일반 신문 기사 : 스포츠 기사 : 불법 도박사이트 본문 = 7: 2: 1 / 총 45000개로 학습 (Train:Test - 8:2 Split)
- InceptionV3 Model 을 사용하여 비텍스트와 텍스트 구분
- Keras와 K-Fold 교차검증법을 사용한 자연어처리
- 방송통신심의위원회 기준에 의거한 불법 도박 사이트 본문과 사진 이용
- Ver 1. Testset Acuuracy: 42.9% (310000개 인덱싱)
- Ver 2. Testset Accuracy: 89.9% (30000개 인덱싱)
- Ver 3. Testset Accuracy: 97.9% (100000개 인덱싱)
