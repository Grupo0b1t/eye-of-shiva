<p align="right"><strong>Potuguês</strong> | <a href="https://github.com/Grupo0b1t/eye-of-shiva/blob/main/README.md">English</a></p>

# Eye of Shiva #

## Tabela de conteúdos

* [Informações gerais](#informações-gerais)
* [Tecnologias](#tecnologias)
* [Instalação e como usar](#instalação-e-como-usar)
* [Descrição](#descrição)

## Informações gerais

Essa ferramenta é capaz de identificar e bloquear um ataque ransomware em uma máquina Windows, além de recuperar arquivos possivelmente comprometidos.\
\
Ela conta com várias formas de:
* Detectar um ransomware. Como: 
    - Hashing de arquivos
    - Arquivos armadilha
    - Filtrando arquivos suspeitos
    - Analisando alterações no sistema de arquivos
    - Machine Learning
* Prevenção. Como:
    - Backup local protegido
    - Backup shadow protegido
* Parar:
    - Filtrando e matando processos

## Tecnologias

Esse projeto foi criado com:
* Python 3.10.4

Bibliotecas utilizadas:
* psutil
* regex
* watchdog
* requests
* scikit-learn
* pillow

## Instalação e como usar

1. Baixe e instale [Python](https://www.python.org/downloads/) no seu computador
2. Baixe o [Eye of Shiva.zip](https://github.com/Grupo0b1t/eye-of-shiva/blob/main/Eye%20of%20Shiva/Eye%20of%20Shiva.rar) e rode:
* No cmd: `python setup.py` para:
    - isntalar as dependências
* `Eye of Shiva Setup.exe` para:
    - instalar a ferramenta no seu computador
* É recomendado criar um atalho na Área de Trabalho já que o uso da ferramenta será facilitado.


## Descrição

### Tela principal

![App Screenshot](https://cdn.discordapp.com/attachments/669945882162233358/1025149527356874752/unknown.png)

É possível ligar/desligar a proteção clicando no botãod e Power na tela principal

### Configurações avançadas

![App Screenshot](https://cdn.discordapp.com/attachments/669945882162233358/1025149565202092052/unknown.png)

* Create backup
    - Ao clicar em backup você pode criar uma versão atualizada do seu shadow copy e deletar a versão antiga.

* Lock/Unlock Backup Folder
    - Ao clicar em locked/unlock você pode conceder acesso próprio para editar os conteúdos da sua protected_folder localizada na Área de Trabalho

