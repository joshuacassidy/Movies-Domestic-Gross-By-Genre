import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

movieData = pd.read_csv('Data.csv', encoding = 'latin1')
genre_filters = ['action', 'adventure','animation','comedy','drama' ]
movieFilters = movieData[movieData.Genre.isin(genre_filters)]
data = movieFilters[(movieFilters.Studio == 'Buena Vista Studios') | (movieFilters.Studio == 'Fox') | (movieFilters.Studio == 'Paramount Pictures') | (movieFilters.Studio == 'Sony') | (movieFilters.Studio == 'Universal') | (movieFilters.Studio == 'WB')]

sns.boxplot(data=data, x='Genre', y='Gross % US',orient='v',  showfliers=False)

sns.stripplot(data=data, x='Genre', y='Gross % US',jitter=True,size=6, linewidth=0, hue = 'Studio', alpha=0.7)

plt.show()