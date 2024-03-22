Segmentation and analysis pipeline
----------------------------------

### Intro

This repository contains details of the 3D nuclear segmentation of the
multi-cell line spheroid volumes obtained with from the time-lapse, 4-colour OPM
imaging.

The spheroids comprise up to 3 cell lines, each expressing a unique fluorophore
labeling H2B (Cerulean, Citrine, iRFP670). There is an mRFP (H2B-mRFP) common
channel for segmentation.

 

### Cellpose 

Cellpose is used for 3D image segmentation and was originally trained in
Cellpose 2.0; the current version of Cellpose is 3.0. Details on this are in the
[Cellpose](https://github.com/LeoRoweBrown/IBIN_Nina_code/blob/main/cellpose)
folder of the repository.

The notebooks in the repository use Cellpose 3.0 syntax, and the Cellpose 2.0
model, which works in Cellpose 3.0 and is used in current analysis,
is`cellpose_residual_on_style_on_concatenation_off__2022_10_28_14_29_47.213939_epoch_151`.

A Cellpose 3.0 model (`nina_model`) is a work in progress and will probably be
trained from scratch, while the original model is trained using the pre-existing
`nuclei` model as a starting point.

Details on how to generate annotation data and run Cellpose in Python will be
described in the
[instructions](https://github.com/LeoRoweBrown/IBIN_Nina_code/tree/main/cellpose/instructions).
