# ============================================================
# AJUDA - PYTHON, VS CODE, POWERSHELL, GIT E GITHUB
# ============================================================


# ============================================================
# 1. PYTHON
# ============================================================

# print() mostra uma informação na tela.

print("Olá, mundo!")


# ============================================================
# 2. POWERSHELL / TERMINAL
# ============================================================

# O terminal permite conversar com o computador
# através de comandos.
#
# Exemplo:
#
# PS C:\Users\Casa 1>
#
# PS                         -> PowerShell
# C:\Users\Casa 1            -> pasta atual
# >                          -> esperando um comando


# ------------------------------------------------------------
# pwd
# ------------------------------------------------------------

# pwd = Print Working Directory
#
# Mostra em qual pasta estamos atualmente.
#
# Comando:
#
# pwd
#
# Exemplo de resultado:
#
# C:\Users\Casa 1


# ------------------------------------------------------------
# dir
# ------------------------------------------------------------

# dir = lista o conteúdo da pasta atual.
#
# Mostra arquivos e pastas existentes naquele local.
#
# Comando:
#
# dir


# ------------------------------------------------------------
# cd
# ------------------------------------------------------------

# cd = Change Directory
#
# Serve para mudar de pasta.
#
# Exemplo:
#
# cd ExerciciosPanda
#
# Significa:
#
# "Entre na pasta ExerciciosPanda."


# ------------------------------------------------------------
# cd ..
# ------------------------------------------------------------

# .. significa "pasta anterior".
#
# Exemplo:
#
# Se estamos em:
#
# C:\Users\Casa 1\projeto\ExerciciosPanda
#
# e executamos:
#
# cd ..
#
# voltamos para:
#
# C:\Users\Casa 1\projeto


# ============================================================
# 3. COMO DESCOBRIR A ÁREA DE TRABALHO
# ============================================================

# Este comando pergunta ao Windows onde fica
# a Área de Trabalho do usuário:
#
# [Environment]::GetFolderPath("Desktop")
#
# Exemplo:
#
# C:\Users\Casa 1\OneDrive\Área de Trabalho


# ------------------------------------------------------------
# O que significa Environment?
# ------------------------------------------------------------

# Environment é uma classe do .NET que o PowerShell
# consegue utilizar.
#
# Ela fornece informações sobre o ambiente do Windows.
#
# Por exemplo, podemos pedir ao Windows informações
# sobre algumas pastas especiais.


# ------------------------------------------------------------
# O que significa GetFolderPath?
# ------------------------------------------------------------

# GetFolderPath significa:
#
# "Obter o caminho de uma pasta."
#
# Get       = obter
# Folder    = pasta
# Path      = caminho


# ------------------------------------------------------------
# O que significa "Desktop"?
# ------------------------------------------------------------

# "Desktop" é o nome usado pelo Windows para
# identificar a Área de Trabalho.
#
# Portanto:
#
# [Environment]::GetFolderPath("Desktop")
#
# significa aproximadamente:
#
# "Windows, obtenha o caminho da minha Área de Trabalho."


# ============================================================
# 4. E SE O PROJETO NÃO ESTIVER NA ÁREA DE TRABALHO?
# ============================================================

# O comando:
#
# [Environment]::GetFolderPath("Desktop")
#
# serve para encontrar a Área de Trabalho.
#
# Ele NÃO procura qualquer projeto no computador.


# Por exemplo, se o projeto estiver em:
#
# C:\Users\Public\projeto\ExerciciosPanda
#
# podemos entrar nele usando:
#
# cd "C:\Users\Public\projeto\ExerciciosPanda"
#
# Depois podemos confirmar nossa localização:
#
# pwd
#
# E podemos verificar os arquivos:
#
# dir


# ============================================================
# 5. COMO NÃO SE PERDER NAS PASTAS
# ============================================================

# Quando estiver perdido, faça:
#
# 1. pwd
#    -> Onde estou?
#
# 2. dir
#    -> O que existe aqui?
#
# 3. cd NomeDaPasta
#    -> Entre nessa pasta.
#
# 4. cd ..
#    -> Volte uma pasta.


# ============================================================
# 6. CRIANDO ARQUIVOS NO VS CODE
# ============================================================

# É possível criar arquivos pelo próprio VS Code.
#
# No Explorer (lado esquerdo):
#
# 1. Abra a pasta do projeto.
# 2. Clique em "New File".
# 3. Digite o nome do arquivo.
#
# Exemplo:
#
# Ajuda.py
#
# O arquivo será criado dentro da pasta que está
# aberta no VS Code.


# ============================================================
# 7. GIT
# ============================================================

# Git é um sistema de controle de versões.
#
# Ele acompanha as alterações dos arquivos
# do nosso projeto.


# ------------------------------------------------------------
# git status
# ------------------------------------------------------------

# Mostra o estado atual do projeto.
#
# Comando:
#
# git status
#
# Pode mostrar:
# - arquivos novos
# - arquivos modificados
# - arquivos não rastreados
# - commits pendentes


# ------------------------------------------------------------
# git clone
# ------------------------------------------------------------

# Faz uma cópia de um repositório do GitHub
# para o computador.
#
# Exemplo:
#
# git clone https://github.com/PACRogerio/ExerciciosPanda.git


# ------------------------------------------------------------
# git add
# ------------------------------------------------------------

# Prepara um arquivo para o próximo commit.
#
# Exemplo:
#
# git add Ajuda.py
#
# Significa:
#
# "Git, prepare o Ajuda.py para ser registrado."


# ------------------------------------------------------------
# git commit
# ------------------------------------------------------------

# Registra a alteração no histórico LOCAL do Git.
#
# Exemplo:
#
# git commit -m "Adiciona Ajuda.py"
#
# -m significa que estamos fornecendo uma mensagem.
#
# A mensagem explica o que foi alterado.


# ------------------------------------------------------------
# git push
# ------------------------------------------------------------

# Envia os commits do computador para o GitHub.
#
# Exemplo:
#
# git push
#
# Fluxo:
#
# COMPUTADOR
#     |
#     | git push
#     v
# GITHUB


# ------------------------------------------------------------
# git pull
# ------------------------------------------------------------

# Baixa alterações que estão no GitHub
# para o computador.
#
# Exemplo:
#
# git pull


# ============================================================
# 8. COMMIT x PUSH
# ============================================================

# COMMIT
#
# Registra a alteração no histórico LOCAL do Git.
#
#
# PUSH
#
# Envia o commit local para o GITHUB.


# ============================================================
# 9. BRANCH
# ============================================================

# Branch é uma linha de desenvolvimento do projeto.
#
# A branch principal do nosso projeto é:
#
# main
#
# Quando aparece:
#
# On branch main
#
# significa:
#
# "Você está trabalhando na branch main."


# ============================================================
# 10. ORIGIN
# ============================================================

# origin é o nome que o Git normalmente dá
# ao repositório remoto que foi clonado.
#
# origin/main
#
# significa:
#
# "branch main do repositório remoto."


# ============================================================
# 11. UNTRACKED
# ============================================================

# Untracked significa:
#
# "não rastreado".
#
# Exemplo:
#
# Untracked files:
#     Ajuda.py
#
# Significa que o arquivo existe,
# mas o Git ainda não está acompanhando esse arquivo.
#
# Para começar a acompanhá-lo:
#
# git add Ajuda.py


# ============================================================
# 12. WORKING TREE CLEAN
# ============================================================

# Quando aparece:
#
# working tree clean
#
# significa que não existem alterações pendentes
# para serem registradas.


# ============================================================
# 13. FLUXO BÁSICO DO GIT
# ============================================================

# 1. Criar ou modificar um arquivo
#
# 2. Verificar:
#
#    git status
#
# 3. Preparar:
#
#    git add Ajuda.py
#
# 4. Registrar:
#
#    git commit -m "Descrição da alteração"
#
# 5. Enviar para o GitHub:
#
#    git push


# ============================================================
# 14. VISÃO GERAL
# ============================================================

#              GITHUB
#                 |
#                 | git clone
#                 v
#            COMPUTADOR
#                 |
#                 | criar/modificar arquivos
#                 v
#             git status
#                 |
#                 | git add
#                 v
#          alteração preparada
#                 |
#                 | git commit
#                 v
#          histórico LOCAL
#                 |
#                 | git push
#                 v
#              GITHUB

