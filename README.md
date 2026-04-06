# Camera Distortion Calibrator

## 1. Overview
This repository contains a Python implementation that uses OpenCV to perform absolute camera calibration and correct geometric lens distortion from a smartphone camera. 

## 2. Camera Calibration Results
The camera's intrinsic parameters were extracted by processing a video of an A4-sized chessboard pattern (12x8 internal vertices, 22mm square size) attached to a completely flat surface. 

### Corner Detection Demo
![Corner Detection Demo]
![corner_demo](https://github.com/user-attachments/assets/35b68ac4-21ea-4b77-b154-7c778efb97d1)

* **RMSE (Root Mean Square Error):** `0.489260`
* **Camera Matrix (K):**
  * **fx:** `590.5476712`
  * **fy:** `593.42211932`
  * **cx:** `636.1797391`
  * **cy:** `362.33514848`
* **Distortion Coefficients (k1, k2, p1, p2, k3):**
  * `[0.006413, -0.01712186, -0.00262058, -0.00240041, 0.01042107]`

## 3. Lens Distortion Correction Demo
Using the calculated intrinsic parameters and distortion coefficients, the raw video frames were remapped to remove the radial and tangential distortion introduced by the camera lens. The side-by-side comparison below demonstrates the successful geometric flattening of the image.

![Distortion Correction Result]
![demo_result](https://github.com/user-attachments/assets/420637fd-147b-4097-9e28-ccb41cf9641b)
