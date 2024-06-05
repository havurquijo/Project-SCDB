import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use Agg backend for non-GUI rendering
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import io
import copy
from os import getcwd
from os.path import join
from pathlib import Path

class decomposingTemporalSeries:
    file_location_folder = getcwd()

    def __init__(self) -> None:
        pass

    def decompose(self,timePeriod=182)->bool:
        try:
            base = pd.read_csv(Path(join(self.file_location_folder,'scdb_ml_app\\models\\temporal_series_with_mean.csv')),sep=';')
        except Exception as e:
            print('An error '+e+' occured when opening the file \'temporal_series_with_mean.csv\'')
            return False
        # Converting to datetime of pandas
        base['dateDecision'] = pd.to_datetime(base['dateDecision'])
        # Setting the variable of time as the index of the dataframe, this is needed for the porper functioning of the model
        base.set_index('dateDecision', inplace=True)
        # Forward fill missing values
        base['decisionDirection'] = base['decisionDirection'].fillna(method='ffill')
        # Decompossing with the model seasonal_decompose of from the package statsmodel
        # timePeriod in days
        decomposition = seasonal_decompose(base['decisionDirection'], model='additive',period=timePeriod)
        # Access individual components
        trend = decomposition.trend
        seasonal = decomposition.seasonal
        residual = decomposition.resid
        # Creating new variable base_ to plot a central black line of refference 
        base_ = copy.copy(base)
        base_['decisionDirection']=1.5
        # Plotting
        fig, axs = plt.subplots(4,1, figsize=(8, 10))
        axs[0].plot(base)
        axs[0].set_ylabel('Original', fontsize=14)
        axs[0].xaxis.set_visible(False)
        axs[0].set_yticks([1,2],['1','2'])
        axs[0].tick_params(axis='x', which='major', labelsize=12)  
        axs[1].plot(trend)
        axs[1].plot(base_,'--k')
        axs[1].set_ylabel('Trend', fontsize=14)
        axs[1].xaxis.set_visible(False)
        axs[1].set_yticks([1,2],['1','2'])
        axs[1].tick_params(axis='x', which='major', labelsize=12)
        axs[2].plot(seasonal)
        axs[2].set_ylabel('Seasonal', fontsize=14)
        axs[2].xaxis.set_visible(False)
        axs[2].tick_params(axis='x', which='major', labelsize=12) 
        #axs[2].set_yticks([1,2],['1','2'])
        axs[3].plot(residual)
        axs[3].set_ylabel('Residual', fontsize=14)
        axs[3].tick_params(axis='x', which='major', labelsize=12) 
        fig.tight_layout()
        
        # Close the figure to prevent memory leaks
        try:
            fig.savefig(Path(join(self.file_location_folder,'scdb_ml_app\\static\\icon\\temporal_series_image.png')),dpi=300.0)
            plt.close(fig)
        except:
            print("Error happened when saving the figure of the model temporal series.")
            plt.close(fig)
            return False
        return True
