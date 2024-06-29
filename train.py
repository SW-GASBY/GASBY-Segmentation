from ultralytics import YOLO

# YOLOv8 모델 불러오기(s3에 저장된 최신의 모델을 사용하면 됨)
# model/yolo_model_latest.pt 뭐 이런식으로 저장되어있으면 YOLO('model/yolo_model_latest.pt') 이렇게 사용하면 됨
model = YOLO('yolov8n-seg.pt')

# 데이터셋 경로 설정 (YOLO 형식으로 구성된 데이터셋)
# 람다에서 엔드포인트에 요청이 오면 데이터셋을 s3에서 다운받고 해당 경로를 넣어주면 됨
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