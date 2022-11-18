# HICO-DET-SG and V-COCO-SG: New Data Splits to Evaluate Systematic Generalization in Human-Object Interaction Detection
## About this repository
This repository contains HICO-DET-SG and V-COCO-SG, new data splits we created based on [HICO-DET](http://www-personal.umich.edu/~ywchao/hico/) and [V-COCO](https://github.com/s-gupta/v-coco) dataset to evaluate systematic generalization in HOI detection.

This repository also contains the source code to create these json files.

## Json files of HICO-DET-SG and V-COCO-SG
The json files defining HICO-DET-SG and V-COCO-SG splits are contained in the `data/` folder.
You can use them to reproduce our results reported in the following study.  

```
Kentaro Takemoto, Moyuru Yamada, Tomotake Sasaki, Hisanao Akima. HICO-DET-SG and V-COCO-SG: New Data Splits to Evaluate Systematic Generalization in Human-Object Interaction Detection. Workshop on Distribution Shifts, 36th Conference on Neural Information Processing Systems, 2022. (to appear) 
```

## How to create json files
### 1. HOI dataset setup
#### HICO-DET
You can download HICO-DET dataset from [here](https://drive.google.com/open?id=1QZcJmGVlF9f4h-XLWe9Gkmnmj2z1gSnk). 

Instead of using the original annotations files, we use the annotation files provided in [this repostory](https://github.com/YueLiao/PPDM). You can download the annotation files from [here](https://drive.google.com/open?id=1WI-gsNLS-t0Kh8TVki1wXqc3y2Ow1f2R). 

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

#### V-COCO
Set the random seed as 564, 966 and 2065 to generate split 1, 2 and 3, respectively.

Set the ratio as 0.7 for V-COCO-SG.

Then run:
```shell
python main.py
```
`trainval_vcoco_[output name].json` and `test_vcoco_[output name].json` will be created in the input directory.


## License
This project is licensed under the terms of the [BSD 3-Clause Clear License](https://spdx.org/licenses/BSD-3-Clause-Clear.html).
Copyright 2022 Fujitsu Limited. All Rights Reserved.

## Citation

If you find this code helpful for your research, please cite our paper.
```
@misc{Takemoto_2022,
    author    = {Kentaro Takemoto and Moyuru Yamada and Tomotake Sasaki and Hisanao Akima},
    title     = {HICO-DET-SG and V-COCO-SG: New Data Splits to Evaluate Systematic Generalization in Human-Object Interaction Detection},
    booktitle = {Workshop on Distribution Shifts, 36th Conference on Neural Information Processing Systems},
    year      = {2022}
}
```