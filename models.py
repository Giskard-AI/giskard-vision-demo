from giskard_vision.landmark_detection.models.base import FaceLandmarksModelBase
import mediapipe as mp
import numpy as np

model_path = "face_landmarker.task"


BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path), running_mode=VisionRunningMode.IMAGE
)

# index of the landmarks to match the dlib landmarks
DLIB_MASK = [
    162,
    234,
    93,
    58,
    172,
    136,
    149,
    148,
    152,
    377,
    378,
    365,
    397,
    288,
    323,
    454,
    389,
    71,
    63,
    105,
    66,
    107,
    336,
    296,
    334,
    293,
    301,
    168,
    197,
    5,
    4,
    75,
    97,
    2,
    326,
    305,
    33,
    160,
    158,
    133,
    153,
    144,
    362,
    385,
    387,
    263,
    373,
    380,
    61,
    39,
    37,
    0,
    267,
    269,
    291,
    405,
    314,
    17,
    84,
    181,
    78,
    82,
    13,
    312,
    308,
    317,
    14,
    87,
]

class MediapipeWrapper(FaceLandmarksModelBase):

    def __init__(self):
        super().__init__(n_landmarks=68, n_dimensions=2, name="Mediapipe")
        self.mp_face_mesh = mp.solutions.face_mesh
        self.landmarker = FaceLandmarker.create_from_options(options)

    def predict_image(self, image):
        image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        results = self.landmarker.detect(image)
        landmarks_array = np.array([[l.x, l.y] for landmarks in results.face_landmarks for l in landmarks], np.float32)
        return landmarks_array[DLIB_MASK]
