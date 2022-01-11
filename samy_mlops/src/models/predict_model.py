import torch
from lightningmodel import MyAwesomeModel
from os.path import dirname, abspath
from data import mnist

save_path = dirname(abspath(__file__))


trained_model = save_path + "/savedmodels/trainedmodel.pt"


def predict_model():
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
