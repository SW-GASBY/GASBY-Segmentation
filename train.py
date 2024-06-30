import torch
from ultralytics import YOLO

# 학습에 gpu사용
device = 'cuda:1' if torch.cuda.is_available() else 'cpu'
print(f'Using device: {device}')

# YOLOv8n-1280 모델 불러오기
model = YOLO('yolov8n-seg.pt').to(device)  # YOLOv8n 모델 사용

# 데이터셋 경로 설정 (YOLO 형식으로 구성된 데이터셋)
data_path = 'data.yaml'

# 학습 설정
epochs = 200
batch_size = 16
img_size = 640


# 모델 학습
results = model.train(
    data=data_path,
    epochs=epochs,
    batch=batch_size,
    imgsz=img_size,
    name='custom_yolov8_model'  # 저장될 모델의 이름 설정
)