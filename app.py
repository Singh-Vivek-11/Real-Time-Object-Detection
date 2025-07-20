from flask import Flask, Response, render_template
import cv2
import torch

app = Flask(__name__)

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def generate_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        # Detect objects
        results = model(frame)
        frame = results.render()[0]
        # Convert frame to JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)