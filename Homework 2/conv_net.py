import torch
import torch.nn as nn


class ConvNet(torch.nn.Module):
    def __init__(self):
        super(ConvNet, self).__init__()
        
        self.conv1 = torch.nn.Conv2d(
            in_channels=3,
            out_channels=64,
            kernel_size=3,
            padding=1
        )
        self.pool1 = torch.nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = torch.nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.pool2 = torch.nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv3 = torch.nn.Conv2d(128, 256, kernel_size=3, padding=1)
        self.conv4 = torch.nn.Conv2d(256, 256, kernel_size=3, padding=1)
        self.pool3 = torch.nn.MaxPool2d(kernel_size=2, stride=2)
        
        self.fc1024 = torch.nn.Linear(50176, 1024)
        self.fc100 = torch.nn.Linear(1024, 100)
        
        self.softmax = torch.nn.Softmax()

    def forward(self, x):
        x = self.conv1(x)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.pool2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.pool3(x)
        x = x.flatten()
        print(x.shape)
        # return 
        x = self.fc1024(x)
        x = self.fc100(x)
        return self.softmax(x)


def get_n_params(model):
    pp=0
    for p in list(model.parameters()):
        nn=1
        for s in list(p.size()):
            nn = nn*s
        pp += nn
    return pp


if __name__ == "__main__":
    model = ConvNet()
    print(get_n_params)
