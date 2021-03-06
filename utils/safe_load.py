import torch
import time
import json

def torch_state(path):
    for i in range(10):
        state = torch.load(path)
        return state


    print("Failed to load state")
    return

def json_state(path):
    for i in range(10):
        try:
            with open(path) as f:
                state = json.load(f)
            return state
        except:
            print("Failed to load",i,path)
            time.sleep(i)
            pass

    print("Failed to load state")
    return None
