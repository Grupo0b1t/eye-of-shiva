<p align="right"><strong>Potuguês</strong> | <a href="INSERIR LINK .MD PT-BR">English</a></p>

# Eye of Shiva #

## Table of contents
- - - -
* [Informações gerais](#informações-gerais)
* [Tecnologias](#tecnologias)
* [Instalação e como usar](#instalação-e-como-usar)

## Informações gerais
- - - -
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
- - - -
Esse projeto foi criado com:
* Python 3.10.4
\
Bibliotecas utilizadas:
* OS
* pathlib
* psutil
* time
* subprocess
* regex
* watchdog
* requests
* hashlib
* sklearn
* tkinter
* PIL
* webbrowser

## Instalação e como usar
- - - -
1. Baixe e instale [Python](https://www.python.org/downloads/) no seu computador
2. Baixe a pasta [ANTI-RANSOMWARE](https://github.com/Grupo0b1t/eye-of-shiva/tree/main/ANTI-RANSOMWARE) e rode:
* `machinelearning_ransomware_detector.py` para:
    - a ferramenta em si
* `arq.py` para:
    - desbloquear o protected_backup
* Não é necessário executar `AddRegistry.py`, `PublicMalware_detection.py` and `ransomware_behave_db.py`, pois eles já são utilizados automaticamente.
