##Abordando el problema

Mi aproximación al problema ha sido la siguiente:

    1º Lectura del enunciado y búsqueda de los ficheros necesarios
       para resolver el ejercicio planteado.
    
    2º Elección del lenguaje para abordar el problema e identificación
       de los posibles módulos que faciliten el trabajo con ficheros csv.
        En este caso me decanté por python, si bien he trabajado con 
        documentos csv a priori en java, he preferido optar por el uso 
        del módulo pandas de Python por las facilidades que aporta a 
        la hora de manejar los documentos en este formato.
    
    3º Identificación de las transformaciones necesarias de los documentos.
        Agrupación por ID del destino, obteniendo la suma  y el conteo
        del los viajes por destino. Reordenación descendente en función de
        la distancia total y selección de destinos con distancia total 
        superior al percentil 0.95. Reordenación descendente de las filas 
        restantes en función del número de viajes y selección del top 10.
        **Left join** del conjunto obtenido previamente con el segundo 
        dataframe que contiene el mapeo de ID destino -> Zona destino.
    
Para ejecutar el script es suficiente con pasarle un argumento con la ruta
de destino del fichero csv con los datos de viaje "Yellow Taxi":

_**python main.py csv_files/yellow_tripdata_2021-07.csv**_
