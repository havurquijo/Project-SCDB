import pandas as pd
#import matplotlib
#matplotlib.use('Agg')  # Use Agg backend for non-GUI rendering
#import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import copy
from os import getcwd
from os.path import join
from pathlib import Path
#imports for interactive plot
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio


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

        # Create individual figures using Plotly Express
        try:
            self.plot_plotly(base=base,base_=base_,trend=trend,seasonal=seasonal,residual=residual)
            return True
        except:
            return False

    def plot_plotly(self,base,base_,trend,seasonal,residual):
        # Create individual figures using Plotly Express
        base_reset=base.reset_index()
        trend_reset = trend.reset_index()
        seasonal_reset = seasonal.reset_index()
        residual_reset = residual.reset_index()
        base_reset_ = base_.reset_index()

        # Create individual figures using Plotly Express
        fig0 = px.line(base_reset, x='dateDecision', y='decisionDirection', line_shape='linear')
        fig1 = px.line(trend_reset, x='dateDecision', y='trend', line_shape='linear')
        fig11 = px.line(base_reset_, x='dateDecision', y='decisionDirection', line_shape='linear')
        fig2 = px.line(seasonal_reset, x='dateDecision', y='seasonal', line_shape='linear')
        fig3 = px.line(residual_reset, x='dateDecision', y='resid', line_shape='linear')


        # Define the number of rows and columns for the subplots
        fig = make_subplots(rows=4, cols=1)

        # Add traces from fig0 to the first subplot
        for trace in fig0.data:
            trace.update(line=dict(color='blue'))
            fig.add_trace(trace, row=1, col=1)

        # Add traces from fig1 and fig11 to the second subplot
        for trace in fig1.data:
            fig.add_trace(trace, row=2, col=1)

        for trace in fig11.data:
            trace.update(line=dict(dash='dash',color='black'))
            fig.add_trace(trace, row=2, col=1)

        # Add traces from fig2 to the third subplot
        for trace in fig2.data:
            trace.update(line=dict(color='blue'))
            fig.add_trace(trace, row=3, col=1)

        # Add traces from fig3 to the fourth subplot
        for trace in fig3.data:
            trace.update(line=dict(color='blue'))
            fig.add_trace(trace, row=4, col=1)

        # Customize the layout
        fig.update_layout(
            height=500, 
            width=800, 
            font=dict(
                size=14,  # Font size for titles and labels
                color='black'  # Font color
            ),
            margin=dict(l=0, r=10, t=30, b=0),  # Set margins to 0 to remove white space
            xaxis=dict(
                tickfont=dict(size=12),  # X-axis tick font size
                title_font=dict(size=16),  # X-axis title font size
            ),
            yaxis=dict(
                tickfont=dict(size=12),  # Y-axis tick font size
                title_font=dict(size=16),  # Y-axis title font size
            )
        )

        # Set the y-axis range for the 'Original' and 'Trend' subplots
        fig.update_yaxes(range=[0.9, 2.1], row=1, col=1)  # 'Original' subplot
        fig.update_yaxes(range=[1, 2], row=2, col=1)  # 'Trend' subplot

        # Set the y-axis range and titles
        fig.update_yaxes(title_text='Original', range=[0.9, 2.1], row=1, col=1)
        fig.update_yaxes(title_text='Trend', range=[1, 2], row=2, col=1)
        fig.update_yaxes(title_text='Seasonal', row=3, col=1)
        fig.update_yaxes(title_text='Residual', row=4, col=1)

        # Show x-axis ticks only on the last subplot
        fig.update_xaxes(showticklabels=False, row=1, col=1)
        fig.update_xaxes(showticklabels=False, row=2, col=1)
        fig.update_xaxes(showticklabels=False, row=3, col=1)
        fig.update_xaxes(showticklabels=True, row=4, col=1)

        # Save the figure as an HTML file
        pio.write_html(fig, file=Path(join(self.file_location_folder,'scdb_ml_app\\static\\icon\\subplot_figure.html')), auto_open=False)

        #
        #fig, axs = plt.subplots(4,1, figsize=(8, 10))
        #axs[0].plot(base)
        #axs[0].set_ylabel('Original', fontsize=14)
        #axs[0].xaxis.set_visible(False)
        #axs[0].set_yticks([1,2],['1','2'])
        #axs[0].tick_params(axis='x', which='major', labelsize=12)  
        #axs[1].plot(trend)
        #axs[1].plot(base_,'--k')
        #axs[1].set_ylabel('Trend', fontsize=14)
        #axs[1].xaxis.set_visible(False)
        #axs[1].set_yticks([1,2],['1','2'])
        #axs[1].tick_params(axis='x', which='major', labelsize=12)
        #axs[2].plot(seasonal)
        #axs[2].set_ylabel('Seasonal', fontsize=14)
        #axs[2].xaxis.set_visible(False)
        #axs[2].tick_params(axis='x', which='major', labelsize=12) 
        #axs[2].set_yticks([1,2],['1','2'])
        #axs[3].plot(residual)
        #axs[3].set_ylabel('Residual', fontsize=14)
        #axs[3].tick_params(axis='x', which='major', labelsize=12) 
        #fig.tight_layout()
        
        # Close the figure to prevent memory leaks
        #try:
        #    fig.savefig(Path(join(self.file_location_folder,'scdb_ml_app\\static\\icon\\temporal_series_image.png')),dpi=300.0)
        #    plt.close(fig)
        #except:
        #    print("Error happened when saving the figure of the model temporal series.")
        #    plt.close(fig)
        #    return False
        #return True
