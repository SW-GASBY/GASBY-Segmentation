<div align="center">

# BING: GASBY-SEGMENTATION

*BING 서비스의 코트 인식 SEGMENTAION 모델 학습 코드 입니다.*

[![Static Badge](https://img.shields.io/badge/language-english-red)](./README.md) [![Static Badge](https://img.shields.io/badge/language-korean-blue)](./README-KR.md) [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FSinging-voice-conversion%2Fsingtome-model&count_bg=%23E3E30F&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

</div>

<br>

**SW중심대학 디지털 경진대회** : SW와 생성 AI의 만남 - SW 부문
팀 GASBY의 BING 서비스
이 리포지토리는 팀 GASBY가 SW중심대학 디지털 경진대회에서 개발한 BING 서비스에 사용된 AWS Lambda 함수의 코드를 포함하고 있습니다. 본 프로젝트는 생성 AI 기술을 활용하여 사용자의 요구에 맞는 다양한 소프트웨어 솔루션을 제공합니다.

**레포지토리 개요**: 
SEGMENTATION 학습 모델

**주요 기능**: 
경기 영상에서 코트를 인식 및 세부적인 영역을 인식

<br>

<div align="center">

<h3> SERVICE part Team members </h3>

| Profile | Name | Role |
| :---: | :---: | :---: |
| <a href="https://github.com/wooing1084"><img src="https://avatars.githubusercontent.com/u/32007781?v=4" height="120px"></a> | SungHoon Jung <br> **wooing1084**| <br> Training YOLOv8-seg MODEL <br> GPT|


<br>


</div>

<br>

## 1. 데이터셋 설명

**GASBY-homography**
Download Dataset
curl -L "https://universe.roboflow.com/ds/Lfc4sBMGVv?key=xEm9XM3JwC" > roboflow.zip; unzip roboflow.zip; rm roboflow.zip

** 라벨 종류 **
Basketball-court : 농구코트 영역 (1342개)
three point line : 3점 라인 내부 영역 (1293개)
paint : 페인트존(골 밑) (776개)
center-circle : 중앙 원 (507개)

** Fine tuning Parameters **
학습 데이터 : 1362장
모델 : YOLOv8m-seg
에포크 : 300
배치: 16

