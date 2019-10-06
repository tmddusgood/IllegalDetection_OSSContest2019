# Illegal Sports Gambling Filtering by Keras NLP + InceptionV3 Classification
Open Source Software Contest 2019
텍스트처리를 피하기 위해서 이미지에 글을 쓰는 도박 사이트에 대한 단속을 목적으로 합니다.

![image](https://user-images.githubusercontent.com/39071543/66269437-4d7e6680-e883-11e9-9051-820ac8556e4c.png)
텍스트를 인식 및 추출 후 다른 텍스트와 함께 자연어처리를 수행합니다.  

# 처리과정
  
![file123](https://user-images.githubusercontent.com/39071543/66269559-b6b2a980-e884-11e9-8038-1bf792acb6ca.PNG)  

* 이미지 처리  
1. url의  페이지를 OpenCV를 사용하여 텍스트 주위의 영역을  박스로 표시합니다  
2. 박스 내의 이미지를 텍스트와 텍스트가 아닌 것으로 분류합니다.  
3. 텍스트를 머신러닝을 이용하여 글자를 인식합니다.  
4. 추출된 텍스트를 일반 텍스트와 취합합니다.  

* 텍스트 처리  
1. 일반 텍스트와 이미지로부터 추출된 텍스트로부터 한글만 추출합니다.  
2. 추출된 한글로부터 명사만 추출합니다.  
3. 2글자 이하의 단어는 제외합니다.  
4. 추출된 단어들을 인덱싱합니다.  
5. 단어들을 분석 모델에 입력하여 불법 사이트인지의 여부를 판정한 뒤, 결과를 출력합니다.

# 개발 환경 및 설치 방법

## Tessract 5.0-alpha  
[Tesseract 5.0-alpha](https://github.com/UB-Mannheim/tesseract/wiki)- 사용자의 운영체제 버전   
* 설치 파일 경로는  C:\Program Files (x86)\Tesseract-OCR   또는 C:\Program Files\Tesseract-OCR  
* Path 설정  
![tesseract2](https://user-images.githubusercontent.com/39071632/66267865-9e855f00-e871-11e9-8de0-13722809c1eb.JPG){: width="40%" height="40%"}
![tesseract3](https://user-images.githubusercontent.com/39071632/66267866-a04f2280-e871-11e9-837d-cc8f5774d4bc.JPG){: width="40%" height="40%"}
* TESSDATA_PREFIX 설정
![tesseract4](https://user-images.githubusercontent.com/39071632/66267892-df7d7380-e871-11e9-8ee7-2f8b6af20331.JPG){: width="40%" height="40%"} 

# 모듈 설치  
## Tensorflow, Opencv, Keras
* gpu는 사용할 경우에만 설치
* 다른 모듈의 경우 Requirements.txt 참조
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
* Java 1.7+ 설치
* JAVA_HOME 설정 (환경 변수)
* JPype1 (>=0.5.7)을 다운로드 후 설치 (아래 링크에서 버전 별 선택)
* Window에서는 Mecab() 지원 X
```
https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype
pip install -upgrade pip
EX) pip install JPype1-0.5.7-cp[your_version]-none-win_amd64.whl
pip install konlpy
```
