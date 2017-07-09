import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

movieData = pd.read_csv('Data.csv', encoding = 'latin1')
genre_filters = ['action', 'adventure','animation','comedy','drama' ]
movieFilters = movieData[movieData.Genre.isin(genre_filters)]
data = movieFilters[(movieFilters.Studio == 'Buena Vista Studios') | (movieFilters.Studio == 'Fox') | (movieFilters.Studio == 'Paramount Pictures') | (movieFilters.Studio == 'Sony') | (movieFilters.Studio == 'Universal') | (movieFilters.Studio == 'WB')]

sns.boxplot(data=data, x='Genre', y='Gross % US')

plt.show()