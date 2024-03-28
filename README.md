# Facial Landmark detection

This is a CI/CD example of an evaluation report produced by `giskard-vision` which compares a set of facial landmark detection models based on the following criteria:

- Performance on partial and entire facial parts
- Performance on images containing faces with different head poses (estimated with `6DRepNet`: https://github.com/thohemp/6DRepNet)
- Performance on images containing people from different ethnicities (estimated with `DeepFace`: https://github.com/serengil/deepface)
- Robustness against image perturbations like blurring, resizing, recoloring (performed by `opencv`: https://github.com/opencv/opencv)

Here're the results of the latest run:
|    | model         | facial_part   | dataloader                                                       |   prediction_time |   prediction_fail_rate | test     | metric   |   metric_value |   threshold | passed   |
|---:|:--------------|:--------------|:-----------------------------------------------------------------|------------------:|-----------------------:|:---------|:---------|---------------:|------------:|:---------|
|  0 | FaceAlignment | left half     | 300W cropped on left half                                        |         82.4951   |               0.564706 | TestDiff | NME_mean |    0.656253    |           0 | False    |
|  1 | FaceAlignment | upper half    | 300W cropped on upper half                                       |        125.236    |               0.470588 | TestDiff | NME_mean |    0.223175    |           0 | False    |
|  2 | FaceAlignment | entire face   | 300W resizing with ratios: 0.5                                   |        100.782    |               0        | TestDiff | NME_mean |    0.0114276   |           0 | False    |
|  3 | FaceAlignment | entire face   | 300W altered with color mode 7                                   |        150.682    |               0        | TestDiff | NME_mean |    0.00672821  |           0 | False    |
|  4 | FaceAlignment | entire face   | 300W blurred                                                     |        152.515    |               0        | TestDiff | NME_mean |    0.00950801  |           0 | False    |
|  5 | FaceAlignment | entire face   | (Cached (300W) with head-pose) filtered using 'positive_roll'    |         83.9858   |               0        | TestDiff | NME_mean |   -0.146944    |           0 | True     |
|  6 | FaceAlignment | entire face   | (Cached (300W) with head-pose) filtered using 'negative_roll'    |        145.777    |               0        | TestDiff | NME_mean |    0.036736    |           0 | False    |
|  7 | FaceAlignment | entire face   | (Cached (300W) with ethnicity) filtered using 'white_ethnicity'  |        119.488    |               0        | TestDiff | NME_mean |   -0.0337788   |           0 | True     |
|  8 | FaceAlignment | entire face   | (Cached (300W) with ethnicity) filtered using 'latino_ethnicity' |         94.7312   |               0        | TestDiff | NME_mean |    0.208285    |           0 | False    |
|  9 | OpenCV        | left half     | 300W cropped on left half                                        |          4.8024   |               0.564706 | TestDiff | NME_mean |    0.644057    |           0 | False    |
| 10 | OpenCV        | upper half    | 300W cropped on upper half                                       |          4.72724  |               0.682353 | TestDiff | NME_mean |   -0.0402161   |           0 | True     |
| 11 | OpenCV        | entire face   | 300W resizing with ratios: 0.5                                   |          4.72427  |               0        | TestDiff | NME_mean |    0.079876    |           0 | False    |
| 12 | OpenCV        | entire face   | 300W altered with color mode 7                                   |          6.81832  |               0        | TestDiff | NME_mean |   -0.0013471   |           0 | True     |
| 13 | OpenCV        | entire face   | 300W blurred                                                     |          6.48775  |               0        | TestDiff | NME_mean |    0.103017    |           0 | False    |
| 14 | OpenCV        | entire face   | (Cached (300W) with head-pose) filtered using 'positive_roll'    |          3.76961  |               0        | TestDiff | NME_mean |   -0.0779265   |           0 | True     |
| 15 | OpenCV        | entire face   | (Cached (300W) with head-pose) filtered using 'negative_roll'    |          6.67981  |               0        | TestDiff | NME_mean |    0.0194816   |           0 | False    |
| 16 | OpenCV        | entire face   | (Cached (300W) with ethnicity) filtered using 'white_ethnicity'  |          5.72157  |               0        | TestDiff | NME_mean |   -0.168421    |           0 | True     |
| 17 | OpenCV        | entire face   | (Cached (300W) with ethnicity) filtered using 'latino_ethnicity' |          4.06064  |               0        | TestDiff | NME_mean |    0.784538    |           0 | False    |
| 18 | Mediapipe     | left half     | 300W cropped on left half                                        |          0.758855 |               0.727941 | TestDiff | NME_mean |  nan           |           0 | False    |
| 19 | Mediapipe     | upper half    | 300W cropped on upper half                                       |          0.735525 |               0.735294 | TestDiff | NME_mean |  nan           |           0 | False    |
| 20 | Mediapipe     | entire face   | 300W resizing with ratios: 0.5                                   |          0.944386 |               0        | TestDiff | NME_mean |   -0.0012767   |           0 | True     |
| 21 | Mediapipe     | entire face   | 300W altered with color mode 7                                   |          0.751228 |               0.4      | TestDiff | NME_mean |   -0.325045    |           0 | True     |
| 22 | Mediapipe     | entire face   | 300W blurred                                                     |          0.832877 |               0        | TestDiff | NME_mean |    1.24002e-06 |           0 | False    |
| 23 | Mediapipe     | entire face   | (Cached (300W) with head-pose) filtered using 'positive_roll'    |          0.500413 |               0        | TestDiff | NME_mean |   -0.32544     |           0 | True     |
| 24 | Mediapipe     | entire face   | (Cached (300W) with head-pose) filtered using 'negative_roll'    |          0.903642 |               0        | TestDiff | NME_mean |    0.08136     |           0 | False    |
| 25 | Mediapipe     | entire face   | (Cached (300W) with ethnicity) filtered using 'white_ethnicity'  |          0.601896 |               0        | TestDiff | NME_mean |   -0.2469      |           0 | True     |
| 26 | Mediapipe     | entire face   | (Cached (300W) with ethnicity) filtered using 'latino_ethnicity' |          0.637554 |               0        | TestDiff | NME_mean |    0.530683    |           0 | False    |