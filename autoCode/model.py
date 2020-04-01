
import torch
import torch.nn as nn


class Model(nn.Module):
    
    def __init__(self,):
        super(Model, self).__init__()

        self.input = nn.Sequential(
            nn.Conv2d(1,16,3,1),
            nn.BatchNorm2d(16),
        )

        self.convs = nn.Sequential(
            nn.Conv2d(16,100,3),
            nn.ReLU(),
            nn.Conv2d(100,100,3),
            nn.BatchNorm2d(16),
            nn.Conv2d(100,100,3),
            nn.MaxPool2d(2),
            nn.Conv2d(100,100,3),            
        )
        self.out = nn.Linear(100,10)
        self.initialize()
    
    def initialize(self,):
        pass

    def forward(self, x):

        x = self.input(x)
        x2 = self.convs(x)
        x = x + x2
        x = self.out(x)

        return x

if __name__ == "__main__":
    model = Model()
    print(model.named_modules)