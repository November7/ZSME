import pandas as pd
import numpy as np
import seaborn as sns #pip install seaborn


from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score 


#zmiana katalogu na ten w którym znajduje się skrypt
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))