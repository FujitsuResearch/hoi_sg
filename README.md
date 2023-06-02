# HICO-DET-SG and V-COCO-SG: New Data Splits for Evaluating the Systematic Generalization Performance of Human-Object Interaction Detection Models
## About this repository
This repository provides the JSON files that determin the HICO-DET-SG and V-COCO-SG, the new data splits we created based on the [HICO-DET](http://www-personal.umich.edu/~ywchao/hico/) and [V-COCO](https://github.com/s-gupta/v-coco) datasets for evaluating the systematic generalization performance of Human-Object Interaction (HOI) detection models.

This repository also provides the source code used to create these JSON files.

The creation process of the new data splits, their statistics, and the evaluation results of the representative HOI detection models ([HOTR](https://github.com/kakaobrain/HOTR), [QPIC](https://github.com/hitachi-rd-cv/qpic), [FGAHOI](https://github.com/xiaomabufei/FGAHOI), and [STIP](https://github.com/zyong812/STIP)) on the new splits are available in the following preprint. 

Kentaro Takemoto, Moyuru Yamada, Tomotake Sasaki, Hisanao Akima. 
[HICO-DET-SG and V-COCO-SG: New Data Splits for Evaluating the Systematic Generalization Performance of Human-Object Interaction Detection Models](https://arxiv.org/abs/2305.09948). 
arXiv preprint, arXiv:2305.09948v2, 2023. 


## JSON files of HICO-DET-SG and V-COCO-SG
The JSON files defining HICO-DET-SG and V-COCO-SG splits are contained in the `SGsplits/` folder.
You can use them to test the systematic generalization performance of HOI detection models.  


## How to create JSON files with the source code
### 1. HOI dataset setup
#### HICO-DET
You can download the HICO-DET dataset from [here](https://drive.google.com/open?id=1QZcJmGVlF9f4h-XLWe9Gkmnmj2z1gSnk). 

Instead of using the original annotations files, we use the annotation files provided in [this repository](https://github.com/YueLiao/PPDM). You can download the annotation files from [here](https://drive.google.com/open?id=1WI-gsNLS-t0Kh8TVki1wXqc3y2Ow1f2R). 

#### V-COCO
Firstly, clone the repository of V-COCO from [here](https://github.com/s-gupta/v-coco), and then follow the instruction to generate the file `instances_vcoco_all_2014.json`. Next, download the prior file `prior.pickle` from [here](https://drive.google.com/drive/folders/10uuzvMUCVVv95-xAZg5KS94QXm7QXZW4).

Then follow the instruction in [here](https://github.com/hitachi-rd-cv/qpic) to generate `trainval_vcoco.json` and `test_vcoco.json`.


### 2. Generate SG splits
Firstly, please modify the parameters in `main.py`.

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


## Remark
We updated this repository after the presentation at [DistShift 2022 (NeurIPS Workshop)](https://sites.google.com/view/distshift2022). The old version used at the time of the workshop can be retrieved from [`7c65140`](https://github.com/FujitsuResearch/hoi_sg/tree/7c651401bb276cee4719eb4dec07d3ab19f4bda0), but please use the current version for your own study.  




## License
- The JSON files determining HICO-DET-SG and V-COCO-SG contained in the `SGsplits/` folder are available under the [CC0 1.0 License](https://creativecommons.org/publicdomain/zero/1.0/).
- The source code contained in this repository is available under the [BSD 3-Clause Clear License](LICENSE).

## Citation

If you find the data splits and code helpful for your research, please cite the following.
```
@misc{Takemoto_2023,
    author    = {Takemoto, Kentaro and Yamada, Moyuru and Sasaki, Tomotake and Akima, Hisanao},
    title     = {{HICO-DET-SG} and {V-COCO-SG}: New Data Splits for Evaluating the Systematic Generalization Performance of Human-Object Interaction Detection Models},
    howpublished = {arXiv preprint, arXiv:2305.09948v2},
    year      = {2023}
}
```