# -*-coding:utf-8-*-

import torch
import torch.nn as nn

class Model(nn.Module):
    def __init__(self,):
        super(Model, self).__init__()
        self.input = nn.Sequential(nn.Conv2d(1, 16, kernel_size=(3, 3), stride=(1, 1)),
nn.BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
)
        self.convs = nn.Sequential(nn.Conv2d(16, 100, kernel_size=(3, 3), stride=(1, 1)),
nn.ReLU(),
nn.Conv2d(100, 100, kernel_size=(3, 3), stride=(1, 1)),
nn.BatchNorm2d(16, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
nn.Conv2d(100, 100, kernel_size=(3, 3), stride=(1, 1)),
nn.MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False),
nn.Conv2d(100, 100, kernel_size=(3, 3), stride=(1, 1)),
)
        self.out = nn.Sequential(nn.Linear(in_features=100, out_features=10, bias=True),
)

model = Model()
print(model)