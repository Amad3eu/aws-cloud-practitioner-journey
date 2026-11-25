# Módulo 3: computação e redes

Aulas 12 a 18. Domínio 3 do exame (34%). Laboratório: [03, EC2 com load balancer](../projetos/03-ec2-load-balancer/).

## Resumo

### Famílias de instância EC2

| Família | Uso | Exemplos |
|---------|-----|----------|
| Uso geral | Servidores web e ambientes de teste | T, M |
| Otimizada para computação | Processamento em lote, jogos | C |
| Otimizada para memória | Bancos em memória, cache | R, X |
| Otimizada para armazenamento | Muita leitura e escrita em disco local | I, D |
| Computação acelerada | Machine learning e gráficos, com GPU | P, G |

### Modelos de compra do EC2

| Modelo | Como funciona | Quando usar |
|--------|---------------|-------------|
| Sob demanda | Paga por segundo, sem compromisso | Carga curta ou imprevisível |
| Savings Plans | Compromisso de gasto por hora por 1 ou 3 anos, até 72% de desconto | Uso constante, com liberdade para trocar de instância |
| Instâncias reservadas | Compromisso com um tipo de instância por 1 ou 3 anos | Uso constante e previsível |
| Spot | Capacidade ociosa com até 90% de desconto, pode ser interrompida com 2 minutos de aviso | Carga que tolera interrupção |
| Dedicated Host | Servidor físico só seu | Licença por soquete ou exigência regulatória |

### Balanceamento e escala

| Serviço | O que faz |
|---------|-----------|
| Application Load Balancer | Distribui HTTP e HTTPS, na camada 7 |
| Network Load Balancer | Distribui TCP e UDP com latência muito baixa, na camada 4 |
| Gateway Load Balancer | Encaminha tráfego para appliances de segurança |
| Auto Scaling | Adiciona e remove instâncias conforme a demanda |

### VPC

| Peça | O que é |
|------|---------|
| Sub-rede pública | Tem rota para o internet gateway |
| Sub-rede privada | Não tem rota direta para a internet |
| Internet gateway | Liga a VPC à internet |
| NAT gateway | Deixa a sub-rede privada sair para a internet, sem aceitar entrada |
| VPC peering | Liga duas VPCs |
| Transit Gateway | Liga muitas VPCs e redes locais em um ponto central |
| VPC endpoint | Acessa serviços da AWS sem passar pela internet |

| | Security group | Network ACL |
|---|----------------|-------------|
| Atua em | Instância | Sub-rede |
| Estado | Com estado: a resposta é liberada sozinha | Sem estado: precisa de regra de ida e de volta |
| Regras | Só de permissão | Permissão e negação |

### Conectividade e borda

| Serviço | O que faz |
|---------|-----------|
| Route 53 | DNS, registro de domínio e verificação de saúde |
| CloudFront | CDN que guarda cópias do conteúdo nos pontos de presença |
| Global Accelerator | Encaminha o tráfego pela rede da AWS com IPs fixos |
| Site-to-Site VPN | Túnel criptografado pela internet até o data center |
| Direct Connect | Conexão física dedicada, sem passar pela internet |

## Pegadinhas

- "Tolera interrupção" aponta para Spot. "Uso constante por um ano" aponta para Savings Plans ou reservada.
- Direct Connect leva semanas para instalar. VPN fica pronta em minutos.
- CloudFront acelera conteúdo que pode ser guardado em cache. Global Accelerator acelera TCP e UDP em geral.
- O NAT gateway é cobrado por hora e não entra no Free Tier.

## Anotações de aula

### Aula 12

-

### Aula 13

-

### Aula 14

-

### Aula 15

-

### Aula 16

-

### Aula 17

-

### Aula 18

-

## Perguntas para responder sem consultar

- [ ] Qual modelo de compra serve para um processamento que pode ser interrompido?
- [ ] O que torna uma sub-rede pública?
- [ ] Qual a diferença entre security group e network ACL?
- [ ] Quando usar Direct Connect no lugar de VPN?
