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
      <td></td>
      <td></td>
      <td>✓</td>
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
      <td>✓</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>latino_ethnicity</th>
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
      <th>negative_roll</th>
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
      <td></td>
      <td>✓</td>
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
      <td>✓</td>
      <td></td>
    </tr>
  </tbody>
</table> 
# Full Report
|    | criteria                 | model         | test     | metric   |   metric_value | Best(metric_value)   |   prediction_time | Best(prediction_time)   |   prediction_fail_rate | Best(prediction_fail_rate)   |
|---:|:-------------------------|:--------------|:---------|:---------|---------------:|:---------------------|------------------:|:------------------------|-----------------------:|:-----------------------------|
|  0 | altered color            | FaceAlignment | TestDiff | NME_mean |   -0.0186375   |                      |          4.97991  |                         |               0        | ✓                            |
|  1 | altered color            | Mediapipe     | TestDiff | NME_mean |   -0.32462     | ✓                    |          0.357795 | ✓                       |               0.8      |                              |
|  2 | altered color            | OpenCV        | TestDiff | NME_mean |   -0.0013471   |                      |          1.9227   |                         |               0        |                              |
|  3 | blurred                  | FaceAlignment | TestDiff | NME_mean |   -0.0205122   | ✓                    |          4.98975  |                         |               0        | ✓                            |
|  4 | blurred                  | Mediapipe     | TestDiff | NME_mean |    1.24002e-06 |                      |          0.431742 | ✓                       |               0        |                              |
|  5 | blurred                  | OpenCV        | TestDiff | NME_mean |    0.103017    |                      |          1.8207   |                         |               0        |                              |
|  6 | cropped on left half     | FaceAlignment | TestDiff | NME_mean |    0.168412    | ✓                    |         10.6874   |                         |               0.782353 |                              |
|  7 | cropped on left half     | Mediapipe     | TestDiff | NME_mean |  nan           |                      |          0.3613   | ✓                       |               1        |                              |
|  8 | cropped on left half     | OpenCV        | TestDiff | NME_mean |    0.644057    |                      |          1.3913   |                         |               0.673529 | ✓                            |
|  9 | cropped on upper half    | FaceAlignment | TestDiff | NME_mean |   -0.0915932   | ✓                    |          4.05533  |                         |               0.682353 | ✓                            |
| 10 | cropped on upper half    | Mediapipe     | TestDiff | NME_mean |  nan           |                      |          0.343592 | ✓                       |               1        |                              |
| 11 | cropped on upper half    | OpenCV        | TestDiff | NME_mean |   -0.0402161   |                      |          1.3646   |                         |               0.894118 |                              |
| 12 | latino_ethnicity         | FaceAlignment | TestDiff | NME_mean |   -0.187597    | ✓                    |          3.01258  |                         |               0        | ✓                            |
| 13 | latino_ethnicity         | Mediapipe     | TestDiff | NME_mean |    0.530683    |                      |          0.255045 | ✓                       |               0        |                              |
| 14 | latino_ethnicity         | OpenCV        | TestDiff | NME_mean |    0.784538    |                      |          1.15346  |                         |               0        |                              |
| 15 | negative_roll            | FaceAlignment | TestDiff | NME_mean |    0.0449532   |                      |          4.48916  |                         |               0        | ✓                            |
| 16 | negative_roll            | Mediapipe     | TestDiff | NME_mean |    0.08136     |                      |          0.388863 | ✓                       |               0        |                              |
| 17 | negative_roll            | OpenCV        | TestDiff | NME_mean |    0.0194816   | ✓                    |          1.84397  |                         |               0        |                              |
| 18 | positive_roll            | FaceAlignment | TestDiff | NME_mean |   -0.179813    |                      |          2.93843  |                         |               0        | ✓                            |
| 19 | positive_roll            | Mediapipe     | TestDiff | NME_mean |   -0.32544     | ✓                    |          0.241261 | ✓                       |               0        |                              |
| 20 | positive_roll            | OpenCV        | TestDiff | NME_mean |   -0.0779265   |                      |          1.06117  |                         |               0        |                              |
| 21 | resized with ratios: 0.5 | FaceAlignment | TestDiff | NME_mean |    0.00961674  |                      |          4.92737  |                         |               0        | ✓                            |
| 22 | resized with ratios: 0.5 | Mediapipe     | TestDiff | NME_mean |   -0.0012767   | ✓                    |          0.425038 | ✓                       |               0        |                              |
| 23 | resized with ratios: 0.5 | OpenCV        | TestDiff | NME_mean |    0.079876    |                      |          1.35077  |                         |               0        |                              |
| 24 | white_ethnicity          | FaceAlignment | TestDiff | NME_mean |    0.0985756   |                      |          3.95138  |                         |               0        | ✓                            |
| 25 | white_ethnicity          | Mediapipe     | TestDiff | NME_mean |   -0.2469      | ✓                    |          0.335338 | ✓                       |               0        |                              |
| 26 | white_ethnicity          | OpenCV        | TestDiff | NME_mean |   -0.168421    |                      |          1.58073  |                         |               0        |                              |