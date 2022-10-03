import os
import numpy as np
import json
from sklearn.model_selection import train_test_split

convert_id = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9, 11: 10, 13: 11, 14: 12, 15: 13, 16: 14, 17: 15, 18: 16, 19: 17, 20: 18, 21: 19, 22: 20, 23: 21, 24: 22, 25: 23, 27: 24, 28: 25, 31: 26, 32: 27, 33: 28, 34: 29, 35: 30, 36: 31, 37: 32, 38: 33, 39: 34, 40: 35, 41: 36, 42: 37, 43: 38, 44: 39, 46: 40, 47: 41, 48: 42, 49: 43, 50: 44, 51: 45, 52: 46, 53: 47, 54: 48, 55: 49, 56: 50, 57: 51, 58: 52, 59: 53, 60: 54, 61: 55, 62: 56, 63: 57, 64: 58, 65: 59, 67: 60, 70: 61, 72: 62, 73: 63, 74: 64, 75: 65, 76: 66, 77: 67, 78: 68, 79: 69, 80: 70, 81: 71, 82: 72, 84: 73, 85: 74, 86: 75, 87: 76, 88: 77, 89: 78, 90: 79}

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

def hico(seed, ratio, input, output):
    path_train = os.path.join(input, 'trainval_hico.json')
    path_test = os.path.join(input, 'test_hico.json')
    with open(path_train) as f:
        sg_train = json.load(f)
    with open(path_test) as f:
        sg_test = json.load(f)

    obj_act_matrix = np.zeros((80,118))
    for s in sg_train:
        for hoi in s['hoi_annotation']:
            act_index = hoi['category_id']
            obj_index = s['annotations'][hoi['object_id']]['category_id']
            obj_index = convert_id[obj_index]
            obj_act_matrix[obj_index, act_index] += 1
    for s in sg_test:
        for hoi in s['hoi_annotation']:
            act_index = hoi['category_id']
            obj_index = s['annotations'][hoi['object_id']]['category_id']
            obj_index = convert_id[obj_index]
            obj_act_matrix[obj_index, act_index] += 1

    if seed < 0:
        for seed in range(368, 10000):
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
            obj_index = convert_id[obj_index]
            sum += np.sum(np.all(test_indice == np.array([obj_index,act_index]),axis=1))
            if np.sum(np.all(test_indice == np.array([obj_index,act_index]),axis=1)):
                new.append(hoi)

        if sum==len(s['hoi_annotation']):
            sg_test_new.append(s)
        elif sum==0:
            sg_train_new.append(s)
        else:
            s['hoi_annotation'] = new
            sg_test_new.append(s)

    for s in sg_test:
        sum=0
        new = []
        for hoi in s['hoi_annotation']:
            act_index = hoi['category_id']
            obj_index = s['annotations'][hoi['object_id']]['category_id']
            obj_index = convert_id[obj_index]
            sum += np.sum(np.all(test_indice == np.array([obj_index,act_index]),axis=1))
            if np.sum(np.all(test_indice == np.array([obj_index,act_index]),axis=1)):
                new.append(hoi)

        if sum==len(s['hoi_annotation']):
            sg_test_new.append(s)
        elif sum==0:
            sg_train_new.append(s)
        else:
            s['hoi_annotation'] = new
            sg_test_new.append(s)


    json_path_train_new = os.path.join(input, 'trainval_hico_{}.json'.format(output))
    json_path_test_new = os.path.join(input, 'test_hico_{}.json'.format(output))
    with open(json_path_train_new, 'w') as f:
        json.dump(sg_train_new, f)
    with open(json_path_test_new, 'w') as f:
        json.dump(sg_test_new, f)
    print('Saved at {}'.format(input))