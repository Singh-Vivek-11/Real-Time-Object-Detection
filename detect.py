import cv2
import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True, trust_repo=True)

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)
    cv2.imshow('YOLOv5 Detection', results.render()[0])
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()