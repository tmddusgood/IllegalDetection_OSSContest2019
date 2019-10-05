# OSSContest2019 일리아이즈  
Open Source Software Contest 2019  
다수의 불법적인 도박 사이트들은 웹 상에 존재하는 수많은 사이트들에 댓글 광고 등의 다양한 수단을 사용하여 일반인들을 유혹하고 있습니다.
수 년간의 꾸준한 단속에도 불구하고, 불법 도박 사이트들은 이러한 단속의 허점을 이용하여 그 광고 수단 또한 진화하고 있으며 현재에도 활발하게 운영되고 있는 실정입니다. 
일리아이즈 소프트웨어는 이러한 불법도박사이트의 효과적인 근절을 위해 개발되었습니다.  
<그림 1>은 불법 도박사이트들이 단속을 피해 사용하는 광고의 예시입니다.  
![KakaoTalk_20191005_022016798](https://user-images.githubusercontent.com/28249894/66255556-d46a0b00-e7bf-11e9-8797-4e8398a15438.jpg)  
<그림1>  
위 그림에는 일반적인 텍스트 광고가 아닌 이미지 위에 텍스트를 표시하여 광고하는 방식으로, 일반적으로 사용되는 텍스트 검사 방식으로는 단속에 어려움이 있습니다.
이러한 문제점을 인식하여  일리아이즈는 <그림1>에 나와 있는 이미지 위의 텍스트를 인식하여 추출 후 자연어처리를 통하여 해당 이미지가 존재하는 사이트가 도박 사이트인 것을 판단하게 해주는 소프트웨어를 개발하였습니다.  

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
  
![도표2](https://user-images.githubusercontent.com/44759382/66236573-cc618b00-e72d-11e9-8112-a91dec913d0a.png)   
<그림3>  
<그림3>에는 일리아이즈의 텍스트/이미지 분석 모델의 발전과정이 나타나 있습니다.  
초기 분석에는 naive bayesian을 이용하여 텍스트를 분류하였고, 이후 정확도를 높이려는 과정에서 텍스트 분석에 머신러닝을 이용, 이미지 인식에 OCR을 이용하는 방식에서 머신러닝을 추가적으로 적용하였습니다.

# 개발 환경  

# 설치 방법  

# 향후 계획  
일리아이즈는 현재 이미지/텍스트 분석 모델에 머신러닝을 이용하고 있습니다.향후 CTC(Connectionist Temporal Classfication를 이용하여 문자열을 분류할 계획이며, 이를 통해 입력된 url의 페이지로부터 판정된 결과의 정확도에 있어 유의미한 향상을 기대하고 있습니다.  
![프레젠테이션 1](https://user-images.githubusercontent.com/44759382/66252262-462c5f80-e794-11e9-8c0c-6b9ff2ac8490.png)  
위의 그림과 같이 문자열 전체를 특정 크기의 구간으로 나누어  해당 구간에서 예측된 결과를 출력하여 중복된 값과 공백은 제거한 뒤 최종 인식된 문자열을 출력하는 방식으로 분류에 정확도를 높일 계획입니다.
