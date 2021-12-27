import pandas as pd
from IPython.display import display
import sys

if __name__ == '__main__':

    if(len(sys.argv) == 2):
        try:
            file_path= sys.argv[1]
            top = 10
            percentage = 1-0.95
            df1 = pd.read_csv(file_path, usecols=['DOLocationID', 'trip_distance'])
            df2 = pd.read_csv('csv_files/taxi+_zone_lookup.csv', usecols=['LocationID', 'Borough', 'Zone'])
            df2.rename(columns={'LocationID': 'DOLocationID', 'Borough': 'end_borough', 'Zone': 'end_zone'}, inplace=True)
            trips = df1.groupby('DOLocationID')['trip_distance'].agg(['sum', 'count']).sort_values(by=['sum'], ascending=False)
            trips.rename(columns={'sum': 'total_distance', 'count': 'trips'}, inplace=True)
            trips = trips.head(int(len(trips)*percentage)).sort_values(by=['trips'], ascending=False)
            result_df = pd.merge(trips.head(top), df2, on='DOLocationID', how='left')

            display(result_df[['trips', 'end_borough', 'end_zone']].to_string(index=False))
        except FileNotFoundError as e:
            print(e)

    else:
        print("Introduce la ruta de un csv valido")