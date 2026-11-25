#!/bin/bash
# User data para Amazon Linux 2023: instala o Nginx e publica uma página
# que mostra de qual instância e de qual zona a resposta veio.
set -euxo pipefail

dnf install -y nginx

# O IMDSv2 exige um token antes de ler os metadados da instância.
TOKEN=$(curl -sX PUT "http://169.254.169.254/latest/api/token" \
  -H "X-aws-ec2-metadata-token-ttl-seconds: 300")
metadado() {
  curl -s -H "X-aws-ec2-metadata-token: $TOKEN" \
    "http://169.254.169.254/latest/meta-data/$1"
}
INSTANCE_ID=$(metadado instance-id)
ZONA=$(metadado placement/availability-zone)

cat > /usr/share/nginx/html/index.html <<EOF
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <title>Laboratório 03 CLF-C02</title>
</head>
<body>
  <h1>Laboratório 03: EC2 atrás de um load balancer</h1>
  <p>Instância: <strong>${INSTANCE_ID}</strong></p>
  <p>Zona de disponibilidade: <strong>${ZONA}</strong></p>
</body>
</html>
EOF

systemctl enable --now nginx
