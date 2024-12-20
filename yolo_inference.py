from ultralytics import YOLO 
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
model = YOLO('yolov8x')

results = model.predict('input_videos/08fd33_4.mp4',save=True,stream=True)

for result in results:
    print(result)
    print("===============================")
    for box in result.boxes:
        print(box)