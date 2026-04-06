import cv2 as cv
import numpy as np
from PIL import Image

video_file = 'my_video.MOV'

# --- CALIBRATION VALUES ---
K = np.array([[590.5476712, 0.0, 636.1797391],
              [0.0, 593.42211932, 362.33514848],
              [0.0, 0.0, 1.0]])

dist_coeff = np.array([0.006413, -0.01712186, -0.00262058, -0.00240041, 0.01042107])
# -----------------------------------

video = cv.VideoCapture(video_file)

map1, map2 = None, None
gif_frames = []
frame_count = 0

while True:
    valid, img = video.read()
    if not valid:
        break

    frame_count += 1

    # Rectify geometric distortion
    if map1 is None or map2 is None:
        map1, map2 = cv.initUndistortRectifyMap(K, dist_coeff, None, None, (img.shape[1], img.shape[0]), cv.CV_32FC1)

    rectified_img = cv.remap(img, map1, map2, interpolation=cv.INTER_LINEAR)
    cv.putText(img, "Original", (10, 30), cv.FONT_HERSHEY_DUPLEX, 1.0, (0, 0, 255), 2)
    cv.putText(rectified_img, "Rectified", (10, 30), cv.FONT_HERSHEY_DUPLEX, 1.0, (0, 255, 0), 2)
    combined = np.hstack((img, rectified_img))
    h, w = combined.shape[:2]
    if w > 1200:
        combined = cv.resize(combined, (0, 0), fx=0.4, fy=0.4)

    cv.imshow('Distortion Correction Demo', combined)

    if frame_count % 3 == 0 and len(gif_frames) < 60:
        rgb_img = cv.cvtColor(combined, cv.COLOR_BGR2RGB)
        gif_frames.append(Image.fromarray(rgb_img))

    if cv.waitKey(30) == 27:  # ESC
        break

video.release()
cv.destroyAllWindows()

if gif_frames:
    gif_frames[0].save('demo_result.gif', save_all=True, append_images=gif_frames[1:], duration=100, loop=0)