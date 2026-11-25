# AWS Cloud Practitioner Journey

![AWS](https://img.shields.io/badge/AWS-Cloud-FF9900)
![Certificação](https://img.shields.io/badge/Certifica%C3%A7%C3%A3o-CLF--C02-232F3E)
![Status](https://img.shields.io/badge/Status-Em%20andamento-yellow)
![Aulas](https://img.shields.io/badge/Aulas-0%2F45-lightgrey)

Caderno de estudos e laboratórios para a certificação AWS Certified Cloud Practitioner (CLF-C02). Acompanha a trilha de 45 aulas da CloudStart Academy: cada módulo tem um arquivo de anotações e um laboratório que roda pelo Console e pela AWS CLI.

## A prova

| Item | Valor |
|------|-------|
| Código | CLF-C02 |
| Questões | 65, das quais 50 valem nota e 15 são de teste |
| Duração | 90 minutos |
| Nota mínima | 700 de 1000 |
| Preço | US$ 100 |
| Formato | múltipla escolha e múltipla resposta |

| Domínio | Peso | Onde estudo |
|---------|------|-------------|
| 1. Conceitos de nuvem | 24% | Módulo 1 |
| 2. Segurança e conformidade | 30% | Módulo 2 |
| 3. Tecnologia e serviços de nuvem | 34% | Módulos 3, 4, 5, 6 e 8 |
| 4. Faturamento, preços e suporte | 12% | Módulo 7 |

Os pesos e a lista de serviços cobrados estão na [página oficial da certificação](https://aws.amazon.com/certification/certified-cloud-practitioner/).

## Progresso

| Módulo | Tema | Aulas | Feitas | Anotações | Laboratório | Status |
|--------|------|-------|--------|-----------|-------------|--------|
| 1 | Conceitos de nuvem | 01 a 05 | 0/5 | [mod-01](anotacoes/mod-01-conceitos-nuvem.md) | [01](projetos/01-arquitetura-well-architected/) | A fazer |
| 2 | Infraestrutura global e IAM | 06 a 11 | 0/6 | [mod-02](anotacoes/mod-02-infraestrutura-iam.md) | [02](projetos/02-iam-politicas-json/) | A fazer |
| 3 | Computação e redes | 12 a 18 | 0/7 | [mod-03](anotacoes/mod-03-computacao-redes.md) | [03](projetos/03-ec2-load-balancer/) | A fazer |
| 4 | Armazenamento | 19 a 23 | 0/5 | [mod-04](anotacoes/mod-04-armazenamento.md) | [04](projetos/04-s3-site-estatico/) | A fazer |
| 5 | Bancos de dados | 24 a 28 | 0/5 | [mod-05](anotacoes/mod-05-bancos-de-dados.md) | [05](projetos/05-rds-dynamodb-python/) | A fazer |
| 6 | Serverless e containers | 29 a 33 | 0/5 | [mod-06](anotacoes/mod-06-serverless-containers.md) | [06](projetos/06-lambda-api-gateway/) | A fazer |
| 7 | Monitoramento e custos | 34 a 39 | 0/6 | [mod-07](anotacoes/mod-07-monitoramento-custos.md) | [07](projetos/07-aws-budgets-finops/) | A fazer |
| 8 | Migração, IA e revisão | 40 a 45 | 0/6 | [mod-08](anotacoes/mod-08-migracao-ia-revisao.md) | [simulados](simulados/erros-e-revisoes.md) | A fazer |

Para marcar uma aula, troque `[ ]` por `[x]` na lista do módulo e atualize a coluna Feitas e o selo de aulas no topo. A numeração segue a trilha; os temas abaixo são os do guia do exame na ordem dos módulos, então ajuste o texto para o título de cada aula conforme avançar.

<details>
<summary>Módulo 1: conceitos de nuvem (aulas 01 a 05)</summary>

- [ ] Aula 01: o que é computação em nuvem e as seis vantagens
- [ ] Aula 02: modelos de serviço (IaaS, PaaS, SaaS) e de implantação
- [ ] Aula 03: economia da nuvem, CapEx, OpEx e TCO
- [ ] Aula 04: Well-Architected Framework e os seis pilares
- [ ] Aula 05: Cloud Adoption Framework (CAF)

</details>

<details>
<summary>Módulo 2: infraestrutura global e IAM (aulas 06 a 11)</summary>

- [ ] Aula 06: regiões, zonas de disponibilidade e pontos de presença
- [ ] Aula 07: modelo de responsabilidade compartilhada
- [ ] Aula 08: IAM com usuários, grupos, funções e políticas
- [ ] Aula 09: usuário raiz, MFA e boas práticas de acesso
- [ ] Aula 10: Organizations, SCP e IAM Identity Center
- [ ] Aula 11: serviços de segurança e conformidade

</details>

<details>
<summary>Módulo 3: computação e redes (aulas 12 a 18)</summary>

- [ ] Aula 12: EC2, famílias de instância e AMI
- [ ] Aula 13: modelos de compra do EC2
- [ ] Aula 14: Elastic Load Balancing e Auto Scaling
- [ ] Aula 15: VPC, sub-redes, rotas e gateways
- [ ] Aula 16: security groups e network ACLs
- [ ] Aula 17: Route 53 e CloudFront
- [ ] Aula 18: VPN, Direct Connect e Global Accelerator

</details>

<details>
<summary>Módulo 4: armazenamento (aulas 19 a 23)</summary>

- [ ] Aula 19: S3, buckets e classes de armazenamento
- [ ] Aula 20: S3 com ciclo de vida, versionamento e site estático
- [ ] Aula 21: EBS e instance store
- [ ] Aula 22: EFS e FSx
- [ ] Aula 23: Storage Gateway, Snow Family e AWS Backup

</details>

<details>
<summary>Módulo 5: bancos de dados (aulas 24 a 28)</summary>

- [ ] Aula 24: RDS e Aurora
- [ ] Aula 25: DynamoDB
- [ ] Aula 26: bancos de propósito específico
- [ ] Aula 27: Redshift, Athena e serviços de análise
- [ ] Aula 28: como escolher o banco e migrar com o DMS

</details>

<details>
<summary>Módulo 6: serverless e containers (aulas 29 a 33)</summary>

- [ ] Aula 29: Lambda
- [ ] Aula 30: API Gateway
- [ ] Aula 31: ECS, EKS, ECR e Fargate
- [ ] Aula 32: SQS, SNS, EventBridge e Step Functions
- [ ] Aula 33: Elastic Beanstalk e Lightsail

</details>

<details>
<summary>Módulo 7: monitoramento e custos (aulas 34 a 39)</summary>

- [ ] Aula 34: CloudWatch
- [ ] Aula 35: CloudTrail, Config e Trusted Advisor
- [ ] Aula 36: modelos de preço e Pricing Calculator
- [ ] Aula 37: Billing, Cost Explorer, Budgets e tags de custo
- [ ] Aula 38: Free Tier e como evitar cobrança inesperada
- [ ] Aula 39: planos de suporte

</details>

<details>
<summary>Módulo 8: migração, IA e revisão (aulas 40 a 45)</summary>

- [ ] Aula 40: estratégias de migração (os 7 Rs) e serviços de migração
- [ ] Aula 41: CloudFormation e ferramentas de desenvolvimento
- [ ] Aula 42: serviços de IA e machine learning
- [ ] Aula 43: revisão dos domínios 1 e 2
- [ ] Aula 44: revisão dos domínios 3 e 4
- [ ] Aula 45: simulado final e estratégia de prova

</details>

## Projetos práticos

Cada pasta tem um guia com objetivo, arquitetura, passos pelo Console, comandos da AWS CLI e a limpeza. O custo abaixo vale para a região `us-east-1` com o laboratório apagado no mesmo dia.

| # | Laboratório | Serviços | Custo esperado | Status |
|---|-------------|----------|----------------|--------|
| 01 | [Arquitetura Well-Architected](projetos/01-arquitetura-well-architected/) | Well-Architected Tool | Zero | A fazer |
| 02 | [Políticas IAM em JSON](projetos/02-iam-politicas-json/) | IAM, S3 | Zero | A fazer |
| 03 | [EC2 com load balancer](projetos/03-ec2-load-balancer/) | EC2, ALB, security groups | Até US$ 0,07 por hora ligado | A fazer |
| 04 | [Site estático no S3](projetos/04-s3-site-estatico/) | S3 | Zero | A fazer |
| 05 | [RDS e DynamoDB com Python](projetos/05-rds-dynamodb-python/) | DynamoDB, RDS | DynamoDB zero; RDS até US$ 0,03 por hora ligado | A fazer |
| 06 | [Lambda com API Gateway](projetos/06-lambda-api-gateway/) | Lambda, API Gateway, IAM | Zero | A fazer |
| 07 | [AWS Budgets e FinOps](projetos/07-aws-budgets-finops/) | Budgets, Billing | Zero | A fazer |

Comece pelo laboratório 07. Ele cria o alerta de US$ 1,00 que avisa por e-mail se algum outro laboratório ficar ligado.

## Free Tier: qual é o seu caso

O Free Tier mudou em 15 de julho de 2025, e os laboratórios se comportam de forma diferente em cada regra.

| Conta criada | O que você tem |
|--------------|----------------|
| Antes de 15/07/2025 | 12 meses de uso gratuito por serviço, como 750 horas por mês de EC2 e de RDS |
| A partir de 15/07/2025 | US$ 100 em créditos, mais até US$ 100 ao ativar alguns serviços; o plano gratuito dura 6 meses e os créditos vencem em 12 |

Nos dois casos continuam valendo as ofertas sem prazo, como 1 milhão de requisições de Lambda por mês e 25 GB de DynamoDB. Confira o seu saldo em Billing and Cost Management > Free Tier, e os detalhes na [página do Free Tier](https://aws.amazon.com/free/).

## Checklist de segurança e FinOps

- [ ] MFA ativado no usuário raiz, que não tem chave de acesso
- [ ] Usuário ou função de administrador para o dia a dia, com MFA, no lugar do raiz
- [ ] Orçamento de US$ 1,00 criado antes do primeiro laboratório ([laboratório 07](projetos/07-aws-budgets-finops/))
- [ ] Alertas do Free Tier ligados em Billing preferences
- [ ] Região `us-east-1` conferida antes de cada comando
- [ ] Todo recurso de laboratório criado com a tag `projeto=clf-c02`
- [ ] Limpeza executada e conferida no fim de cada laboratório
- [ ] Varredura semanal por recursos esquecidos (comando abaixo)
- [ ] Bills conferido uma vez por semana no Console
- [ ] `git status` revisado antes de cada commit, sem chave nem `.env`

A varredura lista o que ainda carrega a tag dos laboratórios na região. O esperado é uma lista vazia.

```bash
aws resourcegroupstaggingapi get-resources \
  --region us-east-1 \
  --tag-filters Key=projeto,Values=clf-c02 \
  --query 'ResourceTagMappingList[].ResourceARN' --output table
```

## Como usar

Você precisa de uma conta AWS, da [AWS CLI versão 2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) e de Python 3.

```bash
aws --version                 # precisa começar com aws-cli/2
aws configure                 # região us-east-1, saída json
aws sts get-caller-identity   # confirma em qual conta você está
```

A rotina de cada módulo:

1. Assista às aulas e anote no arquivo do módulo em `anotacoes/`.
2. Faça o laboratório da pasta `projetos/`.
3. Rode a limpeza e a conferência do fim do guia.
4. Marque as aulas e o laboratório neste README.
5. Registre as questões erradas dos simulados em [simulados/erros-e-revisoes.md](simulados/erros-e-revisoes.md).

## Estrutura

```text
aws-cloud-practitioner-journey/
├── README.md
├── anotacoes/      um arquivo por módulo, com resumo e espaço para as notas de aula
├── projetos/       sete laboratórios, cada um com guia e arquivos prontos
└── simulados/      registro das questões erradas e das notas dos simulados
```
