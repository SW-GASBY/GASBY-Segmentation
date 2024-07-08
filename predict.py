import cv2
import os
import torch
import numpy as np
from ultralytics import YOLO

# GPU 설정
device = 'cuda:1' if torch.cuda.is_available() else 'cpu'
print(f'Using device: {device}')

# 모델 로드
model = YOLO('resources/weights/best.pt').to(device)

# 비디오 경로 설정
video_path = 'resources/test_video.mp4'
cap = cv2.VideoCapture(video_path)

# 출력 폴더 생성
output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 프레임을 모델에 입력하여 결과 얻기
    results = model(frame, save=True, save_txt=True, conf=0.5, verbose=False)
    cv2.imwrite(f'{output_dir}/frame_{frame_count:04d}.jpg', results[0].plot())
    
    frame_count += 1

cap.release()
print(f'Completed. Processed {frame_count} frames.')