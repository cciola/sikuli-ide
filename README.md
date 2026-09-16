# Sikuli IDE

Este repositório reúne exemplos de funcionalidades comumente utilizadas no **Sikuli IDE** para automação de interfaces gráficas (GUI).

Os exemplos têm como objetivo servir como material de consulta e estudo para quem está iniciando na utilização do SikuliX para automação de testes.
---

## 🖥️ Sobre o Sikuli

O **Sikuli** é uma ferramenta de automação e testes de interfaces gráficas (GUI) baseada em **reconhecimento de imagens**.

Diferentemente de ferramentas que dependem diretamente do código HTML, identificadores de elementos ou APIs específicas da aplicação, o Sikuli utiliza imagens como referência para localizar elementos visualmente na tela e executar ações sobre eles.

Entre as ações que podem ser automatizadas estão:

* Clicar em elementos
* Mover o mouse
* Digitar informações
* Utilizar teclas e atalhos
* Identificar elementos por reconhecimento de imagem
* Capturar screenshots
* Aguardar elementos aparecerem na tela

---

## ⚙️ Como funciona

O Sikuli IDE utiliza a linguagem **Jython**, uma implementação do Python executada sobre a plataforma Java.

A automação é baseada principalmente na identificação visual dos elementos.

Por exemplo, em vez de localizar um botão utilizando um seletor como:

```text
id=btnLogin
```

a automação pode utilizar uma imagem do botão para encontrá-lo na tela.

Isso permite trabalhar com aplicações que possuem diferentes tipos de interface, desde que os elementos possam ser identificados visualmente.

---

## 🧪 Aplicações

Uma das principais características do Sikuli é a possibilidade de automatizar aplicações independentemente da tecnologia utilizada na interface.

Ele pode ser utilizado em cenários envolvendo:

* Aplicações web
* Aplicações desktop
* Aplicações mobile, utilizando o espelhamento da tela do dispositivo no computador
* Testes funcionais
* Automação de tarefas repetitivas
* Validação de elementos visuais

O propósito é possibilitar a automação de aplicações que apresentem uma **interface gráfica com o usuário**.

---

## 📂 Exemplos disponíveis

Como este repositório também funciona como material de estudo, os exemplos são adicionados conforme novos recursos e funcionalidades do Sikuli são explorados.

### Captura de screenshots

**[captura_screenshot](captura_screenshot.md)**

Exemplo de implementação de captura de screenshot durante a execução do script.

O código demonstra como:

* Capturar toda a tela;
* Capturar a janela que possui o foco;
* Definir o diretório onde a imagem será salva;
* Utilizar um nome personalizado;
* Criar numeração automática;
* Evitar que screenshots anteriores sejam sobrescritos.

---

### Geração de CPF aleatório

**[gera_cpf_aleatorio](gera_cpf_aleatorio.md)**

Exemplo de implementação para geração randômica de um **CPF válido** durante a execução do script.

O exemplo também demonstra como registrar no log do Sikuli o CPF gerado.

Esse tipo de recurso pode ser útil em testes que precisam de dados de entrada gerados dinamicamente.

---

### Geração de data aleatória

**[gera_data_aleatoria](gera_data_aleatoria.md)**

Exemplo de implementação para geração randômica de uma **data válida** durante a execução do script.

O código também apresenta como informar no log do Sikuli a data que foi gerada.

Esse tipo de funcionalidade pode ser utilizado para criar dados dinâmicos durante a execução de testes.

---

## 🎯 Objetivo do repositório

Este repositório foi criado inicialmente como um espaço de estudo e compartilhamento de exemplos práticos relacionados ao SikuliX com Python.

Os exemplos representam funcionalidades que podem ser reutilizadas ou adaptadas em projetos de automação de testes.

O conteúdo deste repositório pode ser atualizado conforme novos exemplos e funcionalidades forem incorporados.
