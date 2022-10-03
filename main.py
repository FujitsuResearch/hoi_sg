from hico import hico
from vcoco import vcoco

def main():
    ### For HICO-DET-SG ###
    dataset = 'hico' # 'hico' or 'vcoco'
    seed = -1 # 368, 680, 750 for HICO-DET-SG split 1, 2, 3
    ratio = 0.9 # 0.9 for hico and 0.7 for vcoco
    input = [/hico_20160224_det/annotations] # The path you put original jsons 
    output = 'sg1' # output name

    ### For V-COCO-SG ###
    # dataset = 'vcoco' # 'hico' or 'vcoco'
    # seed = -1 # 564, 966, 2065 for V-COCO-SG split 1, 2, 3
    # ratio = 0.7 # 0.9 for hico and 0.7 for vcoco
    # input = [/v-coco/annotations] # The path you put original jsons
    # output = 'sg1' # output name

    if dataset == 'hico':
        hico(seed, ratio, input, output)
    elif dataset == 'vcoco':
        vcoco(seed, ratio, input, output)
    else:
        print('ERROR!')

if __name__ == '__main__':
    main()