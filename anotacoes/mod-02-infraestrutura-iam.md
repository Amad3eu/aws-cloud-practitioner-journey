# Módulo 2: infraestrutura global e IAM

Aulas 06 a 11. Domínio 2 do exame (30%), o de maior peso depois de tecnologia. Laboratório: [02, políticas IAM em JSON](../projetos/02-iam-politicas-json/).

## Resumo

### Infraestrutura global

| Peça | O que é |
|------|---------|
| Região | Área geográfica isolada das outras, com pelo menos três zonas de disponibilidade |
| Zona de disponibilidade (AZ) | Um ou mais data centers com energia e rede próprias |
| Ponto de presença | Local de borda usado pelo CloudFront e pelo Route 53 para ficar perto do usuário |
| Local Zone | Extensão de uma região perto de uma cidade grande, para baixa latência |
| Outposts | Hardware da AWS instalado no data center do cliente |

Para escolher a região, pese quatro critérios: exigência legal sobre onde o dado fica, latência até os usuários, serviços disponíveis nela e preço.

### Responsabilidade compartilhada

A AWS responde pela segurança da nuvem: prédios, hardware, rede e a camada de virtualização. O cliente responde pela segurança na nuvem: dados, permissões, configuração de rede e criptografia.

| Serviço | AWS cuida de | Você cuida de |
|---------|--------------|---------------|
| EC2 | Hardware e hipervisor | Sistema operacional, atualizações, security groups, dados |
| RDS | Sistema operacional e atualização do banco | Usuários do banco, security groups, dados |
| S3 e Lambda | Toda a infraestrutura | Permissões, dados e o código |

### IAM

| Conceito | O que é |
|----------|---------|
| Usuário | Identidade de uma pessoa ou sistema, com credencial permanente |
| Grupo | Conjunto de usuários que recebe as mesmas políticas |
| Função (role) | Identidade sem senha, assumida por tempo limitado por um serviço ou pessoa |
| Política | Documento JSON que permite ou nega ações |

Na avaliação de uma política, a negação explícita vence qualquer permissão. Sem permissão explícita, a resposta é negar.

Só o usuário raiz consegue fechar a conta, trocar o plano de suporte e alterar os dados da conta. Para todo o resto, use outra identidade.

### Organizations

O AWS Organizations agrupa várias contas, consolida a fatura e aplica SCPs, que limitam o que as contas podem fazer. O IAM Identity Center dá um login único para todas elas.

### Serviços de segurança

| Serviço | Para que serve |
|---------|----------------|
| Shield | Proteção contra DDoS. O Standard é gratuito, o Advanced é pago |
| WAF | Filtra requisições HTTP maliciosas, como SQL injection |
| GuardDuty | Detecta ameaças analisando logs da conta |
| Inspector | Procura vulnerabilidades em EC2, imagens de container e funções Lambda |
| Macie | Encontra dados pessoais em buckets S3 |
| KMS | Cria e gerencia chaves de criptografia |
| Secrets Manager | Guarda e rotaciona senhas e chaves |
| Certificate Manager (ACM) | Emite certificados TLS |
| Artifact | Baixa relatórios de conformidade da AWS, como ISO e SOC |
| Security Hub | Reúne os achados de segurança em um painel |

## Pegadinhas

- IAM é global e gratuito.
- Security group pertence a redes, mas cai em questões de segurança. Detalhes no módulo 3.
- GuardDuty detecta ameaça, Inspector procura vulnerabilidade, Macie procura dado sensível.
- Relatório de conformidade da AWS se baixa no Artifact. Conformidade dos seus recursos se acompanha no Config.

## Anotações de aula

### Aula 06

-

### Aula 07

-

### Aula 08

-

### Aula 09

-

### Aula 10

-

### Aula 11

-

## Perguntas para responder sem consultar

- [ ] Quem atualiza o sistema operacional de uma instância EC2? E de um banco RDS?
- [ ] Qual a diferença entre usuário e função no IAM?
- [ ] Quais tarefas só o usuário raiz faz?
- [ ] Qual serviço protege contra DDoS e qual filtra SQL injection?
