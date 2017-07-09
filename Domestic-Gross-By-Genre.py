import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#importing data into file and preparing it for the plots
movieData = pd.read_csv('Data.csv', encoding = 'latin1')
genre_filters = ['action', 'adventure','animation','comedy','drama' ]
movieFilters = movieData[movieData.Genre.isin(genre_filters)]
data = movieFilters[(movieFilters.Studio == 'Buena Vista Studios') | (movieFilters.Studio == 'Fox') | (movieFilters.Studio == 'Paramount Pictures') | (movieFilters.Studio == 'Sony') | (movieFilters.Studio == 'Universal') | (movieFilters.Studio == 'WB')]

def plot():
    #Setting style of graph window
    sns.set(style="white",color_codes=True)
    ax = plt.subplot()
    #Creating and styling strip plot and boxplot
    sns.boxplot(data=data, x='Genre', y='Gross % US',orient='v',  showfliers=False, palette="YlOrRd")
    sns.stripplot(data=data, x='Genre', y='Gross % US',jitter=True,size=6, linewidth=0, hue = 'Studio', alpha=0.7)
    #Setting title of the graph
    ax.axes.set_title('Domestic Gross by Genre',fontsize=30)
    #Setting names and fonts for x and y axis
    ax.set_xlabel('Genre',fontsize=20)
    ax.set_ylabel('Gross in US (%)',fontsize=20)
    #Stying the legend and setting its position
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    ax.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.,frameon=True,fancybox=True,shadow=True,framealpha=1)
    #Setting window title
    plt.gcf().canvas.set_window_title('Domestic Gross by Genre (%)')
    plt.show()

plot()