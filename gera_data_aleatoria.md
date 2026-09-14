# 📅 Gerador de Data Aleatória — Sikuli IDE

Exemplo de implementação de um **gerador de datas aleatórias utilizando Sikuli IDE e Jython**.

A implementação utiliza as bibliotecas `datetime` e `random` para gerar uma data dentro de um intervalo definido e posteriormente convertê-la para o formato `dd/mm/aaaa`.

Esse recurso pode ser utilizado em testes automatizados que necessitam de **datas de teste dinâmicas**, evitando a utilização repetitiva de uma data fixa.

---

## 🎯 Objetivo

A implementação permite:

* Gerar uma data de forma randômica;
* Definir um intervalo de anos;
* Definir o mês aleatoriamente;
* Definir o dia aleatoriamente;
* Evitar a geração de datas inválidas;
* Converter a data para o formato `dd/mm/aaaa`;
* Exibir a data gerada em um popup;
* Registrar a data utilizada no log do Sikuli.

A cada nova execução, uma nova data pode ser gerada dentro dos intervalos definidos.

---

## 📦 Bibliotecas utilizadas

As bibliotecas devem ser declaradas no início do script:

```python
import datetime
import random
```

### `random`

A biblioteca `random` é utilizada para gerar valores aleatórios para **ano**, **mês** e **dia**.

### `datetime`

A biblioteca `datetime` é utilizada para criar e manipular a data, exemplo: `datetime.date(year, month, day)`.

---

## 📆 Definindo o intervalo da data

O código define os valores que serão utilizados para gerar a data:

```python
year = random.randint(1950, 2016)
month = random.randint(1, 12)
day = random.randint(1, 28)
```

Nesse exemplo:

| Campo | Intervalo         |
| ----- | ----------------- |
| Ano   | `1950` até `2016` |
| Mês   | `1` até `12`      |
| Dia   | `1` até `28`      |

O `random.randint()` retorna um número inteiro aleatório dentro do intervalo informado, incluindo os valores inicial e final.

Por exemplo, `random.randint(1950, 2016)` pode retornar:

```text
1950
1978
1992
2005
2016
```

---

## 📅 Por que utilizar dias de 1 a 28?

O dia foi limitado ao intervalo: `day = random.randint(1, 28)`. Essa decisão evita a geração de datas inválidas.

Por exemplo, fevereiro pode possuir apenas 28 dias em um ano comum. Se fossem utilizados dias até `31`, seria possível tentar criar uma data como `31/02/2011` que não existe.

Ao limitar o intervalo até `28`, qualquer combinação de ano, mês e dia será uma data válida.

### ⚠️ Limitação dessa abordagem

Embora seja uma solução simples para evitar datas inválidas, existe uma consequência: **os dias 29, 30 e 31 nunca serão gerados.**

Por exemplo:

```text
01/01/2000  → pode ser gerada
28/02/2000  → pode ser gerada
29/02/2000  → nunca será gerada
30/01/2000  → nunca será gerada
31/01/2000  → nunca será gerada
```

Portanto, essa implementação é adequada quando o objetivo é simplesmente obter uma **data válida aleatória**, mas pode ser melhorada caso o teste precise representar todo o calendário.

---

## 🧱 Criando a data

Depois que ano, mês e dia são definidos, podemos criar um objeto `date`:

```python
data = datetime.date(year, month, day)
```

Por exemplo, supondo que os valores gerados sejam:

```text
year  = 1985
month = 7
day   = 18
```

o resultado será equivalente a `1985-07-18`. Nesse momento, `data` é um objeto do tipo `date`.

---

## 🔄 Convertendo para `dd/mm/aaaa`

O formato retornado pelo `datetime.date` é `aaaa-mm-dd`. Para utilizar o formato mais comum `dd/mm/aaaa`, é utilizado o método `strftime()`:

```python
dtNascto = data.strftime('%d/%m/%Y')
```

Os códigos utilizados no formato são:

| Código | Significado            |
| ------ | ---------------------- |
| `%d`   | Dia                    |
| `%m`   | Mês                    |
| `%Y`   | Ano com quatro dígitos |

Assim, `data.strftime('%d/%m/%Y')` pode transformar `1985-07-18` em `18/07/1985`. O resultado é armazenado na variável `dtNascto`.

---

## ▶️ Script completo

O código abaixo pode ser copiado e executado diretamente no **Sikuli IDE**:

```python
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
```

---

## 🖥️ Resultado esperado

Ao executar o script, será exibido um popup semelhante a:

```text
Script de teste finalizado com sucesso!

Data gerada: 18/07/1985
```

O log do Sikuli também apresentará: `Data de nascimento gerada: 18/07/1985`.

A data será escolhida aleatoriamente dentro dos intervalos definidos. Por exemplo, uma execução pode gerar `12/03/1978` e outra `27/11/2004`.

---

## 📝 Registro no log

É recomendável registrar a data logo depois que ela for gerada: `print('Data de nascimento gerada: %s' % dtNascto)`. Isso permite identificar qual data foi utilizada caso ocorra uma falha posteriormente.

Por exemplo, em `Data de nascimento gerada: 12/03/1978`, se o script apresentar um erro antes de chegar ao `popup()`, o log ainda poderá indicar a data utilizada naquela execução.

---

## 🧪 Utilizando a data durante um teste

Depois de armazenada em `dtNascto`, a data pode ser utilizada em outras etapas da automação. Por exemplo:

```python
dtNascto = data.strftime('%d/%m/%Y')

print('Data utilizada no teste: %s' % dtNascto)

click('CampoData.png')
type(dtNascto)

click('BotaoContinuar.png')
```

Nesse cenário, o teste:

1. Gera uma data;
2. Converte para `dd/mm/aaaa`;
3. Registra a data no log;
4. Localiza o campo de data;
5. Preenche a data;
6. Continua a execução.

---

## 📌 Fluxo da implementação

O funcionamento pode ser resumido da seguinte maneira:

```text
Bibliotecas
    │
    ├── datetime
    └── random
          │
          ▼
Geração aleatória
    │
    ├── Ano: 1950–2016
    ├── Mês: 1–12
    └── Dia: 1–28
          │
          ▼
datetime.date()
          │
          ▼
Data no formato aaaa-mm-dd
          │
          ▼
strftime('%d/%m/%Y')
          │
          ▼
Data no formato dd/mm/aaaa
          │
          ├── Log do Sikuli
          └── Popup / utilização no teste
```

---

## ⚠️ Observações

### Intervalo de anos

O intervalo utilizado neste exemplo é `random.randint(1950, 2016)`. Esses valores são apenas uma configuração do exemplo e podem ser alterados conforme a necessidade do teste, exemplo: `year = random.randint(1980, 2020)`.

### Intervalo de dias

A utilização de: `day = random.randint(1, 28)` garante uma data válida para qualquer mês, mas restringe a geração aos primeiros 28 dias.

Se o objetivo do teste for exercitar situações envolvendo:

* 29 de fevereiro;
* meses com 30 dias;
* meses com 31 dias;
* anos bissextos;

será necessário utilizar uma estratégia diferente para determinar o último dia de cada mês.

---

## 🛠️ Possíveis melhorias

A implementação pode ser evoluída para:

* Gerar qualquer dia válido do mês;
* Considerar anos bissextos;
* Gerar datas entre duas datas específicas;
* Gerar datas futuras;
* Gerar datas passadas;
* Gerar datas de nascimento considerando uma faixa etária;
* Gerar datas úteis;
* Gerar datas com diferentes formatos;
* Criar uma biblioteca reutilizável de dados de teste.

Por exemplo, uma evolução interessante seria substituir o limite fixo de `28` por uma lógica que identifique automaticamente a quantidade de dias existente em cada mês.

---

## 📋 Resumo

| Recurso            | Finalidade                           |
| ------------------ | ------------------------------------ |
| `random`           | Gerar valores aleatórios             |
| `random.randint()` | Gerar números dentro de um intervalo |
| `datetime.date()`  | Criar uma data                       |
| `strftime()`       | Formatar a data                      |
| `%d`               | Dia                                  |
| `%m`               | Mês                                  |
| `%Y`               | Ano com quatro dígitos               |
| `print()`          | Registrar a data no log              |
| `popup()`          | Exibir a data na tela                |
| `dtNascto`         | Armazenar a data formatada           |

---

**Este exemplo foi criado como material de estudo e referência para geração de dados de teste utilizando Sikuli IDE.**
