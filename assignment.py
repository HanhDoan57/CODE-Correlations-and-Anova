import pandas as pd
import statsmodels.api as sm
import statsmodels.graphics.api as smg
import statsmodels.formula.api as sm_api
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# If any of these libraries are missing from your computer,
# please install them using pip.

flights_filename = 'Flight_Delays_2018.csv'
flights_df = pd.read_csv(flights_filename)

coffee_filename = 'coffee.csv'
coffee_df = pd.read_csv(coffee_filename)
