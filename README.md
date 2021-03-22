[![author](https://img.shields.io/badge/author-LeonardoCotta-red)](https://www.linkedin.com/in/leonardo-cotta-4b44013a/)
[![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-365/) 
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/LeonardoCDP/Data-Science/issues)


# **API Livro de Receitas**

Visualizar todas as receitas => **/recipe-list/** - este comando ira te mostrar as informações de todas as receitas 
cadastradas.

Pesquisar por uma receita utilizando o ID dela -> **/recipe-detail/(ID da receita)/** - este comando ira te mostrar as 
informações de uma receita do ID pesquisado.

Pesquisar por receita(s) utilizando o nome do Chef -> **/recipe-detail-author/(Nome do chef)/** - este comando ira te
mostrar as informações de uma ou mais receitas cadastradas no nome do chef pesquisado.

Pesquisar por receita(s) utilizando o nome da receita -> **/recipe-detail-title/(Nome da Receita)/** - este comando ira 
te mostrar as informações de uma ou mais receitas com o mesmo nome pesquisado.

Visualizar todas as receitas marcadas como simples e rapida de fazer -> **/recipe-fast-and-simple/** - este comando ira 
te mostrar as informações todas as receitas que foram informadas como rapidas e faceis de fazer.

Pesquisar receitas simples e faceis de fazer utilizando o nome da receita -> **/recipe-fast-and-simple/(Nome da Receita/**
- esta comando ira te mostrar as informações uma ou mais receitas informadas como rapidas e faceis de fazer com o mesmo 
  nome pesquisado.

Para criar uma receita nova utilize -> **/recipe-create/** - esta comando ira criar uma nova receita utilizando os 
campos abaixo conforme o exemplo.

Campos utilizados para criar uma nova receita ou atualizar uma existente:

{
"author": "Chef",
"title": "Arroz",
"recipe": "Cozinhe ...",
"preparation_time": "30 minutos",
"simple_recipe": "True",
"fast_recipe": "False"
}

Para atualizar as informações de uma receita utilize o ID dela -> **/recipe-update/(ID da receita)/** - este comando 
ira atualizar um ou mais campos de uma receita referente ao ID informado, somente os campos que estão no exemplo acima 
são utilizados.

Para deletar uma receita utilize o ID dela -> **/recipe-delete/(ID da receita)/** - este comando ira apagar de forma 
permanente a receita do ID informado.


#**Como Utilizar**

Copiar os codigos que se encontram em **negrito** e substituir os (parenteses) com os respectivo dado solicitado 
em cada um.


#**Dicionario dos Campos**
id_recipe = Codigo de identificação da receita(não se repete) *`Obs.: Não utilizar este campo na hora de criar uma 
nova receita`*

author = Autor da receita ou Chef da receita

title = Titulo da receita ou Nome da receita

recipe = Informações dos items e modo de preparo da receita

preparation_time = Tempo de preparo da receita

simple_recipe = Utilizar `True` caso seja uma receita simples de fazer

fast_recipe =  Utilizar `True` caso seja uma receita rapida de fazer

create_at = Data na qual a receita foi adicionada ou modificada *`Não utilizar este campo`*