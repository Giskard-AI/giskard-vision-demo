# Facial Landmark detection

This is a CI/CD example of an evaluation report produced by `giskard-vision` which compares a set of facial landmark detection models based on the following criteria:

- Performance on partial and entire facial parts
- Performance on images containing faces with different head poses (estimated with `6DRepNet`: https://github.com/thohemp/6DRepNet)
- Performance on images containing people from different ethnicities (estimated with `DeepFace`: https://github.com/serengil/deepface)
- Robustness against image perturbations like blurring, resizing, recoloring (performed by `opencv`: https://github.com/opencv/opencv)

Here're the results of the latest run:
|    | criteria                                                         | model         | test     | metric   |   metric_value |   threshold | passed   |   prediction_time |   prediction_fail_rate |
|---:|:-----------------------------------------------------------------|:--------------|:---------|:---------|---------------:|------------:|:---------|------------------:|-----------------------:|
|  0 | (Cached (300W) with ethnicity) filtered using 'latino_ethnicity' | FaceAlignment | TestDiff | NME_mean |      0.371225  |           0 | False    |          57.6478  |              0.142857  |
|  1 | (Cached (300W) with ethnicity) filtered using 'latino_ethnicity' | Mediapipe     | TestDiff | NME_mean |      0.038642  |           0 | False    |           5.32492 |              0.285714  |
|  2 | (Cached (300W) with ethnicity) filtered using 'latino_ethnicity' | OpenCV        | TestDiff | NME_mean |     -0.738433  |           0 | True     |          32.0595  |              0         |
|  3 | (Cached (300W) with ethnicity) filtered using 'white_ethnicity'  | FaceAlignment | TestDiff | NME_mean |     -0.604868  |           0 | True     |          82.8643  |              0.0384615 |
|  4 | (Cached (300W) with ethnicity) filtered using 'white_ethnicity'  | Mediapipe     | TestDiff | NME_mean |      0.0260865 |           0 | False    |           7.67246 |              0.173077  |
|  5 | (Cached (300W) with ethnicity) filtered using 'white_ethnicity'  | OpenCV        | TestDiff | NME_mean |     -0.374386  |           0 | True     |          44.3418  |              0.0769231 |
|  6 | (Cached (300W) with head-pose) filtered using 'negative_roll'    | FaceAlignment | TestDiff | NME_mean |     -0.576123  |           0 | True     |          78.1323  |              0.0416667 |
|  7 | (Cached (300W) with head-pose) filtered using 'negative_roll'    | Mediapipe     | TestDiff | NME_mean |     -0.0123974 |           0 | True     |           7.36745 |              0.0833333 |
|  8 | (Cached (300W) with head-pose) filtered using 'negative_roll'    | OpenCV        | TestDiff | NME_mean |     -0.505026  |           0 | True     |          39.3873  |              0.125     |
|  9 | (Cached (300W) with head-pose) filtered using 'positive_roll'    | FaceAlignment | TestDiff | NME_mean |      0.54085   |           0 | False    |          83.482   |              0.0576923 |
| 10 | (Cached (300W) with head-pose) filtered using 'positive_roll'    | Mediapipe     | TestDiff | NME_mean |      0.0147429 |           0 | False    |           7.69844 |              0.288462  |
| 11 | (Cached (300W) with head-pose) filtered using 'positive_roll'    | OpenCV        | TestDiff | NME_mean |      0.505026  |           0 | False    |          45.486   |              0.192308  |
| 12 | 300W altered with color mode 7                                   | FaceAlignment | TestDiff | NME_mean |     -0.186222  |           0 | True     |         110.561   |              0.02      |
| 13 | 300W altered with color mode 7                                   | Mediapipe     | TestDiff | NME_mean |     -0.225328  |           0 | True     |           8.6883  |              0.8       |
| 14 | 300W altered with color mode 7                                   | OpenCV        | TestDiff | NME_mean |      0.536485  |           0 | False    |          56.4112  |              0.14      |
| 15 | 300W blurred                                                     | FaceAlignment | TestDiff | NME_mean |     -0.0451077 |           0 | True     |         114.86    |              0.04      |
| 16 | 300W blurred                                                     | Mediapipe     | TestDiff | NME_mean |      0.0566332 |           0 | False    |          10.2986  |              0.09      |
| 17 | 300W blurred                                                     | OpenCV        | TestDiff | NME_mean |      0.410555  |           0 | False    |          52.8073  |              0.12      |
| 18 | 300W cropped on left half                                        | FaceAlignment | TestDiff | NME_mean |     -0.553663  |           0 | True     |          82.9528  |              0.820441  |
| 19 | 300W cropped on left half                                        | Mediapipe     | TestDiff | NME_mean |     -0.170099  |           0 | True     |           8.89241 |              0.951029  |
| 20 | 300W cropped on left half                                        | OpenCV        | TestDiff | NME_mean |     -0.301223  |           0 | True     |          40.2202  |              0.825882  |
| 21 | 300W cropped on upper half                                       | FaceAlignment | TestDiff | NME_mean |     -0.541586  |           0 | True     |          78.9063  |              0.782941  |
| 22 | 300W cropped on upper half                                       | Mediapipe     | TestDiff | NME_mean |     -0.2261    |           0 | True     |           9.04918 |              0.941765  |
| 23 | 300W cropped on upper half                                       | OpenCV        | TestDiff | NME_mean |     -0.720575  |           0 | True     |          38.917   |              0.978824  |
| 24 | 300W resizing with ratios: 0.5                                   | FaceAlignment | TestDiff | NME_mean |      0.0185174 |           0 | False    |         110.374   |              0.04      |
| 25 | 300W resizing with ratios: 0.5                                   | Mediapipe     | TestDiff | NME_mean |      0.0358656 |           0 | False    |           9.88213 |              0.12      |
| 26 | 300W resizing with ratios: 0.5                                   | OpenCV        | TestDiff | NME_mean |      0.603806  |           0 | False    |          38.9247  |              0.18      |