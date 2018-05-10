# vulper-challenge
Do or do not, there is no try!

## Instruções

**1.** Crie um **fork** deste projeto.

**2.** Desenvolva a história descrita abaixo.

**3.** Depois de concluir, faça um **pull request** contendo tudo que você desenvolveu, informando seu e-mail na descrição do Pull Request.

**4.** Você **deve** utilizar [Django REST](http://www.django-rest-framework.org/#api-guide) para expor seu end-point. 

Dica: o Framework [Django](https://docs.djangoproject.com/pt-br/1.11/intro/tutorial01/) pode te ajudar a dar um rápido bootstrap da aplicação REST usando o Django. 

==============

### Introdução

Seu código será avaliado principalmente nos seguintes aspectos:

**1.** Conhecimento em aspectos de SOA e boas práticas em aplicações REST.

**2.** Capacidade de construção de classes coesas e métodos não complexos.

**3.** Qualidade do código em geral.

**4.** Funcionamento do código (óbvio).

Levamos muito a sério nesse teste a garantia de que tudo esteja funcionando corretamente. Nada de end-points incorretos sendo consumidos nem binds com atributos incorretos hein :)

==============

A Vulpi está reescrevendo seu sistema de buscas no Github e deseja consumir a nova versão da [Github API 3.0](https://developer.github.com/v3/search/#search-users) \o/.

Para isso, precisamos de um sistema implemente a história abaixo.

### História [TEAM A]

Eu como desenvolvedor, quero poder fazer uma requisição à um end-point como:

`http://XX.XX.XX.XX/vulpi-api/professional`

para inserir e obter uma lista de desenvolvedores encontrados no Github.

Dessa forma, poderei obter as seguintes informações sobre cada um dos desenvolvedores encontrados: **login**, **telefone** e **classificação**. O Campo do json **classificação** deve respeitar algumas regras descritas abaixo.

Caso a pontuação dada pelo Github ao desenvolvedor seja:
- **menor** do que 3.5, o campo "classificacao" será: aprendiz jedi.
- **maior ou igual** a 3.5, o campo "classificacao" será: cavaleiro jedi.

Para cumprir o desafio, use a [Github Search API](https://developer.github.com/v3/search/#search-users)


### História [TEAM B]

Eu como desenvolvedor, quero poder fazer uma requisição à um end-point como:

`http://XX.XX.XX.XX/vulpi-api/company`

para inserir e obter uma lista de empresas encontrados no Github.

Dessa forma, poderei obter as seguintes informações sobre cada uma das empresas encontrados: **Razão Social**, **telefone** e **quantidade_de_devs**. O Campo do json **classificação** deve respeitar algumas regras descritas abaixo.

Caso a quantidade de desenvolvedores seja:
- **menor** do que 10, o campo "quantidade_de_devs" será: Vollmir.
- **maior ou igual** a 10, o campo "classificacao" será: Asgard.

Para cumprir o desafio, use a [Love Mondays](https://www.lovemondays.com.br)
