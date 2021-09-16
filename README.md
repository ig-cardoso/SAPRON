# SAPRON

## Primeiros Passos

Inicialmente será necessitário a criação de um ambiente virtual, caso não saiba como criar, basta acessar o [link](https://www.treinaweb.com.br/blog/criando-ambientes-virtuais-para-projetos-python-com-o-virtualenv). Sugiro que crie uma virtualenv com seguinte nome: venv-SAPRON.

Também é necessário a instalação do **Node**, basta acessar o [link](https://nodejs.org/pt-br/download/package-manager/) e segui o passo a passo.  

## Pré-requisitos

### Banckend (Django e outros módulos)

Para rodar o projeto é preciso instalar as dependências que estão no arquivo requirements.txt dentro da virtual env. Com a virtualenv ativada digite o seguinte comando no terminal:

```
pip3 install -r requirements.txt
```



### Simulador da API do Airbnb (JSON Server)

Para simular as requisições feitas a API do Airbnb foi utilizado o JSON Server. Para iniciar o simulador é preciso acessar o diretório pelo terminal, e em seguida digitar os seguintes comandos:

```
npm install
```
E seguinda digite o seguinte comando para iniciar:

```
npm start
```

### Frontend

O frontend da aplicação foi construido em **Angular**, e para incia-lo é preciso acessar o diretório pelo terminal e executar os seguintes comandos:

```
npm install
```

 E em seguinda:

```
npm start
```

## Modelagem do banco de dados

Os models foram criados, embora por decisão de projeto optei por não armazenar os dados que são recebidos da API do Airbnb, pois trata-se de dados mutáveis, e isso agregaria um custo a mais de armazenamento. Somente os dados das  *limpezas* são armazenada no banco de dados. Encontra-se, abaixo a relação entre os dados: 



![Modelagem do banco de dados](/home/basis/Área de Trabalho/SAPRON/model_SAPRON-2.png)



*Vale observar que havia outros campos e tabelas que poderiam ser implementados.*

### Teste



### Observações

Não foi possível integrar, por fata de tempo, efetivamente o backend com fronte. Para testar o recebimento de dados e sugerido acesse a seguinte rota  a *localhost:8000/calendar_template/111* ou /222, que é refente o template  que está dentro do app userCalendar.

## Autor

* **Igor Cardoso** - *Initial work* - [ig-cardoso](https://github.com/ig-cardoso)

## License

Este projeto está sob licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para mais detalhes.

