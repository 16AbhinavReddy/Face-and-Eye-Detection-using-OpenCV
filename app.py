from flask import Flask, render_template, Response

import cv2
app = Flask(__name__)

camera = cv2.VideoCapture(0)


def frame_generator():
    while True:
        success, frames = camera.read()
        if not success:
            break
        else:
            re, buffer = cv2.imencode('.jpg',frames)
            frames = buffer.tobytes()
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frames + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(frame_generator(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == "__main__":
    app.run(debug=True)



