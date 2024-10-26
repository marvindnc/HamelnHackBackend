#!/usr/bin/env python
# Example for:
#
import argparse
import logging
import os
import signal
import cv2
from ultralytics import YOLO
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()
running = True
task_suffixes = {
    'detect': '',
    'segment': '-seg',
    'classify': '-cls',
    'pose': '-pose',
}
COCO_CLASSES = {
    'person': 0,
    'bicycle': 1,
    'car': 2,
    'motorcycle': 3,
    'airplane': 4,
    'bus': 5,
    'train': 6,
    'truck': 7,
    'boat': 8,
    'traffic light': 9,
    'fire hydrant': 10,
    'stop sign': 11,
    'parking meter': 12,
    'bench': 13,
    'bird': 14,
    'cat': 15,
    'dog': 16,
    'horse': 17,
    'sheep': 18,
    'cow': 19,
    'elephant': 20,
    'bear': 21,
    'zebra': 22,
    'giraffe': 23,
    'backpack': 24,
    'umbrella': 25,
    'handbag': 26,
    'tie': 27,
    'suitcase': 28,
    'frisbee': 29,
    'skis': 30,
    'snowboard': 31,
    'sports ball': 32,
    'kite': 33,
    'baseball bat': 34,
    'baseball glove': 35,
    'skateboard': 36,
    'surfboard': 37,
    'tennis racket': 38,
    'bottle': 39,
    'wine glass': 40,
    'cup': 41,
    'fork': 42,
    'knife': 43,
    'spoon': 44,
    'bowl': 45,
    'banana': 46,
    'apple': 47,
    'sandwich': 48,
    'orange': 49,
    'broccoli': 50,
    'carrot': 51,
    'hot dog': 52,
    'pizza': 53,
    'donut': 54,
    'cake': 55,
    'chair': 56,
    'couch': 57,
    'potted plant': 58,
    'bed': 59,
    'dining table': 60,
    'toilet': 61,
    'tv': 62,
    'laptop': 63,
    'mouse': 64,
    'remote': 65,
    'keyboard': 66,
    'cell phone': 67,
    'microwave': 68,
    'oven': 69,
    'toaster': 70,
    'sink': 71,
    'refrigerator': 72,
    'book': 73,
    'clock': 74,
    'vase': 75,
    'scissors': 76,
    'teddy bear': 77,
    'hair drier': 78,
    'toothbrush': 79,
}
def model_name(size, task):
    suffix = task_suffixes[task]
    return f'yolov8{size}{suffix}.pt'

# Erlaubte Klassen fuer den Blur
ALLOWED_CLASSES = {'person', 'car'}  

# Funktion zum Blurren erkannter Objekte
def blur_detected_objects(image, predictions):  
    for detection in predictions:
        if detection.label in ALLOWED_CLASSES:
            # Get bounding box coordinates
            x1, y1, x2, y2 = map(int, detection.boxes[0])
            # Extract the region to blur
            roi = image[y1:y2, x1:x2]
            # Apply a Gaussian blur to this region
            blurred_roi = cv2.GaussianBlur(roi, (99, 99), 30)
            # Replace the original ROI with the blurred ROI
            image[y1:y2, x1:x2] = blurred_roi
    return image


def do_inferencing(source, model_size, class_list):
    global running
    # use USB camera
    if source.isdigit():
        source = int(source)
    # get video source
    cap         = cv2.VideoCapture(source)
    # get details from video source
    width       = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height      = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps         = cap.get(cv2.CAP_PROP_FPS)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    logger.info("start inferencing")
    # instanciate yolo model
    model = YOLO(model_name(model_size, task="detect"))
    image = cv2.imread(source)
    prediction = model.predict(image, verbose=False, tracker='bytetrack.yaml')
    res_plotted = prediction[0].plot()
    cv2.imwrite("inferenced.jpg", res_plotted)
    #cv2.imwrite("infreenced_blured.jpg", blur_detected_objects(image, prediction))

    # be nice to your operating system
    cap.release()
    cv2.destroyAllWindows()
    logger.info("Stopped inferencing")

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('videosource', help='any video source opencv understands, e.g. 0,1,... for usb cams, "rtsp://..." for RTSP streams, /path/video.mp4 for video file')
    arg_parser.add_argument('-m', '--model-size', choices=['n', 's', 'm', 'l', 'x'], default='n', help='the size of the model to use (nano, small, medium, large, xlarge); defaults to "nano"')
    args = arg_parser.parse_args()
    do_inferencing(args.videosource, args.model_size, COCO_CLASSES)