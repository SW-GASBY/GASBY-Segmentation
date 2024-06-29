import json
import os

def convert_coco_to_yolo(coco_json_path, output_dir):
    with open(coco_json_path) as f:
        data = json.load(f)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for image in data['images']:
        image_id = image['id']
        file_name = image['file_name']
        width = image['width']
        height = image['height']

        # YOLO 파일 이름 준비
        yolo_file_name = os.path.splitext(file_name)[0] + '.txt'
        yolo_file_path = os.path.join(output_dir, yolo_file_name)

        with open(yolo_file_path, 'w') as yolo_file:
            # 이미지에 해당하는 모든 어노테이션 찾기
            annotations = [ann for ann in data['annotations'] if ann['image_id'] == image_id]
            for ann in annotations:
                # COCO 포맷에서 YOLO 포맷으로 변환
                category_id = ann['category_id'] - 1  # YOLO는 클래스 인덱스가 0부터 시작
                bbox = ann['bbox']
                x_center = (bbox[0] + bbox[2] / 2) / width
                y_center = (bbox[1] + bbox[3] / 2) / height
                w = bbox[2] / width
                h = bbox[3] / height

                yolo_file.write(f"{category_id} {x_center} {y_center} {w} {h}\n")

# 폴더 경로 설정
folders = ['test', 'train', 'valid']

for folder in folders:
    coco_json_path = f'court segmentation.v4i.coco-mmdetection/images/{folder}/_annotations.coco.json'
    output_dir = f'court segmentation.v4i.coco-mmdetection/labels/{folder}'
    convert_coco_to_yolo(coco_json_path, output_dir)