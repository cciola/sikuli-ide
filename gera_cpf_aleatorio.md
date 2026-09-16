# Gerador de CPF Aleatório

A função apresentada neste exemplo gera CPFs diferentes válidos e aleatórios a cada execução, calculando automaticamente os dois dígitos verificadores do documento.

Esse recurso pode ser utilizado em testes automatizados que necessitam de **dados de teste dinâmicos**, evitando a utilização repetitiva de um CPF fixo.

A funcionalidade apresentada neste exemplo permite:

* Gerar um CPF de forma randômica;
* Calcular automaticamente os dois dígitos verificadores;
* Retornar um CPF válido;
* Utilizar o CPF gerado em outras etapas do teste;
* Exibir o CPF gerado em um popup;
* Registrar o CPF no log do Sikuli.

A cada nova chamada da função, um novo CPF é gerado.

---

## Como funciona a geração de CPF aleatório

A biblioteca `random` deve ser declarada no início do script. Ela será utilizada para gerar os nove primeiros dígitos do CPF de forma aleatória.

Inicialmente, são gerados nove números aleatórios na função:

```python
n = [random.randrange(10) for i in xrange(9)]
```

O resultado é armazenado na lista `n`. Por exemplo:

```text
[5, 2, 7, 3, 1, 8, 4, 6, 9]
```

Esses são os nove primeiros dígitos do CPF.

O **primeiro dígito verificador** é calculado utilizando os nove primeiros números e seus respectivos pesos:

```python
s = sum(x * y for x, y in zip(n, range(10, 1, -1)))
```

Os pesos utilizados são:

```text
10  9  8  7  6  5  4  3  2
```

Depois, é calculado o primeiro dígito:

```python
d1 = 11 - s % 11
```

Caso o resultado seja `10` ou `11`, o dígito recebe `0`:

```python
if d1 >= 10:
    d1 = 0
```

Por fim, o primeiro dígito verificador é adicionado à lista:

```python
n.append(d1)
```

Nesse momento, a lista passa a possuir **dez** dígitos.

O **segundo dígito** é calculado utilizando os dez números já disponíveis, incluindo o primeiro dígito verificador:

```python
s = sum(x * y for x, y in zip(n, range(11, 1, -1)))
```

Os pesos utilizados agora são:

```text
11  10  9  8  7  6  5  4  3  2
```

O segundo dígito é calculado:

```python
d2 = 11 - s % 11
```

Assim como no primeiro dígito, se o resultado for `10` ou `11`, ele será convertido para `0`:

```python
if d2 >= 10:
    d2 = 0
```

Depois, o segundo dígito é adicionado:

```python
n.append(d2)
```

Agora a lista possui os onze dígitos do CPF.

Por fim, a função transforma os números armazenados na lista em uma string: `return "%d%d%d%d%d%d%d%d%d%d%d" % tuple(n)`.

O resultado será algo semelhante a `527318469XX` (os `X` representam os dois dígitos verificadores calculados pela função).

---

## Veja o método funcionando

**[gera_cpf_aleatorio.py](./scripts/gera_cpf_aleatorio.py)**


Após a execução, será exibido um popup semelhante a:

```text
Script de teste finalizado com sucesso!
CPF gerado: 12345678909
```

O CPF será diferente a cada nova execução. O mesmo CPF também será registrado no log `CPF gerado: 12345678909`.

---

## Por que armazenar o CPF em uma variável?

Uma atenção importante ao utilizar essa função é que cada chamada de `cpf_funcional_func()` gera um **novo CPF**.

Por exemplo, `popup('CPF: %s' % cpf_funcional_func())` gera um CPF. Se logo depois for executado `print('CPF: %s' % cpf_funcional_func())`, um **segundo CPF diferente** será gerado.

Por isso, quando o objetivo é utilizar o mesmo CPF em diferentes etapas do teste, é melhor armazenar o resultado com `numCPF = cpf_funcional_func()` e utilizar a variável posteriormente:

```python
print('CPF gerado: %s' % numCPF)

popup(
    'Script de teste finalizado com sucesso!'
    '\nCPF gerado: %s' % numCPF
)
```

Dessa forma, popup e log apresentarão exatamente o mesmo CPF.

---

## Utilizando o CPF durante um teste

Depois de armazenado em uma variável, o CPF pode ser utilizado em outras etapas da automação, exemplo:

```python
numCPF = cpf_funcional_func()

print('CPF utilizado no teste: %s' % numCPF)

click('CampoCPF.png')
type(numCPF)

click('BotaoContinuar.png')
```

Nesse cenário, o teste:

1. Gera um CPF;
2. Armazena o valor em `numCPF`;
3. Registra o CPF no log;
4. Localiza o campo de CPF;
5. Preenche o CPF gerado;
6. Continua a execução do teste.

Isso permite criar dados de teste dinamicamente durante a execução.

### Por que registrar no log?

É recomendável registrar o CPF logo após sua geração, caso o teste apresente uma falha antes de chegar ao `popup()`.

```python
numCPF = cpf_funcional_func()

print('CPF gerado: %s' % numCPF)
```

Nesse cenário, o log do Sikuli ainda poderá indicar qual CPF foi utilizado. Exemplo:

```text
CPF gerado: 12345678909
```

Assim, é possível identificar o dado utilizado naquela execução específica do teste.

---

> **💡 Observação: CPF válido não significa CPF real**. A função gera um número que atende à **regra matemática de validação dos dígitos do CPF**.

Isso não significa que o número:

* pertença a uma pessoa real;
* esteja cadastrado na Receita Federal;
* esteja disponível para uso em um sistema específico;
* seja necessariamente aceito por sistemas que realizam validações adicionais.

Portanto, o gerador deve ser entendido como uma ferramenta para **dados de teste**.

### Uso em ambientes de teste

Recomenda-se utilizar dados gerados dessa forma somente em ambientes destinados a testes, desenvolvimento ou homologação, de acordo com as regras do projeto.

---

## Possíveis melhorias

A função pode ser evoluída para atender diferentes necessidades, como:

* Gerar CPF com ou sem pontuação;
* Gerar CPF e CNPJ;
* Permitir reutilização do CPF durante todo o cenário;
* Criar uma biblioteca de dados de teste;
* Gerar outros dados aleatórios, como nome, telefone e endereço;
* Registrar os dados utilizados em arquivos de evidência;
* Integrar a geração de dados com outros scripts de automação.

---

## 🎯 Objetivo do repositório

Este exemplo faz parte da série de exemplos de **SikuliX com Python** deste repositório. Como o estudo da ferramenta é incremental, novos exemplos podem ser adicionados conforme novos recursos forem explorados. A ideia é manter os códigos como uma **referência rápida** para funcionalidades que podem ser reutilizadas em diferentes scripts de automação.

## 🤝 Contribuições

Sugestões, melhorias e novos exemplos são bem-vindos! Caso você tenha alguma dúvida, sugestão ou queira contribuir com o projeto, fique à vontade para entrar em contato.

## 📌 Observação

Este repositório foi criado inicialmente como material de estudo e referência pessoal durante o aprendizado do SikuliX com Python. Os exemplos aqui apresentados representam funcionalidades que foram exploradas e utilizadas em automações, podendo ser adaptados conforme a necessidade de cada projeto.
