
import datetime
import random


# Gera ano, mês e dia de forma randômica
year = random.randint(1950, 2016)
month = random.randint(1, 12)
day = random.randint(1, 28)

# Cria a data
data = datetime.date(year, month, day)

# Converte a data para o formato dd/mm/aaaa
dtNascto = data.strftime('%d/%m/%Y')

# Registra a data no log
print('Data de nascimento gerada: %s' % dtNascto)

wait(2)

# Exibe a data em um popup
popup(
    'Script de teste finalizado com sucesso! '
    '\nData gerada: %s' % dtNascto,
    'Alerta do Sikuli'
)

wait(1)
exit()