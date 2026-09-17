# Gerador de CPF Aleatório

A função apresentada neste exemplo gera CPFs diferentes válidos e aleatórios a cada execução, calculando automaticamente os dois dígitos verificadores do documento. Esse recurso pode ser utilizado em testes automatizados que necessitam de **dados de teste dinâmicos**, evitando a utilização repetitiva de um CPF fixo.

## Detalhamento da função

A biblioteca `random` deve ser declarada no início do script. Ela será utilizada para gerar os nove primeiros dígitos do CPF de forma aleatória.

Inicialmente, são gerados nove números aleatórios na função: `n = [random.randrange(10) for i in xrange(9)]`. O resultado é armazenado na lista `n` `[5, 2, 7, 3, 1, 8, 4, 6, 9]`. Esses são os nove primeiros dígitos do CPF.

O **primeiro dígito verificador** é calculado utilizando os nove primeiros números e seus respectivos pesos: `s = sum(x * y for x, y in zip(n, range(10, 1, -1)))`. Os pesos utilizados são: `10  9  8  7  6  5  4  3  2`.

Depois, é calculado o primeiro dígito: `d1 = 11 - s % 11`. Caso o resultado seja `10` ou `11`, o dígito recebe `0`.

Por fim, o primeiro dígito verificador é adicionado à lista: `n.append(d1)`. Nesse momento, a lista passa a possuir **dez** dígitos.

O **segundo dígito** é calculado utilizando os dez números já disponíveis, incluindo o primeiro dígito verificador:

```python
s = sum(x * y for x, y in zip(n, range(11, 1, -1)))
```

Os pesos utilizados agora são: `11  10  9  8  7  6  5  4  3  2`. O segundo dígito é calculado: `d2 = 11 - s % 11`.

Assim como no primeiro dígito, se o resultado for `10` ou `11`, ele será convertido para `0`:

```python
if d2 >= 10:
    d2 = 0
```

Depois, o segundo dígito é adicionado: `n.append(d2)`. Agora a lista possui os onze dígitos do CPF.

Por fim, a função transforma os números armazenados na lista em uma string: `return "%d%d%d%d%d%d%d%d%d%d%d" % tuple(n)`. O resultado será algo semelhante a `527318469XX` (os `X` representam os dois dígitos verificadores calculados pela função).

---

## Veja o método funcionando

📜 **[gera_cpf_aleatorio.py](./scripts/gera_cpf_aleatorio.py)**


Após a execução, será exibido um popup semelhante a:

```text
Script de teste finalizado com sucesso!
CPF gerado: 12345678909
```

O CPF será diferente a cada nova execução. O mesmo CPF também será registrado no log `CPF gerado: 12345678909`.

## Por que armazenar o CPF em uma variável?

Nessa função, cada chamada de `cpf_funcional_func()` gera um **novo CPF**. a cada nova chamada, um **segundo CPF diferente** será gerado. Por isso, quando o objetivo é utilizar o mesmo CPF em diferentes etapas do teste, é melhor armazenar o resultado com `numCPF = cpf_funcional_func()` e utilizar a variável posteriormente. Dessa forma, popup e log apresentarão exatamente o mesmo CPF.

```python
print('CPF gerado: %s' % numCPF)

popup(
    'Script de teste finalizado com sucesso!'
    '\nCPF gerado: %s' % numCPF
)
```

Depois de armazenado em uma variável, o CPF pode ser utilizado em outras etapas da automação, exemplo:

```python
numCPF = cpf_funcional_func()

print('CPF utilizado no teste: %s' % numCPF)

click('CampoCPF.png')
type(numCPF)

click('BotaoContinuar.png')
```

### Por que registrar no log?

É recomendável registrar o CPF logo após sua geração, caso o teste apresente uma falha antes de chegar ao `popup()`.

```python
numCPF = cpf_funcional_func()
print('CPF gerado: %s' % numCPF)
```

Nesse cenário, o log do Sikuli ainda poderá indicar qual CPF foi utilizado: `CPF gerado: 12345678909`. Assim, é possível identificar o dado utilizado naquela execução específica do teste.

> 💡 **Observação: CPF válido não significa CPF real**. A função gera um número que atende à regra matemática de validação dos dígitos do CPF; o gerador deve ser entendido como uma ferramenta para dados de teste, apenas.
