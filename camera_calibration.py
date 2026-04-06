import cv2 as cv
import numpy as np
from PIL import Image


def select_img_from_video(video_file, wait_msec=10):
    video = cv.VideoCapture(video_file)

    img_select = []
    frame_count = 0
    while True:
        valid, img = video.read()
        if not valid:
            break
        frame_count += 1
        if frame_count % 15 == 0:
            img_select.append(img)

    video.release()
    return img_select


def calib_camera_from_chessboard(images, board_pattern, board_cellsize, K=None, dist_coeff=None, calib_flags=None):
    # Find 2D corner points from given images
    img_points = []
    image_shape = None

    gif_frames = []

    for img in images:
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        if image_shape is None:
            image_shape = gray.shape[::-1]

        complete, pts = cv.findChessboardCorners(gray, board_pattern)

        if complete:
            img_points.append(pts)

            display_img = img.copy()
            cv.drawChessboardCorners(display_img, board_pattern, pts, complete)

            h, w = display_img.shape[:2]
            if w > 1200:
                display_img = cv.resize(display_img, (0, 0), fx=0.5, fy=0.5)

            cv.imshow('Finding Chessboard Corners', display_img)

            rgb_img = cv.cvtColor(display_img, cv.COLOR_BGR2RGB)
            gif_frames.append(Image.fromarray(rgb_img))
            # ----------------------------------------------------------

            cv.waitKey(100)

    cv.destroyAllWindows()

    if gif_frames:
        print("Saving visual demo to 'corner_demo.gif'...")
        gif_frames[0].save('corner_demo.gif',
                           save_all=True,
                           append_images=gif_frames[1:],
                           duration=100,
                           loop=0)

    assert len(img_points) > 0, 'There is no set of complete chessboard points!'

    obj_pts = [[c, r, 0] for r in range(board_pattern[1]) for c in range(board_pattern[0])]
    obj_points = [np.array(obj_pts, dtype=np.float32) * board_cellsize] * len(img_points)

    # Calibrate the camera
    ret, K, dist_coeff, rvecs, tvecs = cv.calibrateCamera(obj_points, img_points, image_shape, K, dist_coeff,
                                                          flags=calib_flags)
    return ret, K, dist_coeff


if __name__ == '__main__':
    video_file = 'my_video.MOV  '
    board_pattern = (12, 8)
    board_cellsize = 0.022

    print("Extracting frames from video...")
    images = select_img_from_video(video_file)

    print(f"Calibrating camera using {len(images)} valid frames...")
    ret, K, dist_coeff = calib_camera_from_chessboard(images, board_pattern, board_cellsize)

    print("\n## Camera Calibration Results")
    print(f"* RMS error = {ret:.6f}")
    print(f"* Camera matrix (K) =\n{K}")
    print(f"* Distortion coefficient (k1, k2, p1, p2, k3) =\n{dist_coeff.ravel()}")