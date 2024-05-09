# Como Rodar
> _Este documento terá as informações necessárias para que você consiga rodar a aplicação devidamente._
## Tutorial de Instalação:

1. [Git](https://git-scm.com/downloads): Utilize o git para poder clonar o repositório.

2. [Python](https://www.python.org/downloads/): Será necessário o python para rodar o ambiente virtual, e será por meio dele, utilizado o Microframework Flask, que está incluso no requirements.txt

## Na prática:

<details>
  <summary><b>Clonando Repositório</b></summary>

  Para clonar o projeto e utilizá-lo em seu computador, siga os seguintes passos:
  
  Crie uma pasta onde deseja armazenar nosso projeto, e então abra-a e clique no url da pasta, após isto, escreva em cima do url `cmd`, para abrir o prompt de comando. E então execute o comando abaixo:
  
  > _Obs.: Caso você esteja no LINUX, a parte de escrever "cmd" não irá funcionar, então clique com o botão direito na pasta que você criou e selecione a opção "Abrir no terminal"_

  
  ```
  git clone https://github.com/DuuhZero/Site_GTA.git
  ``` 

</details>
<br>

<details>
  <summary><b>Instalando Ambiente Virtual</b></summary>

  Após a clonagem, clique com o botão direito na pasta e selecione a opção de abrir com o Terminal, e insira os seguintes comandos :

  ```
  python3 -m venv venv
  venv\Scripts\activate
  pip install -r requirements.txt
  ```

  > _Caso você esteja em LINUX, digite os comandos desta maneira:_<br>
  `python3 -m venv venv`<br>
  `source venv/bin/activate`<br>
  `pip install -r requirements.txt`

</details>
<br>

<details>
  <summary><b>Executando Aplicação</b></summary>

  1. Ainda dentro do ambiente virtual, execute o seguinte comando:
  ```
  flask run
  ```
  > _Também é possivel executar pelo próprio arquivo app.py, onde no seu editor de texto você seleciona:_<br>
  `Executar Arquivo do Python`<br>
  ou<br>
  `"Clique no botão de play "▶️"`<br>

  2. Por fim, entre no link que aparecerá no cmd copiando e colando ele no seu navegador de preferência.

  3. Após finalizar o uso do nosso site, para sair do ambiente virtual, no terminal, execute o atalho `Ctrl+C` para finalizar o serviço do Flask, e então execute o seguinte comando:
  ```
  deactivate
  ```

</details>



