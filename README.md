# Facial Landmark detection

This is a CI/CD example of an evaluation report produced by `giskard-vision` which compares a set of facial landmark detection models based on the following criteria:

- Performance on partial and entire facial parts
- Performance on images containing faces with different head poses (estimated with `6DRepNet`: https://github.com/thohemp/6DRepNet)
- Performance on images containing people from different ethnicities (estimated with `DeepFace`: https://github.com/serengil/deepface)
- Robustness against image perturbations like blurring, resizing, recoloring (performed by `opencv`: https://github.com/opencv/opencv)

Here're the results of the latest run:
|    | model         | facial_part   | dataloader                                                       |   prediction_time |   prediction_fail_rate | test     | metric   |   metric_value |   threshold | passed   |
|---:|:--------------|:--------------|:-----------------------------------------------------------------|------------------:|-----------------------:|:---------|:---------|---------------:|------------:|:---------|
|  0 | FaceAlignment | left half     | 300W cropped on left half                                        |          77.2777  |               0.564706 | TestDiff | NME_mean |     0.656253   |        -0.1 | False    |
|  1 | FaceAlignment | upper half    | 300W cropped on upper half                                       |          97.4043  |               0.470588 | TestDiff | NME_mean |     0.223175   |        -0.1 | False    |
|  2 | FaceAlignment | entire face   | 300W resizing with ratios: 0.5                                   |         100.542   |               0        | TestDiff | NME_mean |     0.0114276  |        -0.1 | False    |
|  3 | FaceAlignment | entire face   | 300W altered with color mode 7                                   |         142.454   |               0        | TestDiff | NME_mean |     0.00672821 |        -0.1 | False    |
|  4 | FaceAlignment | entire face   | 300W blurred                                                     |         143.332   |               0        | TestDiff | NME_mean |     0.00950801 |        -0.1 | False    |
|  5 | FaceAlignment | entire face   | (Cached (300W) with head-pose) filtered using 'positive_roll'    |          78.9935  |               0        | TestDiff | NME_mean |    -0.146944   |        -0.1 | True     |
|  6 | FaceAlignment | entire face   | (Cached (300W) with head-pose) filtered using 'negative_roll'    |         134.409   |               0        | TestDiff | NME_mean |     0.036736   |        -0.1 | False    |
|  7 | FaceAlignment | entire face   | (Cached (300W) with ethnicity) filtered using 'white_ethnicity'  |         127.485   |               0        | TestDiff | NME_mean |    -0.0520713  |        -0.1 | False    |
|  8 | FaceAlignment | entire face   | (Cached (300W) with ethnicity) filtered using 'latino_ethnicity' |          90.3276  |               0        | TestDiff | NME_mean |     0.208285   |        -0.1 | False    |
|  9 | OpenCV        | left half     | 300W cropped on left half                                        |           6.95979 |               0.564706 | TestDiff | NME_mean |     0.644057   |        -0.1 | False    |
| 10 | OpenCV        | upper half    | 300W cropped on upper half                                       |           8.30021 |               0.682353 | TestDiff | NME_mean |    -0.0402161  |        -0.1 | False    |
| 11 | OpenCV        | entire face   | 300W resizing with ratios: 0.5                                   |           7.17906 |               0        | TestDiff | NME_mean |     0.079876   |        -0.1 | False    |
| 12 | OpenCV        | entire face   | 300W altered with color mode 7                                   |          11.3042  |               0        | TestDiff | NME_mean |    -0.0013471  |        -0.1 | False    |
| 13 | OpenCV        | entire face   | 300W blurred                                                     |           7.69256 |               0        | TestDiff | NME_mean |     0.103017   |        -0.1 | False    |
| 14 | OpenCV        | entire face   | (Cached (300W) with head-pose) filtered using 'positive_roll'    |           4.04742 |               0        | TestDiff | NME_mean |    -0.0779265  |        -0.1 | False    |
| 15 | OpenCV        | entire face   | (Cached (300W) with head-pose) filtered using 'negative_roll'    |           7.1806  |               0        | TestDiff | NME_mean |     0.0194816  |        -0.1 | False    |
| 16 | OpenCV        | entire face   | (Cached (300W) with ethnicity) filtered using 'white_ethnicity'  |           6.75093 |               0        | TestDiff | NME_mean |    -0.196134   |        -0.1 | True     |
| 17 | OpenCV        | entire face   | (Cached (300W) with ethnicity) filtered using 'latino_ethnicity' |           4.33144 |               0        | TestDiff | NME_mean |     0.784538   |        -0.1 | False    |