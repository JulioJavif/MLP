import csv

class load_OSI:

    feature_names = []
    data = []
    target = []
    count = 0

    meses = {
        "Jan":1,
        "Feb":2,
        "Mar":3,
        "Apr":4,
        "May":5,
        "June":6,
        "Jul":7,
        "Aug":8,
        "Sep":9,
        "Oct":10,
        "Nov":11,
        "Dec":12
    }

    tipo_visitante = {
        "New_Visitor":0,
        "Returning_Visitor":1,
        "Other":2
    }

    booleano = {
        "TRUE":1,
        "FALSE":0
    }

    def __init__(self) -> None:
        pass


    with open('online_shoppers_intention.csv', newline='') as File:
        reader = csv.reader(File)
        i = -1
        for row in reader:
            if i == -1:
                feature_names.append(row[2])
                feature_names.append(row[3])
                feature_names.append(row[4])
                feature_names.append(row[5])
                feature_names.append(row[8])
                feature_names.append(row[9])
                feature_names.append(row[10])
                feature_names.append(row[15])
                feature_names.append(row[16])
                #feature_names.append(row[17])
                i = i + 1
                continue
            aux = []
            aux.append(row[2])
            aux.append(row[3])
            aux.append(row[4])
            aux.append(row[5])
            aux.append(row[8])
            aux.append(row[9])
            aux.append(meses[row[10]])#Mes
            aux.append(tipo_visitante[row[15]])#Tipo visitante
            aux.append(booleano[row[16]])#Fin de semana
            #aux.append(row[17])
            data.append(aux)
            target.append(booleano[row[17]])
            i = i + 1
        count = i