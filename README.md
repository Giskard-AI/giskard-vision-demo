# Facial Landmark detection

This is a CI/CD example of an evaluation report produced by `giskard-vision` which compares a set of facial landmark detection models based on the following criteria:

- Performance on partial and entire facial parts
- Performance on images containing faces with different head poses (estimated with `6DRepNet`: https://github.com/thohemp/6DRepNet)
- Performance on images containing people from different ethnicities (estimated with `DeepFace`: https://github.com/serengil/deepface)
- Robustness against image perturbations like blurring, resizing, recoloring (performed by `opencv`: https://github.com/opencv/opencv)

Here're the results of the latest run:
|    | model         | facial_part   | dataloader                                                       |   prediction_time |   prediction_fail_rate | test     | metric   |   metric_value |   threshold | passed   |
|---:|:--------------|:--------------|:-----------------------------------------------------------------|------------------:|-----------------------:|:---------|:---------|---------------:|------------:|:---------|
|  0 | FaceAlignment | left half     | 300W cropped on left half                                        |         82.0379   |               0.564706 | TestDiff | NME_mean |    0.656253    |        -0.1 | False    |
|  1 | FaceAlignment | upper half    | 300W cropped on upper half                                       |        114.163    |               0.470588 | TestDiff | NME_mean |    0.223175    |        -0.1 | False    |
|  2 | FaceAlignment | entire face   | 300W resizing with ratios: 0.5                                   |         97.5293   |               0        | TestDiff | NME_mean |    0.0114276   |        -0.1 | False    |
|  3 | FaceAlignment | entire face   | 300W altered with color mode 7                                   |        149.049    |               0        | TestDiff | NME_mean |    0.00672821  |        -0.1 | False    |
|  4 | FaceAlignment | entire face   | 300W blurred                                                     |        150.677    |               0        | TestDiff | NME_mean |    0.00950801  |        -0.1 | False    |
|  5 | FaceAlignment | entire face   | (Cached (300W) with head-pose) filtered using 'positive_roll'    |         82.5509   |               0        | TestDiff | NME_mean |   -0.146944    |        -0.1 | True     |
|  6 | FaceAlignment | entire face   | (Cached (300W) with head-pose) filtered using 'negative_roll'    |        141.236    |               0        | TestDiff | NME_mean |    0.036736    |        -0.1 | False    |
|  7 | FaceAlignment | entire face   | (Cached (300W) with ethnicity) filtered using 'white_ethnicity'  |        130.233    |               0        | TestDiff | NME_mean |   -0.0520713   |        -0.1 | False    |
|  8 | FaceAlignment | entire face   | (Cached (300W) with ethnicity) filtered using 'latino_ethnicity' |         93.2886   |               0        | TestDiff | NME_mean |    0.208285    |        -0.1 | False    |
|  9 | OpenCV        | left half     | 300W cropped on left half                                        |          4.93539  |               0.564706 | TestDiff | NME_mean |    0.644057    |        -0.1 | False    |
| 10 | OpenCV        | upper half    | 300W cropped on upper half                                       |          4.73126  |               0.682353 | TestDiff | NME_mean |   -0.0402161   |        -0.1 | False    |
| 11 | OpenCV        | entire face   | 300W resizing with ratios: 0.5                                   |          4.59532  |               0        | TestDiff | NME_mean |    0.079876    |        -0.1 | False    |
| 12 | OpenCV        | entire face   | 300W altered with color mode 7                                   |          6.83177  |               0        | TestDiff | NME_mean |   -0.0013471   |        -0.1 | False    |
| 13 | OpenCV        | entire face   | 300W blurred                                                     |          6.49898  |               0        | TestDiff | NME_mean |    0.103017    |        -0.1 | False    |
| 14 | OpenCV        | entire face   | (Cached (300W) with head-pose) filtered using 'positive_roll'    |          3.77832  |               0        | TestDiff | NME_mean |   -0.0779265   |        -0.1 | False    |
| 15 | OpenCV        | entire face   | (Cached (300W) with head-pose) filtered using 'negative_roll'    |          6.68447  |               0        | TestDiff | NME_mean |    0.0194816   |        -0.1 | False    |
| 16 | OpenCV        | entire face   | (Cached (300W) with ethnicity) filtered using 'white_ethnicity'  |          8.22435  |               0        | TestDiff | NME_mean |   -0.196134    |        -0.1 | True     |
| 17 | OpenCV        | entire face   | (Cached (300W) with ethnicity) filtered using 'latino_ethnicity' |          4.06116  |               0        | TestDiff | NME_mean |    0.784538    |        -0.1 | False    |
| 18 | Mediapipe     | left half     | 300W cropped on left half                                        |          0.910076 |               0.727941 | TestDiff | NME_mean |  nan           |        -0.1 | False    |
| 19 | Mediapipe     | upper half    | 300W cropped on upper half                                       |          0.59947  |               0.735294 | TestDiff | NME_mean |  nan           |        -0.1 | False    |
| 20 | Mediapipe     | entire face   | 300W resizing with ratios: 0.5                                   |          0.941159 |               0        | TestDiff | NME_mean |   -0.0012767   |        -0.1 | False    |
| 21 | Mediapipe     | entire face   | 300W altered with color mode 7                                   |          0.738705 |               0.4      | TestDiff | NME_mean |   -0.325044    |        -0.1 | True     |
| 22 | Mediapipe     | entire face   | 300W blurred                                                     |          0.821196 |               0        | TestDiff | NME_mean |    1.24002e-06 |        -0.1 | False    |
| 23 | Mediapipe     | entire face   | (Cached (300W) with head-pose) filtered using 'positive_roll'    |          0.49506  |               0        | TestDiff | NME_mean |   -0.32544     |        -0.1 | True     |
| 24 | Mediapipe     | entire face   | (Cached (300W) with head-pose) filtered using 'negative_roll'    |          0.894151 |               0        | TestDiff | NME_mean |    0.08136     |        -0.1 | False    |
| 25 | Mediapipe     | entire face   | (Cached (300W) with ethnicity) filtered using 'white_ethnicity'  |          0.757157 |               0        | TestDiff | NME_mean |   -0.132671    |        -0.1 | True     |
| 26 | Mediapipe     | entire face   | (Cached (300W) with ethnicity) filtered using 'latino_ethnicity' |          0.50659  |               0        | TestDiff | NME_mean |    0.530683    |        -0.1 | False    |