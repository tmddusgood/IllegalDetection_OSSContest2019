# 불법 도박 사이트 분류 - 일리아이즈  
Open Source Software Contest 2019
텍스트처리를 피하기 위해서 이미지에 글을 쓰는 도박 사이트에 대한 단속 목적 

<center><img src="https://user-images.githubusercontent.com/28249894/66255556-d46a0b00-e7bf-11e9-8797-4e8398a15438.jpg" width="300" height="300"></center>

텍스트를 인식 및 추출 후 다른 텍스트와 함께 자연어처리를 수행합니다.

# 처리과정
일리아이즈 소프트웨어의 전체적인 처리순서는 <그림2>와 같이 진행됩니다.    
![도표1](https://user-images.githubusercontent.com/44759382/66236568-c9ff3100-e72d-11e9-8e2c-be17e95ae27e.png)   
 <그림2>   
End user로부터 url 페이지를 입력받은 뒤, 해당 url 의 페이지로부터 텍스트와 이미지를 추출합니다.  
텍스트 처리  
1. 일반 텍스트와 이미지로부터 추출된 텍스트로부터 한글만 추출합니다.  
2. 추출된 한글로부터 명사만 추출합니다.  
3. 2글자 이하의 단어는 제외합니다.  
4. 추출된 단어들을 인덱싱합니다.  
5. 단어들을 분석 모델에 입력하여 불법 사이트인지의 여부를 판정한 뒤, 결과를 출력합니다.
  
이미지 처리  
 1. url의  페이지를 OpenCV를 사용하여 텍스트 주위의 영역을  박스로 표시합니다  
2. 박스 내의 이미지를 텍스트와 텍스트가 아닌 것으로 분류합니다.  
3. 텍스트를 머신러닝을 이용하여 글자를 인식합니다.  
4. 추출된 텍스트를 일반 텍스트와 취합합니다.   
  
![2222](https://user-images.githubusercontent.com/28249894/66268599-f627c880-e879-11e9-8981-bdf1ae359eff.jpg)   
<그림3>  
<그림3>에는 일리아이즈의 텍스트/이미지 분석 모델의 발전과정이 나타나 있습니다.  
초기 분석에는 naive bayesian을 이용하여 텍스트를 분류하였고, 이후 정확도를 높이려는 과정에서 텍스트 분석에 머신러닝을 이용, 이미지 인식에 OCR을 이용하는 방식에서 머신러닝을 추가적으로 적용하였습니다.

# 개발 환경 및 설치 방법

## 아나콘다
[Anaconda](https://www.anaconda.com/distribution/#download-section)- 파이썬 3.x 버전
  
## Tessract 5.0-alpha  
[Tesseract 5.0-alpha](https://github.com/UB-Mannheim/tesseract/wiki)- 사용자의 운영체제 버전   

* 설치 파일 경로는  C:\Program Files (x86)\Tesseract-OCR   또는 C:\Program Files\Tesseract-OCR  
* 설치 후 아래와 같이 환경변수 탭 클릭  

![tesseract1](https://user-images.githubusercontent.com/39071632/66267863-9b8a6e80-e871-11e9-9ac2-cc9224976936.JPG)


* Path 설정  
![tesseract2](https://user-images.githubusercontent.com/39071632/66267865-9e855f00-e871-11e9-8de0-13722809c1eb.JPG)

![tesseract3](https://user-images.githubusercontent.com/39071632/66267866-a04f2280-e871-11e9-837d-cc8f5774d4bc.JPG)

* TESSDATA_PREFIX 설정

![tesseract4](https://user-images.githubusercontent.com/39071632/66267892-df7d7380-e871-11e9-8ee7-2f8b6af20331.JPG)  

## pip 업그레이드, 가상환경 생성 후 활성화 

Anaconda prompt 에서 수행 
```
pip install --upgrade pip
conda create --name [가상환경명] python=[파이썬 3.x버전]
activate [가상환경명]
```
# 모듈 설치  
## Tensorflow, Opencv, Keras, Tqdm, 

* gpu는 사용할 경우에만 설치
```
pip install tensorflow==1.12  
pip install tensorflow-gpu==1.12  
pip install opencv-contrib-python
pip install keras==2.3.0
pip install keras-gpu==2.3.0
pip install tqdm
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

 
## 향후 계획1  
그림4는 OpenCV를 이용하여 Image text를 boxing하는 과정을 보여줍니다.
![KakaoTalk_20191005_161440639](https://user-images.githubusercontent.com/28249894/66251727-3c9ff900-e78e-11e9-95d8-83c6ee343b22.jpg)  
<그림 4>   
이미지에서 텍스트를 무리없이 가져올 수 있는데 이는 배경 이미지에 따라 영향을 많이 받습니다. 그에대한 방안으로 이미지를 팽창시켜서 글자가 있는 영역으로 추정되는 곳을 텍스트 박스 영역으로 추정하여 박스 작업을 합니다. 이를 deiltion이라 합니다. 이는 뒤의 배경이 단순하고 복잡하지 않는 이미지의 텍스트에만 많은 효과를 발휘합니다. 하지만 뒷 배경이 복잡한 이미지는 다음과 같은 문제를 발생시킵니다.  
![KakaoTalk_20191005_161848846](https://user-images.githubusercontent.com/28249894/66251728-3e69bc80-e78e-11e9-993d-17aa9283e454.jpg)   
<그림 5>  
그림5는 deiltion의 수치를 높게 하여 이미지 텍스트에 boxing 작업을 한 결과입니다. 그림에서 볼 수 있듯이 이미지 팽창으로 인하여 boxing이 텍스트와는 별개로 크게 잡히는 현상을 볼 수 있습니다.    
![KakaoTalk_20191005_162143535](https://user-images.githubusercontent.com/28249894/66251729-3f9ae980-e78e-11e9-9ed3-353dd6ab43c1.jpg)  
<그림 6>  
그림6은 반대로 deiltion의 수치를 낮게하여 한 글자씩 boxing 과정을 한 모습입니다. 이 경우 한 글자씩 되는 경우가 많지만 자음 혹은 모음만 boxing을 하거나 안하는 경우가 생겨 이후 인식과정에 영향을 미치도록 합니다.  
따라서 일리아이즈는 이러한 문제를 해결하여 안정된 boxing을 할 수 있도록 하려 합니다.  
  
## 향후 계획2
일리아이즈는 현재 이미지/텍스트 분석 모델에 머신러닝을 이용하고 있습니다.향후 CTC(Connectionist Temporal Classfication를 이용하여 문자열을 분류할 계획이며, 이를 통해 입력된 url의 페이지로부터 판정된 결과의 정확도에 있어 유의미한 향상을 기대하고 있습니다.  
![프레젠테이션 1](https://user-images.githubusercontent.com/44759382/66252262-462c5f80-e794-11e9-8c0c-6b9ff2ac8490.png)  
위의 그림과 같이 문자열 전체를 특정 크기의 구간으로 나누어  해당 구간에서 예측된 결과를 출력하여 중복된 값과 공백은 제거한 뒤 최종 인식된 문자열을 출력하는 방식으로 분류에 정확도를 높일 계획입니다.
