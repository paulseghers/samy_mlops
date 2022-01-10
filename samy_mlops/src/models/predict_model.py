import torch
from model.py import MyAwesomeModel

trained_model = "/savedmodels/trainedmodel.pt"

model = MyAwesomeModel()
model.load_state_dict(torch.load(trained_model))
model.eval()
