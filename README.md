# PNU-bean-count-night

- PNU Mini Kaggle Competition(콩세는 밤)

    👉 input: 콩이 담겨져 있는 사진(동서남북, 위)   
    👉 output: 담겨져 있는 콩의 개수

- team PongPongLab
    - [성강(skyriver)](https://github.com/skyriver228)
    - [송주현(izen1231)](https://github.com/izen1231)

---------
## 목차
1. [환경](#2-환경)
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
scipy==1.6.3  
</code></pre>

### 1.2. 제한
👉 local data : under 10MB  
👉 no internet usage       

----------
## 2. 파일 구조
<pre>
<code>
├── Hiden: test data          
│       └── t00   
│             └── 1~4.jpg : 동서남북 방향
│             └── 5.jpg : 위 방향
├── Open: train data          
│       └── t00   
│             └── 1~4.jpg : 동서남북 방향
│             └── 5.jpg : 위 방향
└── PongPongLab         
        └── Out  
              └── Kong_PongPongLab.txt : Output data
        └── System
              └── main.py
</code></pre>
----------
## 3. Algorithm Flow
### 3.1. Preprocessing
#### 3.1.1. Get target img
#### 3.1.2. RGB2Binary
#### 3.1.3. Erasing Noise
### 3.2. Evaluate Preprocessed Output
#### 3.2.1. Selecting && Concating Output
### 3.2. Building Model
### 3.3. Evaluate Model
----------
## 3. Code Structure
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
├── circleCount(self, egde_bi_img: nd.array()) -> num: int
│       └── get counted circle(pea)'s number by edge detected binary img and add to res_df
├── hsvRGB2Binary(self, rgb_img: nd.array()) -> hsv_bi_img: nd.array()
│       └── get binary img by hsv 
├── areaCount(self, hsv_bi_img: nd.array()) -> area: int
│       └── get counted circle(pea)'s area by binary img converted by hsv and add to res_df
├── bulidingModel(self, self.res_df: pd.DataFrame) -> self.res_df: pd.DataFrame, model: ?
│       └── building model by res_df
├── runningModel(self, self.model: ?, self.res_df: pd.DataFrame, self.output_df: pd.DataFrame) -> self.output_df: pd.DataFrame
│       └── running model and predict count result of pea(bean)
└── exportOutput(self, self.output_df: pd.DataFrame) -> file: .txt
        └── export output_df based on competition's rule
</code></pre>