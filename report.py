from face_alignment import FaceAlignment, LandmarksType
from datetime import datetime

from giskard_vision.landmark_detection.dataloaders.loaders import DataLoaderFFHQ, DataLoader300W
from giskard_vision.landmark_detection.dataloaders.wrappers import (
    CroppedDataLoader,
    ResizedDataLoader,
    ColoredDataLoader,
    BlurredDataLoader,
    FilteredDataLoader,
    HeadPoseDataLoader,
    EthnicityDataLoader,
    CachedDataLoader,
)

from giskard_vision.landmark_detection.models.wrappers import OpenCVWrapper, FaceAlignmentWrapper
from giskard_vision.landmark_detection.tests.performance import NMEMean
from giskard_vision.landmark_detection.marks.facial_parts import FacialParts
from giskard_vision.landmark_detection.tests.report import Report

dl_ref = DataLoader300W(dir_path="300W")

# cropping
dl_cropped_left = CroppedDataLoader(dl_ref, part=FacialParts.LEFT_HALF.value)
dl_cropped_upper = CroppedDataLoader(dl_ref, part=FacialParts.UPPER_HALF.value)

# resizing
dl_resized = ResizedDataLoader(dl_ref, scales=0.5)

# coloring
dl_colored = ColoredDataLoader(dl_ref)

# blurring
dl_blurred = BlurredDataLoader(dl_ref)


# head pose filtering
def positive_roll(elt):
    return elt[2]["headPose"]["roll"] > 0


def negative_roll(elt):
    return elt[2]["headPose"]["roll"] < 0


cached_dl = CachedDataLoader(HeadPoseDataLoader(dl_ref), cache_size=None, cache_img=False, cache_marks=False)
dl_positive_roll = FilteredDataLoader(cached_dl, positive_roll)
dl_negative_roll = FilteredDataLoader(cached_dl, negative_roll)


# ethnicity filtering
def white_ethnicity(elt):
    return elt[2]["ethnicity"] == "white"


def latino_ethnicity(elt):
    return elt[2]["ethnicity"] == "latino hispanic"


cached_dl = CachedDataLoader(
    EthnicityDataLoader(dl_ref, ethnicity_map={"indian": "asian"}), cache_size=None, cache_img=False, cache_marks=False
)
dl_white = FilteredDataLoader(cached_dl, white_ethnicity)
dl_latino = FilteredDataLoader(cached_dl, latino_ethnicity)

dataloaders_list = [
    dl_cropped_left,
    dl_cropped_upper,
    dl_resized,
    dl_colored,
    dl_blurred,
    dl_positive_roll,
    dl_negative_roll,
    dl_white,
    dl_latino,
]

models_list = [
    FaceAlignmentWrapper(model=FaceAlignment(LandmarksType.TWO_D, device="cpu", flip_input=False)),
    OpenCVWrapper(),
]

models_list = [models_list[1]]

report = Report(models_list, dataloaders_list, dataloader_ref=dl_ref)

df = report.to_dataframe()

current_time = str(datetime.now()).replace(" ", "")
df.to_markdown("report_"+current_time+".md")