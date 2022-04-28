# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import csv
ttd28="""{"ttdDate":"2022-03-29T00:00:00Z","requests":[{"procedureType":"Port","serviceNumber":"93556656","abdId":"5681","gwId":57,"donorCarrierId":"0002","receiverCarrierId":"0001","procedureNumber":10000005357},{"procedureType":"Port","serviceNumber":"96222260","abdId":"5603","gwId":57,"donorCarrierId":"0003","receiverCarrierId":"0001","procedureNumber":10000005349},{"procedureType":"Port","serviceNumber":"96222261","abdId":"5604","gwId":57,"donorCarrierId":"0003","receiverCarrierId":"0001","procedureNumber":10000005349},{"procedureType":"Port","serviceNumber":"96222262","abdId":"5605","gwId":57,"donorCarrierId":"0003","receiverCarrierId":"0001","procedureNumber":10000005349},{"procedureType":"Port","serviceNumber":"96222263","abdId":"5606","gwId":57,"donorCarrierId":"0003","receiverCarrierId":"0001","procedureNumber":10000005349},{"procedureType":"Port","serviceNumber":"96222264","abdId":"5607","gwId":57,"donorCarrierId":"0003","receiverCarrierId":"0001","procedureNumber":10000005349}]}"""

def cantidad_request(ttd):
    jsonttd = json.loads(ttd)
    return (len(jsonttd['requests']))

def cantidad_warn(log):
    arc="D:\\Isbel\\Portabilidad\\Logs\\"+log
    procedures = []
    lineas=[]
    with open(arc, "r") as archivo:
        for l in archivo:
            sub_1=l.split("solicitud_portabilidad_")
            if len(sub_1) >= 2:
                sub_2=sub_1[1].split("-Certificado.pdf.PDF")
                #print(sub_2[0])
                if sub_2[0] not in procedures:
                    procedures.append(sub_2[0])
                    lineas.append(l)
    return procedures,lineas

def cantidad_donor_request(log):
    arc="D:\\Isbel\\Portabilidad\\Logs\\"+log
    lineas=[]
    with open(arc, "r") as archivo:
        for l in archivo:
            sub_1=l.split("Data:  ")
            if len(sub_1) >= 2:
                ti=sub_1[0].split(" [debug]")
                l2=json.loads(sub_1[1])
                #l=sub_1[1]
                print(l2.keys())
                lineas.append("Día: 15/04   Hora: "+str(ti[0])+"     Mensaje: "+str(l2['body']))
                #lineas.append(l)
    return lineas

def cantidad_donor_failed(log):
    arc="D:\\Isbel\\Portabilidad\\Logs\\"+log
    lineas=[]
    with open(arc, "r") as archivo:
        for l in archivo:
            sub_1=l.split("New Request ")
            if len(sub_1) >= 2:
                ti=sub_1[0].split(" [info]")
                l2=json.loads(sub_1[1])
                #l=sub_1[1]
                print(l2['SOAMessage'].keys())
                lineas.append("Día: 15/04   Hora: "+str(ti[0])+"     Mensaje: "+str(l2))
                #lineas.append(l)
    return lineas

def gtw_errores(log):
    arc = "D:\\Isbel\\Portabilidad\\Logs\\" + log
    lineas = []
    gwids=[]
    with open(arc, "r") as archivo:
        for l in archivo:
            subl=l.split("[")
            gwid=subl[6].split("]")[0]
            if gwid not in gwids:
                gwids.append(gwid)
    return gwids

def gtw_errores_abd(log):
    arc = "D:\\Isbel\\Portabilidad\\Logs\\" + log
    lineas = []
    gwids=[]
    with open(arc, "r") as archivo:
        for l in archivo:
            subl = l.split("[")
            gwid = subl[6].split("]")[0]
            subl2=l.split("Call Service Error:  ")
            eljs=json.loads(subl2[1])
            #print(eljs['exception'])
            #subl2=l.split("[GTW][")[1].split("][sendABDRequest]")[0]
            subl3 = l.split("<invoke_id>")[1].split("<")[0]

            linea="GW ID "+str(gwid)+"   Invoke id "+subl3+"    Error: "+str(eljs['exception']['status'])+" "+eljs['exception']['statusText']+"    Fecha: "+eljs['exception']['headers']['date']
            lineas.append(linea)
    return lineas

def file_content(log):
    arc = "D:\\Isbel\\Portabilidad\\Logs\\" + log
    lineas = []
    with open(arc, "r") as archivo:
        for l in archivo:
            subl = l.split("<file_content>")
            lineas.append(subl[1].split("</file_content>")[0])
    print(lineas[0])


if __name__ == '__main__':
    y = file_content("file_content.txt")
    #print(len(y))
    #print(len(x))
    #print(x)
    list_num=""
    print(y[0])
    #for i in y:
    #    print(i)
     #   list_num+=i+"|"
    #print(list_num)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
