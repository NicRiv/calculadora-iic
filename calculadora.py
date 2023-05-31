#!/bin/python3

import os

"""
Limpiar Pantalla
"""
def limpiar():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

"""
Es numero?
"""
def es_numero(entrada):
    """
    type <entrada> string
    """
    parte_numerica = entrada
    parte_entera = []
    parte_decimal = []

    if entrada[0] == '-':
        parte_numerica = entrada[1:]

    parte_numerica = parte_numerica.split('.')

    if len(parte_numerica) > 0 or len(parte_numerica) < 3:
        for parte in parte_numerica:
            for numero in parte:
                if numero not in '0123456789':
                    return False     
            
    return True

"""
Es fraccion?
"""
def es_fraccion(entrada):
    entrada_split =  entrada.split('/')
    if len(entrada_split) == 2:
        if es_numero(entrada_split[0]) and es_numero(entrada_split[1]):
            return True
    return False

"""
Es Signo?
"""
def es_signo(entrada):
    if len(entrada) == 1:
        if entrada in '+-*/':
            return True
    return False

"""
funciones de CONVERSION
"""
def bin(entrada):
    binario = []
    num = entrada
    while num // 2 != 0:
        print(num)
        binario.append(str(num%2))
        num = num//2
    binario.append(str(num%2))
    binario.reverse()
    binario = ''.join(binario)
    return binario

def hex(entrada):
    letras = [
        ['10', 'A'],
        ['11', 'B'],
        ['12', 'C'],
        ['13', 'D'],
        ['14', 'E'],
        ['15', 'F']
    ]
    hexadecimal = []
    num = entrada
    valor_a = None
    valor_b = None

    while num // 16 > 15:
        print(num)
        valor_a = num%16
        for letra in letras:
            if letra[0] == str(valor_a):
                valor_a = letra[1]
        hexadecimal.append(str(valor_a))
        num = num//16

    valor_a = num%16
    valor_b = num//16
    for letra in letras:
        if letra[0] == str(valor_a):
            valor_a = letra[1]
        if letra[0] == str(valor_b):
            valor_b = letra[1]

    hexadecimal.append(str(valor_a))
    hexadecimal.append(str(valor_b))
    hexadecimal.reverse()


    hexadecimal = ''.join(hexadecimal)
    return hexadecimal
    
def oct(entrada):
    octal = []
    num = entrada
    
    while num // 8 > 7:
        print(num)
        octal.append(str(num%8))
        num = num//8
    
    octal.append(str(num%8))
    octal.append(str(num//8))
    octal.reverse()
    octal = ''.join(octal)
    return octal

""" 
FUNCIONES Disponibles
"""
# Clasica
def f_clasica():    
    entrada = None
    lista_numeros = []
    mensaje = ''

    resultado = 0
    buffer_signo = ''

    while entrada != '=':
        limpiar()
        print('calculadora clasica\n')

        print(mensaje)
        print(' '.join(lista_numeros))

        print("""
        [+] sumar
        [-] restar
        [*] multiplicar
        [/] dividir
        [s] salir
        """)

        entrada = input('> ')
        if es_numero(entrada) or es_signo(entrada) or entrada == '=':
            # ingresar primer numero
            if len(lista_numeros) == 0 and es_numero(entrada):
                lista_numeros.append(entrada)
                resultado = float(entrada)

            if len(lista_numeros) % 2 != 0 and es_signo(entrada):
                lista_numeros.append(entrada)
                buffer_signo = entrada

            if len(lista_numeros) % 2 == 0 and es_numero(entrada):
                lista_numeros.append(entrada)
                
                # segun signo del buffer
                if buffer_signo == '+':
                    resultado += float(entrada)
                elif buffer_signo == '-':
                    resultado -= float(entrada)
                elif buffer_signo == '*':
                    resultado *= float(entrada)
                elif buffer_signo == '/':
                    resultado /= float(entrada)
        else:
            mensaje = f'<{entrada}> no es una entrada valida'
    
    limpiar()
    lista_numeros = ' '.join(lista_numeros)
    print(f'{lista_numeros} = {resultado}')

# Fracciones
def f_fracciones():
    entrada = None
    lista_numeros = []
    lista_operandos = []
    mensaje = ''

    numerador = -1
    denominador = -1
    resultado = 0
    buffer_signo = ''

    while entrada != '=':
        limpiar()
        print('calculadora de fracciones\n')
        print(mensaje)
        print(' '.join(lista_numeros))
        print("""
        [+] sumar
        [-] restar
        [*] multiplicar
        [/] dividir
        [s] salir
        """)

        entrada = input('> ')
       
        if es_fraccion(entrada) or es_signo(entrada) or entrada == '=':
            # primer valor
            if len(lista_numeros) == 0 and es_fraccion(entrada):
                valores_entrada = entrada.split('/')
                numerador = valores_entrada[0]
                denominador = valores_entrada[1]
                if denominador != '0':
                    lista_operandos.append([numerador, denominador])
                    lista_numeros.append(entrada)
                    resultado = entrada
                    mensaje = ''
                else:
                    mensaje = f'Math error: El denominador no puede ser cero'

            # es signo
            if len(lista_numeros) % 2 != 0 and es_signo(entrada):
                lista_numeros.append(entrada)
                buffer_signo = entrada

            # extraer valores de la fraccion
            if len(lista_numeros) > 0 and len(lista_numeros) % 2 == 0 and es_fraccion(entrada):
                valores_entrada = entrada.split('/')
                numerador = float(valores_entrada[0])
                denominador = float(valores_entrada[1])
                if denominador != 0:
                    # lista_operandos.append([numerador, denominador])
                    lista_numeros.append(entrada)
                    
                    # extraer resultado
                    valor_resultado = resultado.split('/')
                    numerador_resultado = float(valor_resultado[0])
                    denominador_resultado = float(valor_resultado[1])

                    # Operacion
                    if buffer_signo == '+':
                        nuevo_numerador = (numerador_resultado * denominador) + (denominador_resultado * numerador)
                        nuevo_denominador = denominador_resultado * denominador
                        resultado = str(f'{nuevo_numerador}/{nuevo_denominador}')
                    if buffer_signo == '-':
                        nuevo_numerador = (numerador_resultado * denominador) - (denominador_resultado * numerador)
                        nuevo_denominador = denominador_resultado * denominador
                        resultado = str(f'{nuevo_numerador}/{nuevo_denominador}')
                    if buffer_signo == '*':
                        nuevo_numerador = numerador_resultado * numerador
                        nuevo_denominador = denominador_resultado * denominador
                        resultado = str(f'{nuevo_numerador}/{nuevo_denominador}')
                    if buffer_signo == '/':
                        nuevo_numerador = numerador_resultado * denominador
                        nuevo_denominador = denominador_resultado * numerador
                        resultado = str(f'{nuevo_numerador}/{nuevo_denominador}')
                else:
                    mensaje = f'Math error: El denominador no puede ser cero'
        else:
            mensaje = f'<{entrada}> no es una entrada valida'
    
    limpiar()
    lista_numeros = ' '.join(lista_numeros)
    print(f'{lista_numeros} = {resultado}')

# Conversion
def f_conversion():
    entrada = ''
    mensaje = ''
    resultado = ''
    numero_ingresado = ''

    while entrada != '=':
        limpiar()
        print('calculadora de conversion\n')
        print(mensaje)
        print(numero_ingresado)
        print("""
        [bin] binario
        [hex] hexadecimal
        [oct] octal
        """)

        entrada = input('> ')

        # ya hay un numero para convertir
        if numero_ingresado != '':
            if entrada == 'bin':
                resultado = bin(int(numero_ingresado))
                break
            elif entrada == 'hex':
                resultado = hex(int(numero_ingresado))
                break
            elif entrada == 'oct':
                resultado = oct(int(numero_ingresado))
                break
            else:
                mensaje = f'La opcion <{entrada}> no esta disponible'    

        # ingresa numero decimal
        if es_numero(entrada) and numero_ingresado == '':
            if int(entrada) >= 0 and int(entrada) % 1 == 0:
                numero_ingresado = entrada
            else:
                mensaje = f'El numero <{entrada}> no es entero positivo'
        else:
            mensaje = 'Ingrese un numero decimal entero positivo'   

    limpiar()
    print(f'{numero_ingresado} -> {resultado}')


"""
**********
** MENU **
**********
"""
def menu():
    limpiar()
    
    opcion = -1
    while opcion != 4:
        # Menu
        print("""
        1) calculadora clasica
        2) calculadora de fracciones
        3) calculadora de conversiones
        4) salir
        """)

        # prompt
        opcion = input('> ')
        if opcion in '1234':
            opcion = int(opcion)      
        else:
            limpiar()
            print(f"La opcion ingresada <{opcion}> no es valida.")
            opcion = -1

        # funciones
        if opcion == 1:
            f_clasica()
        if opcion == 2:
            f_fracciones()
        if opcion == 3:
            f_conversion()

        # Salir
        if opcion == 4:
            print('Off')

if __name__ == '__main__':
    menu()
