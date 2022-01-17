from os.path import abspath, dirname

import torch
from lightningmodel import MyAwesomeModel
from torch import nn, optim

from data import mnist

save_path = dirname(abspath(__file__))


def train_model():
    model = MyAwesomeModel()
    train_set, _ = mnist()
    train_images = torch.tensor(train_set["images"]).view(5000, 1, 28, 28)
    train_labels = torch.tensor(train_set["labels"])
    train_data = []
    for i in range(len(train_images)):
        train_data.append([train_images[i], train_labels[i]])

    trainloader = torch.utils.data.DataLoader(train_data, batch_size=64, shuffle=True)
    criterion = nn.NLLLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.003)

    epochs = 100

    for e in range(epochs):
        running_loss = 0
        for images, labels in trainloader:
            optimizer.zero_grad()

            log_ps = model(images.float())
            loss = criterion(log_ps, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
        else:
            ## TODO: Implement the validation pass and print out the validation accuracy
            print(f"Training loss: {running_loss/len(trainloader)}")
        torch.save(
            model.state_dict(), save_path + "/savedmodels/checkpoints/checkpoint.pth"
        )
    torch.save(model.state_dict(), save_path + "/savedmodels/trainedmodel.pt")
