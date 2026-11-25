# Módulo 4: armazenamento

Aulas 19 a 23. Domínio 3 do exame (34%). Laboratório: [04, site estático no S3](../projetos/04-s3-site-estatico/).

## Resumo

### Tipos de armazenamento

| Tipo | Serviço | Como se acessa |
|------|---------|----------------|
| Objeto | S3 | Por HTTP, de qualquer lugar |
| Bloco | EBS | Como disco de uma instância EC2 |
| Arquivo | EFS, FSx | Como pasta de rede montada em várias instâncias |

### Classes do S3

| Classe | Para quê | Recuperação |
|--------|----------|-------------|
| Standard | Acesso frequente | Imediata |
| Intelligent-Tiering | Padrão de acesso desconhecido, move sozinho entre camadas | Imediata |
| Standard-IA | Acesso raro, em várias zonas | Imediata, com taxa por recuperação |
| One Zone-IA | Acesso raro, em uma zona só, mais barato | Imediata, com taxa por recuperação |
| Glacier Instant Retrieval | Arquivo acessado poucas vezes por ano | Milissegundos |
| Glacier Flexible Retrieval | Arquivo | Minutos a horas |
| Glacier Deep Archive | Arquivo de longo prazo, o mais barato | De 12 a 48 horas |

O S3 foi projetado para 99,999999999% de durabilidade, os onze noves.

### Recursos do S3

| Recurso | O que faz |
|---------|-----------|
| Versionamento | Guarda as versões antigas de cada objeto |
| Ciclo de vida | Move objetos de classe ou apaga depois de um prazo |
| Replicação | Copia objetos para outro bucket, na mesma região ou em outra |
| Block Public Access | Trava que impede acesso público, ligada por padrão |
| Política de bucket | JSON que define quem acessa o bucket |
| Site estático | Serve HTML direto do bucket |

### Bloco e arquivo

| Serviço | Características |
|---------|-----------------|
| EBS | Disco persistente, preso a uma zona, com snapshots guardados no S3 |
| Instance store | Disco físico do servidor, muito rápido, que perde os dados quando a instância para |
| EFS | Sistema de arquivos NFS para Linux, em várias zonas, que cresce sozinho |
| FSx | Sistemas de arquivos gerenciados, como Windows File Server e Lustre |

### Híbrido, transferência e backup

| Serviço | O que faz |
|---------|-----------|
| Storage Gateway | Faz o data center enxergar o S3 como disco, pasta ou fita |
| Snow Family | Equipamentos físicos para levar grandes volumes de dados até a AWS |
| DataSync | Copia dados pela rede entre o data center e a AWS |
| AWS Backup | Centraliza as políticas de backup de vários serviços |

## Pegadinhas

- Nome de bucket é único no mundo todo, mas o bucket fica em uma região.
- EBS atende uma instância por vez, salvo exceções. Pasta compartilhada entre várias instâncias Linux é EFS.
- Instance store some quando a instância para. EBS continua.
- "Menor custo para guardar por anos" é Glacier Deep Archive.
- Snapshot de EBS é incremental e fica no S3.

## Anotações de aula

### Aula 19

-

### Aula 20

-

### Aula 21

-

### Aula 22

-

### Aula 23

-

## Perguntas para responder sem consultar

- [ ] Qual classe do S3 usar quando não se sabe a frequência de acesso?
- [ ] Qual a diferença entre EBS, EFS e S3?
- [ ] O que acontece com os dados do instance store quando a instância para?
- [ ] Qual serviço leva 80 TB para a AWS com uma internet lenta?
