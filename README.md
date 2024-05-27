# Facial Landmark Detection Demo 

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
      <th>300W</th>
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
      <th>altered color</th>
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
      <td>✓</td>
      <td></td>
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
      <td>✓</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

## Full Report
|    | criteria                 | model         | test   | metric   |   metric_value | Best(metric_value)   |   prediction_time | Best(prediction_time)   |   prediction_fail_rate | Best(prediction_fail_rate)   |
|---:|:-------------------------|:--------------|:-------|:---------|---------------:|:---------------------|------------------:|:------------------------|-----------------------:|:-----------------------------|
|  0 | 300W                     | FaceAlignment | Test   | NME_mean |      0.214453  |                      |         64.1483   |                         |              0.05      | ✓                            |
|  1 | 300W                     | Mediapipe     | Test   | NME_mean |      3.08786   |                      |          4.93624  | ✓                       |              0.19      |                              |
|  2 | 300W                     | OpenCV        | Test   | NME_mean |      0.195668  | ✓                    |         29.9249   |                         |              0.16      |                              |
|  3 | altered color            | FaceAlignment | Test   | NME_mean |      0.174517  | ✓                    |         58.1809   |                         |              0.02      | ✓                            |
|  4 | altered color            | Mediapipe     | Test   | NME_mean |      2.5315    |                      |          3.96894  | ✓                       |              0.79      |                              |
|  5 | altered color            | OpenCV        | Test   | NME_mean |      0.243567  |                      |         28.037    |                         |              0.14      |                              |
|  6 | blurred                  | FaceAlignment | Test   | NME_mean |      0.204779  | ✓                    |         63.3339   |                         |              0.04      | ✓                            |
|  7 | blurred                  | Mediapipe     | Test   | NME_mean |      3.26273   |                      |          5.59357  | ✓                       |              0.09      |                              |
|  8 | blurred                  | OpenCV        | Test   | NME_mean |      0.331916  |                      |         24.6266   |                         |              0.12      |                              |
|  9 | cropped on left half     | FaceAlignment | Test   | NME_mean |      0.0950334 | ✓                    |         22.3192   |                         |              0.820441  | ✓                            |
| 10 | cropped on left half     | Mediapipe     | Test   | NME_mean |      2.39931   |                      |          3.95156  | ✓                       |              0.951029  |                              |
| 11 | cropped on left half     | OpenCV        | Test   | NME_mean |      0.17521   |                      |         11.1745   |                         |              0.825882  |                              |
| 12 | cropped on upper half    | FaceAlignment | Test   | NME_mean |      0.0948426 |                      |         26.6648   |                         |              0.782941  | ✓                            |
| 13 | cropped on upper half    | Mediapipe     | Test   | NME_mean |      2.19568   |                      |          4.02357  | ✓                       |              0.941765  |                              |
| 14 | cropped on upper half    | OpenCV        | Test   | NME_mean |      0.0519043 | ✓                    |         10.7939   |                         |              0.978824  |                              |
| 15 | latino_ethnicity         | FaceAlignment | Test   | NME_mean |      0.294063  |                      |          4.06596  |                         |              0.142857  |                              |
| 16 | latino_ethnicity         | Mediapipe     | Test   | NME_mean |      3.20718   |                      |          0.469689 | ✓                       |              0.285714  |                              |
| 17 | latino_ethnicity         | OpenCV        | Test   | NME_mean |      0.0664585 | ✓                    |          3.8904   |                         |              0         | ✓                            |
| 18 | negative_roll            | FaceAlignment | Test   | NME_mean |      0.0909015 | ✓                    |         25.7093   |                         |              0.0416667 | ✓                            |
| 19 | negative_roll            | Mediapipe     | Test   | NME_mean |      3.04958   |                      |          2.03313  | ✓                       |              0.0833333 |                              |
| 20 | negative_roll            | OpenCV        | Test   | NME_mean |      0.0968505 |                      |         10.9992   |                         |              0.125     |                              |
| 21 | positive_roll            | FaceAlignment | Test   | NME_mean |      0.330439  | ✓                    |         30.441    |                         |              0.0576923 | ✓                            |
| 22 | positive_roll            | Mediapipe     | Test   | NME_mean |      3.13338   |                      |          2.88912  | ✓                       |              0.288462  |                              |
| 23 | positive_roll            | OpenCV        | Test   | NME_mean |      0.411305  |                      |         17.3002   |                         |              0.192308  |                              |
| 24 | resized with ratios: 0.5 | FaceAlignment | Test   | NME_mean |      0.218424  | ✓                    |         59.4045   |                         |              0.04      | ✓                            |
| 25 | resized with ratios: 0.5 | Mediapipe     | Test   | NME_mean |      3.19861   |                      |          5.10067  | ✓                       |              0.12      |                              |
| 26 | resized with ratios: 0.5 | OpenCV        | Test   | NME_mean |      0.252987  |                      |         10.9042   |                         |              0.18      |                              |
| 27 | white_ethnicity          | FaceAlignment | Test   | NME_mean |      0.084737  | ✓                    |         29.2241   |                         |              0.0384615 | ✓                            |
| 28 | white_ethnicity          | Mediapipe     | Test   | NME_mean |      3.16841   |                      |          2.83826  | ✓                       |              0.173077  |                              |
| 29 | white_ethnicity          | OpenCV        | Test   | NME_mean |      0.0986856 |                      |         15.3149   |                         |              0.0769231 |                              |
