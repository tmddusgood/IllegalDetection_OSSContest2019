# Project Title

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing  

#### 아나콘다     
[Anaconda](https://www.anaconda.com/distribution/#download-section)- 파이썬 3.x 버전   
  
#### Tessract 5.0-alpha     
[Tesseract 5.0-alpha](https://github.com/UB-Mannheim/tesseract/wiki)- 사용자의 운영체제 버전   

1.설치 파일 경로는  C:\Program Files (x86)\Tesseract-OCR   또는 C:\Program Files\Tesseract-OCR  

2.설치 후 아래와 같이 환경변수 탭 클릭  

![Alt installation1](C:\Users\rlarlghks\Desktop\tesseract1.jpg)  

3.Path 설정  
![Alt installation2](C:\Users\rlarlghks\Desktop\tesseract2.jpg)    
![Alt installation3](C:\Users\rlarlghks\Desktop\tesseract3.jpg)    

4.TESSDATA_PREFIX 설정  
![Alt installation4](C:\Users\rlarlghks\Desktop\tesseract4.jpg)    





#### 가상환경 생성   

Anaconda prompt 실행 후 

```
conda create --name [가상환경명] python=[파이썬 3.x버전]
```

#### 가상환경 활성화

```
activate [가상환경명]
```
#### 모듈 설치  
  
pip 업그레이드  
 
```
pip install --upgrade pip
```  

텐서플로우  

```
pip install tensorflow
```






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
