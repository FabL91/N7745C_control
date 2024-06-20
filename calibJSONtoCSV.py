import pandas as pd

def calibValuesJSONToCSV(file="data/calibration_data.json",wavelength=[1.07,1.2,1.55,1.65]):
    """ convertit le fichier de calibration json en csv pour ouvrir avec excel plus vite
        il faut renseigner le chemin du fichier json et vérifier que le 
        nombre de longueurs d'onde est toujours de 4 (sinon changer la ligne 3)
    """
    df = pd.read_json(file)
    split_lum = pd.DataFrame(df['lum_calib'].tolist()) #séparation du json en dataframes
    lum = split_lum.transpose()
    split_pow = pd.DataFrame(df['power_calib'].tolist())
    power = split_pow.transpose()
    A = pd.DataFrame(df['A'].tolist())
    B = pd.DataFrame(df['B'].tolist())
    C = pd.DataFrame(df['C'].tolist())
    
    newdf = pd.concat([A,B,C,lum,power], axis=1) #fusion des df    
    
    fieldnames = ['A', 'B', 'C'] # csv header
    for i in range(len(wavelength)): #créer le header
        fieldnames.append('Luminance'+str(i+1))
    for i in range(len(wavelength)):
        fieldnames.append('Power'+str(i+1))
    
    newdf.to_csv("data/calibration_values.csv",index=False,header=fieldnames,sep=';') #convertir

if __name__ == "__main__":
    calibValuesJSONToCSV()