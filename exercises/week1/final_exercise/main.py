import argparse
import sys

import torch
from torch import nn, optim    
from pathlib import Path
from data import mnist
from model import MyAwesomeModel
save_path = str(Path().resolve().parents[1]) + '\\savedmodels'

class TrainOREvaluate(object):
    """ Helper class that will help launch class methods as commands
        from a single script
    """
    def __init__(self):
        parser = argparse.ArgumentParser(
            description="Script for either training or evaluating",
            usage="python main.py <command>"
        )
        parser.add_argument("command", help="Subcommand to run")
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            
            parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()
    
    def train(self):
        print("Training day and night")
        parser = argparse.ArgumentParser(description='Training arguments')
        parser.add_argument('--lr', default=0.1)
        # add any additional argument that you want
        args = parser.parse_args(sys.argv[2:])
        print(args)
        
        # TODO: Implement training loop here
        model = MyAwesomeModel()
        train_set, _ = mnist()
        train_images = torch.tensor(train_set['images']).view(5000,1,28,28)
        train_labels = torch.tensor(train_set['labels'])
        train_data = []
        for i in range(len(train_images)):
            train_data.append([train_images[i], train_labels[i]])

        trainloader = torch.utils.data.DataLoader(train_data, batch_size=64, shuffle=True)
        criterion = nn.NLLLoss()
        optimizer = optim.Adam(model.parameters(), lr=0.003)


        epochs = 30

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
            torch.save(model.state_dict(), save_path + '\\checkpoints\\checkpoint.pth')
        torch.save(model.state_dict(), save_path + '\\trainedmodel.pt')

    def evaluate(self):
        print("Evaluating until hitting the ceiling")
        parser = argparse.ArgumentParser(description='Training arguments')
        #parser.add_argument('load_model_from', default="")
        # add any additional argument that you want
        #args = parser.parse_args(sys.argv[2:])
        #print(args)
        
        state_dict = torch.load(save_path + '\\trainedmodel.pt')
        model = MyAwesomeModel()
        model.load_state_dict(state_dict)
        model.eval()
        _, test_set = mnist()
        images = torch.tensor(test_set['images']).view(5000,1,28,28)
        labels = torch.tensor(test_set['labels'])
        ps = torch.exp(model(images.float()))
        top_p, top_class = ps.topk(1, dim=1)
        equals = top_class == labels.view(*top_class.shape)
        accuracy = torch.mean(equals.type(torch.FloatTensor))
        print(f'Accuracy: {accuracy.item()*100}%')


if __name__ == '__main__':
    TrainOREvaluate()
    
    
    
    
    
    
    
    
    