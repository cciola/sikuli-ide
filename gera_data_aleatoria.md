# Gerador de Data Aleatória

A função apresentada neste exemplo utiliza as bibliotecas `datetime` e `random` para gerar uma data dentro de um intervalo definido e posteriormente convertê-la para o formato `dd/mm/aaaa`. Esse recurso pode ser utilizado em testes automatizados que necessitam de **datas de teste dinâmicas**, evitando a utilização repetitiva de uma data fixa.

## Explicação detalhada

A biblioteca `random` é utilizada para gerar valores aleatórios para **ano**, **mês** e **dia**. A biblioteca `datetime` é utilizada para criar e manipular a data, exemplo: `datetime.date(year, month, day)`. Ambas devem ser declaradas no início do script.

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

O `random.randint()` retorna um número inteiro aleatório dentro do intervalo informado, incluindo os valores inicial e final. Por exemplo, `random.randint(1950, 2016)` pode retornar `1950, 1978, 1992, 2005, 2016`.

O dia foi limitado ao intervalo de **1** a **28** `day = random.randint(1, 28)`. Essa decisão evita a geração de datas inválidas.

Por exemplo, fevereiro pode possuir apenas 28 dias em um ano comum. Se fossem utilizados dias até `31`, seria possível tentar criar uma data como `31/02/2011` que não existe. Ao limitar o intervalo até `28`, qualquer combinação de ano, mês e dia será uma data válida.

Embora seja uma solução simples para evitar datas inválidas, existe uma consequência: **os dias 29, 30 e 31 nunca serão gerados.** Portanto, essa implementação é adequada quando o objetivo é simplesmente obter uma **data válida aleatória**, mas pode ser melhorada caso o teste precise representar todo o calendário.

Depois que ano, mês e dia são definidos, podemos criar um objeto **date**: `data = datetime.date(year, month, day)`. Supondo que os valores gerados sejam `year = 1985`, `month = 7`, e `day = 18`, o resultado será equivalente a `1985-07-18`. Nesse momento, `data` é um objeto do tipo `date`.

O formato retornado pelo `datetime.date` é `aaaa-mm-dd`. Para utilizar o formato mais comum `dd/mm/aaaa`, é utilizado o método **strftime()**: `dtNascto = data.strftime('%d/%m/%Y')`.

Os códigos utilizados no formato são:

| Código | Significado            |
| ------ | ---------------------- |
| `%d`   | Dia                    |
| `%m`   | Mês                    |
| `%Y`   | Ano com quatro dígitos |

Assim, `data.strftime('%d/%m/%Y')` pode transformar `1985-07-18` em `18/07/1985`. O resultado é armazenado na variável `dtNascto`.

---

## Veja o método funcionando

📜 **[gera_data_aleatoria.py](./scripts/gera_data_aleatoria.py)**

Ao executar o script, será exibido um popup semelhante a:

```text
Script de teste finalizado com sucesso!
Data gerada: 18/07/1985
```

O log do Sikuli também apresentará: `Data de nascimento gerada: 18/07/1985`. A data será escolhida aleatoriamente dentro dos intervalos definidos. Por exemplo, uma execução pode gerar `12/03/1978` e outra `27/11/2004`.

### Por que registrar no log?

É recomendável registrar a data logo depois que ela for gerada: `print('Data de nascimento gerada: %s' % dtNascto)`, pois isso permite identificar qual data foi utilizada caso ocorra uma falha posteriormente. Por exemplo, em `Data de nascimento gerada: 12/03/1978`, se o script apresentar um erro antes de chegar ao `popup()`, o log ainda poderá indicar a data utilizada naquela execução.

Depois de armazenada em `dtNascto`, a data pode ser utilizada em outras etapas da automação. Por exemplo:

```python
dtNascto = data.strftime('%d/%m/%Y')

print('Data utilizada no teste: %s' % dtNascto)

click('CampoData.png')
type(dtNascto)

click('BotaoContinuar.png')
```

## Observações

* **Intervalo de anos:** o intervalo utilizado neste exemplo é `random.randint(1950, 2016)`. Esses valores são apenas uma configuração do exemplo e podem ser alterados conforme a necessidade do teste, exemplo: `year = random.randint(1980, 2020)`.

* **Intervalo de dias:** a utilização de: `day = random.randint(1, 28)` garante uma data válida para qualquer mês, mas restringe a geração aos primeiros 28 dias.

Se o objetivo do teste for exercitar situações envolvendo **29 de fevereiro**, **meses com 30 dias**, **meses com 31 dias** ou **anos bissextos**, será necessário utilizar uma estratégia diferente para determinar o último dia de cada mês.
