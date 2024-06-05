import torch




def get_model():
    model = torch.load("MOBILENET.pt")
    model.load_state_dict(model.state_dict())
    return model

