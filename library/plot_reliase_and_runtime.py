import pandas as pd
import matplotlib.pyplot as plt


def create_plot_realise_and_runtime(data):

    # Gør at vi kan printe all kolonner.
    pd.set_option('display.max_columns', None)
    
    # Sorted by runtime 
    # data = data.sort_values('runtime')
    
    #print(data['runtime'])

    #plot_file = 'release_date.png'

    #data_to_be_plotted = pd.concat([data['release_date'], runtime_sorted ], axis=1, keys=['Non Adult Movies','Adult Movies'])
    #data.plot.scatter(x='runtime',y='release_date')
        
    # For tests.
    # plt.show()
    
    """ ax = data.plot()
    ax.set_title('Release Date and Runtime')
    ax.legend(loc='upper center')
    ax.set_ylabel('Release Date')
    ax.grid(False) """ # Get som space just below 0 on x axe.
    
    #fig = ax.get_figure()

    #fig.savefig(plot_file)
