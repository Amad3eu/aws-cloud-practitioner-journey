# Módulo 6: serverless e containers

Aulas 29 a 33. Domínio 3 do exame (34%). Laboratório: [06, Lambda com API Gateway](../projetos/06-lambda-api-gateway/).

## Resumo

Serverless quer dizer que você não administra servidor. A AWS provisiona, escala e cobra pelo uso.

### Lambda

| Característica | Valor |
|----------------|-------|
| Cobrança | Por requisição e por tempo de execução, em milissegundos |
| Tempo máximo | 15 minutos por execução |
| Escala | Automática, uma execução por evento |
| Gatilhos comuns | API Gateway, S3, DynamoDB, EventBridge, SQS |
| Free Tier | 1 milhão de requisições por mês, sem prazo |

### API Gateway

Cria, publica e protege APIs. Há três tipos: HTTP API, mais simples e barata; REST API, com mais recursos; e WebSocket API, para comunicação nos dois sentidos.

### Containers

| Serviço | O que é |
|---------|---------|
| ECR | Registro de imagens de container |
| ECS | Orquestrador de containers da AWS |
| EKS | Kubernetes gerenciado |
| Fargate | Roda containers do ECS ou do EKS sem você administrar instâncias |

### Integração de aplicações

| Serviço | Modelo | Uso |
|---------|--------|-----|
| SQS | Fila | Um consumidor retira cada mensagem; desacopla dois sistemas |
| SNS | Publicação e assinatura | Uma mensagem vai para vários assinantes: e-mail, SMS, Lambda, SQS |
| EventBridge | Barramento de eventos | Regras encaminham eventos da AWS e de aplicações, e agendam tarefas |
| Step Functions | Orquestração | Encadeia passos, com espera, tentativa e desvio |

### Computação gerenciada

| Serviço | O que é |
|---------|---------|
| Elastic Beanstalk | Você envia o código e ele cria EC2, load balancer e Auto Scaling |
| Lightsail | Servidor virtual com preço fixo mensal, para projetos pequenos |
| Batch | Executa lotes de tarefas em containers |

## Pegadinhas

- Tarefa de mais de 15 minutos não cabe na Lambda. Use Fargate, Batch ou EC2.
- SQS é fila, com um consumidor por mensagem. SNS distribui a mesma mensagem para vários.
- Fargate é a forma serverless de rodar container. ECS e EKS são os orquestradores.
- "Desacoplar" quase sempre pede SQS.
- No Elastic Beanstalk o serviço é gratuito, e você paga pelos recursos que ele cria.

## Anotações de aula

### Aula 29

-

### Aula 30

-

### Aula 31

-

### Aula 32

-

### Aula 33

-

## Perguntas para responder sem consultar

- [ ] Qual o tempo máximo de execução de uma função Lambda?
- [ ] Qual a diferença entre SQS e SNS?
- [ ] O que o Fargate tira da sua responsabilidade?
- [ ] Qual serviço usar para rodar uma função todo dia às 8h?
