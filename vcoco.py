# SPDX-License-Identifier: BSD-3-Clause-Clear
# Copyright (c) 2022 Fujitsu Limited. All rights reserved.
# Licensed under the BSD 3-Clause Clear License. See LICENSE for details.

import os
import numpy as np
import json
from sklearn.model_selection import train_test_split

def checker(train_indice, test_indice):
    for test_index in test_indice:
        flag1=True
        flag2=True
        for train_index in train_indice:
            if test_index[0]==train_index[0]:
                flag1=False
            if test_index[1]==train_index[1]:
                flag2=False
        if flag1 or flag2:
            return(False)
    return(True)

def vcoco(seed, ratio, input, output):
    path_train = os.path.join(input, 'trainval_vcoco.json')
    path_test = os.path.join(input, 'test_vcoco.json')
    with open(path_train) as f:
        sg_train = json.load(f)
    with open(path_test) as f:
        sg_test = json.load(f)

    obj_act_matrix = np.zeros((91,29))
    for s in sg_train:
        for hoi in s['hoi_annotation']:
            if hoi['object_id']>-1:
                act_index = hoi['category_id']
                obj_index = s['annotations'][hoi['object_id']]['category_id']
                obj_act_matrix[obj_index, act_index] += 1

    for s in sg_test:
        for hoi in s['hoi_annotation']:
            if hoi['object_id']>-1:
                act_index = hoi['category_id']
                obj_index = s['annotations'][hoi['object_id']]['category_id']
                obj_act_matrix[obj_index, act_index] += 1

    if seed < 0:
        for seed in range(0, 10000):
            train_indice, test_indice = train_test_split(np.transpose(np.nonzero(obj_act_matrix)), train_size=ratio, random_state=seed)
            if checker(train_indice, test_indice):
                print('Random seed is {}'.format(seed))
                break

    train_indice, test_indice = train_test_split(np.transpose(np.nonzero(obj_act_matrix)), train_size=ratio, random_state=seed)

    sg_train_new = []
    sg_test_new = []
    counter=0
    for s in sg_train:
        sum=0
        new = []
        for hoi in s['hoi_annotation']:
            act_index = hoi['category_id']
            obj_index = s['annotations'][hoi['object_id']]['category_id']
            sum += np.sum(np.all(test_indice == np.array([obj_index,act_index]),axis=1))
            if np.sum(np.all(test_indice == np.array([obj_index,act_index]),axis=1)):
                new.append(hoi)

        if sum==len(s['hoi_annotation']):
            sg_test_new.append(s)
        elif sum==0:
            sg_train_new.append(s)

    for s in sg_test:
        sum=0
        new = []
        for hoi in s['hoi_annotation']:
            act_index = hoi['category_id']
            obj_index = s['annotations'][hoi['object_id']]['category_id']
            sum += np.sum(np.all(test_indice == np.array([obj_index,act_index]),axis=1))
            if np.sum(np.all(test_indice == np.array([obj_index,act_index]),axis=1)):
                new.append(hoi)

        if sum==len(s['hoi_annotation']):
            sg_test_new.append(s)
        elif sum==0:
            sg_train_new.append(s)

    json_path_train_new = os.path.join(input, 'trainval_vcoco_{}.json'.format(output))
    json_path_test_new = os.path.join(input, 'test_vcoco_{}.json'.format(output))
    with open(json_path_train_new, 'w') as f:
        json.dump(sg_train_new, f)
    with open(json_path_test_new, 'w') as f:
        json.dump(sg_test_new, f)
    print('Saved at {}'.format(input))