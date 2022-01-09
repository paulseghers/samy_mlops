import torch
import torchvision
import numpy as np
from torch.utils.data import TensorDataset, DataLoader
import glob
from pathlib import Path



data_path = str(Path().resolve()) + '/data/corruptmnist'
train_data = data_path + '/train/train_merged.npz'
test_data = data_path + '/test/test.npz'

file_list = glob.glob(data_path + '/train/*')

data_all = [np.load(fname) for fname in file_list]
merged_data = {}
for data in data_all:
    [merged_data.update({k: v}) for k, v in data.items()]
np.savez(data_path + '/train/train_merged.npz', **merged_data)

def mnist():
    # exchange with the corrupted mnist dataset
    train = np.load(train_data)
    test = np.load(test_data) 
    return train, test




