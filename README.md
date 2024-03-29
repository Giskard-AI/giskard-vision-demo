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
|  6 | cropped on left half     | FaceAlignment | ✓                    |                         | ✓                            |
|  7 | cropped on left half     | Mediapipe     |                      | ✓                       |                              |
|  8 | cropped on left half     | OpenCV        |                      |                         |                              |
|  9 | cropped on upper half    | FaceAlignment |                      |                         | ✓                            |
| 10 | cropped on upper half    | Mediapipe     |                      | ✓                       |                              |
| 11 | cropped on upper half    | OpenCV        | ✓                    |                         |                              |
| 12 | latino_ethnicity         | FaceAlignment |                      |                         |                              |
| 13 | latino_ethnicity         | Mediapipe     |                      | ✓                       |                              |
| 14 | latino_ethnicity         | OpenCV        | ✓                    |                         | ✓                            |
| 15 | negative_roll            | FaceAlignment | ✓                    |                         | ✓                            |
| 16 | negative_roll            | Mediapipe     |                      | ✓                       |                              |
| 17 | negative_roll            | OpenCV        |                      |                         |                              |
| 18 | positive_roll            | FaceAlignment |                      |                         | ✓                            |
| 19 | positive_roll            | Mediapipe     | ✓                    | ✓                       |                              |
| 20 | positive_roll            | OpenCV        |                      |                         |                              |
| 21 | resized with ratios: 0.5 | FaceAlignment | ✓                    |                         | ✓                            |
| 22 | resized with ratios: 0.5 | Mediapipe     |                      | ✓                       |                              |
| 23 | resized with ratios: 0.5 | OpenCV        |                      |                         |                              |
| 24 | white_ethnicity          | FaceAlignment | ✓                    |                         | ✓                            |
| 25 | white_ethnicity          | Mediapipe     |                      | ✓                       |                              |
| 26 | white_ethnicity          | OpenCV        |                      |                         |                              | 
# Full Report
|    | criteria                 | model         | test     | metric   |   metric_value | Best(metric_value)   |   prediction_time | Best(prediction_time)   |   prediction_fail_rate | Best(prediction_fail_rate)   |   group |
|---:|:-------------------------|:--------------|:---------|:---------|---------------:|:---------------------|------------------:|:------------------------|-----------------------:|:-----------------------------|--------:|
|  0 | altered color            | FaceAlignment | TestDiff | NME_mean |     -0.186222  |                      |         106.932   |                         |              0.02      | ✓                            |       0 |
|  1 | altered color            | Mediapipe     | TestDiff | NME_mean |     -0.224704  | ✓                    |           8.8242  | ✓                       |              0.79      |                              |       0 |
|  2 | altered color            | OpenCV        | TestDiff | NME_mean |      0.244796  |                      |          55.8885  |                         |              0.14      |                              |       0 |
|  3 | blurred                  | FaceAlignment | TestDiff | NME_mean |     -0.0451077 | ✓                    |         111.341   |                         |              0.04      | ✓                            |       1 |
|  4 | blurred                  | Mediapipe     | TestDiff | NME_mean |      0.0566332 |                      |          10.2652  | ✓                       |              0.09      |                              |       1 |
|  5 | blurred                  | OpenCV        | TestDiff | NME_mean |      0.0862813 |                      |          52.3313  |                         |              0.12      |                              |       1 |
|  6 | cropped on left half     | FaceAlignment | TestDiff | NME_mean |     -0.553663  | ✓                    |          81.3858  |                         |              0.820441  | ✓                            |       2 |
|  7 | cropped on left half     | Mediapipe     | TestDiff | NME_mean |     -0.170099  |                      |           8.82618 | ✓                       |              0.951029  |                              |       2 |
|  8 | cropped on left half     | OpenCV        | TestDiff | NME_mean |     -0.0978757 |                      |          39.8459  |                         |              0.825882  |                              |       2 |
|  9 | cropped on upper half    | FaceAlignment | TestDiff | NME_mean |     -0.541586  |                      |          76.7908  |                         |              0.782941  | ✓                            |       3 |
| 10 | cropped on upper half    | Mediapipe     | TestDiff | NME_mean |     -0.2261    |                      |           8.88667 | ✓                       |              0.941765  |                              |       3 |
| 11 | cropped on upper half    | OpenCV        | TestDiff | NME_mean |     -0.651753  | ✓                    |          38.5212  |                         |              0.978824  |                              |       3 |
| 12 | latino_ethnicity         | FaceAlignment | TestDiff | NME_mean |      0.371225  |                      |          56.255   |                         |              0.142857  |                              |       4 |
| 13 | latino_ethnicity         | Mediapipe     | TestDiff | NME_mean |      0.038642  |                      |           5.36608 | ✓                       |              0.285714  |                              |       4 |
| 14 | latino_ethnicity         | OpenCV        | TestDiff | NME_mean |     -0.738433  | ✓                    |          31.7009  |                         |              0         | ✓                            |       4 |
| 15 | negative_roll            | FaceAlignment | TestDiff | NME_mean |     -0.576123  | ✓                    |          77.1264  |                         |              0.0416667 | ✓                            |       5 |
| 16 | negative_roll            | Mediapipe     | TestDiff | NME_mean |     -0.0123974 |                      |           6.85317 | ✓                       |              0.0833333 |                              |       5 |
| 17 | negative_roll            | OpenCV        | TestDiff | NME_mean |     -0.551934  |                      |          38.7747  |                         |              0.125     |                              |       5 |
| 18 | positive_roll            | FaceAlignment | TestDiff | NME_mean |      0.54085   |                      |          80.6734  |                         |              0.0576923 | ✓                            |       6 |
| 19 | positive_roll            | Mediapipe     | TestDiff | NME_mean |      0.0147429 | ✓                    |           7.70982 | ✓                       |              0.288462  |                              |       6 |
| 20 | positive_roll            | OpenCV        | TestDiff | NME_mean |      0.386019  |                      |          46.4338  |                         |              0.192308  |                              |       6 |
| 21 | resized with ratios: 0.5 | FaceAlignment | TestDiff | NME_mean |      0.0185174 | ✓                    |         106.051   |                         |              0.04      | ✓                            |       7 |
| 22 | resized with ratios: 0.5 | Mediapipe     | TestDiff | NME_mean |      0.0358656 |                      |           9.9396  | ✓                       |              0.12      |                              |       7 |
| 23 | resized with ratios: 0.5 | OpenCV        | TestDiff | NME_mean |      0.292944  |                      |          38.5987  |                         |              0.18      |                              |       7 |
| 24 | white_ethnicity          | FaceAlignment | TestDiff | NME_mean |     -0.604868  | ✓                    |          79.9887  |                         |              0.0384615 | ✓                            |       8 |
| 25 | white_ethnicity          | Mediapipe     | TestDiff | NME_mean |      0.0260865 |                      |           7.74814 | ✓                       |              0.173077  |                              |       8 |
| 26 | white_ethnicity          | OpenCV        | TestDiff | NME_mean |     -0.495647  |                      |          43.0677  |                         |              0.0769231 |                              |       8 |