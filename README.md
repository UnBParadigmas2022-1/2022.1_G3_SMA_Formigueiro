# Formigueiro

**Disciplina**: FGA0210 - PARADIGMAS DE PROGRAMAÇÃO - T01 <br>
**Nro do Grupo**: 03<br>
**Paradigma**: Sistemas Multiagentes<br>

## Alunos

|Matrícula | Aluno |
| :--: | :--: |
| 20/2028211 |  [Antônio Aldísio](https://github.com/AntonioAldisio/) |
| 19/0026243 |  [Dafne Moretti Moreira](https://github.com/DafneM/) |
| 18/0122258 |  [Igor Queiroz Lima](https://github.com/igorq937/) |
| 19/0030879 |  [João Pedro Moura Oliveira](https://github.com/Joao-Moura/) |
| 17/0080102 |  [Lucas Gomes Lopes](https://github.com/LucasGlopes/) |
| 18/0114093 |  [Lucas Ursulino Boaventura](https://github.com/lboaventura25/) |
| 19/0019085 |  [Rafael Cleydson da Silva Ramos](https://github.com/RcleydsonR/) |
| 19/0020377 |  [Thiago Sampaio de Paiva](https://github.com/thiagohdaqw/) |

## Sobre 
O projeto trata da representação de um formigueiro fantasia, onde foram criadas algumas regras de convivências para cada agente existente no ecosistema. 

Inicialmente foram criadas rainhas para determinar o ponto onde fica o formigueiro e também repoduzir para cada formigueiro existente, a cada reprodução, nascem de 6 a 12 formigas, existe 15% de chances de vir uma formiga macho, 70% de chances de ser uma operária e 15% de chances de ser uma formiga combatente.

As formigas machos sempre procuram rainhas para reproduzir desde que não sejam suas progenitoras, e quando encontram nem sempre conseguem reproduzir...

As formigas combatentes possuem um poder randômico para atacar as outros e possuem mais vida que as operárias. Sempre que ele encontra uma formiga de outro formigueiro ela ataca!

As formigas precisam comer, se não uma hora morrem, por isso sempre que come uma comidinha elas incrementam a vida em alguns pontos.

O cheiro da comida é o rastro deixado pela comida para que as formigas aas encontrem mais facilmente.

O feromônio é a substância química deixada pelas formigas para comunicarem as outras que encontrarem uma comida.

## Screenshots

<p>
    <img src="https://user-images.githubusercontent.com/49161615/188467430-4aa6450d-3db8-4cd2-b8e8-0e5857e18b6a.png" width="700" height="400" />
    <img src="https://user-images.githubusercontent.com/49161615/188467460-f61cc0c3-2c44-45de-a911-82920679e8fc.png" width="700" height="400" />
</p>


## Instalação 
**Linguagens**: Python<br>
**Tecnologias**: Mesa e python<br>


## Uso 
Uso por ambiente virtual 
```bash
$ git clone  https://github.com/UnBParadigmas2022-1/2022.1_G3_SMA_Formigueiro.git
$ cd 2022.1_G3_SMA_Formigueiro

$ python -m venv formigas
$ source formigueiro/bin/activate
$ pip install -r requirements.txt

$ mesa runserver
```

Também pode ser usado com docker:

```bash
$ make build
$ make run
```
Para parar o container

```bash
$ make stop
```
e para parar e exculir

```bash
$ make clean
```

Explique como usar seu projeto.
Procure ilustrar em passos, com apoio de telas do software.

## Vídeo
Adicione 1 ou mais vídeos com a execução do projeto.
Procure: 
(i) Introduzir o projeto;
(ii) Mostrar passo a passo o código, explicando-o, e deixando claro o que é de terceiros, e o que é contribuição real da equipe;
(iii) Apresentar particularidades do Paradigma, da Linguagem, e das Tecnologias, e
(iV) Apresentar lições aprendidas, contribuições, pendências, e ideias para trabalhos futuros.
OBS: TODOS DEVEM PARTICIPAR, CONFERINDO PONTOS DE VISTA.
TEMPO: +/- 15min


## Participações

|Nome do Membro | Contribuição | Significância da Contribuição para o Projeto (Excelente/Boa/Regular/Ruim/Nula) |
| :--:| :--: | :--: |
| Antonio Aldisio  |  Rainha e formiga Macho | Excelente |
| Rafael Ramos  | --- | Excelente |
| Thiago Paiva  |  ---- | Excelente |
| João Pedro Moura | ---- | Excelente |
| Lucas Gomes | ---- | Excelente |
| Lucas Boaventura |  ---| Excelente |
| Dafne Moretti | --- | Excelente |
| Igor Lima | ---- | Excelente |

## Outros 
Quaisquer outras informações sobre o projeto podem ser descritas aqui.
(i) Lições Aprendidas;

### Percepções:
Como o python tem uma trava no GIL(Global interpreter lock) as threads não são reais, uma vez que apenas uma thread tem controle sobre o interpretador, então não tivemos os desafios do paralelismo e concorrência.

### Fragilidades:
As nossas fragilidades são relacionadas com a fidelidade do mundo real com o desenvolvido nesse projeto. Sendo assim, temos as seguintes:
- Rainha eterna, ela não morre.
- Decomposição imeditada de formiga morta.
- Reprodução imeditada de novas formigas.
- Ausência da necessidade de levar comida a rainha e as formigas machos.


### Trabalhos Futuros.
Os trabalhamos futuros podem ser em cima das nossas fragilidades, mas também pode ser melhorar gráficamente o projeto, ou seja, colocar imagem de formigas ao invés de quadradinhos


## Fontes
Referencie, adequadamente, as referências utilizadas.
Indique ainda, fontes de leitura complementares.
