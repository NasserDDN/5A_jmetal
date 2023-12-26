import pandas as pd
import matplotlib.pyplot as plt

# Pour TP1
data = pd.read_csv('FUN', delimiter=" ", names=['col1', 'col2', 'nan'])
data.sort_values(by=['col1'], ascending=False, inplace=True)
plt.plot(data['col1'], data['col2'])
plt.title("Front de pareto TP1")
plt.xlabel('F1')
plt.ylabel('F2')
plt.show()



# Pour TP2
# Lire les données depuis un fichier CSV
df = pd.read_csv('FUN_capteurs', sep=' ', header=None, names=['X', 'Y', 'nan'])

# Tri des données pour faciliter la visualisation du front de Pareto
df_sorted = df.sort_values(by='X')

# Tracer les points
plt.scatter(-df_sorted['X'], -df_sorted['Y'])

# Ajout de titres et labels (optionnel)
plt.title('Front de Pareto TP2')
plt.xlabel('F1')
plt.ylabel('F2')

# Afficher le graphique
plt.show()
