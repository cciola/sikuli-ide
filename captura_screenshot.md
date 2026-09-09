# 📸 Captura de Screenshot — Sikuli IDE

Exemplo de implementação de **captura automática de screenshots utilizando o Sikuli IDE**.

O código permite capturar a tela durante a execução de um script, armazenar as imagens em um diretório específico e gerar nomes sequenciais para os arquivos, evitando que screenshots anteriores sejam sobrescritos.

---

## 🎯 Objetivo

A funcionalidade apresentada neste exemplo permite:

* Capturar screenshots durante a execução do teste;
* Definir o diretório onde as imagens serão armazenadas;
* Criar nomes personalizados para os arquivos;
* Numerar automaticamente os screenshots;
* Evitar a sobrescrita de imagens anteriores;
* Capturar a tela inteira;
* Capturar somente a janela que está em foco;
* Registrar no log do Sikuli o número do screenshot gerado.

Esse recurso pode ser especialmente útil para **evidências de testes automatizados**, permitindo verificar visualmente o estado da aplicação durante a execução do script.

---

## 📦 Biblioteca utilizada

A biblioteca `shutil` deve ser declarada no início do script:

```python
import shutil
```

O `shutil` será utilizado para mover o arquivo temporário gerado pelo `capture()` para o diretório definido no script.

---

## 📁 Definindo a pasta dos screenshots

A variável `screenshotsPasta` define o diretório onde os screenshots serão armazenados.

```python
screenshotsPasta = r"C:\Users\cciola\Desktop\Sikuli_IDE\Screenshots_Sikuli\\"
```

Nesse exemplo, as imagens serão armazenadas em:

```text
C:\Users\cciola\Desktop\Sikuli_IDE\Screenshots_Sikuli\
```

### ⚠️ Observação

O caminho deve ser alterado de acordo com o diretório existente no computador onde o script será executado.

A utilização de `r` antes da string permite tratar o caminho como uma **raw string**, reduzindo problemas relacionados às barras invertidas (`\`) utilizadas nos caminhos do Windows.

---

## 🔢 Controle da numeração

Para evitar que um screenshot sobrescreva outro, é utilizado um contador.

Inicialmente, a variável `numPrint` recebe o valor `0`:

```python
numPrint = 0
```

Em seguida, é criada a função responsável por incrementar esse contador:

```python
def numPrint_func():
    global numPrint
    numPrint += 1
```

### Como funciona

A função:

1. Declara que `numPrint` é uma variável global;
2. Acessa a variável definida fora da função;
3. Incrementa seu valor em `1`.

Assim, a cada execução da função:

```text
0 → 1 → 2 → 3 → 4 → ...
```

---

## 📸 Função para captura da imagem

A função `capturaImagem_func()` é responsável por realizar todo o processo de captura e armazenamento do screenshot.

```python
def capturaImagem_func():
    wait(1)
    numPrint_func()
    shutil.move(
        capture(Screen()),
        screenshotsPasta + 'NomeDoArquivo_' + str(int(numPrint)) + '.png'
    )
```

### Etapas executadas

#### 1. Aguarda um segundo

```python
wait(1)
```

A execução aguarda um segundo antes de realizar a captura.

#### 2. Incrementa o contador

```python
numPrint_func()
```

A função de incremento é chamada para gerar o próximo número do screenshot.

#### 3. Captura a tela

```python
capture(Screen())
```

O `capture()` realiza a captura da tela.

Nesse caso, `Screen()` indica que a captura será realizada na tela.

#### 4. Move o arquivo para o diretório definido

```python
shutil.move(...)
```

O arquivo gerado pela captura é movido para a pasta definida na variável:

```python
screenshotsPasta
```

#### 5. Define o nome do arquivo

O nome do screenshot é construído dinamicamente:

```python
'NomeDoArquivo_' + str(int(numPrint)) + '.png'
```

Por exemplo:

```text
NomeDoArquivo_1.png
NomeDoArquivo_2.png
NomeDoArquivo_3.png
NomeDoArquivo_4.png
```

O `numPrint` é convertido para `string` para que possa ser concatenado ao nome do arquivo.

---

## ▶️ Script completo

O código abaixo pode ser copiado e executado no **Sikuli IDE**.

```python
import shutil

screenshotsPasta = r"C:\Users\cciola\Desktop\Sikuli_IDE\Screenshots_Sikuli\\"

# Função para incrementar 1 no número do print
numPrint = 0

def numPrint_func():
    global numPrint
    numPrint += 1


# Função para capturar screenshot
def capturaImagem_func():
    wait(1)
    numPrint_func()

    shutil.move(
        capture(Screen()),
        screenshotsPasta + 'NomeDoArquivo_' + str(int(numPrint)) + '.png'
    )


capturaImagem_func()

popup(
    'Script de teste finalizado com sucesso! '
    'Veja o print gerado no caminho \n %s' % screenshotsPasta
)

print('Número do arquivo gerado: %d' % numPrint)

wait(1)
exit()
```

### Resultado esperado

Após a execução, será exibido um popup informando que o script foi finalizado.

O arquivo será armazenado no diretório configurado:

```text
Screenshots_Sikuli\
```

Com um nome semelhante a:

```text
NomeDoArquivo_1.png
```

Ao executar novamente o código dentro da mesma execução do script, o contador poderá gerar:

```text
NomeDoArquivo_1.png
NomeDoArquivo_2.png
NomeDoArquivo_3.png
```

---

## 🖥️ Capturando somente a janela em foco

Por padrão, o exemplo utiliza:

```python
capture(Screen())
```

para capturar a tela.

Caso seja necessário capturar **somente a janela que está em foco**, pode-se obter a janela utilizando:

```python
firstWindow = App.focusedWindow()
firstWindow.highlight(2)
```

### Identificando a janela em foco

O comando:

```python
firstWindow = App.focusedWindow()
```

obtém a janela que atualmente está em foco.

Já:

```python
firstWindow.highlight(2)
```

destaca a janela identificada durante dois segundos.

Isso pode ser útil para visualizar qual janela o Sikuli está considerando como foco antes da captura.

---

### Utilizando a janela na captura

Depois de obter a janela em foco, ela pode ser utilizada no `capture()`:

```python
shutil.move(
    capture(firstWindow),
    screenshotsPasta + 'NomeDoArquivo_' + str(int(numPrint)) + '.png'
)
```

Dessa forma, em vez de capturar toda a tela:

```python
capture(Screen())
```

a captura será realizada considerando a janela identificada:

```python
capture(firstWindow)
```

O comportamento é semelhante à ideia de utilizar **Alt + Print Screen** para capturar a janela ativa.

---

## 📝 Identificando o último screenshot gerado

Durante a execução de um teste, pode ser útil registrar no log qual foi o último screenshot capturado.

Para isso, pode-se utilizar:

```python
print('Arquivo gerado: %d' % numPrint)
```

Esse comando pode ser colocado logo após a captura.

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

Imagine que o script execute várias etapas e ocorra um erro antes da exibição do popup final.

Nesse cenário, o log do Sikuli pode ajudar a identificar **qual foi o último screenshot gerado antes da falha**.

Exemplo:

```text
Arquivo gerado: 1
Arquivo gerado: 2
Arquivo gerado: 3
```

Se o teste falhar depois disso, é possível verificar que o último screenshot capturado foi o número `3`.

---

## 💡 Exemplo de uso em testes

A função pode ser chamada em diferentes pontos do script:

```python
login()

capturaImagem_func()

preencherDados()

capturaImagem_func()

enviarFormulario()

capturaImagem_func()
```

Nesse caso, poderiam ser geradas evidências como:

```text
NomeDoArquivo_1.png
NomeDoArquivo_2.png
NomeDoArquivo_3.png
```

Isso permite acompanhar visualmente diferentes etapas da execução do teste.

---

## 📌 Resumo

A implementação utiliza principalmente:

| Recurso                | Finalidade                            |
| ---------------------- | ------------------------------------- |
| `shutil`               | Mover o arquivo de screenshot         |
| `capture()`            | Realizar a captura                    |
| `Screen()`             | Representar a tela                    |
| `App.focusedWindow()`  | Identificar a janela em foco          |
| `wait()`               | Aguardar determinado período          |
| `popup()`              | Exibir uma mensagem na tela           |
| `print()`              | Registrar informações no log          |
| `numPrint`             | Controlar a numeração dos screenshots |
| `numPrint_func()`      | Incrementar o contador                |
| `capturaImagem_func()` | Centralizar a lógica de captura       |

---

## 🚀 Possíveis melhorias

A implementação pode ser evoluída para:

* Criar automaticamente a pasta de screenshots caso ela não exista;
* Utilizar data e hora no nome dos arquivos;
* Associar o screenshot ao nome da etapa do teste;
* Capturar screenshots automaticamente em caso de falha;
* Criar uma função reutilizável para diferentes tipos de evidência;
* Armazenar screenshots em subpastas por execução ou cenário de teste.

---

**Este exemplo foi criado como material de estudo e referência para automações utilizando Sikuli IDE.**
