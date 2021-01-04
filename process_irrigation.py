import json
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 
def clean_data(data):
    for i in range(len(data)):
        if data[i]==200:
            data[i]=np.nan #retourner tout les donnees egale 200 a nan
    return data
with open('tp\data.json') as fich:
    data_dict = json.load(fich)
#myjsonfile=open('tp\data.json','r')
#jsondata=myjsonfile.read()
json_data = json.loads(jsondata) #transformer fichier json en dictionnaire
data1=file1["datasets"]["data"]
data2=file2["datasets"]["data"]
data3=file3["datasets"]["data"]
file1 = json_data[0]
file2 = json_data[1]
file3 = json_data[2]
label1=file1["datasets"]["label"]
label2=file2["datasets"]["label"]
label3=file3["datasets"]["label"]
time_index=file1["labels"]
humidity_dataframe = pd.DataFrame(
data={
    label1: data1,
    label2: data2,
    label3: data3,
    },
    index=time_index,
    dtype='float'
)
humidity_dataframe.index = pd.to_datetime(humidity_dataframe.index)
humidity_dataframe[label1]=clean_data(data1)
humidity_dataframe[label2]=clean_data(data2)
humidity_dataframe[label3]=clean_data(data3)
def save_plot_to_file(dataframe,title, labels, start_date, end_date, filename):
    #print(dir(plt)) 
    index= humidity_dataframe[start_date:end_date].index
    j=0
    #subdivisera la zone de graph en 3 subplots
    fig, axs=plt.subplots(3,sharex=True,sharey=True,figsize=(10,10)) #créera une figure de 10x10 pouces
    plt.ylim(bottom=0)
    fig.autofmt_xdate()
    plt.rcParams["figure.dpi"]=100 #créera une figure en 100dpi
    plt.ylim(top=200)
    axs[0].set_title(title)
    for i in labels:
        values = humidity_dataframe[start_date:end_date][i].values
        #diviser l'axe j 
        #Colorier ces zones
        axs[j].fill_between(index,15,0,facecolor="#FC33FF",alpha=0.2)
        axs[j].fill_between(index,30,15,facecolor="orange",alpha=0.2)
        axs[j].fill_between(index,60,30,facecolor="#ADFF2F",alpha=0.2)
        axs[j].fill_between(index,100,60,facecolor="#FBFD92",alpha=0.2)
        axs[j].fill_between(index,200,100,facecolor="#FC33FF",alpha=0.2)
        axs[j].margins(0) #sansmarge
        axs[j].set_yticks([7.5,22.5,45,80,150])
        axs[j].plot(index, values, label=i)
        axs[j].legend(loc="upper left") #placée dans le coin en haut à gauche
        axs[j].set_yticklabels(["saturated","too wet","perfect","plan to water","dry"])
save_plot_to_file(humidity_dataframe[label1],"Irrigation june 2020", [label1, label2, label3], "2020-06-01", "2020-06-29","data.json")
save_plot_to_file(humidity_dataframe[label2],"Irrigation july 2020", [label1, label2, label3], "2020-07-05", "2020-07-29","data.json")
save_plot_to_file(humidity_dataframe[label3],"Irrigation august 2020", [label1, label2, label3], "2020-08-05", "2020-08-29","data.json")
