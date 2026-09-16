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