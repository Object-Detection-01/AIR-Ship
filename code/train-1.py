import warnings

warnings.filterwarnings('ignore')
from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/v8/yolov10n.yaml')
    # model.load('yolov8n.pt') # loading pretrain weights
    model.train(data='/root/code/dataset/dataset_visdrone/data.yaml',
                cache=False,
                imgsz=640,
                epochs=500,
                batch=16,
                close_mosaic=0,
                workers=8, # Windows下出现莫名其妙卡主的情况可以尝试把workers设置为0
                optimizer='SGD', # using SGD
                device='0', # 指定显卡和多卡
                # patience=0, # set 0 to close earlystop.
                # resume=True, # 断点续训,YOLO初始化时选择last.pt,例如YOLO('last.pt')
                # amp=False, # close amp
                # fraction=0.2,
                project='runs/coco-n',
                name='DS_SPPF-500', # 保存路径和文件名
                )