import sqlite3
import json

def export2json(filename):
    conn = sqlite3.connect('data/tsp.db')
    cursor = conn.cursor()
    cursor.execute('select route from TSP order by costs limit 1')
    values = cursor.fetchall()
    values_json=json.loads(values[0][0])

    coord=list()
    csv_name=filename
    file=open(csv_name,"r")
    for line in file.readlines():
        x=line.strip("\r\n").split(",")
        coord.append({'lat':x[0],'lng':x[1]})
    file.close()

    export_data=list()
    for i in range(len(values_json)):
        export_data.append(coord[values_json[i]])

    file = open("path.json", 'w')
    file.write(json.dumps(export_data))
    file.close()
