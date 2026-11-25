# Módulo 5: bancos de dados

Aulas 24 a 28. Domínio 3 do exame (34%). Laboratório: [05, RDS e DynamoDB com Python](../projetos/05-rds-dynamodb-python/).

## Resumo

### Relacionais

| Serviço | O que é |
|---------|---------|
| RDS | Banco relacional gerenciado, com MySQL, PostgreSQL, MariaDB, Oracle, SQL Server e Db2 |
| Aurora | Banco da AWS compatível com MySQL e PostgreSQL, com armazenamento replicado em três zonas |

No RDS, a AWS cuida de backup, atualização e troca de hardware. Você cuida do esquema, das consultas e de quem acessa.

| Recurso do RDS | Para que serve |
|----------------|----------------|
| Multi-AZ | Disponibilidade: mantém uma cópia em outra zona e assume sozinha em caso de falha |
| Réplica de leitura | Performance: divide as consultas de leitura |
| Backup automático | Restaura o banco para um ponto no tempo |

### NoSQL e propósito específico

| Serviço | Tipo | Uso típico |
|---------|------|------------|
| DynamoDB | Chave-valor, serverless | Resposta em milissegundos em qualquer escala |
| ElastiCache | Cache em memória (Redis, Valkey, Memcached) | Tirar carga do banco e guardar sessão |
| DocumentDB | Documentos, compatível com MongoDB | Catálogos e perfis |
| Neptune | Grafos | Redes sociais, detecção de fraude |
| Keyspaces | Colunar, compatível com Cassandra | Migração de Cassandra |
| Timestream | Séries temporais | Métricas e dados de IoT |

### Análise de dados

| Serviço | O que faz |
|---------|-----------|
| Redshift | Data warehouse para consultas analíticas em grande volume |
| Athena | Consulta arquivos no S3 com SQL, sem servidor |
| Glue | ETL e catálogo de dados |
| Kinesis | Recebe e processa dados em tempo real |
| EMR | Clusters de Hadoop e Spark |
| QuickSight | Painéis e relatórios |

### Migração

| Serviço | O que faz |
|---------|-----------|
| DMS | Migra o banco com a origem funcionando |
| Schema Conversion Tool | Converte o esquema quando o banco de destino é de outro tipo |

## Pegadinhas

- Multi-AZ serve para disponibilidade e a cópia não atende leitura. Réplica de leitura serve para performance.
- OLTP (transações do dia a dia) é RDS ou Aurora. OLAP (análise) é Redshift.
- "SQL direto em arquivos no S3" é Athena.
- DynamoDB é serverless: não tem instância para escolher.
- Rodar banco no EC2 é possível, mas o backup e as atualizações voltam a ser seus.

## Anotações de aula

### Aula 24

-

### Aula 25

-

### Aula 26

-

### Aula 27

-

### Aula 28

-

## Perguntas para responder sem consultar

- [ ] Qual a diferença entre Multi-AZ e réplica de leitura?
- [ ] Qual banco usar para um carrinho de compras que precisa responder em milissegundos?
- [ ] Qual serviço consulta arquivos CSV no S3 com SQL?
- [ ] Qual serviço migra um banco Oracle para Aurora com a origem no ar?
