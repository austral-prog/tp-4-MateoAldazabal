def leap_year():
    año = int(input("Ingrese un año: "))

    if año % 400 == 0:
    	valor = "bisiesto"
	
    elif año % 100 == 0:
	    valor = "no es bisiesto"

    elif año % 4 == 0:
	    valor = "es bisiesto"

    else: 
	    valor = "no bisiesto"

    print(f'El año {año} {valor}')
