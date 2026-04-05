# Camera Distortion Calibrator

## Overview
This repository contains a Python implementation for absolute camera calibration and geometric distortion correction using OpenCV. It extracts 2D corner points from a recorded video of a physical chessboard pattern to calculate the camera's intrinsic parameters and perfectly flatten radial and tangential lens distortion.

## Camera Calibration Results
The camera was calibrated using an A4 printed chessboard with 12x8 internal vertices and 22mm squares.

* **RMS Error (RMSE):** `[Paste your RMSE here]`
* **Camera Matrix (K):**
  * **fx:** `[Paste fx here]`
  * **fy:** `[Paste fy here]`
  * **cx:** `[Paste cx here]`
  * **cy:** `[Paste cy here]`
* **Distortion Coefficients (k1, k2, p1, p2, k3):** `[Paste the array of distortion coefficients here]`

## Lens Distortion Correction Demo
Using the calculated intrinsic parameters, the raw video frames were remapped to remove lens distortion. As demonstrated below, the spatial curvature introduced by the camera lens has been successfully rectified.
