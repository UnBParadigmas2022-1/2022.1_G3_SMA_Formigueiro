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
O projeto trata da representação de um formigueiro fantasia, onde foram criadas algumas regras de convivência para cada agente existente no ecossistema. 
Inicialmente foram criadas rainhas para determinar o ponto onde fica o formigueiro e também reproduzir para cada formigueiro existente. A cada reprodução da rainha, nascem de 6 a 12 formigas, com 25% de chance de vir uma formiga macho, 60% de chance de ser uma operária e 15% de chance de ser uma formiga combatente.

As formigas machos sempre procuram rainhas para reproduzir desde que não sejam suas progenitoras, e quando encontram nem sempre conseguem reproduzir...

As formigas combatentes possuem um poder randômico para atacar as outros e possuem mais vida que as operárias. Sempre que ele encontra uma formiga de outro formigueiro ela ataca!

As formigas precisam comer, se não uma hora morrem, por isso sempre que comem a sua vida é incrementada em alguns pontos.

O cheiro da comida é o rastro deixado pela comida para que as formigas às encontrem mais facilmente.

O feromônio é a substância química deixada pelas formigas para comunicarem as outras que encontrarem uma comida.

## Screenshots

<p>
    <img src="https://user-images.githubusercontent.com/49161615/188467430-4aa6450d-3db8-4cd2-b8e8-0e5857e18b6a.png"/>
    <img src="https://user-images.githubusercontent.com/49161615/188467460-f61cc0c3-2c44-45de-a911-82920679e8fc.png"/>
    <img src="https://user-images.githubusercontent.com/46077033/188521537-7a9bf23d-d00d-42f2-aca4-046efc7a6790.gif"/>
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

Também pode ser usado com o <b>docker</b>:

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

## Vídeo
https://youtu.be/zzppunu7x84

## Participações

|Nome do Membro | Contribuição | Significância da Contribuição para o Projeto (Excelente/Boa/Regular/Ruim/Nula) |
| :--:| :--: | :--: |
| Antonio Aldisio  |  Rainha e formiga Macho | Excelente |
| Rafael Ramos  | Combatentes | Excelente |
| Thiago Paiva  | Comida e Renderização | Excelente |
| João Pedro Moura | Operárias e Estrutura geral do projeto | Excelente |
| Lucas Gomes | Rainha e Formiga Macho | Excelente |
| Lucas Boaventura | Combatentes | Excelente |
| Dafne Moretti | Operárias | Excelente |
| Igor Lima | Comida e Cheiro da Comida | Excelente |

### Percepções:
Como o python tem uma trava no GIL(Global interpreter lock) as threads não são reais, uma vez que apenas uma thread tem controle sobre o interpretador, então não tivemos os desafios do paralelismo e concorrência.

### Fragilidades:
As nossas fragilidades são relacionadas com a fidelidade do mundo real, e com a utilização do paradigma em sí. Sendo assim, pontos de destaque:
- Rainha eterna, ela não morre.
- Decomposição imeditada de formiga morta.
- Reprodução imeditada de novas formigas.
- Ausência da necessidade de levar comida a rainha e as formigas machos.
- Grande utilização do paradígma Orientado à Objetos para resolução de problemas.

### Trabalhos Futuros.
Os trabalhamos futuros podem ser em cima das nossas fragilidades, mas também pode ser melhorar gráficamente o projeto, ou seja, colocar imagem de formigas ao invés de quadradinhos. Outro ponto que pode ser destacado, é o desenvolvimento de novos agentes e a evolução dos já existentes, tornando cada vez mais fidedígna a simulação com a realidade. Por fim, vale a pena citar que a utilização de uma plataforma que possua uma maior escalabilidade também é bem vinda como uma inovação.

## Fontes
- Inpirado em: Ants Model. Disponível em: https://github.com/mgoadric/ants-mesa
- Documentação do Mesa. Disponível em: https://mesa.readthedocs.io/en/latest/index.html
