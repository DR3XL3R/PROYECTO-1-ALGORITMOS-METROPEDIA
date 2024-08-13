from util import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

class CsvModule:

    def option1(self):
        df = pd.read_csv('Modules\csv\characters.csv')
        planet_counts = df['homeworld'].value_counts()

        # Crear un gráfico de barras
        plt.figure(figsize=(10, 6))
        planet_counts.plot(kind='bar', color='skyblue')

        # Personalizar el gráfico
        plt.title('Cantidad de personajes nacidos en cada planeta')
        plt.xlabel('Planeta')
        plt.ylabel('Cantidad de personajes')
        plt.xticks(rotation=45, ha='right')

        # Mostrar el gráfico
        plt.tight_layout()
        plt.show()


    def option2(self):
        import pandas as pd
        import matplotlib.pyplot as plt
        import seaborn as sns

        # Leer el archivo CSV
        df = pd.read_csv('Modules\\csv\\starships.csv')

        # Filtrar las columnas necesarias
        columns = ['name', 'length', 'cargo_capacity', 'hyperdrive_rating', 'MGLT']
        df_filtered = df[columns].dropna()

        # Convertir a tipo numérico las columnas necesarias
        df_filtered['length'] = pd.to_numeric(df_filtered['length'], errors='coerce')
        df_filtered['cargo_capacity'] = pd.to_numeric(df_filtered['cargo_capacity'], errors='coerce')
        df_filtered['hyperdrive_rating'] = pd.to_numeric(df_filtered['hyperdrive_rating'], errors='coerce')
        df_filtered['MGLT'] = pd.to_numeric(df_filtered['MGLT'], errors='coerce')

        # Eliminar filas con valores NaN después de la conversión
        df_filtered = df_filtered.dropna()

        # Gráfico de comparación de longitud
        plt.figure(figsize=(10, 6))
        sns.barplot(x='length', y='name', data=df_filtered.sort_values('length', ascending=False))
        plt.title('Comparación de la Longitud de las Naves')
        plt.xlabel('Longitud')
        plt.ylabel('Nave')
        plt.show()

        # Gráfico de comparación de capacidad de carga
        plt.figure(figsize=(10, 6))
        sns.barplot(x='cargo_capacity', y='name', data=df_filtered.sort_values('cargo_capacity', ascending=False))
        plt.title('Comparación de la Capacidad de Carga de las Naves')
        plt.xlabel('Capacidad de Carga')
        plt.ylabel('Nave')
        plt.show()

        # Gráfico de comparación de clasificación de hiperimpulsor
        plt.figure(figsize=(10, 6))
        sns.barplot(x='hyperdrive_rating', y='name', data=df_filtered.sort_values('hyperdrive_rating'))
        plt.title('Comparación de la Clasificación de Hiperimpulsor de las Naves')
        plt.xlabel('Clasificación de Hiperimpulsor')
        plt.ylabel('Nave')
        plt.show()

        # Gráfico de comparación de MGLT
        plt.figure(figsize=(10, 6))
        sns.barplot(x='MGLT', y='name', data=df_filtered.sort_values('MGLT', ascending=False))
        plt.title('Comparación de MGLT de las Naves')
        plt.xlabel('MGLT')
        plt.ylabel('Nave')
        plt.show()