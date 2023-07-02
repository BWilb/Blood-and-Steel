import torch
import random
import numpy as np
from collections import deque

MAX_MEMORY = 200_000
BATCH_SIZE = 2000
LR = 0.001

class Agent:
    def __init__(self):
        # setting up number of rounds of diplomacy, national agent
        self.diplomatic_rounds = 0
        self.epsilon = 0 # randomness of agent
        self.gamma = None
        self.memory = deque(maxlen=MAX_MEMORY)
        # self.model
        # self.trainer
