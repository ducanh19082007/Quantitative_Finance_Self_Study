import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class Agent:
    def __init__(self, epoch):
        self.epoch