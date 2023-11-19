import torch
import sys

VOCAB = set()

with open("/home/hackathon1/loganalysis/data/test_log1.out", "r") as f:
    VOCAB.update(set(f.read().replace("\n", " ").split(" ")))
    
with open("/home/hackathon1/loganalysis/data/test_log2.out", "r") as f:
    VOCAB.update(set(f.read().replace("\n", " ").split(" ")))

VOCAB = list(VOCAB)

print(len(VOCAB))

sys.exit()
class Model(torch.nn.Module):
    in_layer = torch.nn.Linear(len(VOCAB), 500)
    middle_layer = torch.nn.Linear(500, 500)
    out_layer = torch.nn.Linear(500, 2)
    