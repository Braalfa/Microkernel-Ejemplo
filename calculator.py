import subprocess

plugins = {
    'resta' : 'subs.py',
    'multiplicacion' : 'mul.py',
}

op1 = int(input("Cual es el operando 1?\n"))
op2 = int(input("Cual es el operando 2?\n"))

operacion = input("Que operacion desea realizar?\n")

if operacion == "suma":
    print("El resultado es " + str(op1+op2))
else:
    plugin = plugins.get(operacion)
    if plugin != None:
        proc = subprocess.Popen(['python', plugin, str(op1), str(op2)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        result = proc.communicate()[0]
        print(result.decode("utf-8")[:-2])
    else:
        print('Operacion no soportada')

