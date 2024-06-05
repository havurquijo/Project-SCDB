import numpy as np
import pandas as pd
from os import getcwd
from os.path import join
from pathlib import Path

class miningTemporalSeries:
    file_location_folder = getcwd()

    def __init__(self) -> None:
        pass

    def mine_now(self)->bool:
        try:
            file_location = Path(join(self.file_location_folder,'scdb_ml_app\\models\\SCDB_2023_01_justiceCentered_Citation\\SCDB_2023_01_justiceCentered_Citation.csv'))
            data = pd.read_csv(file_location,encoding='ISO-8859-1')
            #Creating a Data Frame to save the time series
            sub_temporal = data[['dateDecision','decisionDirection']]
            sub_temporal = sub_temporal.drop(sub_temporal[sub_temporal.decisionDirection==3].index)
            #sub_temporal.decisionDirection[sub_temporal.decisionDirection==3]=0
            temporal_dic = {
                'dateDecision':[],
                'decisionDirection':[],
            }
            #Convert dictionary to Data Frame
            temporal = pd.DataFrame(temporal_dic)
            #Take only the unique dates
            temporal.dateDecision = sub_temporal.dateDecision.unique()
            #For every unique date, take the mean value of the decisions in the day
            for date_ in temporal.dateDecision:
                tmp = sub_temporal[sub_temporal.dateDecision==date_]
                temporal['decisionDirection'][temporal['dateDecision']==date_] = np.mean(tmp.decisionDirection)
            #saving the file with temporal series for further use
            temporal.to_csv(Path(join(self.file_location_folder,'scdb_ml_app\\models\\temporal_series_with_mean.csv')),sep=';',index=False)
            return True
        except:
            print("Error while mining temporal series")
            return False