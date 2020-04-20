import torch
import torch.nn as nn
from torchvision.datasets import MNIST
from torchvision import transforms
from torch.utils.data import  DataLoader
import torch.backends.cudnn as cudnn
from torch.optim import Adam
from torch.nn import CrossEntropyLoss

class BottleNeck(nn.Module):
    def __init__(self, inp, oup, stride):
        super(BottleNeck,self).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(inp, oup, kernel_size=3, stride=stride, padding=1,bias=False),
            nn.BatchNorm2d(oup),
            nn.ReLU()
        )

    def forward(self, x):
        return self.conv(x)

class Net(nn.Module):
    def __init__(self, num_class):
        super(Net,self).__init__()
        self.construct = [
            (1, 16, 1),
            (16, 32, 2),
            (32, 64 ,1),
            (64, 128 ,2),
            (128, 256, 1),
            (256, 256, 2)
        ]
        self.pool = nn.AvgPool2d(kernel_size=4)
        self.dense = nn.Linear(256, num_class, bias=True)
        self.encoder = []
        for inp, oup, stride in self.construct:
            self.encoder.append(BottleNeck(inp, oup, stride))
        self.encoder = nn.Sequential(*self.encoder)

    def forward(self, x):
        out = self.encoder(x)
        out = self.pool(out)
        out = out.mean(3).mean(2)
        out = self.dense(out)
        return out

def main():
    transform = transforms.Compose([
        transforms.RandomCrop(28)
    ])
    data_train = MNIST(root='/home/pan/repository/python_data_structure/', train=True, download=True, transform=transform)
    data_test = MNIST(root='/home/pan/repository/python_data_structure/')

    num_class = 10
    batch_size = 32
    epochs = 20
    lr = 0.001
    train_datas = DataLoader(data_train, batch_size=batch_size, shuffle=True, num_workers=4)
    test_datas = DataLoader(data_test, batch_size=batch_size, shuffle=True, num_workers=4)
    # device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    device = torch.device('cpu')
    cudnn.benchmark = True

    model = Net(num_class)
    model = model.cuda()
    model.to(device)
    parameter_to_update = model.parameters()
    optimizer = Adam(parameter_to_update, lr=lr)
    criterion = CrossEntropyLoss()

    running_correct = 0
    for epoch in range(epochs):
        model.train()
        for train_data, train_label in train_datas:
            train_data.to(device)
            train_label.to(device)
            optimizer.zero_grad()

            with torch.set_grad_enabled(mode=True):
                outputs = model(train_data)
                loss = criterion(outputs, train_label)
                _, pred = torch.max(outputs, 1)
                loss.backward()
                optimizer.step()

            running_correct += torch.sum(pred == train_label)
        epoch_acc = running_correct.double() / len(train_datas.dataset)
        print('train Acc: {.4f%}'.format(epoch_acc))

    model.eval()
    test_correct = 0
    for test_data, test_label in test_datas:
        test_data.to(device)
        test_label.to(device)
        optimizer.zero_grad()

        outputs = model(test_data)
        _, pred = torch.max(outputs, 1)
        test_correct += torch.sum(pred == test_label)
    test_acc = test_correct.double() / len(test_datas.dataset)
    print('test acc: {.4f%}'.format(test_acc))


if __name__ == '__main__':
    main()