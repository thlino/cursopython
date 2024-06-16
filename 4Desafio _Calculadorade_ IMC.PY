## CRIAR UM PROGRAMA QUE CALCUAL MASSA CORPORAL 
### USANDO IF ELIF ELSE 

peso = float(input('digite sua peso em kg:'))
altura = float(input('digite sua altura em cm :'))
imc = peso / (altura/100)** 2

if imc < 18.5:
   print('abaixo do peso')
elif imc >= 18.5 and imc < 24.9:
   print('esta com peso normal') 
elif imc >= 25.0 and imc < 29.9:
   print('esta com sobrepeso') 

elif imc >= 30.0 and imc < 39.9:
   print('esta ja com obessidade ') 

else:
   print('Obesidade grave ')










