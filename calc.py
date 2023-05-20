def calculo_x1(x2, x3):
    return (4 + (0.1*x2) - (0.5*x3))/3

def calculo_x2(x1, x3):
    return (0 - (0.3*x1) - (0.5*x3))/5

def calculo_x3(x1, x2):
    return (4 - (0.3*x1) - (1.3*x2))/2.7

modulo_x1 = 1
modulo_x2 = 1
modulo_x3 = 1
interations = 0

def gauss_jacobi(x1, x2, x3, x1a, x2a, x3a, modulo_x1, modulo_x2, modulo_x3, interations):
    x = 0
    while x < 5:
        interations += 1
        x1 = round(calculo_x1(x2a, x3a),6)
        x2 = round(calculo_x2(x1a, x3a),6)
        x3 = round(calculo_x3(x1a, x2a),6)
        modulo_x1 = round((abs(x1-x1a)/abs(x1)),8)
        modulo_x2 = round((abs(x2-x2a)/abs(x2)),8)
        modulo_x3 = round((abs(x3-x3a)/abs(x3)),8)
        x1a = x1
        x2a = x2
        x3a = x3

        x += 1

    erro_maximo_relativo = max(modulo_x1, modulo_x2, modulo_x3)
    if (erro_maximo_relativo == modulo_x1):
        erro_maximo_absoluto = round(abs(modulo_x1*x1),6)
    elif (erro_maximo_relativo == modulo_x2):
        erro_maximo_absoluto = round(abs(modulo_x2*x2),6)
    else:
        erro_maximo_absoluto = round(abs(modulo_x3*x3),6)

    print('x1 =', x1)
    print('x2 =', x2)
    print('x3 =', x3)
    print('Iterações =', interations)
    print('Erro Máximo Absoluto =', erro_maximo_absoluto)
    print('Erro Máximo Relativo =', round(erro_maximo_relativo*100, 6), '%')

def gauss_seidel(x1, x2, x3, x1a, x2a, x3a, modulo_x1, modulo_x2, modulo_x3, interations):
    x = 0
    while x < 5:
        interations += 1
        x1 = round(calculo_x1(x2a, x3a),6)
        x2 = round(calculo_x2(x1, x3a),6)
        x3 = round(calculo_x3(x1, x2),6)
        modulo_x1 = round((abs(x1-x1a)/abs(x1)),8)
        modulo_x2 = round((abs(x2-x2a)/abs(x2)),8)
        modulo_x3 = round((abs(x3-x3a)/abs(x3)),8)
        x1a = x1
        x2a = x2
        x3a = x3

        x += 1

    erro_maximo_relativo = max(modulo_x1, modulo_x2, modulo_x3)
    if (erro_maximo_relativo == modulo_x1):
        erro_maximo_absoluto = round(abs(modulo_x1*x1),6)
    elif (erro_maximo_relativo == modulo_x2):
        erro_maximo_absoluto = round(abs(modulo_x2*x2),6)
    else:
        erro_maximo_absoluto = round(abs(modulo_x3*x3),6)

    print('x1 =', x1)
    print('x2 =', x2)
    print('x3 =', x3)
    print('Iterações =', interations)
    print('Erro Máximo Absoluto =', erro_maximo_absoluto)
    print('Erro Máximo Relativo =', round(erro_maximo_relativo*100, 6), '%')
    print('\n')

def trabalho ():
    i = 0
    while i < 4:
        if i == 0:
            print('Petterson - 3843408:\n')
            x1 = 3
            x2 = 8
            x3 = 4
        elif i == 1:
            print('Fernando - 7755287:\n')
            x1 = 7
            x2 = 7
            x3 = 5
        elif i == 2:
            print('João - 7480326:\n')
            x1 = 7
            x2 = 4
            x3 = 8
        else:
            print('Miguel - 7620586:\n')
            x1 = 7
            x2 = 6
            x3 = 2
        
        x1a = x1
        x2a = x2
        x3a = x3

        print('Gauss-Jacobi:')
        gauss_jacobi(x1, x2, x3, x1a, x2a, x3a, modulo_x1, modulo_x2, modulo_x3, interations)
        print('\nGauss-Seidel:')
        gauss_seidel(x1, x2, x3, x1a, x2a, x3a, modulo_x1, modulo_x2, modulo_x3, interations)

        i += 1
    
    return '\n\nFim do Trabalho'

print(trabalho())