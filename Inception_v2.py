import torch
import torch.nn as nn
import torch.nn.functional as F

class BasicConv2d(nn.Module):
    def __init__(self, in_channels, out_channels, **kwargs):
        super(BasicConv2d,self).__init__()
        self.conv = nn.Conv2d(in_channels,out_channels, **kwargs)
        self.bn = nn.BatchNorm2d(out_channels)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        return F.relu(x)

class Inception(nn.Module):
    def __init__(self,in_planes,
                 n1x1, n3x3red, n3x3, n5x5red, n5x5, pool_planes):
        super(Inception,self).__init__()
        self.b1 = BasicConv2d(in_planes, n1x1, kernel_size=1)
        self.b2_1x1_a = BasicConv2d(in_planes, n3x3red, kernel_size=1)
        self.b2_3x3_b = BasicConv2d(n3x3red, n3x3, kernel_size=3, padding=1)
        self.b3_1x1_a = BasicConv2d(in_planes, n5x5red, kernel_size=1)
        self.b3_3x3_b = BasicConv2d(n5x5red, n5x5, kernel_size=3, padding=1)
        self.b3_3x3_c = BasicConv2d(n5x5, n5x5, kernel_size=3, padding=1)
        self.b4_pool = nn.MaxPool2d(3, stride=1, padding=1)
        self.b4_1x1 = BasicConv2d(in_planes, pool_planes, kernel_size=1)

    def forward(self, x):
        y1 = self.b1(x)
        y2 = self.b2_3x3_b(self.b2_1x1_a(x))
        y3 = self.b3_3x3_c(self.b3_3x3_b(self.b3_1x1_a(x)))
        y4 = self.b4_1x1(self.b4_pool(x))
        return torch.cat([y1,y2,y3,y4],1)

class Inception_v2(nn.Module):
    def __init__(self):
        super(Inception_v2, self).__init__()
        self.pre_layers = BasicConv2d(3,192, kernel_size=3, padding=1)
        