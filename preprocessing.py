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
        img_width = image['width']
        img_height = image['height']
        
        # YOLO 파일 이름 준비
        yolo_file_name = os.path.splitext(file_name)[0] + '.txt'
        yolo_file_path = os.path.join(output_dir, yolo_file_name)

        with open(yolo_file_path, 'w') as yolo_file:
            # 이미지에 해당하는 모든 어노테이션 찾기
            annotations = [ann for ann in data['annotations'] if ann['image_id'] == image_id]
            for ann in annotations:
                # COCO 포맷에서 YOLO 포맷으로 변환
                category_id = ann['category_id'] - 1  # YOLO는 클래스 인덱스가 0부터 시작
                segmentation = ann['segmentation'][0]
                normalized_segmentation = [coord / img_width if i % 2 == 0 else coord / img_height for i, coord in enumerate(segmentation)]
                
                segmentation_str = ' '.join(map(str, normalized_segmentation))

                yolo_file.write(f"{category_id} {segmentation_str}\n")

# 폴더 경로 설정
folders = ['test', 'train', 'valid']

for folder in folders:
    coco_json_path = f'dataset/images/{folder}/_annotations.coco.json'
    output_dir = f'dataset/labels/{folder}'
    convert_coco_to_yolo(coco_json_path, output_dir)