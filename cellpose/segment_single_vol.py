import sys

from cellpose import models
from tifffile import imread
from tifffile import imwrite
from glob import glob
import numpy as np
import time
from glob import glob
import os
import torch
import gc


load_dir = sys.argv[1]
seq = glob(os.path.join(load_dir, "*.tif"))
stack = imread(seq)

model_path = "G:/Data/IBIN_Nina/workspace/nina_cellpose/training_data/with_reslice/model/models/cellpose_residual_on_style_on_concatenation_off__2022_10_18_14_57_00.795536"

savepath = sys.argv[2]

if len(sys.argv) > 3:
    model_path = sys.argv[3]


diam_mean = 15

print("segmenting %s" % load_dir)
start_time = time.time()

## remove bg from data
stack = np.asarray(stack, dtype=np.int32)
stack -= 100  #subtract zero signed int
negative_mask = stack > 0
stack = stack*negative_mask  # remove negative values
stack = np.asarray(stack, dtype=np.uint16)  # convert back to unsigned

# should we initialise this less often
model = models.CellposeModel(pretrained_model = model_path,
                        diam_mean = diam_mean,
                        model_type=None,
                        gpu=True,
                        torch = True,
                        net_avg = True,
                    )

output = model.eval(stack, channels=[0,0], do_3D=True, diameter=diam_mean, batch_size=1)
masks = output[0]

segment_time = time.time() - start_time
print("Time taken to segment:", segment_time, "s")

## save
print("saving:", savepath)
imwrite(os.path.join(savepath, "cellpose_segmentation.tif"), np.asarray(masks, dtype=np.uint16))