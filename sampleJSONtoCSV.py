#uniquement pour les mesures en continu
import pandas as pd
import json

def sampleValuesJSONToCSV(file,wavelength=[1.07,1.2,1.55,1.65]):
    """ convertit le fichier de mesures json en csv pour ouvrir avec excel plus vite
        il faut renseigner le chemin du fichier json et vérifier que le 
        nombre de longueurs d'onde est toujours de 4 (sinon changer wavelength=[...])
    """
    dfsample = pd.read_json(file) #Separating json in dataframes
    contTimeList = pd.DataFrame(dfsample['contTimeList'].tolist()) 
    contTempListCel = pd.DataFrame(dfsample['contTempListCel'].tolist())
    contEpsList = pd.DataFrame(dfsample['contEpsList'].tolist())
    contPower = pd.DataFrame(dfsample['contPower'].tolist())
    contLuminanceSample = pd.DataFrame(dfsample['contLuminanceSample'].tolist())
    contLuminanceFit = pd.DataFrame(dfsample['contLuminanceFit'].tolist())
    contResiduals = pd.DataFrame(dfsample['contResiduals'].tolist())
    contResidualsPercent = pd.DataFrame(dfsample['contResidualsPercent'].tolist())
    
    csvdfsample = pd.concat([contTimeList,contTempListCel,contEpsList,contPower,
                              contLuminanceSample,contLuminanceFit,contResiduals,
                              contResidualsPercent], axis=1) #merging dataframes
    
    
    wavelength = [1.07,1.2,1.55,1.65]
    p = len(wavelength)
    fieldnames = ['contTimeList', 'contTempListCel', 'contEpsList'] # csv header
    for i in range(p): #créer le header
        fieldnames.append('Power'+str(i+1))
    for i in range(p):
        fieldnames.append('LuminanceSample'+str(i+1))
    for i in range(p):
        fieldnames.append('LuminanceFit'+str(i+1))
    for i in range(p):
        fieldnames.append('Residuals'+str(i+1))
    for i in range(p):
        fieldnames.append('Residuals(%)'+str(i+1))
    
    csvdfsample.to_csv(file+".csv",index=False,header=fieldnames,sep=';') #converting to csv
  
sampleValuesJSONToCSV(file="data/Sample27_07_2022_13_59_42continuous_sample_values.json") #changer le nom du fichier



# with open(file="data/combined.json") as o: #ouvrir un fichier json qui contient les valeurs "combinées" de EDGAR (plus utile car organisation des valeurs différentes)
#     val = json.load(o)
# power=[] #créer une liste des puissances

# for i in val["combinedResults"]: #pour chaque mesure
#     power.append(i[0]) #ajouter les puissances à la liste
    
# with open("data/power.json", 'w', encoding='utf-8') as file:  
#     json.dump(power, file, ensure_ascii=False, indent=2) #sauvegarder les puissances dans un fichier json 

# with open(file="data/power.json") as o: #ouvrir un fichier json
#     power = json.load(o)
