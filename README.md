# Facial Landmark detection

This is a CI/CD example of an evaluation report produced by `giskard-vision` which compares a set of facial landmark detection models based on the following criteria:

- Performance on partial and entire facial parts
- Performance on images containing faces with different head poses (estimated with `6DRepNet`: https://github.com/thohemp/6DRepNet)
- Performance on images containing people from different ethnicities (estimated with `DeepFace`: https://github.com/serengil/deepface)
- Robustness against image perturbations like blurring, resizing, recoloring (performed by `opencv`: https://github.com/opencv/opencv)

## Summary of the latest run:
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">Best(prediction_time)</th>
      <th colspan="3" halign="left">Best(prediction_fail_rate)</th>
      <th colspan="3" halign="left">Best(metric_value)</th>
    </tr>
    <tr>
      <th>model</th>
      <th>FaceAlignment</th>
      <th>Mediapipe</th>
      <th>OpenCV</th>
      <th>FaceAlignment</th>
      <th>Mediapipe</th>
      <th>OpenCV</th>
      <th>FaceAlignment</th>
      <th>Mediapipe</th>
      <th>OpenCV</th>
    </tr>
    <tr>
      <th>criteria</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>altered color</th>
      <td></td>
      <td>✓</td>
      <td></td>
      <td>✓</td>
      <td></td>
      <td></td>
      <td></td>
      <td>✓</td>
      <td></td>
    </tr>
    <tr>
      <th>blurred</th>
      <td></td>
      <td>✓</td>
      <td></td>
      <td>✓</td>
      <td></td>
      <td></td>
      <td>✓</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>cropped on left half</th>
      <td></td>
      <td>✓</td>
      <td></td>
      <td>✓</td>
      <td></td>
      <td></td>
      <td>✓</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>cropped on upper half</th>
      <td></td>
      <td>✓</td>
      <td></td>
      <td>✓</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>✓</td>
    </tr>
    <tr>
      <th>latino_ethnicity</th>
      <td></td>
      <td>✓</td>
      <td></td>
      <td></td>
      <td></td>
      <td>✓</td>
      <td></td>
      <td></td>
      <td>✓</td>
    </tr>
    <tr>
      <th>negative_roll</th>
      <td></td>
      <td>✓</td>
      <td></td>
      <td>✓</td>
      <td></td>
      <td></td>
      <td>✓</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>positive_roll</th>
      <td></td>
      <td>✓</td>
      <td></td>
      <td>✓</td>
      <td></td>
      <td></td>
      <td></td>
      <td>✓</td>
      <td></td>
    </tr>
    <tr>
      <th>resized with ratios: 0.5</th>
      <td></td>
      <td>✓</td>
      <td></td>
      <td>✓</td>
      <td></td>
      <td></td>
      <td>✓</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>white_ethnicity</th>
      <td></td>
      <td>✓</td>
      <td></td>
      <td>✓</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>✓</td>
    </tr>
  </tbody>
</table>

## Full Report
|    | criteria                 | model         | test     | metric   |   metric_value | Best(metric_value)   |   prediction_time | Best(prediction_time)   |   prediction_fail_rate | Best(prediction_fail_rate)   |
|---:|:-------------------------|:--------------|:---------|:---------|---------------:|:---------------------|------------------:|:------------------------|-----------------------:|:-----------------------------|
|  0 | altered color            | FaceAlignment | TestDiff | NME_mean |     -0.186222  |                      |         104.175   |                         |              0.02      | ✓                            |
|  1 | altered color            | Mediapipe     | TestDiff | NME_mean |     -0.2253    | ✓                    |           8.56092 | ✓                       |              0.8       |                              |
|  2 | altered color            | OpenCV        | TestDiff | NME_mean |      0.244796  |                      |          54.6988  |                         |              0.14      |                              |
|  3 | blurred                  | FaceAlignment | TestDiff | NME_mean |     -0.0451077 | ✓                    |         109.475   |                         |              0.04      | ✓                            |
|  4 | blurred                  | Mediapipe     | TestDiff | NME_mean |      0.0566332 |                      |          10.1168  | ✓                       |              0.09      |                              |
|  5 | blurred                  | OpenCV        | TestDiff | NME_mean |      0.410555  |                      |          51.1825  |                         |              0.12      |                              |
|  6 | cropped on left half     | FaceAlignment | TestDiff | NME_mean |     -0.553663  | ✓                    |          79.8703  |                         |              0.820441  | ✓                            |
|  7 | cropped on left half     | Mediapipe     | TestDiff | NME_mean |     -0.170099  |                      |           8.61944 | ✓                       |              0.951029  |                              |
|  8 | cropped on left half     | OpenCV        | TestDiff | NME_mean |     -0.0978757 |                      |          39.5248  |                         |              0.825882  |                              |
|  9 | cropped on upper half    | FaceAlignment | TestDiff | NME_mean |     -0.541586  |                      |          75.5163  |                         |              0.782941  | ✓                            |
| 10 | cropped on upper half    | Mediapipe     | TestDiff | NME_mean |     -0.2261    |                      |           8.67485 | ✓                       |              0.941765  |                              |
| 11 | cropped on upper half    | OpenCV        | TestDiff | NME_mean |     -0.720575  | ✓                    |          37.8815  |                         |              0.978824  |                              |
| 12 | latino_ethnicity         | FaceAlignment | TestDiff | NME_mean |      0.371225  |                      |          56.0924  |                         |              0.142857  |                              |
| 13 | latino_ethnicity         | Mediapipe     | TestDiff | NME_mean |      0.038642  |                      |           5.24106 | ✓                       |              0.285714  |                              |
| 14 | latino_ethnicity         | OpenCV        | TestDiff | NME_mean |     -0.66035   | ✓                    |          31.2278  |                         |              0         | ✓                            |
| 15 | negative_roll            | FaceAlignment | TestDiff | NME_mean |     -0.576123  | ✓                    |          74.778   |                         |              0.0416667 | ✓                            |
| 16 | negative_roll            | Mediapipe     | TestDiff | NME_mean |     -0.0123974 |                      |           6.75812 | ✓                       |              0.0833333 |                              |
| 17 | negative_roll            | OpenCV        | TestDiff | NME_mean |     -0.505026  |                      |          38.0079  |                         |              0.125     |                              |
| 18 | positive_roll            | FaceAlignment | TestDiff | NME_mean |      0.54085   |                      |          79.4839  |                         |              0.0576923 | ✓                            |
| 19 | positive_roll            | Mediapipe     | TestDiff | NME_mean |      0.0147429 | ✓                    |           7.58607 | ✓                       |              0.288462  |                              |
| 20 | positive_roll            | OpenCV        | TestDiff | NME_mean |      0.505026  |                      |          44.1633  |                         |              0.192308  |                              |
| 21 | resized with ratios: 0.5 | FaceAlignment | TestDiff | NME_mean |      0.0185174 | ✓                    |         106.595   |                         |              0.04      | ✓                            |
| 22 | resized with ratios: 0.5 | Mediapipe     | TestDiff | NME_mean |      0.0358656 |                      |           9.7031  | ✓                       |              0.12      |                              |
| 23 | resized with ratios: 0.5 | OpenCV        | TestDiff | NME_mean |      0.292944  |                      |          38.0669  |                         |              0.18      |                              |
| 24 | white_ethnicity          | FaceAlignment | TestDiff | NME_mean |     -0.604868  |                      |          78.4921  |                         |              0.0384615 | ✓                            |
| 25 | white_ethnicity          | Mediapipe     | TestDiff | NME_mean |      0.0260865 |                      |           7.55602 | ✓                       |              0.173077  |                              |
| 26 | white_ethnicity          | OpenCV        | TestDiff | NME_mean |     -0.611593  | ✓                    |          42.2883  |                         |              0.0769231 |                              |