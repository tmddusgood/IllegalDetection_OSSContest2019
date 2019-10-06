# Project Title

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

## Installing  

### 아나콘다     
[Anaconda](https://www.anaconda.com/distribution/#download-section)- 파이썬 3.x 버전
* 설치시 아래와 같이 환경변수 설정 포함 선택


  
### Tessract 5.0-alpha     
[Tesseract 5.0-alpha](https://github.com/UB-Mannheim/tesseract/wiki)- 사용자의 운영체제 버전   

* 설치 파일 경로는  C:\Program Files (x86)\Tesseract-OCR   또는 C:\Program Files\Tesseract-OCR  

* 설치 후 아래와 같이 환경변수 탭 클릭  

![tesseract1](https://user-images.githubusercontent.com/39071632/66267863-9b8a6e80-e871-11e9-9ac2-cc9224976936.JPG)


* Path 설정  
![tesseract2](https://user-images.githubusercontent.com/39071632/66267865-9e855f00-e871-11e9-8de0-13722809c1eb.JPG)

![tesseract3](https://user-images.githubusercontent.com/39071632/66267866-a04f2280-e871-11e9-837d-cc8f5774d4bc.JPG)

* TESSDATA_PREFIX 설정

![tesseract4](https://user-images.githubusercontent.com/39071632/66267892-df7d7380-e871-11e9-8ee7-2f8b6af20331.JPG)  

### 가상환경 생성   

Anaconda prompt 실행 후 

```
conda create --name [가상환경명] python=[파이썬 3.x버전]
```

### 가상환경 활성화

```
activate [가상환경명]
```
### 모듈 설치  
  
#### pip 업그레이드  
 
```
pip install --upgrade pip
```  

#### Tensorflow  

* cpu 사용
```
pip install tensorflow==1.12  
```  
* GPU 사용    
```
pip install tensorflow-gpu==1.12  
```  

#### Opencv  

```
pip install opencv-contrib-python
```  
#### Keras  

* cpu 사용 
```
pip install keras==2.3.0
```

* gpu 사용 
```
pip install keras-gpu==2.3.0
```

#### Tqdm  

```
pip install tqdm
```

#### Pytesseract  

```
pip install pytesseract
```
#### h5py  

```
pip install h5py
```

#### Konlpy  

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
