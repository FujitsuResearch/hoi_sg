# HICO-DET-SG and V-COCO-SG: New Data Splits to Evaluate Systematic Generalization in Human-Object Interaction Detection
## About this repository
This repository contains JSON files that define HICO-DET-SG and V-COCO-SG, the new data splits we created based on [HICO-DET](http://www-personal.umich.edu/~ywchao/hico/) and [V-COCO](https://github.com/s-gupta/v-coco) dataset to evaluate systematic generalization in Human-Object Interaction (HOI) detection.

This repository also contains the source code to create these JSON files.

## JSON files of HICO-DET-SG and V-COCO-SG
The JSON files defining HICO-DET-SG and V-COCO-SG splits are contained in the `SGsplits/` folder.
You can use them to test the systematic generalization performance of HOI detection models.  


\# We updated this repository after the following presentation. 

Kentaro Takemoto, Moyuru Yamada, Tomotake Sasaki, Hisanao Akima. 
[HICO-DET-SG and V-COCO-SG: New Data Splits to Evaluate Systematic Generalization in Human-Object Interaction Detection](https://openreview.net/forum?id=1Ketalw43B). 
Workshop on Distribution Shifts, 36th Conference on Neural Information Processing Systems, 2022. 

The old version used at the time of the workshop can be retrieved from [`7c65140`](https://github.com/FujitsuResearch/hoi_sg/tree/7c651401bb276cee4719eb4dec07d3ab19f4bda0).  


## How to create JSON files
### 1. HOI dataset setup
#### HICO-DET
You can download HICO-DET dataset from [here](https://drive.google.com/open?id=1QZcJmGVlF9f4h-XLWe9Gkmnmj2z1gSnk). 

Instead of using the original annotations files, we use the annotation files provided in [this repository](https://github.com/YueLiao/PPDM). You can download the annotation files from [here](https://drive.google.com/open?id=1WI-gsNLS-t0Kh8TVki1wXqc3y2Ow1f2R). 

#### V-COCO
First clone the repository of V-COCO from [here](https://github.com/s-gupta/v-coco), and then follow the instruction to generate the file `instances_vcoco_all_2014.json`. Next, download the prior file `prior.pickle` from [here](https://drive.google.com/drive/folders/10uuzvMUCVVv95-xAZg5KS94QXm7QXZW4).

Then follow the instruction in [here](https://github.com/hitachi-rd-cv/qpic) to generate `trainval_vcoco.json` and `test_vcoco.json`.


### 2. Generate SG splits
Please modify the parameters in `main.py` first.

#### HICO-DET-SG
Set the random seed as 368, 680 and 750 to generate split 1, 2 and 3, respectively.

Set the ratio as 0.9 for HICO-DET-SG.

Then run:
```shell
python main.py
```
`trainval_hico_[output name].json` and `test_hico_[output name].json` will be created in the input directory.

#### V-COCO-SG
Set the random seed as 564, 966 and 2065 to generate split 1, 2 and 3, respectively.

Set the ratio as 0.7 for V-COCO-SG.

Then run:
```shell
python main.py
```
`trainval_vcoco_[output name].json` and `test_vcoco_[output name].json` will be created in the input directory.


## License
This project is licensed under the terms of the [BSD 3-Clause Clear License](https://spdx.org/licenses/BSD-3-Clause-Clear.html).
Copyright 2023 Fujitsu Limited. All Rights Reserved.

## Citation

If you find the data splits and code helpful for your research, please cite the following.
```
@misc{Takemoto_2023,
    author    = {Kentaro Takemoto and Moyuru Yamada and Tomotake Sasaki and Hisanao Akima},
    title     = {{HICO-DET-SG} and {V-COCO-SG}: New Data Splits to Evaluate Systematic Generalization in Human-Object Interaction Detection},
    howpublished = {\url{https://github.com/FujitsuResearch/hoi_sg}},
    year      = {2023}
}
```