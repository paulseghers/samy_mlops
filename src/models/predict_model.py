from os.path import abspath, dirname

import torch
from lightningmodel import MyAwesomeModel

from data import mnist

# loading the trained model based on the path of the file rather than where the file is run
save_path = dirname(abspath(__file__))
trained_model = save_path + "/savedmodels/trainedmodel.pt"


def predict_model():
    """
    Makes mnist predictions based on the trained model (hard-coded), then outputs the accuracy of those predictions
    """
    state_dict = torch.load(trained_model)
    model = MyAwesomeModel()
    model.load_state_dict(state_dict)
    model.eval()
    _, test_set = mnist()
    images = torch.tensor(test_set["images"]).view(5000, 1, 28, 28)
    labels = torch.tensor(test_set["labels"])
    ps = torch.exp(model(images.float()))
    top_p, top_class = ps.topk(1, dim=1)
    equals = top_class == labels.view(*top_class.shape)
    accuracy = torch.mean(equals.type(torch.FloatTensor))
    print(f"Accuracy: {accuracy.item()*100}%")


predict_model()
