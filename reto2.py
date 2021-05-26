#Reto 2 Ciclo 1, John Sora - Uninorte

#cantidad de medicamentos a distribuir
med1=int(input())
med2=int(input())

#Contadores de pacientes con Medicamentos 1 y 2 suministrados
contMed1=0
contMed2=0
#contador de pacientes
numPacientes=0

while med1>0 and med2>0:
    pSistolica=int(input())
    pDiastolica=int(input())
    
    if (pDiastolica<90 and pDiastolica<70) and (pDiastolica>0 and pSistolica>0):
        med2=med2-15
        numPacientes+=1
        contMed2+=1
    elif (pSistolica>=90 and pSistolica<130) and (pDiastolica>=70 and pDiastolica<90):
        numPacientes+=1
    elif (pSistolica>=130 and pSistolica<140) and (pDiastolica>=90 and pDiastolica<95):
        numPacientes+=1
    elif (pSistolica>=140 and pSistolica<150) and (pDiastolica>=95 and pDiastolica<100):
        med1=med1-10
        numPacientes+=1
        contMed1+=1
    elif (pSistolica>=150 and pSistolica<170) and (pDiastolica>=100 and pDiastolica<110):
        med1=med1-10
        numPacientes+=1
        contMed1+=1
    elif (pSistolica>=170 and pSistolica<190) and (pDiastolica>=110 and pDiastolica<120):
        med1=med1-20
        numPacientes+=1
        contMed1+=1
    elif pSistolica>=190 and pDiastolica>=120:
        med1=med1-50
        numPacientes+=1
        contMed1+=1
    elif pSistolica>=150 and pDiastolica<100:
        med1=med1-20
        numPacientes+=1
        contMed1+=1
else:
    promedioM1=0
    promedioM2=0
    if numPacientes==0:
        print(numPacientes)
        #la expresión f"{X:.2f}" donde X es el valor a formatear y el 2 el número de decimales 
        print(contMed1,f"{promedioM1:.2f}"+"%")
        print(contMed2,f"{promedioM2:.2f}"+"%")
    else:
        promedioM1=(contMed1/numPacientes)*100
        promedioM2=(contMed2/numPacientes)*100
        print(numPacientes)
        print(contMed1,f"{promedioM1:.2f}"+"%")
        print(contMed2,f"{promedioM2:.2f}"+"%")
    