import random


# Função para gerar CPF válido de forma randômica
def cpf_funcional_func():
    n = [random.randrange(10) for i in xrange(9)]

    # Calcula o primeiro dígito verificador
    s = sum(x * y for x, y in zip(n, range(10, 1, -1)))
    d1 = 11 - s % 11

    if d1 >= 10:
        d1 = 0

    n.append(d1)

    # Calcula o segundo dígito verificador
    s = sum(x * y for x, y in zip(n, range(11, 1, -1)))
    d2 = 11 - s % 11

    if d2 >= 10:
        d2 = 0

    n.append(d2)

    return "%d%d%d%d%d%d%d%d%d%d%d" % tuple(n)


# Gera o CPF e armazena o resultado
numCPF = cpf_funcional_func()

# Exibe o CPF no log
print('CPF gerado: %s' % numCPF)

# Exibe o CPF em um popup
popup(
    'Script de teste finalizado com sucesso! '
    '\nCPF gerado: %s' % numCPF
)

wait(1)
exit()