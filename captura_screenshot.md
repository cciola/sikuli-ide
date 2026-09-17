# Captura de Screenshot

O código permite capturar a tela durante a execução de um script, armazenar as imagens em um diretório específico e gerar nomes sequenciais para os arquivos, evitando que screenshots anteriores sejam sobrescritos. Esse recurso pode ser especialmente útil para **evidências de testes automatizados**, permitindo verificar visualmente o estado da aplicação durante a execução do script.

## Explicação detalhada

A biblioteca `shutil` deve ser declarada no início do script. O `shutil` será utilizado para mover o arquivo temporário gerado pelo `capture()` para o diretório definido no script.

A variável `screenshotsPasta` define o diretório onde os screenshots serão armazenados.

```python
import shutil

screenshotsPasta = r"C:\Users\cciola\Desktop\Sikuli_IDE\Screenshots_Sikuli\\"
```

A utilização de `r` antes da string permite tratar o caminho como uma **raw string**, reduzindo problemas relacionados às barras invertidas (`\`) utilizadas nos caminhos do Windows.

Para evitar que um screenshot sobrescreva outro, é utilizado um **contador**, inicialmente recebendo o valor `0`. Em seguida, é criada a função responsável por incrementar esse contador:

```python
numPrint = 0

def numPrint_func():
    global numPrint
    numPrint += 1
```

Esta função declara que o contador `numPrint` é uma variável global, acessa a variável definida fora da função, e incrementa seu valor em `1`. Assim, teremos a cada execução da função `0 → 1 → 2 → 3 → 4 → ...`.

A função `capturaImagem_func()` é responsável por realizar todo o processo de captura e armazenamento do screenshot:

```python
def capturaImagem_func():
    wait(1)
    numPrint_func()
    shutil.move(
        capture(Screen()),
        screenshotsPasta + 'NomeDoArquivo_' + str(int(numPrint)) + '.png'
    )
```

Etapas executadas na função:

1. A execução `wait(1)` aguarda 1 segundo antes de realizar a captura
2. A função de incremento do contador `numPrint_func()` é chamada para gerar o próximo número do screenshot
3. O `capture()` realiza a captura da tela. Nesse caso, `Screen()` indica que a captura será realizada na tela
4. `shutil.move(...)` faz com que arquivo gerado pela captura seja movido para a pasta definida na variável `screenshotsPasta`

O nome do screenshot é construído dinamicamente: `'NomeDoArquivo_' + str(int(numPrint)) + '.png'`.

O `numPrint` é convertido para `string` para que possa ser concatenado ao nome do arquivo, exemplo:

```text
NomeDoArquivo_1.png
NomeDoArquivo_2.png
NomeDoArquivo_3.png
NomeDoArquivo_4.png
```

## Veja o método funcionando

📜 **[captura_screenshot.py](./scripts/captura_screenshot.py)**

Após a execução, será exibido um popup informando que o script foi finalizado. O arquivo será armazenado no diretório configurado `Screenshots_Sikuli\` com um nome semelhante a `NomeDoArquivo_1.png`.

Ao executar novamente o código dentro da mesma execução do script, o contador poderá gerar:

```text
NomeDoArquivo_1.png
NomeDoArquivo_2.png
NomeDoArquivo_3.png
```

## Capturando somente a janela em foco

O comando `firstWindow = App.focusedWindow()` obtém a janela que atualmente está em foco. Já o comando `firstWindow.highlight(2)` destaca a janela identificada durante dois segundos.

```python
firstWindow = App.focusedWindow()
firstWindow.highlight(2)
```

Depois de obter a janela em foco, ela pode ser utilizada no `capture()`:

```python
shutil.move(
    capture(firstWindow),
    screenshotsPasta + 'NomeDoArquivo_' + str(int(numPrint)) + '.png'
)
```

O comportamento é semelhante à ideia de utilizar **Alt + Print Screen** para capturar a janela ativa.

## Identificando o último screenshot gerado

Durante a execução de um teste, pode ser útil registrar no log qual foi o último screenshot capturado. Para isso, utilize `print('Arquivo gerado: %d' % numPrint)`. Esse comando pode ser colocado logo após a captura.

Por exemplo:

```python
def capturaImagem_func():
    wait(1)
    numPrint_func()

    shutil.move(
        capture(Screen()),
        screenshotsPasta + 'NomeDoArquivo_' + str(int(numPrint)) + '.png'
    )

    print('Arquivo gerado: %d' % numPrint)
```

### Por que registrar no log?

Imagine que o script execute várias etapas e ocorra um erro antes da exibição do popup final. Nesse cenário, o log do Sikuli pode ajudar a identificar **qual foi o último screenshot gerado antes da falha**. Exemplo:

```text
Arquivo gerado: 1
Arquivo gerado: 2
Arquivo gerado: 3
```

Se o teste falhar depois disso, é possível verificar que o último screenshot capturado foi o número `3`.

---

## 🎯 Objetivo do repositório

Este exemplo faz parte da série de exemplos de **SikuliX com Python** deste repositório. Como o estudo da ferramenta é incremental, novos exemplos podem ser adicionados conforme novos recursos forem explorados. A ideia é manter os códigos como uma **referência rápida** para funcionalidades que podem ser reutilizadas em diferentes scripts de automação.

## 🤝 Contribuições

Sugestões, melhorias e novos exemplos são bem-vindos! Caso você tenha alguma dúvida, sugestão ou queira contribuir com o projeto, fique à vontade para entrar em contato.

## 📌 Observação

Este repositório foi criado inicialmente como material de estudo e referência pessoal durante o aprendizado do SikuliX com Python. Os exemplos aqui apresentados representam funcionalidades que foram exploradas e utilizadas em automações, podendo ser adaptados conforme a necessidade de cada projeto.
