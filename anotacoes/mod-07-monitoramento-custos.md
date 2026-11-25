# Módulo 7: monitoramento e custos

Aulas 34 a 39. Domínio 4 do exame (12%), mais as partes de monitoramento dos domínios 2 e 3. Laboratório: [07, AWS Budgets e FinOps](../projetos/07-aws-budgets-finops/).

## Resumo

### Monitoramento e auditoria

| Serviço | Pergunta que responde |
|---------|-----------------------|
| CloudWatch | Como está o desempenho? Métricas, alarmes, logs e painéis |
| CloudTrail | Quem fez o quê, quando e de onde? Registro das chamadas de API |
| Config | Como estava a configuração deste recurso e ela segue as regras? |
| Trusted Advisor | O que posso melhorar em custo, performance, segurança, tolerância a falhas, limites de serviço e operação? |
| Health Dashboard | Há algum incidente da AWS afetando a minha conta? |

### Como a AWS cobra

A cobrança tem três princípios: pague pelo que usa, pague menos quando se compromete e pague menos por unidade quando usa mais.

| Item | Regra geral |
|------|-------------|
| Dados entrando na AWS | Gratuito |
| Dados saindo para a internet | Cobrado por GB |
| Dados entre regiões | Cobrado |
| IPv4 público | US$ 0,005 por hora por endereço |

### Ferramentas de custo

| Ferramenta | Para quê |
|------------|----------|
| Pricing Calculator | Estimar o custo antes de criar |
| Cost Explorer | Analisar o gasto passado em gráficos e prever o futuro |
| Budgets | Definir um limite e receber alerta quando o gasto chegar perto |
| Cost and Usage Report | O relatório mais detalhado, em arquivo no S3 |
| Tags de alocação de custo | Separar o gasto por projeto, time ou ambiente |
| Compute Optimizer | Recomendar o tamanho certo das instâncias |

O Organizations consolida a fatura de várias contas, e o volume somado entra nas faixas de desconto.

### Planos de suporte

A prova CLF-C02 cobra os cinco planos abaixo.

| Plano | Canal | Tempo de resposta mais rápido | Extra |
|-------|-------|-------------------------------|-------|
| Basic | Só faturamento e conta | Não tem | Gratuito, com Trusted Advisor limitado |
| Developer | E-mail em horário comercial | 12 horas, sistema com problema | Um contato |
| Business | Telefone e chat 24 horas | 1 hora, produção fora do ar | Trusted Advisor completo |
| Enterprise On-Ramp | Telefone e chat 24 horas | 30 minutos, sistema crítico fora do ar | Grupo de gerentes técnicos (TAM) |
| Enterprise | Telefone e chat 24 horas | 15 minutos, sistema crítico fora do ar | TAM designado |

O catálogo real mudou depois do guia do exame. Desde 2 de dezembro de 2025 a AWS não vende mais Developer nem Business para novas assinaturas, e os planos Developer, Business e Enterprise On-Ramp saem de linha em 1º de janeiro de 2027. Os planos atuais são Business Support+, Enterprise e Unified Operations. Para a prova, estude a tabela acima. Os detalhes estão na [documentação de planos de suporte](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html).

## Pegadinhas

- CloudWatch mede desempenho. CloudTrail audita chamadas de API. Config acompanha configuração.
- Pricing Calculator estima antes. Cost Explorer analisa depois. Budgets alerta.
- Gerente técnico de conta (TAM) designado só existe no Enterprise.
- O console do Cost Explorer é gratuito, mas a API dele cobra US$ 0,01 por requisição.
- Budgets avisa, e por padrão não desliga nada.

## Anotações de aula

### Aula 34

-

### Aula 35

-

### Aula 36

-

### Aula 37

-

### Aula 38

-

### Aula 39

-

## Perguntas para responder sem consultar

- [ ] Qual serviço mostra quem apagou um bucket?
- [ ] Qual ferramenta estima o custo de uma arquitetura que ainda não existe?
- [ ] Qual o plano de suporte mais barato com telefone 24 horas?
- [ ] O que é cobrado na transferência de dados e o que é gratuito?
