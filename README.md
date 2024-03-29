# Facial Landmark detection

This is a CI/CD example of an evaluation report produced by `giskard-vision` which compares a set of facial landmark detection models based on the following criteria:

- Performance on partial and entire facial parts
- Performance on images containing faces with different head poses (estimated with `6DRepNet`: https://github.com/thohemp/6DRepNet)
- Performance on images containing people from different ethnicities (estimated with `DeepFace`: https://github.com/serengil/deepface)
- Robustness against image perturbations like blurring, resizing, recoloring (performed by `opencv`: https://github.com/opencv/opencv)

## Summary of the latest run:
|    | criteria                 | model         | Best(metric_value)   | Best(prediction_time)   | Best(prediction_fail_rate)   |
|---:|:-------------------------|:--------------|:---------------------|:------------------------|:-----------------------------|
|  0 | altered color            | FaceAlignment |                      |                         | ✓                            |
|  1 | altered color            | Mediapipe     | ✓                    | ✓                       |                              |
|  2 | altered color            | OpenCV        |                      |                         |                              |
|  3 | blurred                  | FaceAlignment | ✓                    |                         | ✓                            |
|  4 | blurred                  | Mediapipe     |                      | ✓                       |                              |
|  5 | blurred                  | OpenCV        |                      |                         |                              |
|  6 | cropped on left half     | FaceAlignment | ✓                    |                         |                              |
|  7 | cropped on left half     | Mediapipe     |                      | ✓                       |                              |
|  8 | cropped on left half     | OpenCV        |                      |                         | ✓                            |
|  9 | cropped on upper half    | FaceAlignment | ✓                    |                         | ✓                            |
| 10 | cropped on upper half    | Mediapipe     |                      | ✓                       |                              |
| 11 | cropped on upper half    | OpenCV        |                      |                         |                              |
| 12 | latino_ethnicity         | FaceAlignment | ✓                    |                         | ✓                            |
| 13 | latino_ethnicity         | Mediapipe     |                      | ✓                       |                              |
| 14 | latino_ethnicity         | OpenCV        |                      |                         |                              |
| 15 | negative_roll            | FaceAlignment |                      |                         | ✓                            |
| 16 | negative_roll            | Mediapipe     |                      | ✓                       |                              |
| 17 | negative_roll            | OpenCV        | ✓                    |                         |                              |
| 18 | positive_roll            | FaceAlignment |                      |                         | ✓                            |
| 19 | positive_roll            | Mediapipe     | ✓                    | ✓                       |                              |
| 20 | positive_roll            | OpenCV        |                      |                         |                              |
| 21 | resized with ratios: 0.5 | FaceAlignment |                      |                         | ✓                            |
| 22 | resized with ratios: 0.5 | Mediapipe     | ✓                    | ✓                       |                              |
| 23 | resized with ratios: 0.5 | OpenCV        |                      |                         |                              |
| 24 | white_ethnicity          | FaceAlignment |                      |                         | ✓                            |
| 25 | white_ethnicity          | Mediapipe     | ✓                    | ✓                       |                              |
| 26 | white_ethnicity          | OpenCV        |                      |                         |                              | 
# Full Report
|    | criteria                 | model         | test     | metric   |   metric_value | Best(metric_value)   |   prediction_time | Best(prediction_time)   |   prediction_fail_rate | Best(prediction_fail_rate)   |   group |
|---:|:-------------------------|:--------------|:---------|:---------|---------------:|:---------------------|------------------:|:------------------------|-----------------------:|:-----------------------------|--------:|
|  0 | altered color            | FaceAlignment | TestDiff | NME_mean |   -0.0186375   |                      |          5.27362  |                         |               0        | ✓                            |       0 |
|  1 | altered color            | Mediapipe     | TestDiff | NME_mean |   -0.32547     | ✓                    |          0.367082 | ✓                       |               0.8      |                              |       0 |
|  2 | altered color            | OpenCV        | TestDiff | NME_mean |   -0.0013471   |                      |          1.96542  |                         |               0        |                              |       0 |
|  3 | blurred                  | FaceAlignment | TestDiff | NME_mean |   -0.0205122   | ✓                    |          5.41026  |                         |               0        | ✓                            |       1 |
|  4 | blurred                  | Mediapipe     | TestDiff | NME_mean |    1.24002e-06 |                      |          0.458288 | ✓                       |               0        |                              |       1 |
|  5 | blurred                  | OpenCV        | TestDiff | NME_mean |    0.103017    |                      |          1.85182  |                         |               0        |                              |       1 |
|  6 | cropped on left half     | FaceAlignment | TestDiff | NME_mean |    0.168412    | ✓                    |         11.1869   |                         |               0.782353 |                              |       2 |
|  7 | cropped on left half     | Mediapipe     | TestDiff | NME_mean |  nan           |                      |          0.382515 | ✓                       |               1        |                              |       2 |
|  8 | cropped on left half     | OpenCV        | TestDiff | NME_mean |    0.644057    |                      |          1.47775  |                         |               0.673529 | ✓                            |       2 |
|  9 | cropped on upper half    | FaceAlignment | TestDiff | NME_mean |   -0.0915932   | ✓                    |          4.26845  |                         |               0.682353 | ✓                            |       3 |
| 10 | cropped on upper half    | Mediapipe     | TestDiff | NME_mean |  nan           |                      |          0.359448 | ✓                       |               1        |                              |       3 |
| 11 | cropped on upper half    | OpenCV        | TestDiff | NME_mean |   -0.0402161   |                      |          1.40859  |                         |               0.894118 |                              |       3 |
| 12 | latino_ethnicity         | FaceAlignment | TestDiff | NME_mean |   -0.187597    | ✓                    |          3.15358  |                         |               0        | ✓                            |       4 |
| 13 | latino_ethnicity         | Mediapipe     | TestDiff | NME_mean |    0.530683    |                      |          0.268342 | ✓                       |               0        |                              |       4 |
| 14 | latino_ethnicity         | OpenCV        | TestDiff | NME_mean |    0.784538    |                      |          1.18086  |                         |               0        |                              |       4 |
| 15 | negative_roll            | FaceAlignment | TestDiff | NME_mean |    0.0449532   |                      |          4.82363  |                         |               0        | ✓                            |       5 |
| 16 | negative_roll            | Mediapipe     | TestDiff | NME_mean |    0.08136     |                      |          0.407336 | ✓                       |               0        |                              |       5 |
| 17 | negative_roll            | OpenCV        | TestDiff | NME_mean |    0.0194816   | ✓                    |          1.88197  |                         |               0        |                              |       5 |
| 18 | positive_roll            | FaceAlignment | TestDiff | NME_mean |   -0.179813    |                      |          3.19019  |                         |               0        | ✓                            |       6 |
| 19 | positive_roll            | Mediapipe     | TestDiff | NME_mean |   -0.32544     | ✓                    |          0.258157 | ✓                       |               0        |                              |       6 |
| 20 | positive_roll            | OpenCV        | TestDiff | NME_mean |   -0.0779265   |                      |          1.08636  |                         |               0        |                              |       6 |
| 21 | resized with ratios: 0.5 | FaceAlignment | TestDiff | NME_mean |    0.00961674  |                      |          8.12542  |                         |               0        | ✓                            |       7 |
| 22 | resized with ratios: 0.5 | Mediapipe     | TestDiff | NME_mean |   -0.0012767   | ✓                    |          0.445029 | ✓                       |               0        |                              |       7 |
| 23 | resized with ratios: 0.5 | OpenCV        | TestDiff | NME_mean |    0.079876    |                      |          1.38343  |                         |               0        |                              |       7 |
| 24 | white_ethnicity          | FaceAlignment | TestDiff | NME_mean |    0.0985756   |                      |          4.30445  |                         |               0        | ✓                            |       8 |
| 25 | white_ethnicity          | Mediapipe     | TestDiff | NME_mean |   -0.2469      | ✓                    |          0.352954 | ✓                       |               0        |                              |       8 |
| 26 | white_ethnicity          | OpenCV        | TestDiff | NME_mean |   -0.168421    |                      |          1.6172   |                         |               0        |                              |       8 |