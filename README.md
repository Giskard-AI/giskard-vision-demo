# Facial Landmark detection

This is a CI/CD example of an evaluation report produced by `giskard-vision` which compares a set of facial landmark detection models based on the following criteria:

- Performance on partial and entire facial parts
- Performance on images containing faces with different head poses (estimated with `6DRepNet`: https://github.com/thohemp/6DRepNet)
- Performance on images containing people from different ethnicities (estimated with `DeepFace`: https://github.com/serengil/deepface)
- Robustness against image perturbations like blurring, resizing, recoloring (performed by `opencv`: https://github.com/opencv/opencv)

Here're the results of the latest run:
|    | model   | facial_part   | dataloader                                                       |   prediction_time |   prediction_fail_rate | test     | metric   |   metric_value |   threshold | passed   |
|---:|:--------|:--------------|:-----------------------------------------------------------------|------------------:|-----------------------:|:---------|:---------|---------------:|------------:|:---------|
|  0 | OpenCV  | left half     | 300W cropped on left half                                        |           41.3459 |              0.646324  | TestDiff | NME_mean |      2.42248   |        -0.1 | False    |
|  1 | OpenCV  | upper half    | 300W cropped on upper half                                       |           75.2639 |              0.740588  | TestDiff | NME_mean |      0.114283  |        -0.1 | False    |
|  2 | OpenCV  | entire face   | 300W resizing with ratios: 0.5                                   |           75.8891 |              0.09      | TestDiff | NME_mean |      0.152531  |        -0.1 | False    |
|  3 | OpenCV  | entire face   | 300W altered with color mode 7                                   |          112.853  |              0.07      | TestDiff | NME_mean |      0.190853  |        -0.1 | False    |
|  4 | OpenCV  | entire face   | 300W blurred                                                     |          103.561  |              0.06      | TestDiff | NME_mean |      0.359308  |        -0.1 | False    |
|  5 | OpenCV  | entire face   | (Cached (300W) with head-pose) filtered using 'positive_roll'    |           85.5028 |              0.0834783 | TestDiff | NME_mean |     -0.0834604 |        -0.1 | False    |
|  6 | OpenCV  | entire face   | (Cached (300W) with head-pose) filtered using 'negative_roll'    |           84.4564 |              0.077037  | TestDiff | NME_mean |      0.0701067 |        -0.1 | False    |
|  7 | OpenCV  | entire face   | (Cached (300W) with ethnicity) filtered using 'white_ethnicity'  |           94.7254 |              0.0694118 | TestDiff | NME_mean |     -0.189798  |        -0.1 | True     |
|  8 | OpenCV  | entire face   | (Cached (300W) with ethnicity) filtered using 'latino_ethnicity' |           63.253  |              0.04      | TestDiff | NME_mean |     -0.0862391 |        -0.1 | False    |