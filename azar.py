if __name__ == '__main__':
	print("hasta qué número?")
	max = int()
	adivinar = int()
	contador = int()
	entrada = int()
	max = int(input())
	adivinar = ALEATORIO(1,max)
	contador = 0
	entrada = -1
	while entrada!=0 and entrada!=adivinar:
		print("Adivina el nro entre 1 y ",max," o ingresa 0 para abandonar")
		entrada = int(input())
		contador = contador+1
		if entrada==adivinar:
			print("GANASTE en ",contador," intentos")
		else:
			if entrada>adivinar:
				print("DEMASIADO ALTO")
			else:
				print("DEMASIADO BAJO")
	print("ADIÓS")

