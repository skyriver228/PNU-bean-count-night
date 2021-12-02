# PNU-bean-count-night

- PNU Mini Kaggle Competition(콩세는 밤)

    👉 input: 콩이 담겨져 있는 사진(동서남북, 위)   
    👉 output: 담겨져 있는 콩의 개수

    👉 21년도 대회 회고: error 식을 잘못 세워 피팅 방향성을 잘못 잡았었음...
    👉 result
        👉 Error1(square): 76660.25443252905
        👉 Error2        : 1022.9702061451912

- team PongPongLab
    - [성강(skyriver)](https://github.com/skyriver228)
    - [송주현(izen1231)](https://github.com/izen1231)

---------
## 목차
1. [환경](#1-환경)
2. [파일 구조](#2-파일-구조)
3. [Algorithm Flow](#3-Algorithm-Flow)
4. [Code Structure](#4-Code-Structure)
-----------
## 1. 환경
👉 OS : Windows 10  
👉 python 3.9.0

### 1.1. 사용 라이브러리
👉 requirements.txt 참조  
<pre>
<code>matplotlib==3.4.0  
numpy==1.20.3  
opencv-python==3.4.15.55  
scipy==1.7.3  
</code></pre>

### 1.2. 제한
👉 local data : under 10MB  
👉 no internet usage       

----------
## 2. 파일 구조
<pre>
<code>
├── Hidden: test data          
│       └── t00   
│             └── 1~4.jpg : 동서남북 방향
│             └── 5.jpg : 위 방향
├── Open: train data          
│       └── t00   
│             └── 1~4.jpg : 동서남북 방향
│             └── 5.jpg : 위 방향
└── PongPongLab(01)         
        ├── Out  
        │     └── Kong_01.txt : Output data
        └── System
              ├── data : Hidden, Open의 
              ├── idea  
              └── main.py
</code></pre>
----------
## 3. Algorithm Flow
### 3.1. Preprocessing
- rgb 데이터는 사용하기에 너무 무거우며, 현재 대회에서는 CNN과 같은 부분의 사용이 하드웨어 리소스, 사용가능 라이브러리면에서 제한적이므로 전처리 과정을 통해 필요한 부분만을 가져온다. 
- 전체적인 전처리 과정을 통한 결과물은 아래와 같다. 
    1. rgb img
    2. binary img
    3. count and area data
#### 3.1.1. Get target img
> BeanCount.getImgPath(self, path: str) -> img_paths: List[str]  

[img]
- 모든 부분을 사용할 필요는 없으며, 외부에 보이는 환경에 "원"으로 볼 수 있는 요소가 있으므로 필요부분(target)만을 잘라내 준다. 
#### 3.1.2. RGB2Binary
- 크게 2가지 방법을 사용하여 2가지 다른 데이터를 얻어서 사용하고자 한다.   

👉 edge detection
> edgeRGB2Binary(self, rgb_img: nd.array()) -> edge_bi_img: nd.array() 
- edge detection을 활용하여 rgb → binary 를 진행한다. 
> circleCount(self, egde_bi_img: nd.array()) -> num: int
- edge detection 결과물인 binary img를 활용하여 binary → circle count를 진행한다. 

[img]

👉 hsv
> hsvRGB2Binary(self, rgb_img: nd.array()) -> hsv_bi_img: nd.array() 
- hsv를 활용하여 rgb → binary 를 진행한다. 
> areaCount(self, hsv_bi_img: nd.array()) -> area: int
- hsv 결과물인 binary img를 활용하여 binary → area counting(white space = bean space)를 진행한다. 

[img]

#### 3.1.3. Erasing Noise
>erasingNoise(self, ~_bi_img: nd.array()) -> ~_bi_img: nd.array()
- molophology(열기) 연산: 침식 -> 팽창 으로 노이즈를 제거한다.
    - 작은 돌기,작은 객체가 사라지고 얇은 연결선이 끊어진다.

[img]

### 3.2. Evaluate Preprocessed Output

#### 3.2.1. Selecting && Concating Output
- 3.1.2. RGB2Binary의 결과물들 count, area에 해당하는 데이터들을 res_df에 정리하고 관찰한다. 

### 3.3. Building Model
- 3.2.1. res_df에 정리하고 관찰한다. 
- 
### 3.4. Running && Evaluate Model
----------
## 4. Code Structure
<pre>
<code>
Class BeanCount
├── __init__(self, path: str)       
│       ├── self.path = path
│       │     └── input pictures' folder path
│       ├── self.res_df: pd.DataFrame
│       │     └── df for binary img analysised data(circleCount,areaCount)
│       ├── self.model: ?
│       │     └── model for predicting count result of pea(bean)
│       └── self.output_df: pd.DataFrame
│             └── df for output
├── beanCount(self, path: str) -> file: .txt
│       └── whole process
├── getImgPath(self, path: str) -> img_paths: List[str]
│       └── get pictures' path
├── getTargetImg(self, img_path: str) -> rgb_img: nd.array()
│       └── get cutted picture only with target
├── edgeRGB2Binary(self, rgb_img: nd.array()) -> edge_bi_img: nd.array()
│       └── get binary img by edge detection 
├── hsvRGB2Binary(self, rgb_img: nd.array()) -> hsv_bi_img: nd.array()
│       └── get binary img by hsv 
├── erasingNoise(self, ~_bi_img: nd.array()) -> ~_bi_img: nd.array()
│       └── erase noise of binary img of output(edgeRGB2Binary, hsvRGB2Binary) by using morphology
├── circleCount(self, egde_bi_img: nd.array()) -> num: int
│       └── get counted circle(pea)'s number by edge detected binary img and add to res_df
├── areaCount(self, hsv_bi_img: nd.array()) -> area: int
│       └── get counted circle(pea)'s area by binary img converted by hsv and add to res_df
├── bulidingModel(self, self.res_df: pd.DataFrame) -> self.res_df: pd.DataFrame, model: ?
│       └── building model by res_df
├── runningModel(self, self.model: ?, self.res_df: pd.DataFrame, self.output_df: pd.DataFrame) -> self.output_df: pd.DataFrame
│       └── running model and predict count result of pea(bean)
└── exportOutput(self, self.output_df: pd.DataFrame) -> file: .txt
        └── export output_df based on competition's rule
</code></pre>
