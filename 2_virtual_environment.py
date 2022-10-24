##################################################
#                                                #
#          Criação e utilização de um            #
#              Virtual Environment               #
#                                                #
##################################################

"""
Espaço dedicado / isolado para determinado projeto
Isola o projeto de versoes de python diferentes, bibliotecas e scripts de outros
"ambientes virtuais" ou versões instaladas ao nível do sistema
Bastante util quando temos várias versões de Python instaladas


DEMO:


Criar um Virtual Environment:
-----------------------------
python -m venv <application_name>

Ativar/desativar um virtual environment:
----------------------------------------
.\scripts\activate.bat
.\scrtips\deactivate.bat

Instalar bibliotecas:
---------------------
.\scripts\pip install <library_name>

Desinstalar bibliotecas:
------------------------
.\scripts\pip uninstall <library_name>

Ver bibliotecas instaladas:
---------------------------
.\scripts\pip freeze ou .\scripts\pip list

"""