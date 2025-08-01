import warnings

warnings.filterwarnings('ignore')
from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/v10/YOLOv10-ViS-FogNet-detect.yaml')
    # model.load('yolov8n.pt') # loading pretrain weights
    model.train(data='/root/code/dataset/dataset_visdrone/coco.yaml',
                cache=False,
                imgsz=640,
                epochs=500,
                batch=128,
                close_mosaic=10,
                workers=8, #
                optimizer='SGD', # using SGD
                device='0,1',
                # patience=0, # set 0 to close earlystop.
                # resume=True, # 断点续训
                # amp=False, # close amp
                # fraction=0.2,
                project='runs/coco-n',
                name='ViS-FogNet-500',
                )