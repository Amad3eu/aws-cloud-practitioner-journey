# Módulo 8: migração, IA e revisão

Aulas 40 a 45. Fecha os domínios 1 e 3 e revisa os quatro. Prática: [registro de simulados](../simulados/erros-e-revisoes.md).

## Resumo

### As sete estratégias de migração (7 Rs)

| Estratégia | O que é |
|------------|---------|
| Retire | Desligar o que não é mais usado |
| Retain | Manter onde está, por enquanto |
| Rehost | Mover sem alterar, o "lift and shift" |
| Relocate | Mover a plataforma inteira, como VMware, sem alterar |
| Repurchase | Trocar por um produto SaaS |
| Replatform | Mover com pequenos ajustes, como trocar o banco por RDS |
| Refactor | Reescrever para aproveitar a nuvem |

### Serviços de migração

| Serviço | O que faz |
|---------|-----------|
| Migration Hub | Acompanha a migração em um painel |
| Application Migration Service | Replica servidores para a AWS (rehost) |
| Database Migration Service | Migra bancos de dados |
| DataSync | Copia arquivos pela rede |
| Snow Family | Leva dados em equipamento físico |

### Infraestrutura como código e ferramentas de desenvolvimento

| Serviço | O que faz |
|---------|-----------|
| CloudFormation | Cria a infraestrutura a partir de um modelo em YAML ou JSON |
| CDK | Descreve a infraestrutura em linguagem de programação e gera CloudFormation |
| CodeBuild | Compila e testa o código |
| CodeDeploy | Publica o código nos servidores |
| CodePipeline | Encadeia as etapas de entrega |
| Systems Manager | Opera e aplica correções em frotas de servidores |

### IA e machine learning

| Serviço | O que faz |
|---------|-----------|
| SageMaker | Constrói, treina e publica modelos próprios |
| Bedrock | Dá acesso a modelos de fundação por API |
| Amazon Q | Assistente de IA para negócios e para desenvolvimento |
| Rekognition | Analisa imagens e vídeos |
| Textract | Extrai texto e tabelas de documentos |
| Comprehend | Analisa texto: sentimento, entidades, idioma |
| Transcribe | Converte fala em texto |
| Polly | Converte texto em fala |
| Translate | Traduz texto |
| Lex | Cria chatbots de voz e texto |
| Kendra | Busca inteligente em documentos da empresa |

## Estratégia de prova

São 65 questões em 90 minutos, o que dá cerca de 83 segundos por questão. Resposta errada não desconta ponto, então nenhuma questão fica em branco. As questões de múltipla resposta dizem quantas alternativas marcar.

1. Leia a última frase da questão primeiro, para saber o que se pede.
2. Procure a palavra que decide: "mais barato", "menor esforço operacional", "alta disponibilidade".
3. Elimine as alternativas com serviço de outra categoria.
4. Marque para revisão o que passar de dois minutos e siga em frente.

## Pegadinhas

- Rehost não altera nada. Replatform ajusta pouco. Refactor reescreve.
- Polly fala, Transcribe escuta.
- Textract lê documentos. Rekognition analisa imagens e vídeos.
- SageMaker é para quem treina o próprio modelo. Bedrock é para quem usa um modelo pronto.

## Anotações de aula

### Aula 40

-

### Aula 41

-

### Aula 42

-

### Aula 43

-

### Aula 44

-

### Aula 45

-

## Perguntas para responder sem consultar

- [ ] Qual estratégia de migração é o "lift and shift"?
- [ ] Qual serviço cria infraestrutura a partir de um arquivo YAML?
- [ ] Qual serviço converte um áudio de reunião em texto?
- [ ] Quais são os quatro domínios da prova e o peso de cada um?
