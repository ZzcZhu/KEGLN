# author: Zhichao Zhu
# coding: UTF-8
import time
import torch
import numpy as np
from train_eval import train, init_network, eval
from importlib import import_module
import argparse
from utils import build_dataset, build_iterator, get_time_dif

parser = argparse.ArgumentParser(description='Chinese Event Extraction')
parser.add_argument('--model', type=str, default='bert', help='choose a model: Bert')
args = parser.parse_args()


if __name__ == '__main__':
    dataset = 'data'  # 数据集

    model_name = args.model  # bert
    x = import_module('models.' + model_name)

    config = x.Config(dataset)
    np.random.seed(11)
    torch.manual_seed(11)
    torch.cuda.manual_seed_all(11)
    torch.backends.cudnn.deterministic = True  # 保证每次结果一样

    start_time = time.time()
    print("Loading data...")
    train_data = build_dataset(config)
    # print(len(train_data))
    # exit()
    test_data = train_data[6423:]
    train_data = train_data[0:6423]
    train_iter = build_iterator(train_data, config)

    test_iter = build_iterator(test_data, config)
    time_dif = get_time_dif(start_time)
    print("Time usage:", time_dif)
    model = x.Model(config).to(config.device)
    predict_label = 0
    if predict_label == 0:
        # train
        train(config, model, train_iter, test_iter)
    else:
        # predict
        metric,trigger_f1,argument_f1 = eval(model, train_iter, 'data/result_data/predict_result')