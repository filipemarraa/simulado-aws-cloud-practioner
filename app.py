# simulado_aws_gui.py
# Requisitos: Python 3 (Tkinter já vem na instalação padrão de Python em Windows/macOS).
# Execução: python simulado_aws_gui.py

import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'  # Suprime aviso de depreciação no macOS

import tkinter as tk
from tkinter import messagebox, ttk, filedialog

# ====== Base de dados dos simulados ======
# Formato:
# {
#   "q": "enunciado",
#   "options": ["A", "B", "C", "D", ...],
#   "correct": [indices_corretos],  # ex.: [2] para alternativa C, ou [1,3] para múltipla
#   "multiple": True/False
# }

# Simulado 0 - Simulado atual (60 questões)
SIMULADO_0 = [
    # 1-30
    {"q":"Uma empresa quer armazenar seus arquivos na Nuvem AWS. Os usuários precisam conseguir baixar esses arquivos diretamente usando uma URL pública. Qual serviço ou recurso da AWS atenderá a esse requisito?",
     "options":["Amazon Redshift","Amazon Elastic Block Store (Amazon EBS)","Amazon Elastic File System (Amazon EFS)","Amazon S3"],
     "correct":[3],"multiple":False},
    {"q":"Uma empresa quer executar o código de seu aplicativo sem ter que provisionar e gerenciar servidores. Qual serviço da AWS atenderá a esse requisito?",
     "options":["AWS Lambda","AWS Glue","AWS CodeDeploy","Amazon CodeGuru"],
     "correct":[0],"multiple":False},
    {"q":"Uma empresa migrou para a Nuvem AWS. Agora, a empresa paga pelos serviços conforme a necessidade. De qual vantagem da computação em nuvem a empresa está se beneficiando?",
     "options":["Pare de gastar dinheiro executando e mantendo data centers","Aumente a velocidade e a agilidade","Torne-se global em minutos","Troque despesas fixas por despesas variáveis"],
     "correct":[3],"multiple":False},
    {"q":"Uma empresa tem um requisito de conformidade para registrar e avaliar alterações de configuração, bem como executar ações de correção em recursos da AWS. Qual serviço da AWS a empresa deve usar?",
     "options":["AWS Config","AWS Secrets Manager","AWS CloudTrail","AWS Trusted Advisor"],
     "correct":[0],"multiple":False},
    {"q":"Uma empresa tem um banco de dados MariaDB no local. A empresa quer mover os dados para a Nuvem AWS. Qual serviço AWS hospedará esse banco de dados com a MENOR quantidade de sobrecarga operacional?",
     "options":["Amazon RDS","Amazon Neptune","Amazon S3","Amazon DynamoDB"],
     "correct":[0],"multiple":False},
    {"q":"No modelo de responsabilidade compartilhada da AWS, qual das opções a seguir é responsabilidade do cliente?",
     "options":["Destrua unidades de disco antes que elas saiam do data center.","Impedir que os clientes coletem pacotes ou tráfego no nível do hipervisor.","Aplique os patches de segurança mais recentes no sistema operacional convidado.","Manter sistemas de segurança que forneçam monitoramento físico dos data centers."],
     "correct":[2],"multiple":False},
    {"q":"Uma empresa tem cargas de trabalho em lote que precisam ser executadas por curtos períodos de tempo no Amazon EC2. As cargas de trabalho podem lidar com interrupções e podem começar novamente de onde pararam. Qual é a opção de compra de instância EC2 MAIS econômica para atender a esses requisitos?",
     "options":["Instâncias reservadas","Instâncias Spot","Instâncias dedicadas","Instâncias sob demanda"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço da AWS usa uma combinação de editores e assinantes?",
     "options":["AWS Lambda","Amazon Simple Notification Service (Amazon SNS)","Amazon CloudWatch","AWS CloudFormation"],
     "correct":[1],"multiple":False},
    {"q":"Um desenvolvedor precisa interagir com a AWS usando a AWS CLI. Qual recurso de segurança ou serviço da AWS deve ser provisionado na conta do desenvolvedor para atender a esse requisito?",
     "options":["Nome de usuário e senha","Gerente de sistemas da AWS","Acesso à senha root","Chave de acesso AWS"],
     "correct":[3],"multiple":False},
    {"q":"Qual pilar do AWS Well-Architected Framework se concentra na alocação estruturada e simplificada de recursos de computação?",
     "options":["Confiabilidade","Excelência operacional","Eficiência de desempenho","Sustentabilidade"],
     "correct":[2],"multiple":False},
    {"q":"Qual princípio de design de arquitetura descreve a necessidade de isolar falhas entre componentes dependentes na Nuvem AWS?",
     "options":["Use um design monolítico.","Projeto para automação.","Projeto para pontos únicos de falha.","Acople fracamente os componentes."],
     "correct":[3],"multiple":False},
    {"q":"Qual serviço ou ferramenta da AWS monitorará os recursos e aplicativos da AWS em tempo real?",
     "options":["AWS Trusted Advisor","Amazon CloudWatch","AWS CloudTrail","AWS Cost Explorer"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço ou ferramenta da AWS oferece aos usuários a capacidade de se conectar à AWS e implantar recursos de maneira programática?",
     "options":["Amazon QuickSight","AWS PrivateLink","AWS Direct Connect","SDKs da AWS"],
     "correct":[3],"multiple":False},
    {"q":"Uma empresa está nos estágios iniciais de planejamento de uma migração para a AWS. A empresa deseja obter o custo total de propriedade da AWS previsto mensalmente para futuras instâncias do Amazon EC2 e armazenamento associado.",
     "options":["AWS Pricing Calculator","AWS Compute Optimizer","AWS Trusted Advisor","AWS Application Migration Service"],
     "correct":[0],"multiple":False},
    {"q":"Qual componente de VPC uma empresa pode usar para configurar um firewall virtual no nível de instância do Amazon EC2?",
     "options":["Network ACL","Grupo de Segurança","Tabela de Rotas","NAT gateway"],
     "correct":[1],"multiple":False},
    {"q":"Uma empresa quer fornecer baixa latência para seus usuários ao redor do mundo. Qual recurso da AWS Cloud atende a esse requisito?",
     "options":["Infraestrutura global","Preços de pagamento conforme o uso","Serviços gerenciados","Economia de escala"],
     "correct":[0],"multiple":False},
    {"q":"Qual componente deve ser anexado a uma VPC para habilitar o acesso de entrada à Internet?",
     "options":["NAT gateway","VPC endpoint","VPN connection","Internet gateway"],
     "correct":[3],"multiple":False},
    {"q":"Uma empresa quer atualizar seu aplicativo de processamento de dados on-line implementando serviços baseados em contêiner que rodam por 4 horas por vez. A empresa não quer provisionar ou gerenciar instâncias de servidor.",
     "options":["AWS Lambda","AWS Fargate","Amazon EC2","AWS Elastic Beanstalk"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço da AWS facilita o monitoramento e a solução de problemas de logs de aplicativos e recursos de nuvem?",
     "options":["Amazon EC2","AWS Identity and Access Management (IAM)","Amazon CloudWatch","AWS CloudTrail"],
     "correct":[2],"multiple":False},
    {"q":"Uma empresa implantou um aplicativo em várias regiões da AWS ao redor do mundo. A empresa quer melhorar o desempenho e a disponibilidade do aplicativo.",
     "options":["AWS Global Accelerator","Amazon DataZone","AWS Cloud Map","AWS Auto Scaling"],
     "correct":[0],"multiple":False},
    {"q":"Uma empresa hospeda seu site em instâncias do Amazon EC2. A empresa precisa garantir que o site alcance um público global e forneça latência mínima aos usuários.",
     "options":["Amazon Route 53","Amazon CloudFront","Elastic Load Balancing","AWS Lambda"],
     "correct":[1],"multiple":False},
    {"q":"Um fornecedor de software independente quer entregar e compartilhar suas Amazon Machine Images (AMIs) personalizadas para clientes em potencial.",
     "options":["AWS Marketplace","AWS Data Exchange","Amazon EC2","AWS Organizations"],
     "correct":[0],"multiple":False},
    {"q":"Quais tarefas são de responsabilidade da AWS de acordo com o modelo de responsabilidade compartilhada da AWS? (Escolha duas.)",
     "options":["Configurar o AWS Identity and Access Management (IAM).","Configurar grupos de segurança em instâncias do Amazon EC2.","Proteja o acesso às instalações físicas da AWS.","Aplique patches em aplicativos executados em instâncias do Amazon EC2.","Executar manutenção e aplicação de patches na infraestrutura."],
     "correct":[2,4],"multiple":True},
    {"q":"Uma empresa quer implantar um aplicativo que armazena dados em um banco de dados relacional. A empresa quer que tarefas de banco de dados, como backups automatizados e snapshots de banco de dados, sejam gerenciadas pela AWS.",
     "options":["Amazon DocumentDB","Amazon RDS","Amazon Elastic Block Store (Amazon EBS)","Amazon S3"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço da AWS é um serviço de banco de dados NoSQL totalmente gerenciado?",
     "options":["Amazon RDS","Amazon Redshift","Amazon DynamoDB","Amazon Aurora"],
     "correct":[2],"multiple":False},
    {"q":"Uma empresa executa muitas instâncias do Amazon EC2 em sua VPC. A empresa quer usar um recurso de segurança nativo da AWS para controlar o tráfego de rede entre determinadas instâncias do EC2.",
     "options":["ACLs de rede","AWS WAF","Amazon GuardDuty","Grupos de segurança"],
     "correct":[3],"multiple":False},
    {"q":"Qual serviço AWS oferece a capacidade de hospedar um banco de dados NoSQL na Nuvem AWS?",
     "options":["Amazon Aurora","Amazon DynamoDB","Amazon RDS","Amazon Redshift"],
     "correct":[1],"multiple":False},
    {"q":"Qual benefício da computação em nuvem oferece a uma empresa a capacidade de implantar aplicativos para usuários em todo o mundo por meio de uma rede de regiões, zonas de disponibilidade e pontos de presença da AWS?",
     "options":["Economia de escala","Alcance global","Agilidade","Alta disponibilidade"],
     "correct":[1],"multiple":False},
    {"q":"Uma empresa que opera servidores no local decide iniciar uma nova linha de negócios. A empresa determina que servidores adicionais são necessários para as novas cargas de trabalho.",
     "options":["Beneficie de enormes economias de escala","Aumente a velocidade e a agilidade","Troque despesas fixas por despesas variáveis","Torne-se global em minutos"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço ou ferramenta da AWS fornece aos usuários uma interface gráfica que eles podem usar para gerenciar serviços da AWS?",
     "options":["AWS Copilot","AWS CLI","AWS Management Console","AWS SDKs"],
     "correct":[2],"multiple":False},

    # 31-60
    {"q":"Uma empresa quer melhorar continuamente processos e procedimentos para entregar valor comercial.",
     "options":["Eficiência de desempenho","Excelência operacional","Confiabilidade","Sustentabilidade"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço da AWS se integra a outros serviços da AWS para fornecer a capacidade de criptografar dados em repouso?",
     "options":["AWS Key Management Service (AWS KMS)","AWS Certificate Manager (ACM)","AWS Identity and Access Management (IAM)","AWS Security Hub"],
     "correct":[0],"multiple":False},
    {"q":"Qual serviço da AWS pode gerenciar permissões para recursos da AWS usando políticas?",
     "options":["AWS Identity and Access Management (IAM)","Amazon Inspector","Amazon Detective","Amazon GuardDuty"],
     "correct":[0],"multiple":False},
    {"q":"Qual é o benefício de usar um balanceador de carga Elastic Load Balancing (ELB) com aplicativos em execução na Nuvem AWS?",
     "options":["Um ELB dimensionará automaticamente os recursos para atender às necessidades de capacidade.","Um ELB pode balancear o tráfego entre vários recursos de computação.","Um ELB pode abranger várias regiões da AWS.","Um ELB pode balancear o tráfego entre vários gateways de internet."],
     "correct":[1],"multiple":False},
    {"q":"Uma empresa precisa hospedar um aplicativo em uma área geográfica específica para cumprir com regulamentações.",
     "options":["Escalabilidade","Presença global","Disponibilidade","Desempenho"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço ou recurso da AWS pode ser usado para monitorar possíveis picos de gravação de disco em um sistema em execução no Amazon EC2?",
     "options":["AWS CloudTrail","AWS Health Dashboard","AWS Trusted Advisor","Amazon CloudWatch"],
     "correct":[3],"multiple":False},
    {"q":"Qual serviço ou ferramenta da AWS fornece aos usuários uma interface gráfica que eles podem usar para gerenciar serviços da AWS?",
     "options":["AWS Copilot","AWS CLI","AWS Management Console","AWS SDKs"],
     "correct":[2],"multiple":False},
    {"q":"Uma empresa de entrega de comida precisa bloquear usuários em certos países de acessar seu site.",
     "options":["AWS WAF","AWS Control Tower","Amazon Fraud Detector","Amazon Pinpoint"],
     "correct":[0],"multiple":False},
    {"q":"Uma empresa quer migrar sistemas críticos de produção on-premises para instâncias do Amazon EC2. As instâncias de produção serão usadas por pelo menos 3 anos. A empresa quer uma opção de preço que minimize os custos.",
     "options":["Instâncias sob demanda","Instâncias reservadas","Instâncias Spot","Nível gratuito da AWS"],
     "correct":[1],"multiple":False},
    {"q":"Qual recurso ou classe de armazenamento do Amazon S3 usa a rede backbone e os pontos de presença da AWS para reduzir as latências do usuário final ao Amazon S3?",
     "options":["S3 Cross-Region Replication","S3 Transfer Acceleration","S3 Event Notifications","S3 Standard-Infrequent Access (S3 Standard-IA)"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço AWS é um banco de dados relacional compatível com MySQL e PostgreSQL?",
     "options":["Amazon Redshift","Amazon DynamoDB","Amazon Aurora","Amazon Neptune"],
     "correct":[2],"multiple":False},
    {"q":"Qual serviço da AWS permite que os usuários criem cópias de recursos em regiões da AWS?",
     "options":["Amazon ElastiCache","AWS CloudFormation","AWS CloudTrail","AWS Systems Manager"],
     "correct":[1],"multiple":False},
    {"q":"Uma empresa deseja implantar um aplicativo web não-contêinerizado baseado em Java na AWS. Serviço gerenciado que provisione capacidade, balanceie carga, dimensione e monitore a integridade automaticamente:",
     "options":["Amazon ECS","AWS Lambda","Amazon EKS","AWS Elastic Beanstalk"],
     "correct":[3],"multiple":False},
    {"q":"Uma empresa precisa configurar conectividade de rede dedicada entre seu data center local e a Nuvem AWS. A rede não pode usar a internet pública.",
     "options":["AWS Direct Connect","AWS Transit Gateway","AWS VPN","Amazon CloudFront"],
     "correct":[0],"multiple":False},
    {"q":"Um administrador de sistemas quer monitorar a utilização da CPU das instâncias Amazon EC2 de uma empresa.",
     "options":["AWS Config","AWS Trusted Advisor","AWS CloudTrail","Amazon CloudWatch"],
     "correct":[3],"multiple":False},
    {"q":"Qual serviço da AWS oferece suporte a mecanismos de banco de dados MySQL?",
     "options":["Amazon DynamoDB","Amazon RDS","Amazon DocumentDB (with MongoDB compatibility)","Amazon ElastiCache"],
     "correct":[1],"multiple":False},
    {"q":"Uma empresa precisa bloquear ataques de injeção de SQL.",
     "options":["AWS WAF","Network ACLs","Grupos de Segurança","AWS Trusted Advisor"],
     "correct":[0],"multiple":False},
    {"q":"Uma empresa executa instâncias do Amazon EC2 em um laboratório de pesquisa. As instâncias são executadas por 3 horas por semana e não podem ser interrompidas. Opção de compra MAIS econômica:",
     "options":["Compute Savings Plan","On-Demand Instances","Convertible Reserved Instances","Spot Instances"],
     "correct":[1],"multiple":False},
    {"q":"Uma empresa tem várias contas AWS. Precisa faturamento consolidado e gestão central de segurança e conformidade.",
     "options":["AWS Cost and Usage Report","AWS Organizations","AWS Config","AWS Security Hub"],
     "correct":[1],"multiple":False},
    {"q":"Uma empresa quer visualizar e gerenciar os custos e o uso da AWS Cloud por um período específico de tempo.",
     "options":["Cost Explorer","Consolidated billing (Faturamento consolidado)","AWS Organizations","AWS Budgets"],
     "correct":[0],"multiple":False},
    {"q":"O responsável pela conformidade quer revisar os relatórios do AWS Service Organization Control (SOC).",
     "options":["AWS Artifact","AWS Concierge Support","AWS Support","AWS Trusted Advisor"],
     "correct":[0],"multiple":False},
    {"q":"Uma empresa está lançando um aplicativo móvel e quer login via IdPs de mídia social.",
     "options":["AWS Lambda","Amazon Cognito","AWS Secrets Manager","Amazon CloudFront"],
     "correct":[1],"multiple":False},
    {"q":"Uma empresa precisa de um sistema de arquivos NFS gerenciado para usar com seus recursos de computação da AWS.",
     "options":["Amazon Elastic Block Store (Amazon EBS)","AWS Storage Gateway Tape Gateway","Amazon S3 Glacier Flexible Retrieval","Amazon Elastic File System (Amazon EFS)"],
     "correct":[3],"multiple":False},
    {"q":"Qual serviço AWS oferece suporte à implantação e gerenciamento de aplicativos na Nuvem AWS?",
     "options":["Amazon CodeGuru","AWS Fargate","AWS CodeCommit","AWS Elastic Beanstalk"],
     "correct":[3],"multiple":False},
    {"q":"Uma empresa quer adquirir recursos automaticamente quando necessário e liberá-los quando não forem mais necessários. Qual conceito descreve isso?",
     "options":["Disponibilidade","Elasticidade","Durabilidade","Confiabilidade"],
     "correct":[1],"multiple":False},
    {"q":"A empresa quer que as cargas de trabalho executem sua função pretendida de forma correta e consistente ao longo de seu ciclo de vida. Qual pilar do Well-Architected?",
     "options":["Excelência operacional","Segurança","Confiabilidade","Eficiência de desempenho"],
     "correct":[2],"multiple":False},
    {"q":"A empresa provisionou várias instâncias EC2 para melhorar disponibilidade e quer um único ponto de contato distribuindo tráfego.",
     "options":["VPC endpoints","Application Load Balancer","NAT gateway","Internet gateway"],
     "correct":[1],"multiple":False},
    {"q":"Responsabilidades do cliente no modelo de responsabilidade compartilhada (Escolha duas.)",
     "options":["Proteja a camada de virtualização.","Criptografar dados e manter a integridade dos dados.","Corrija o sistema operacional Amazon RDS.","Manter controles de gerenciamento de identidade e acesso.","Zonas de disponibilidade seguras."],
     "correct":[1,3],"multiple":True},
    {"q":"Como a AWS ajuda a reduzir custos? (Escolha duas.)",
     "options":["AWS cobra os mesmos preços em todas as regiões.","A AWS permite que a capacidade seja ajustada sob demanda.","A AWS oferece descontos para EC2 ociosas por mais de 1 semana.","A AWS não cobra dados de saída para a Internet.","A AWS elimina muitos custos de construção e manutenção de data centers locais."],
     "correct":[1,4],"multiple":True},
    {"q":"O financeiro quer definir limites de gastos e receber alertas quando excedidos.",
     "options":["AWS Budgets","EC2","Amazon S3","Amazon EFS"],
     "correct":[0],"multiple":False},
]

# Simulados 1-6 (serão adicionados com as questões do PDF)
SIMULADO_1 = [
    {"q":"Quais vantagens um administrador de banco de dados obtém ao usar o Amazon Relational Database Service (RDS)?",
     "options":["O RDS fornece 99,99999999999% de confiabilidade e durabilidade.","Os bancos de dados RDS escalam automaticamente com base na carga.","O RDS permite que os usuários ajustem dinamicamente os recursos de CPU e RAM.","O RDS simplifica as tarefas de administração de banco de dados relacional."],
     "correct":[3],"multiple":False},
    {"q":"Um Cloud Practitioner precisa de recuperação pontual (PITR) para uma tabela Amazon DynamoDB. Quem é responsável por configurar e realizar backups?",
     "options":["A AWS é responsável por ambas as tarefas.","O cliente é responsável por configurar e a AWS é responsável por realizar backups.","O cliente é responsável por ambas as tarefas.","A AWS é responsável por configurar e o usuário é responsável por realizar backups."],
     "correct":[1],"multiple":False},
    {"q":"Uma grande empresa está interessada em evitar contratos de longo prazo e passar de custos fixos para custos variáveis. Qual é a proposta de valor da AWS para esta empresa?",
     "options":["Economias de escala","Preços pay-as-you-go","Descontos de preços por volume","Otimização de custos automatizada"],
     "correct":[1],"multiple":False},
    {"q":"Um cliente precisa determinar o Custo Total de Propriedade (TCO) para uma carga de trabalho que requer isolamento físico. Qual modelo de hospedagem deve ser considerado?",
     "options":["Dedicated Hosts","Reserved Instances","On-Demand Instances","Spot Instances"],
     "correct":[0],"multiple":False},
    {"q":"Quais tarefas um usuário pode completar usando as ferramentas de Gerenciamento de Custos da AWS? (Selecione DUAS.)",
     "options":["Encerrar automaticamente recursos AWS se os limites de orçamento forem excedidos.","Dividir custos AWS por dia, serviço e conta AWS vinculada.","Criar orçamentos e receber notificações se o uso atual ou previsto exceder os orçamentos.","Lançar instâncias EC2 Spot ou On-Demand com base no preço atual.","Mover dados armazenados no Amazon S3 Standard para uma classe de armazenamento de arquivamento para reduzir custos."],
     "correct":[1,2],"multiple":True},
    {"q":"Quais dos seguintes serviços AWS são serviços de computação? (Selecione DUAS.)",
     "options":["AWS Batch","AWS CloudTrail","AWS Elastic Beanstalk","Amazon EFS","Amazon Inspector"],
     "correct":[0,2],"multiple":True},
    {"q":"Quais princípios de design são habilitados pela AWS Cloud para melhorar a operação de cargas de trabalho? (Selecione DUAS.)",
     "options":["Minimizar o design da plataforma","Acoplamento frouxo","Hardware personalizado","Remover pontos únicos de falha","Produto mínimo viável"],
     "correct":[1,3],"multiple":True},
    {"q":"Um usuário está planejando lançar três instâncias EC2 atrás de um único Elastic Load Balancer. A implantação deve ser altamente disponível.",
     "options":["Lançar as instâncias em múltiplas Zonas de Disponibilidade em uma única Região AWS.","Lançar as instâncias como EC2 Spot Instances na mesma Região AWS e na mesma Zona de Disponibilidade.","Lançar as instâncias em múltiplas Regiões AWS e usar endereços Elastic IP.","Lançar as instâncias como EC2 Reserved Instances na mesma Região AWS, mas em diferentes Zonas de Disponibilidade."],
     "correct":[0],"multiple":False},
    {"q":"Qual recurso um novo usuário na AWS deve usar para obter ajuda com a implantação de tecnologias populares baseadas nas melhores práticas da AWS, incluindo arquitetura e instruções de implantação?",
     "options":["AWS CloudFormation","AWS Artifact","AWS Config","AWS Quick Starts"],
     "correct":[3],"multiple":False},
    {"q":"Uma empresa precisa publicar mensagens para milhares de assinantes simultaneamente usando um mecanismo push. Qual serviço AWS a empresa deve usar?",
     "options":["AWS Step Functions","Amazon Simple Workflow Service (SWF)","Amazon Simple Notification Service (Amazon SNS)","Amazon Simple Queue Service (Amazon SQS)"],
     "correct":[2],"multiple":False},
    {"q":"Uma empresa usa instâncias Amazon EC2 para executar aplicações dedicadas a diferentes departamentos. A empresa precisa separar os custos dessas aplicações e alocá-los ao departamento relevante. As instâncias EC2 executam em uma única VPC.",
     "options":["Habilitar acesso de cobrança para usuários IAM e visualizar os custos no Cost Explorer.","Habilitar alertas de cobrança através do Amazon CloudWatch e Amazon SNS.","Criar tags por departamento nas instâncias e depois executar um relatório de alocação de custos.","Adicionar VPCs Amazon adicionais e lançar cada aplicação em uma VPC separada."],
     "correct":[2],"multiple":False},
    {"q":"Uma aplicação usa um banco de dados PostgreSQL executando em uma única instância Amazon EC2. Um Cloud Practitioner foi solicitado a aumentar a disponibilidade do banco de dados para que haja recuperação automática em caso de falha.",
     "options":["Migrar o banco de dados para Amazon RDS e habilitar o recurso Multi-AZ.","Configurar um Elastic Load Balancer na frente da instância EC2.","Configurar EC2 Auto Recovery para mover a instância para outra Região.","Definir o valor DeleteOnTermination como false para o volume raiz EBS."],
     "correct":[0],"multiple":False},
    {"q":"Uma empresa está lançando um novo site que deve ter níveis altamente variáveis de tráfego. O site executará no Amazon EC2 e deve ser altamente disponível. Qual é a abordagem MAIS econômica?",
     "options":["Usar a AWS CLI para lançar e encerrar instâncias Amazon EC2 para corresponder à demanda.","Criar um grupo Amazon EC2 Auto Scaling e configurar um Elastic Load Balancer.","Determinar o tráfego esperado mais alto e usar um tipo de instância apropriado.","Lançar o site usando uma instância Amazon EC2 executando em um host dedicado."],
     "correct":[1],"multiple":False},
    {"q":"Quais das seguintes declarações melhor descrevem o conceito de agilidade em relação à computação em nuvem na AWS? (Selecione DUAS.)",
     "options":["A velocidade com que a AWS lança novos recursos.","A capacidade de experimentar rapidamente.","A eliminação de capacidade desperdiçada.","A capacidade de escalar automaticamente a capacidade.","A velocidade com que os recursos AWS podem ser criados."],
     "correct":[1,4],"multiple":True},
    {"q":"Uma empresa executa um trabalho em lote em uma instância Amazon EC2 e leva 6 horas para ser concluído. A carga de trabalho deve dobrar de volume a cada mês com um aumento proporcional no tempo de processamento.",
     "options":["Executar o trabalho em lote em um tipo de instância Amazon EC2 maior com mais CPU.","Alterar o tipo de volume Amazon EC2 para um volume SSD Provisioned IOPS.","Executar a aplicação em uma instância Amazon EC2 bare metal.","Executar a carga de trabalho em lote em paralelo em múltiplas instâncias Amazon EC2."],
     "correct":[3],"multiple":False},
    {"q":"Qual elemento em uma política de bucket S3 deve ser atualizado para definir a conta de usuário para a qual o acesso será concedido?",
     "options":["Action","Principal","Resource","Condition"],
     "correct":[1],"multiple":False},
    {"q":"Um Cloud Practitioner precisa de uma ferramenta que possa ajudar com a visualização e gerenciamento de custos e uso da AWS ao longo do tempo. Qual ferramenta o Cloud Practitioner deve usar?",
     "options":["AWS Budgets","Amazon Inspector","AWS Organizations","AWS Cost Explorer"],
     "correct":[3],"multiple":False},
    {"q":"Uma empresa está planejando implantar um banco de dados relacional na AWS. O departamento de TI realizará a administração do banco de dados. Qual serviço a empresa deve usar?",
     "options":["Amazon EC2","Amazon RedShift","Amazon ElastiCache","Amazon DynamoDB"],
     "correct":[0],"multiple":False},
    {"q":"Uma empresa está planejando mover várias aplicações legadas para a AWS Cloud. A solução deve ser econômica. Qual abordagem a empresa deve tomar?",
     "options":["Migrar as aplicações para hosts dedicados no Amazon EC2.","Rehospedar as aplicações em instâncias Amazon EC2 que são dimensionadas corretamente.","Usar AWS Lambda para hospedar as aplicações legadas na nuvem.","Usar um site estático Amazon S3 para hospedar o código da aplicação legada."],
     "correct":[1],"multiple":False},
    {"q":"Uma empresa deve fornecer acesso aos recursos AWS para seus funcionários. Quais práticas de segurança eles devem seguir? (Selecione DUAS.)",
     "options":["Habilitar autenticação multifator para usuários.","Criar políticas IAM baseadas em princípios de menor privilégio.","Desabilitar políticas de senha e acesso ao console de gerenciamento.","Criar usuários IAM em diferentes Regiões AWS.","Criar Funções IAM e aplicá-las a grupos IAM."],
     "correct":[0,1],"multiple":True},
    {"q":"Uma Amazon Virtual Private Cloud (VPC) pode incluir múltiplas:",
     "options":["Regiões AWS.","Localizações de borda.","Gateways de internet.","Zonas de Disponibilidade."],
     "correct":[3],"multiple":False},
    {"q":"Um Cloud Practitioner antecipa um aumento no tráfego da aplicação em uma data e hora futuras quando um evento de vendas ocorrerá. Como o Cloud Practitioner pode configurar o Amazon EC2 Auto Scaling para garantir que o número certo de instâncias Amazon EC2 esteja disponível antes do evento?",
     "options":["Configurar dimensionamento preditivo.","Configurar uma política de dimensionamento de rastreamento de destino.","Configurar uma política de dimensionamento programada.","Configurar uma política de dimensionamento em etapas."],
     "correct":[2],"multiple":False},
    {"q":"Uma empresa está implantando uma aplicação no Amazon EC2 que requer acesso de baixa latência aos componentes da aplicação em um data center local. Qual serviço ou recurso AWS a empresa pode usar para estender sua VPC existente ao data center local?",
     "options":["Amazon Connect","AWS Outposts","AWS Direct Connect","Amazon Workspaces"],
     "correct":[1],"multiple":False},
    {"q":"Qual tipo de credencial um Cloud Practitioner deve usar para acesso programático aos recursos AWS da AWS CLI/API?",
     "options":["Certificado SSL/TLS","Chaves públicas SSH","Chaves de acesso","Nome de usuário e senha"],
     "correct":[2],"multiple":False},
    {"q":"Uma empresa está projetando um novo serviço que deve se alinhar com o pilar de excelência operacional do AWS Well-Architected Framework. Quais princípios de design a empresa deve seguir? (Selecione DUAS.)",
     "options":["Antecipar falhas.","Fazer mudanças em grande escala.","Executar operações como código.","Executar operações manuais.","Criar procedimentos operacionais estáticos."],
     "correct":[0,2],"multiple":True},
    {"q":"Um site tem uma base de clientes global e os usuários relataram baixo desempenho ao se conectar ao site. Qual serviço AWS melhorará a experiência do cliente reduzindo a latência?",
     "options":["AWS Direct Connect","Amazon EC2 Auto Scaling","Amazon CloudFront","Amazon ElastiCache"],
     "correct":[2],"multiple":False},
    {"q":"Qual é um método de proteção contra ataques de negação de serviço distribuído (DDoS) na AWS Cloud?",
     "options":["Usar monitoramento Amazon CloudWatch.","Configurar um firewall na frente dos recursos.","Monitorar o Service Health Dashboard.","Habilitar logging AWS CloudTrail."],
     "correct":[1],"multiple":False},
    {"q":"Quanta dados uma empresa pode armazenar no serviço Amazon S3?",
     "options":["1 PB","100 TB","100 PB","Virtualmente ilimitado"],
     "correct":[3],"multiple":False},
    {"q":"Uma empresa está implantando uma nova carga de trabalho e os requisitos de licenciamento de software ditam que a carga de trabalho deve ser executada em um servidor físico específico. Qual opção de implantação de instância Amazon EC2 deve ser usada?",
     "options":["Dedicated Instances","Spot Instances","Reserved Instances","Dedicated Hosts"],
     "correct":[3],"multiple":False},
    {"q":"Quais dos seguintes são benefícios válidos de usar a AWS Cloud? (Selecione DUAS.)",
     "options":["Terceirizar todo o risco operacional.","Controle total sobre a infraestrutura do data center.","Provisionamento rápido de recursos de TI.","Capacidade de se tornar global rapidamente.","Terceirizar todo o desenvolvimento de aplicações para a AWS."],
     "correct":[2,3],"multiple":True},
    {"q":"Quais tarefas requerem o uso do usuário root da conta AWS? (Selecione DUAS.)",
     "options":["Habilitar criptografia para S3.","Visualizar logs AWS CloudTrail.","Alterar o nome da conta.","Alterar planos de suporte AWS.","Alterar moeda de pagamento."],
     "correct":[2,3],"multiple":True},
    {"q":"Qual serviço AWS uma empresa pode usar para descobrir e proteger dados sensíveis que são armazenados em buckets Amazon S3?",
     "options":["Amazon GuardDuty","AWS Policy Generator","Amazon Detective","Amazon Macie"],
     "correct":[3],"multiple":False},
    {"q":"Quais benefícios uma empresa pode obter implantando um banco de dados relacional no Amazon RDS em vez do Amazon EC2? (Selecione DUAS.)",
     "options":["Backups automatizados","Gerenciamento de esquema","Indexação de tabelas","Aplicação de patches de software","Acesso root ao SO"],
     "correct":[0,3],"multiple":True},
    {"q":"Uma empresa está planejando implantar uma aplicação com um banco de dados relacional na AWS. A camada de aplicação requer acesso ao sistema operacional da instância do banco de dados para executar scripts. A empresa prefere manter a sobrecarga de gerenciamento ao mínimo. Qual implantação deve ser usada para o banco de dados?",
     "options":["Amazon RDS","Amazon DynamoDB","Amazon EC2","Amazon S3"],
     "correct":[2],"multiple":False},
    {"q":"Clientes usando serviços AWS devem aplicar patches nos sistemas operacionais em qual dos seguintes serviços?",
     "options":["AWS Lambda","Amazon EC2","AWS Fargate","Amazon DynamoDB"],
     "correct":[1],"multiple":False},
    {"q":"Qual recurso AWS pode ser usado para lançar uma instância Amazon Elastic Compute Cloud (EC2) pré-configurada?",
     "options":["Amazon Elastic Block Store (EBS)","Amazon EC2 Systems Manager","Amazon Machine Image (AMI)","Amazon AppStream 2.0"],
     "correct":[2],"multiple":False},
    {"q":"Qual dos seguintes recursos ou serviços AWS pode ser usado para fornecer volumes de armazenamento raiz para instâncias Amazon EC2?",
     "options":["Amazon Elastic Block Store (EBS)","Amazon Machine Image","Amazon Elastic File System (EFS)","Amazon Simple Storage Service (S3)"],
     "correct":[0],"multiple":False},
    {"q":"Qual serviço ou recurso AWS pode ajudar a proteger um site que está hospedado fora da AWS?",
     "options":["Tabelas de rota Amazon VPC","Grupos de segurança Amazon EC2","ACLs de rede Amazon VPC","AWS Web Application Firewall (WAF)"],
     "correct":[3],"multiple":False},
    {"q":"Qual serviço AWS uma equipe pode usar para implantar infraestrutura na AWS usando linguagens de programação familiares?",
     "options":["AWS Cloud Development Kit (AWS CDK)","Amazon CodeGuru","AWS Config","AWS CodeCommit"],
     "correct":[0],"multiple":False},
    {"q":"Quais tarefas comuns a AWS pode gerenciar em nome de seus clientes ao executar aplicações na AWS Cloud? (Selecione DUAS.)",
     "options":["Aplicar patches no software do banco de dados","Auditoria do código-fonte da aplicação","Criar um esquema de banco de dados","Fazer backup de um banco de dados","Teste de segurança da aplicação"],
     "correct":[0,3],"multiple":True},
    {"q":"O que um Cloud Practitioner pode usar para determinar se precisa solicitar um aumento de limite de serviço Amazon EC2?",
     "options":["AWS Personal Health Dashboard","AWS Cost Explorer","AWS Trusted Advisor","AWS Service Health Dashboard"],
     "correct":[2],"multiple":False},
    {"q":"Como a nuvem AWS aumenta a velocidade e agilidade de execução para clientes? (Selecione DUAS.)",
     "options":["Provisionamento rápido de recursos","Conexões privadas para data centers","Data centers seguros","Menor custo de implantação","Capacidade de computação escalável"],
     "correct":[0,4],"multiple":True},
    {"q":"Uma empresa tem múltiplas contas AWS e está usando AWS Organizations com cobrança consolidada. Quais vantagens eles se beneficiarão? (Selecione DUAS.)",
     "options":["Eles receberão uma fatura para as contas na Organização.","Os limites de serviço padrão em todas as contas serão aumentados.","Eles receberão um desconto fixo para todo o uso entre contas.","Eles podem se beneficiar de preços unitários mais baixos para uso agregado.","Eles serão automaticamente inscritos em um plano de suporte empresarial."],
     "correct":[0,3],"multiple":True},
    {"q":"Qual das seguintes representa uma proposta de valor para usar a AWS Cloud?",
     "options":["A AWS é responsável por proteger suas aplicações.","Não é necessário entrar em contratos de longo prazo.","Clientes podem solicitar hardware especializado.","A AWS fornece acesso total aos seus data centers."],
     "correct":[1],"multiple":False},
    {"q":"Uma empresa tem muitos recursos de computação subutilizados no local. Qual recurso da AWS Cloud ajudará a resolver este problema?",
     "options":["Alta disponibilidade","Elasticidade","Implantação global","Tolerância a falhas"],
     "correct":[1],"multiple":False},
    {"q":"O que um Cloud Practitioner pode usar para categorizar e rastrear custos AWS por projeto?",
     "options":["Cost Allocation Tags","AWS Trusted Advisor","Cobrança consolidada","Múltiplas contas"],
     "correct":[0],"multiple":False},
    {"q":"Uma empresa está implantando um banco de dados MySQL na AWS. O banco de dados deve escalar facilmente e ter backup automático habilitado. Qual serviço AWS a empresa deve usar?",
     "options":["Amazon Athena","Amazon DynamoDB","Amazon Aurora","Amazon DocumentDB"],
     "correct":[2],"multiple":False},
    {"q":"Uma empresa planeja usar instâncias reservadas para obter preços com desconto para instâncias Amazon EC2. A empresa pode precisar alterar o tipo de instância EC2 durante o período de um ano. Qual opção de compra de instância é MAIS econômica para este caso de uso?",
     "options":["Standard Reserved Instances","Convertible Reserved Instances","Zonal Reserved Instances","Regional Reserved Instances"],
     "correct":[1],"multiple":False},
    {"q":"Qual das seguintes é uma responsabilidade exclusiva da AWS?",
     "options":["Implantação de aplicação","Gerenciamento de patches","Gerenciamento de Zona de Disponibilidade","Controles de acesso a dados do cliente"],
     "correct":[2],"multiple":False},
    {"q":"Qual serviço AWS fornece um sistema de controle de versão de software gerenciado?",
     "options":["Amazon CodeDeploy","AWS CodePipeline","AWS DataSync","AWS CodeCommit"],
     "correct":[3],"multiple":False},
    {"q":"Qual das seguintes implantações envolve o pilar de confiabilidade do AWS Well-Architected Framework?",
     "options":["Implantação Amazon RDS Multi-AZ","Volume Amazon EBS provisioned IOPS","Anexar um WebACL a uma distribuição CloudFront","Usar CloudFormation para implantar infraestrutura"],
     "correct":[0],"multiple":False},
    {"q":"Um Cloud Practitioner precisa monitorar a utilização de CPU e rede de uma nova instância Amazon EC2. Qual serviço AWS deve ser usado?",
     "options":["Amazon Inspector","AWS CloudTrail","AWS Systems Manager","Amazon CloudWatch"],
     "correct":[3],"multiple":False},
    {"q":"A AWS é capaz de reduzir continuamente seus preços devido a:",
     "options":["Economias de escala.","Preços pay-as-you go.","Serviços de computação elástica.","Planos de economia de computação."],
     "correct":[0],"multiple":False},
    {"q":"Quais serviços AWS uma empresa pode usar para coletar informações sobre atividade em sua conta AWS? (Selecione DUAS.)",
     "options":["Amazon CloudFront","AWS CloudTrail","AWS Trusted Advisor","Amazon Connect","Amazon CloudWatch"],
     "correct":[1,4],"multiple":True},
    {"q":"Uma empresa está implantando uma aplicação na AWS Cloud. Como eles podem proteger a aplicação? (Selecione DUAS.)",
     "options":["Habilitar criptografia para os dados da aplicação em repouso.","Configurar acesso público para os serviços AWS usados pela aplicação.","Habilitar monitoramento desligando a criptografia para dados em trânsito.","Limitar privilégios de acesso de acordo com o princípio de menor privilégio.","Fornecer acesso total de administrador para funcionários de desenvolvimento e operações."],
     "correct":[0,3],"multiple":True},
    {"q":"Um Cloud Practitioner está desenvolvendo uma nova aplicação e deseja integrar recursos de serviços AWS diretamente na aplicação. Qual das seguintes é a MELHOR ferramenta para este propósito?",
     "options":["AWS Software Development Kit","AWS CodeDeploy","AWS Command Line Interface (CLI)","AWS CodePipeline"],
     "correct":[0],"multiple":False},
    {"q":"Um usuário precisa identificar instâncias Amazon EC2 subutilizadas para reduzir custos. Qual serviço ou recurso AWS atenderá a este requisito?",
     "options":["AWS CodeBuild","AWS Trusted Advisor","AWS Cost Explorer","AWS Personal Health Dashboard"],
     "correct":[1],"multiple":False},
    {"q":"Quais dos seguintes um cliente AWS pode usar para lançar um novo cluster ElastiCache? (Selecione DUAS.)",
     "options":["AWS CloudFormation","AWS Concierge","AWS Systems Manager","AWS Management Console","AWS Data Pipeline"],
     "correct":[0,3],"multiple":True},
    {"q":"Uma empresa está implantando uma nova aplicação web em uma única Região AWS que será usada por usuários globalmente. Quais serviços AWS ajudarão a reduzir a latência e melhorar as velocidades de transferência para os usuários globais? (Selecione DUAS.)",
     "options":["AWS Direct Connect","AWS Global Accelerator","Amazon CloudFront","AWS Transfer Gateway","AWS Snowcone"],
     "correct":[1,2],"multiple":True},
    {"q":"Para que propósito um Cloud Practitioner acessaria o AWS Artifact?",
     "options":["Baixar detalhes de configuração para todos os recursos AWS.","Acessar materiais de treinamento para serviços AWS.","Criar um relatório de avaliação de segurança para serviços AWS.","Obter acesso a documentos de segurança e conformidade da AWS."],
     "correct":[3],"multiple":False},
    {"q":"Qual serviço AWS Cloud fornece recomendações sobre como otimizar o desempenho para serviços AWS?",
     "options":["Amazon Inspector","AWS Trusted Advisor","Amazon CloudWatch","AWS CloudTrail"],
     "correct":[1],"multiple":False},
    {"q":"Uma empresa está migrando uma aplicação monolítica que não escala bem para a nuvem e refatorando-a em uma arquitetura de microsserviços. Qual melhor prática do AWS Well-Architected Framework este plano se relaciona?",
     "options":["Parar de gastar dinheiro com trabalho pesado indiferenciado.","Implementar serviços fracamente acoplados.","Gerenciar mudanças na automação.","Usar múltiplas soluções para melhorar o desempenho."],
     "correct":[1],"multiple":False},
    {"q":"Para que as chaves de acesso AWS Identity and Access Management (IAM) são usadas?",
     "options":["Fazer login no AWS Management Console.","Garantir a integridade dos arquivos de log.","Fazer chamadas programáticas para AWS de APIs AWS.","Habilitar criptografia em trânsito para servidores web."],
     "correct":[2],"multiple":False},
    {"q":"Qual é a melhor prática para gerenciar chaves de acesso AWS IAM?",
     "options":["Não há necessidade de gerenciar chaves de acesso.","Clientes devem rotacionar chaves de acesso regularmente.","A AWS rotaciona chaves de acesso em um cronograma.","Nunca usar chaves de acesso, sempre usar funções IAM."],
     "correct":[1],"multiple":False},
    {"q":"De acordo com o modelo de responsabilidade compartilhada da AWS, qual das seguintes é uma responsabilidade da AWS?",
     "options":["Configurar ACLs de rede para bloquear ataques maliciosos.","Aplicar patches em software executando em instâncias Amazon EC2.","Atualizar o firmware nos hosts EC2 subjacentes.","Atualizar regras de grupo de segurança para habilitar conectividade."],
     "correct":[2],"multiple":False}
]

SIMULADO_2 = [
    {"q":"De acordo com o modelo de responsabilidade compartilhada, qual tarefa de segurança e conformidade é responsabilidade da AWS?",
     "options":["Conceder permissões a usuários e serviços","Atualizar firmware de host Amazon EC2","Criptografar dados em repouso","Atualizar sistemas operacionais"],
     "correct":[1],"multiple":False},
    {"q":"Uma empresa tem uma base de usuários global e precisa implantar serviços AWS que podem diminuir a latência de rede para seus usuários. Quais serviços podem ajudar? (Selecione DUAS.)",
     "options":["Amazon CloudFront","Amazon VPC","Application Auto Scaling","AWS Direct Connect","AWS Global Accelerator"],
     "correct":[0,4],"multiple":True},
    {"q":"O que pode ser usado para permitir que uma aplicação executando em uma instância Amazon EC2 armazene dados com segurança em um bucket Amazon S3 sem usar credenciais de longo prazo?",
     "options":["AWS Systems Manager","Amazon Connect","Função AWS IAM","Chave de acesso AWS IAM"],
     "correct":[2],"multiple":False},
    {"q":"Qual serviço AWS o AWS Snowball Edge suporta nativamente?",
     "options":["AWS Server Migration Service (AWS SMS)","AWS Database Migration Service (AWS DMS)","AWS Trusted Advisor","Amazon EC2"],
     "correct":[3],"multiple":False},
    {"q":"A AWS é capaz de continuar reduzindo seus preços devido a:",
     "options":["Preços pay-as-you go","A infraestrutura global da AWS","Economias de escala","Preços de instâncias reservadas"],
     "correct":[2],"multiple":False},
    {"q":"De acordo com o modelo de responsabilidade compartilhada da AWS, qual tarefa é responsabilidade do cliente?",
     "options":["Manter a infraestrutura necessária para executar Amazon DynamoDB.","Atualizar o sistema operacional das instâncias AWS Lambda.","Manter a infraestrutura Amazon API Gateway.","Atualizar o sistema operacional convidado nas instâncias Amazon EC2."],
     "correct":[3],"multiple":False},
    {"q":"Um Cloud Practitioner notou que endereços IP que pertencem à AWS estão sendo usados para tentar inundar portas em alguns dos sistemas da empresa. Para quem o problema deve ser relatado?",
     "options":["AWS Professional Services","AWS Partner Network (APN)","Equipe AWS Trust & Safety","Gerente de Conta Técnica AWS (TAM)"],
     "correct":[2],"multiple":False},
    {"q":"Quais custos locais devem ser incluídos em um cálculo de Custo Total de Propriedade (TCO) ao comparar com a AWS Cloud? (Selecione DUAS.)",
     "options":["Hardware de computação físico","Administração do sistema operacional","Infraestrutura de rede no data center","Serviços de gerenciamento de projeto","Desenvolvimento de esquema de banco de dados"],
     "correct":[0,2],"multiple":True},
    {"q":"Qual dos seguintes pode ser usado para identificar um usuário específico que encerrou uma instância de banco de dados Amazon RDS?",
     "options":["AWS CloudTrail","Amazon Inspector","Amazon CloudWatch","AWS Trusted Advisor"],
     "correct":[0],"multiple":False},
    {"q":"Qual serviço AWS pode ser usado para realizar operações de extração, transformação e carregamento (ETL) de dados para preparar dados para análise?",
     "options":["Amazon QuickSight","AWS Glue","Amazon Athena","Amazon S3 Select"],
     "correct":[1],"multiple":False},
    {"q":"Quais das seguintes tarefas um usuário pode realizar para otimizar custos Amazon EC2? (Selecione DUAS.)",
     "options":["Implementar grupos Auto Scaling para adicionar e remover instâncias com base na demanda.","Criar uma política para restringir usuários IAM de acessar o console Amazon EC2.","Definir um orçamento para limitar gastos em instâncias Amazon EC2 usando AWS Budgets.","Comprar Amazon EC2 Reserved Instances.","Criar usuários em uma única Região para reduzir a dispersão de instâncias EC2 globalmente."],
     "correct":[0,3],"multiple":True},
    {"q":"De acordo com o modelo de responsabilidade compartilhada, qual tarefa relacionada à segurança é responsabilidade do cliente?",
     "options":["Manter criptografia do lado do servidor.","Proteger servidores e racks em data centers da AWS.","Manter configurações de firewall no nível de hardware.","Manter configuração de rede física."],
     "correct":[0],"multiple":False},
    {"q":"Uma empresa planeja mover o desenvolvimento de aplicações para a AWS. Quais benefícios eles podem alcançar ao desenvolver e executar aplicações na AWS Cloud em comparação com local? (Selecione DUAS.)",
     "options":["A AWS replica automaticamente todos os dados globalmente.","A AWS gerenciará completamente toda a aplicação.","A AWS facilita a implementação de alta disponibilidade.","A AWS pode acomodar grandes mudanças na demanda da aplicação.","A AWS cuida da aplicação de patches de segurança da aplicação."],
     "correct":[2,3],"multiple":True},
    {"q":"Quais serviços AWS oferecem capacidades de computação? (Selecione DUAS.)",
     "options":["Amazon DynamoDB","Amazon ECS","Amazon EFS","Amazon CloudHSM","AWS Lambda"],
     "correct":[1,4],"multiple":True},
    {"q":"Um cloud practitioner precisa migrar 70 TB de dados de um data center local para a AWS Cloud. A empresa tem uma conexão de internet lenta e não confiável.",
     "options":["Amazon S3 Glacier","AWS Snowball","AWS Storage Gateway","AWS DataSync"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço AWS é um serviço de controle de versão de código-fonte totalmente gerenciado que hospeda repositórios Git seguros?",
     "options":["AWS CodeBuild","AWS CodeDeploy","AWS CodeCommit","AWS CodePipeline"],
     "correct":[2],"multiple":False},
    {"q":"Um Cloud Practitioner está re-arquitetando uma aplicação monolítica. Quais princípios de design para arquitetura de nuvem a AWS recomenda? (Selecione DUAS.)",
     "options":["Implementar escalabilidade manual.","Implementar acoplamento frouxo.","Usar servidores auto-gerenciados.","Depender de componentes individuais.","Projetar para escalabilidade."],
     "correct":[1,4],"multiple":True},
    {"q":"Quais das seguintes são práticas recomendadas válidas para usar o serviço AWS Identity and Access Management (IAM)? (Selecione DUAS.)",
     "options":["Incorporar chaves de acesso no código da aplicação.","Criar usuários IAM individuais.","Usar políticas inline em vez de políticas gerenciadas pelo cliente.","Usar grupos para atribuir permissões a usuários IAM.","Conceder privilégios máximos a usuários IAM."],
     "correct":[1,3],"multiple":True},
    {"q":"Qual benefício da AWS permite que as empresas substituam despesas fixas antecipadas por despesas variáveis ao usar serviços de tecnologia sob demanda?",
     "options":["Preços pay-as-you-go","Economias de escala","Alcance global","Alta disponibilidade"],
     "correct":[0],"multiple":False},
    {"q":"Uma Política de Controle de Serviço (SCP) é usada para gerenciar as permissões máximas disponíveis e está associada a qual dos seguintes?",
     "options":["Infraestrutura Global AWS","Regiões AWS","AWS Organizations","Zonas de Disponibilidade"],
     "correct":[2],"multiple":False},
    {"q":"O que um Cloud Practitioner deve garantir ao projetar uma arquitetura altamente disponível na AWS?",
     "options":["Servidores têm conectividade de rede de baixa latência e alta taxa de transferência.","A falha de um único componente não deve afetar a aplicação.","Há servidores suficientes para executar na carga máxima disponível o tempo todo.","Um único componente de aplicação monolítica lida com todas as operações."],
     "correct":[1],"multiple":False},
    {"q":"Qual tecnologia pode ajustar automaticamente a capacidade de computação conforme a demanda por uma aplicação aumenta ou diminui?",
     "options":["Balanceamento de carga","Auto Scaling","Tolerância a falhas","Alta disponibilidade"],
     "correct":[1],"multiple":False},
    {"q":"Qual das seguintes é uma vantagem para uma empresa executando cargas de trabalho na AWS Cloud vs local? (Selecione DUAS.)",
     "options":["Menos tempo de equipe é necessário para lançar novas cargas de trabalho.","Tempo aumentado para colocar no mercado novos recursos de aplicação.","Custos de aquisição mais altos para suportar cargas de trabalho elásticas.","Maior utilização geral de sistemas de servidor e armazenamento.","Produtividade aumentada para equipes de desenvolvimento de aplicações."],
     "correct":[0,4],"multiple":True},
    {"q":"Qual princípio de design de arquitetura de nuvem é suportado pela implantação de cargas de trabalho em múltiplas Zonas de Disponibilidade?",
     "options":["Automatizar infraestrutura.","Projetar para agilidade.","Habilitar elasticidade.","Projetar para falha."],
     "correct":[3],"multiple":False},
    {"q":"Uma empresa requer um painel para relatórios ao usar uma solução de business intelligence. Qual serviço AWS um Cloud Practitioner pode usar?",
     "options":["Amazon Redshift","Amazon Kinesis","Amazon Athena","Amazon QuickSight"],
     "correct":[3],"multiple":False},
    {"q":"Um Cloud Practitioner quer configurar a AWS CLI para acesso programático aos serviços AWS. Quais componentes de credencial são necessários? (Selecione DUAS.)",
     "options":["Um ID de chave de acesso","Uma chave pública","Uma chave de acesso secreta","Uma Função IAM","Uma chave privada"],
     "correct":[0,2],"multiple":True},
    {"q":"Qual serviço um Cloud Practitioner pode usar para configurar limites personalizados de custo e uso e habilitar alertas quando os limites definidos forem excedidos?",
     "options":["Cobrança consolidada","AWS Trusted Advisor","Cost Explorer","AWS Budgets"],
     "correct":[3],"multiple":False},
    {"q":"Qual é a função do Amazon EC2 Auto Scaling?",
     "options":["Escala o tamanho das instâncias EC2 para cima ou para baixo automaticamente, com base na demanda.","Atualiza automaticamente o modelo de preços EC2, com base na demanda.","Escala o número de instâncias EC2 para dentro ou para fora automaticamente, com base na demanda.","Modifica automaticamente a taxa de transferência de rede das instâncias EC2, com base na demanda."],
     "correct":[2],"multiple":False},
    {"q":"Qual serviço AWS um Cloud Practitioner deve usar para estabelecer uma conexão de rede segura entre uma rede local e a AWS?",
     "options":["AWS Mobile Hub","AWS Web Application Firewall (WAF)","Amazon Virtual Private Cloud (VPC)","Virtual Private Network"],
     "correct":[3],"multiple":False},
    {"q":"Qual serviço gerenciado pela AWS pode ser usado para processar vastas quantidades de dados usando um framework Hadoop hospedado?",
     "options":["Amazon DynamoDB","Amazon Athena","Amazon EMR","Amazon Redshift"],
     "correct":[2],"multiple":False},
    {"q":"Qual modelo de preços Amazon EC2 deve ser evitado se uma carga de trabalho não pode aceitar interrupção se a capacidade se tornar temporariamente indisponível?",
     "options":["Spot Instances","On-Demand Instances","Standard Reserved Instances","Convertible Reserved Instances"],
     "correct":[0],"multiple":False},
    {"q":"Qual serviço AWS um Cloud Practitioner pode usar para identificar de forma simples se acesso irrestrito a recursos foi permitido por grupos de segurança?",
     "options":["AWS Trusted Advisor","Amazon CloudWatch","VPC Flow Logs","AWS CloudTrail"],
     "correct":[0],"multiple":False},
    {"q":"Uma empresa de eCommerce planeja usar a AWS Cloud para entregar rapidamente nova funcionalidade de forma iterativa, minimizando o tempo para o mercado. Qual recurso da AWS Cloud fornece essa funcionalidade?",
     "options":["Elasticidade","Agilidade","Tolerância a falhas","Eficiência de custos"],
     "correct":[1],"multiple":False},
    {"q":"O que um Cloud Practitioner pode fazer com as ferramentas de Gerenciamento de Custos da AWS? (Selecione DUAS.)",
     "options":["Visualizar custos AWS por dia, serviço e conta AWS vinculada.","Encerrar instâncias EC2 automaticamente se os limites de orçamento forem excedidos.","Modificar automaticamente instâncias EC2 para usar preços Spot para reduzir custos.","Criar orçamentos e receber notificações se o uso atual ou previsto exceder os orçamentos.","Arquivar dados para Amazon Glacier se não forem acessados por um período configurado."],
     "correct":[0,3],"multiple":True},
    {"q":"Qual painel AWS exibe informações relevantes e oportunas para ajudar os usuários a gerenciar eventos em andamento e fornece notificações proativas para ajudar no planejamento de atividades programadas?",
     "options":["AWS Service Health Dashboard","AWS Personal Health Dashboard","Painel AWS Trusted Advisor","Painel Amazon CloudWatch"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço AWS um Cloud Practitioner deve usar para automatizar o gerenciamento de configuração usando Puppet?",
     "options":["AWS Config","AWS OpsWorks","AWS CloudFormation","AWS Systems Manager"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço AWS é usado para enviar mensagens de texto e email de aplicações distribuídas?",
     "options":["Amazon Simple Notification Service (Amazon SNS)","Amazon Simple Email Service (Amazon SES)","Amazon Simple Workflow Service (Amazon SWF)","Amazon Simple Queue Service (Amazon SQS)"],
     "correct":[0],"multiple":False},
    {"q":"Qual serviço ou recurso AWS permite que uma empresa receba uma única fatura mensal da AWS ao usar múltiplas contas AWS?",
     "options":["Cobrança consolidada","Amazon Cloud Directory","AWS Cost Explorer","Relatório AWS Cost and Usage"],
     "correct":[0],"multiple":False},
    {"q":"Um usuário precisa de um relatório de avaliação de segurança automatizado que identificará acesso de rede não intencional a instâncias Amazon EC2 e vulnerabilidades nessas instâncias.",
     "options":["Grupos de segurança EC2","AWS Config","Amazon Macie","Amazon Inspector"],
     "correct":[3],"multiple":False},
    {"q":"Qual das seguintes melhor descreve uma Zona de Disponibilidade na AWS Cloud?",
     "options":["Um ou mais data centers físicos","Uma localização geográfica completamente isolada","Uma ou mais localizações de borda baseadas ao redor do mundo","Uma sub-rede para implantar recursos"],
     "correct":[0],"multiple":False},
    {"q":"Uma empresa precisa de uma conexão consistente e dedicada entre recursos AWS e um sistema local.",
     "options":["AWS Direct Connect","AWS Managed VPN","Amazon Connect","AWS DataSync"],
     "correct":[0],"multiple":False},
    {"q":"Qual serviço AWS ajuda os clientes a atender requisitos de conformidade corporativa, contratual e regulatória para segurança de dados usando aparelhos de hardware dedicados dentro da AWS Cloud?",
     "options":["AWS Secrets Manager","AWS CloudHSM","AWS Key Management Service (AWS KMS)","AWS Directory Service"],
     "correct":[1],"multiple":False},
    {"q":"Para que um Cloud Practitioner pode usar a Calculadora de Custo Total de Propriedade (TCO) da AWS?",
     "options":["Gerar relatórios que dividem custos de computação da AWS Cloud por duração, recurso ou tags","Estimar economias ao comparar a AWS Cloud com um ambiente local","Estimar uma fatura mensal para os recursos AWS Cloud que serão usados","Habilitar alertas de cobrança para monitorar custos reais da AWS em comparação com custos estimados"],
     "correct":[1],"multiple":False},
    {"q":"Qual dos seguintes deve ser usado para melhorar a segurança do acesso ao AWS Management Console? (Selecione DUAS.)",
     "options":["AWS Secrets Manager","AWS Certificate Manager","AWS Multi-Factor Authentication (AWS MFA)","Regras de grupo de segurança","Políticas de senha fortes"],
     "correct":[2,4],"multiple":True},
    {"q":"Uma aplicação tem padrões de uso altamente dinâmicos. Quais características da AWS Cloud tornam econômica para este tipo de carga de trabalho? (Selecione DUAS.)",
     "options":["Alta disponibilidade","Segurança rigorosa","Elasticidade","Preços pay-as-you-go","Confiabilidade"],
     "correct":[2,3],"multiple":True},
    {"q":"Quais benefícios uma empresa pode realizar imediatamente usando a AWS Cloud? (Selecione DUAS.)",
     "options":["Despesas variáveis são substituídas por despesas de capital","Despesas de capital são substituídas por despesas variáveis","Controle do usuário sobre infraestrutura física","Agilidade aumentada","Nenhuma responsabilidade pela segurança"],
     "correct":[1,3],"multiple":True},
    {"q":"Qual serviço de armazenamento híbrido AWS permite que aplicações locais usem armazenamento AWS Cloud de forma transparente?",
     "options":["AWS Backup","Amazon Connect","AWS Direct Connect","AWS Storage Gateway"],
     "correct":[3],"multiple":False},
    {"q":"Um usuário tem conhecimento limitado de serviços AWS, mas quer implantar rapidamente uma aplicação Node.js escalável em uma Amazon VPC.",
     "options":["AWS CloudFormation","AWS Elastic Beanstalk","Amazon EC2","Amazon LightSail"],
     "correct":[1],"multiple":False},
    {"q":"Como um oficial de conformidade de segurança pode recuperar documentação de conformidade AWS como um relatório SOC 2?",
     "options":["Usando AWS Artifact","Usando AWS Trusted Advisor","Usando AWS Inspector","Usando o AWS Personal Health Dashboard"],
     "correct":[0],"multiple":False},
    {"q":"Qual serviço AWS pode ser usado para executar containers Docker?",
     "options":["AWS Lambda","Amazon ECR","Amazon ECS","Amazon AMI"],
     "correct":[2],"multiple":False},
    {"q":"Quais são os benefícios de usar os Serviços Gerenciados da AWS? (Selecione DUAS.)",
     "options":["Alinhamento com processos ITIL","Aplicações gerenciadas para que você possa focar na infraestrutura","Integração básica com ferramentas ITSM","Projetado para pequenas empresas","Suporte para todos os serviços AWS"],
     "correct":[0,2],"multiple":True},
    {"q":"Quais serviços estão envolvidos com segurança? (Selecione DUAS.)",
     "options":["AWS CloudHSM","AWS DMS","AWS KMS","AWS SMS","Amazon ELB"],
     "correct":[0,2],"multiple":True},
    {"q":"Quais são os nomes de dois tipos de AWS Storage Gateway? (Selecione DUAS.)",
     "options":["S3 Gateway","File Gateway","Block Gateway","Tape Gateway","Cached Gateway"],
     "correct":[1,3],"multiple":True},
    {"q":"Uma aplicação armazena imagens que serão recuperadas com pouca frequência, mas devem estar disponíveis para recuperação imediata. Qual é a opção de armazenamento mais econômica que atende a esses requisitos?",
     "options":["Amazon Glacier com recuperações expeditas","Amazon S3 Standard-Infrequent Access","Amazon EFS","Amazon S3 Standard"],
     "correct":[1],"multiple":False},
    {"q":"Quais planos de suporte AWS fornecem suporte via email, chat e telefone? (Selecione DUAS.)",
     "options":["Basic","Developer","Business","Enterprise","Global"],
     "correct":[2,3],"multiple":True},
    {"q":"Qual serviço AWS pode ser usado para hospedar um site estático?",
     "options":["Amazon S3","Amazon EBS","AWS CloudFormation","Amazon EFS"],
     "correct":[0],"multiple":False},
    {"q":"Quais das seguintes são práticas recomendadas da AWS em relação ao IAM? (Selecione DUAS.)",
     "options":["Atribuir permissões a usuários","Criar usuários IAM individuais","Incorporar chaves de acesso no código da aplicação","Habilitar MFA para todos os usuários","Conceder maior privilégio"],
     "correct":[1,3],"multiple":True},
    {"q":"Quais das seguintes tarefas de operações de segurança devem ser realizadas pelos clientes AWS? (Selecione DUAS.)",
     "options":["Coletar mensagens syslog de firewalls físicos","Emitir cartões de acesso de data center","Instalar atualizações de segurança em instâncias EC2","Habilitar autenticação multifator (MFA) para usuários privilegiados","Instalar atualizações de segurança para firmware do servidor"],
     "correct":[2,3],"multiple":True},
    {"q":"Como uma organização pode avaliar aplicações para vulnerabilidades e desvios das melhores práticas?",
     "options":["Usar AWS Artifact","Usar AWS Inspector","Usar AWS Shield","Usar AWS WAF"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço AWS protege contra exploits comuns que poderiam comprometer a disponibilidade da aplicação, comprometer a segurança ou consumir recursos excessivos?",
     "options":["AWS WAF","AWS Shield","Security Group","Network ACL"],
     "correct":[0],"multiple":False},
    {"q":"Um novo usuário não consegue acessar nenhum serviço AWS, qual é a explicação mais provável?",
     "options":["O usuário precisa fazer login com um par de chaves","Os serviços estão atualmente indisponíveis","Por padrão, novos usuários são criados sem acesso a nenhum serviço AWS","O limite padrão para logons de usuário foi atingido"],
     "correct":[2],"multiple":False},
    {"q":"Qual programa de conformidade permite que o ambiente AWS processe, mantenha e armazene informações de saúde protegidas?",
     "options":["ISO 27001","PCI DSS","HIPAA","SOC 1"],
     "correct":[2],"multiple":False},
    {"q":"Qual serviço AWS pode ser usado para carregar dados do Amazon S3, transformá-los e movê-los para outro destino?",
     "options":["Amazon RedShift","Amazon EMR","Amazon Kinesis","AWS Glue"],
     "correct":[3],"multiple":False},
    {"q":"Como uma organização deve implantar uma aplicação executando em múltiplas instâncias EC2 para garantir que uma falha de energia não cause uma interrupção da aplicação?",
     "options":["Lançar as instâncias EC2 em regiões separadas","Lançar as instâncias EC2 em VPCs diferentes","Lançar as instâncias EC2 em Zonas de Disponibilidade diferentes","Lançar as instâncias EC2 em Edge Locations"],
     "correct":[2],"multiple":False},
    {"q":"Qual das declarações abaixo está correta em relação à Cobrança Consolidada? (Selecione DUAS.)",
     "options":["Você recebe uma fatura por conta AWS","Você recebe uma única fatura para múltiplas contas","Você paga uma taxa por conta vinculada","Você pode combinar uso e compartilhar descontos de preços por volume","Você é cobrado uma taxa por usuário"],
     "correct":[1,3],"multiple":True},
    {"q":"O Amazon S3 é tipicamente usado para quais dos seguintes casos de uso? (Selecione DUAS.)",
     "options":["Hospedar um site estático","Instalar um sistema operacional","Hospedagem de mídia","Cache de dados em memória","Fila de mensagens"],
     "correct":[0,2],"multiple":True}
]

SIMULADO_3 = [
    {"q":"Qual serviço ou recurso AWS pode ser usado para restringir as ações de API individuais que usuários e funções em cada conta membro podem acessar?",
     "options":["Amazon Macie","AWS Organizations","AWS Shield","AWS IAM"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço AWS pode ser usado para rastrear a atividade de usuários na AWS?",
     "options":["AWS CloudTrail","AWS Directory Service","Amazon Inspector","Amazon CloudWatch"],
     "correct":[0],"multiple":False},
    {"q":"Uma empresa precisa otimizar custos e uso de recursos através do monitoramento da saúde operacional para todos os recursos executando na AWS.",
     "options":["AWS Control Tower","Amazon CloudWatch","AWS CloudTrail","AWS Config"],
     "correct":[1],"multiple":False},
    {"q":"Um usuário precisa de uma forma rápida de determinar se alguma instância Amazon EC2 tem portas que permitem acesso irrestrito.",
     "options":["VPC Flow Logs","AWS Shield","AWS Trusted Advisor","AWS CloudWatch Logs"],
     "correct":[2],"multiple":False},
    {"q":"Uma empresa tem um site que entrega conteúdo estático de um bucket Amazon S3 para usuários de todo o mundo. Qual serviço AWS entregará o conteúdo com baixa latência?",
     "options":["AWS Lambda","Amazon CloudFront","AWS Elastic Beanstalk","AWS Global Accelerator"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço ou componente AWS permite tráfego de entrada da internet para acessar uma VPC?",
     "options":["NAT Gateway","Internet gateway","VPC Route Table","Virtual Private Gateway"],
     "correct":[1],"multiple":False},
    {"q":"Uma empresa planeja conectar seu data center local à AWS Cloud e requer largura de banda e performance consistentes.",
     "options":["AWS VPN","Amazon Connect","AWS Direct Connect","Amazon CloudFront"],
     "correct":[2],"multiple":False},
    {"q":"Um gerente está planejando migrar aplicações para a AWS Cloud e precisa obter relatórios de conformidade da AWS.",
     "options":["Baixar os relatórios do AWS Secrets Manager.","Contatar a equipe de Conformidade da AWS.","Criar um ticket de suporte com o AWS Support.","Baixar os relatórios do AWS Artifact."],
     "correct":[3],"multiple":False},
    {"q":"Uma empresa tem usado uma política IAM gerenciada pela AWS para conceder permissões a usuários, mas precisa adicionar algumas permissões.",
     "options":["Criar uma regra no AWS WAF.","Criar uma política IAM personalizada.","Editar a política gerenciada pela AWS.","Criar uma Política de Controle de Serviço."],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço ou recurso AWS pode ser usado para capturar informações sobre tráfego IP de entrada e saída em interfaces de rede em uma VPC?",
     "options":["Internet gateway","AWS CloudTrail","VPC Endpoint","VPC Flow Logs"],
     "correct":[3],"multiple":False},
    {"q":"Quais serviços AWS podem ser usados como ferramentas de automação de infraestrutura? (Selecione DUAS.)",
     "options":["AWS CloudFormation","Amazon CloudFront","AWS Batch","AWS OpsWorks","Amazon QuickSight"],
     "correct":[0,3],"multiple":True},
    {"q":"Que tecnologia permite que a capacidade de computação se ajuste conforme as cargas mudam?",
     "options":["Balanceamento de carga","Failover automático","Round robin","Auto Scaling"],
     "correct":[3],"multiple":False},
    {"q":"Como uma empresa pode separar custos para armazenamento, Amazon EC2, Amazon S3 e outros serviços AWS por departamento?",
     "options":["Adicionar tags específicas do departamento a cada recurso","Criar uma VPC separada para cada departamento","Criar uma conta AWS separada para cada departamento","Usar AWS Organizations"],
     "correct":[0],"multiple":False},
    {"q":"Qual plano de suporte AWS fornece acesso a revisões arquiteturais e operacionais, bem como acesso 24/7 a Engenheiros de Suporte Cloud por email, chat online e telefone?",
     "options":["Basic","Business","Developer","Enterprise"],
     "correct":[3],"multiple":False},
    {"q":"Sob o modelo de responsabilidade compartilhada da AWS, qual das seguintes é um exemplo de segurança na AWS Cloud?",
     "options":["Gerenciar localizações de borda","Segurança física","Configuração de firewall","Infraestrutura global"],
     "correct":[2],"multiple":False},
    {"q":"Qual serviço AWS fornece downloads sob demanda de relatórios de segurança e conformidade da AWS?",
     "options":["AWS Directory Service","AWS Artifact","AWS Trusted Advisor","Amazon Inspector"],
     "correct":[1],"multiple":False},
    {"q":"Qual modelo de preços Amazon EC2 é o mais econômico para um servidor de banco de dados sempre ativo e dimensionado corretamente executando um projeto que durará 1 ano?",
     "options":["On-Demand Instances","Convertible Reserved Instances","Spot Instances","Standard Reserved Instances"],
     "correct":[3],"multiple":False},
    {"q":"Qual recurso permite transferências rápidas, fáceis e seguras de arquivos por longas distâncias entre um cliente e um bucket Amazon S3?",
     "options":["S3 Static Websites","S3 Copy","Multipart Upload","S3 Transfer Acceleration"],
     "correct":[3],"multiple":False},
    {"q":"Sob o modelo de responsabilidade compartilhada da AWS, pelo que a AWS é responsável? (Selecione DUAS.)",
     "options":["Segurança física do data center","Substituição e descarte de discos rígidos","Configuração de grupos de segurança","Gerenciamento de patches de sistemas operacionais","Criptografia de dados do cliente"],
     "correct":[0,1],"multiple":True},
    {"q":"Qual serviço AWS é conhecido como um serviço \"serverless\" e executa código como funções acionadas por eventos?",
     "options":["Amazon ECS","AWS Lambda","Amazon CodeDeploy","Amazon Cognito"],
     "correct":[1],"multiple":False},
    {"q":"Qual declaração melhor descreve o Amazon Route 53?",
     "options":["Amazon Route 53 é um serviço que permite roteamento dentro de VPCs em uma conta","Amazon Route 53 é um serviço de Sistema de Nomes de Domínio (DNS) altamente disponível e escalável","Amazon Route 53 permite modelos de nuvem híbrida estendendo as redes locais de uma organização para a nuvem AWS","Amazon Route 53 é um serviço para distribuir conexões de entrada entre uma frota de instâncias EC2 registradas"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço fornece uma forma de converter arquivos de vídeo e áudio de seu formato de origem em versões que serão reproduzidas em dispositivos como smartphones, tablets e PCs?",
     "options":["Amazon Elastic Transcoder","AWS Glue","Amazon Rekognition","Amazon Comprehend"],
     "correct":[0],"multiple":False},
    {"q":"Ao usar AWS Organizations com cobrança consolidada, quais são duas práticas recomendadas válidas? (Selecione DUAS.)",
     "options":["Sempre habilitar autenticação multifator (MFA) na conta raiz","Sempre usar uma senha simples na conta raiz","A conta pagadora deve ser usada apenas para fins de cobrança","Usar a conta pagadora para implantar recursos","Nunca exceder o limite de 20 contas vinculadas"],
     "correct":[0,2],"multiple":True},
    {"q":"Qual plano de suporte AWS vem com um Gerente de Conta Técnica (TAM)?",
     "options":["Basic","Developer","Business","Enterprise"],
     "correct":[3],"multiple":False},
    {"q":"Qual serviço fornece a capacidade de simplesmente fazer upload de aplicações e ter a AWS lidar com os detalhes de implantação de provisionamento de capacidade, balanceamento de carga, auto-scaling e monitoramento de saúde da aplicação?",
     "options":["Amazon EC2","AWS Elastic Beanstalk","Amazon EC2 Auto Scaling","AWS OpsWorks"],
     "correct":[1],"multiple":False},
    {"q":"Você está preocupado que pode estar se aproximando de alguns dos limites de serviço padrão para vários serviços AWS. Qual ferramenta AWS pode ser usada para exibir uso atual e limites?",
     "options":["AWS CloudWatch","AWS Personal Health Dashboard","AWS Trusted Advisor","AWS Systems Manager"],
     "correct":[2],"multiple":False},
    {"q":"Você precisa executar um processo de produção que usará várias instâncias EC2 e executará constantemente de forma contínua. O processo não pode ser interrompido ou reiniciado sem problemas. Qual modelo de preços EC2 seria melhor para esta carga de trabalho?",
     "options":["Reserved instances","Spot instances","On-demand instances","Flexible instances"],
     "correct":[0],"multiple":False},
    {"q":"Qual serviço AWS o API Gateway integra para permitir que usuários de todo o mundo alcancem a menor latência possível para solicitações e respostas de API?",
     "options":["AWS Direct Connect","Amazon S3 Transfer Acceleration","Amazon CloudFront","AWS Lambda"],
     "correct":[2],"multiple":False},
    {"q":"Qual serviço uma organização pode usar para rastrear atividade de API dentro de sua conta?",
     "options":["AWS CloudTrail","Amazon CloudWatch","AWS IAM","AWS CloudHSM"],
     "correct":[0],"multiple":False},
    {"q":"Que ferramenta fornece orientação em tempo real para ajudar você a provisionar seus recursos seguindo as melhores práticas nas áreas de otimização de custos, performance, segurança e tolerância a falhas?",
     "options":["AWS Inspector","AWS Trusted Advisor","AWS Personal Health Dashboard","AWS IAM"],
     "correct":[1],"multiple":False},
    {"q":"Qual é a melhor forma para uma organização transferir centenas de terabytes de dados de seu data center local para o Amazon S3 com largura de banda limitada disponível?",
     "options":["Usar S3 Transfer Acceleration","Aplicar compressão antes do upload","Usar AWS Snowball","Usar Amazon CloudFront"],
     "correct":[2],"multiple":False},
    {"q":"Qual banco de dados permite que você escale com o toque de um botão sem incorrer em tempo de inatividade?",
     "options":["Amazon RDS","Amazon EMR","Amazon DynamoDB","Amazon RedShift"],
     "correct":[2],"multiple":False},
    {"q":"Quais são as cobranças para usar Amazon Glacier? (Selecione DUAS.)",
     "options":["Dados transferidos para Glacier","Solicitações de recuperação","Armazenamento de dados","Rede aprimorada","Número de Zonas de Disponibilidade"],
     "correct":[1,2],"multiple":True},
    {"q":"Quais das seguintes declarações estão corretas sobre os benefícios do AWS Direct Connect? (Selecione DUAS.)",
     "options":["Rápido de implementar","Maior confiabilidade (performance previsível)","Menor custo que uma VPN","Maior largura de banda (largura de banda previsível)","Usa caminhos redundantes através da Internet"],
     "correct":[1,3],"multiple":True},
    {"q":"Qual serviço permite que uma organização use Chef e Puppet para automatizar como servidores são configurados, implantados e gerenciados em suas instâncias Amazon EC2 ou ambientes de computação locais?",
     "options":["AWS Elastic Beanstalk","AWS CloudFormation","AWS Systems Manager","AWS OpsWorks"],
     "correct":[3],"multiple":False},
    {"q":"Qual serviço de banco de dados AWS fornece um data warehouse totalmente gerenciado que pode ser analisado usando ferramentas SQL e business intelligence?",
     "options":["Amazon RDS","Amazon DynamoDB","Amazon RedShift","Amazon ElastiCache"],
     "correct":[2],"multiple":False},
    {"q":"Qual serviço pode ser usado para criar aplicações de gráfico sofisticadas e interativas?",
     "options":["Amazon RedShift","Amazon Neptune","AWS X-Ray","Amazon Athena"],
     "correct":[1],"multiple":False},
    {"q":"Ao usar Amazon IAM, quais métodos de autenticação estão disponíveis para usar? (Selecione DUAS.)",
     "options":["Certificados de cliente","Chaves de acesso","AWS KMS","Certificados de servidor","AES 256"],
     "correct":[1,3],"multiple":True},
    {"q":"Como o recurso de cobrança consolidada do AWS Organizations trata Reserved Instances que foram compradas por outra conta na organização?",
     "options":["Todas as contas na organização são tratadas como uma conta, então qualquer conta pode receber o benefício de custo horário","Apenas a conta master pode se beneficiar do benefício de custo horário das instâncias reservadas","Todas as contas na organização são tratadas como uma conta para descontos de volume, mas não para instâncias reservadas","AWS Organizations não suporta benefícios de volume ou instância reservada entre contas, é apenas um método de agregar faturas"],
     "correct":[0],"multiple":False},
    {"q":"Qual dos seguintes serviços AWS suporta backups automatizados como configuração padrão?",
     "options":["Amazon S3","Amazon RDS","Amazon EC2","Amazon EBS"],
     "correct":[1],"multiple":False},
    {"q":"Quais são as vantagens das Zonas de Disponibilidade? (Selecione DUAS.)",
     "options":["Elas permitem recuperação de desastres regional","Elas fornecem isolamento de falhas","Elas permitem o cache de dados para entrega mais rápida aos usuários finais","Elas são conectadas por conexões de rede de baixa latência","Elas permitem conectar suas redes locais à AWS para formar uma nuvem híbrida"],
     "correct":[1,3],"multiple":True},
    {"q":"Quais das opções abaixo são recomendações no pilar de otimização de custos do framework bem arquitetado? (Selecione DUAS.)",
     "options":["Adotar um modelo de consumo","Adotar um modelo de despesa de capital","Começar a gastar dinheiro em operações de data center","Analisar e atribuir despesas","Gerenciar seus serviços independentemente"],
     "correct":[0,3],"multiple":True},
    {"q":"Para que Edge Locations são usadas?",
     "options":["Elas são usadas para terminar conexões VPN","Elas são usadas pelo CloudFront para cache de conteúdo","Elas são as APIs públicas do Amazon S3","Elas são usadas por regiões para conectividade inter-região"],
     "correct":[1],"multiple":False},
    {"q":"Para garantir a segurança de sua conta AWS, quais são duas práticas recomendadas da AWS para gerenciar chaves de acesso? (Selecione DUAS.)",
     "options":["Não criar nenhuma chave de acesso, usar funções IAM em vez disso","Não gerar uma chave de acesso para o usuário da conta raiz","Quando possível, usar funções IAM com credenciais de segurança temporárias","Rotacionar chaves de acesso diariamente","Usar MFA para chaves de acesso"],
     "correct":[1,2],"multiple":True},
    {"q":"Uma instância Amazon EC2 executando a AMI Amazon Linux 2 é cobrada em que incremento?",
     "options":["Por segundo","Por hora","Por CPU","Por GB"],
     "correct":[0],"multiple":False},
    {"q":"Para obter descontos maiores, quais serviços podem ser reservados? (Selecione DUAS.)",
     "options":["Amazon RedShift","Amazon S3","AWS Lambda","Amazon DynamoDB","Amazon CloudWatch"],
     "correct":[0,3],"multiple":True},
    {"q":"Qual serviço permite que uma organização visualize dados operacionais de múltiplos serviços AWS através de uma interface unificada e automatize tarefas operacionais?",
     "options":["AWS Config","AWS OpsWorks","AWS Systems Manager","Amazon CloudWatch"],
     "correct":[2],"multiple":False},
    {"q":"Como uma organização pode rastrear inventário de recursos e histórico de configuração para fins de segurança e conformidade regulatória?",
     "options":["Configurar AWS Config com os tipos de recursos","Criar uma trilha Amazon CloudTrail","Implementar Amazon GuardDuty","Executar um relatório com AWS Artifact"],
     "correct":[0],"multiple":False},
    {"q":"Um engenheiro de operações de segurança precisa implementar detecção de ameaças e monitoramento para comportamento malicioso ou não autorizado. Qual serviço deve ser usado?",
     "options":["AWS Shield","AWS KMS","AWS CloudHSM","AWS GuardDuty"],
     "correct":[3],"multiple":False},
    {"q":"Qual método de autenticação é usado para autenticar chamadas programáticas para serviços AWS?",
     "options":["Senha do console","Certificado de servidor","Par de chaves","Chaves de acesso"],
     "correct":[3],"multiple":False},
    {"q":"Qual é um benefício de mover um banco de dados local para o Amazon Relational Database Service (RDS)?",
     "options":["Não há necessidade de gerenciar sistemas operacionais","Você pode escalar verticalmente sem tempo de inatividade","Não há administração de banco de dados necessária","Você pode executar qualquer engine de banco de dados"],
     "correct":[0],"multiple":False},
    {"q":"Quais são os benefícios de usar Amazon Rekognition com arquivos de imagem?",
     "options":["Pode ser usado para redimensionar imagens","Pode ser usado para identificar objetos em uma imagem","Pode ser usado para transcodificar áudio","Pode ajudar com compressão de imagem"],
     "correct":[1],"multiple":False},
    {"q":"Qual entidade IAM está associada a um ID de chave de acesso e chave de acesso secreta?",
     "options":["Grupo IAM","Função IAM","Política IAM","Usuário IAM"],
     "correct":[3],"multiple":False},
    {"q":"Qual entidade IAM pode ser usada para atribuir permissões a múltiplos usuários?",
     "options":["Usuário IAM","Grupo IAM","Função IAM","Política de senha IAM"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço pode ser usado para mover de forma econômica exabytes de dados para a AWS?",
     "options":["AWS Snowmobile","AWS Snowball","S3 Transfer Acceleration","S3 Cross-Region Replication (CRR)"],
     "correct":[0],"multiple":False},
    {"q":"Quais serviços AWS estão associados a Edge Locations? (Selecione DUAS.)",
     "options":["Amazon CloudFront","AWS Direct Connect","AWS Shield","Amazon EBS","AWS Config"],
     "correct":[0,2],"multiple":True},
    {"q":"Qual serviço pode ser usado para criar facilmente múltiplas contas?",
     "options":["AWS IAM","AWS CloudFormation","AWS Organizations","Amazon Connect"],
     "correct":[2],"multiple":False},
    {"q":"Qual é um benefício específico de um plano de suporte Enterprise?",
     "options":["Gerente de Suporte Técnico incluído","Arquiteto de Soluções AWS incluído","Associado de Suporte Cloud incluído","Gerente de Conta Técnica incluído"],
     "correct":[3],"multiple":False},
    {"q":"Você tem executado uma instância Amazon EC2 Linux sob demanda por 4hrs, 5 minutos e 6 segundos. Por quanto tempo você será cobrado?",
     "options":["5hrs","4hrs, 6mins","4hrs, 5mins e 6 segundos","4hrs"],
     "correct":[2],"multiple":False},
    {"q":"Qual das opções abaixo é um exemplo de benefício arquitetural de mover para a nuvem?",
     "options":["Elasticidade","Serviços monolíticos","Hardware proprietário","Escalabilidade vertical"],
     "correct":[0],"multiple":False},
    {"q":"Quais são os benefícios de usar instâncias reservadas? (Selecione DUAS.)",
     "options":["Custo reduzido","Mais flexibilidade","Reservar capacidade","Usa hardware dedicado","Alta disponibilidade"],
     "correct":[0,2],"multiple":True},
    {"q":"Quais ferramentas AWS podem ser usadas para automação? (Selecione DUAS.)",
     "options":["AWS Elastic Beanstalk","Elastic Load Balancing","AWS CloudFormation","Amazon Elastic File System (EFS)","AWS Lambda"],
     "correct":[0,2],"multiple":True},
    {"q":"Qual entidade IAM pode ser usada para atribuir permissões a serviços AWS?",
     "options":["ID de Chave de Acesso IAM e Chave de Acesso Secreta","Política IAM","Função IAM","Security Token Service (STS)"],
     "correct":[2],"multiple":False},
    {"q":"Como o Amazon EC2 Auto Scaling ajuda com resiliência?",
     "options":["Distribuindo conexões para instâncias EC2","Lançando e terminando instâncias conforme necessário","Mudando tipos de instância para aumentar capacidade","Automatizando o failover de aplicações"],
     "correct":[1],"multiple":False},
    {"q":"Seu CTO quer mover para a nuvem. Quais vantagens de custo existem ao mover para a nuvem?",
     "options":["Você provisiona apenas o que precisa e ajusta para carga de pico","Você pode reduzir seus custos de marketing","Você não precisa pagar por licenciamento de aplicação","Você obtém transferência de dados gratuita para dentro e fora da nuvem"],
     "correct":[0],"multiple":False}
]

SIMULADO_4 = [
    {"q":"Qual serviço AWS deve ser usado para criar um alarme de cobrança?",
     "options":["AWS Trusted Advisor","AWS CloudTrail","Amazon CloudWatch","Amazon QuickSight"],
     "correct":[2],"multiple":False},
    {"q":"Como a cobrança consolidada dentro do AWS Organizations pode ajudar a reduzir as despesas mensais gerais?",
     "options":["Fornecendo uma visão consolidada da cobrança mensal em múltiplas contas","Agrupando uso em múltiplas contas para alcançar um desconto de nível de preço","Automatizando a criação de novas contas através de APIs","Aproveitando políticas de controle de serviço (SCP) para gerenciamento centralizado de serviços"],
     "correct":[1],"multiple":False},
    {"q":"Qual modelo de preços Amazon EC2 deve ser usado para cumprir requisitos de licença de software por núcleo?",
     "options":["Dedicated Hosts","On-Demand Instances","Spot Instances","Reserved Instances"],
     "correct":[0],"multiple":False},
    {"q":"Quais das seguintes são vantagens da AWS Cloud? (Selecione DUAS.)",
     "options":["A AWS gerencia a manutenção da infraestrutura de nuvem","A AWS gerencia a segurança de aplicações construídas na AWS","A AWS gerencia o planejamento de capacidade para servidores físicos","A AWS gerencia o desenvolvimento de aplicações na AWS","A AWS gerencia o planejamento de custos para servidores virtuais"],
     "correct":[0,2],"multiple":True},
    {"q":"A capacidade de escalar horizontalmente instâncias Amazon EC2 baseado na demanda é um exemplo de qual conceito?",
     "options":["Economia de escala","Elasticidade","Alta disponibilidade","Agilidade"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço AWS fornece uma forma rápida e automatizada de criar e gerenciar contas AWS?",
     "options":["AWS QuickSight","Amazon LightSail","AWS Organizations","Amazon Connect"],
     "correct":[2],"multiple":False},
    {"q":"Qual ferramenta pode ser usada para criar alertas quando o custo real ou previsto dos serviços AWS exceder um certo limite?",
     "options":["AWS Cost Explorer","AWS Budgets","AWS Cost and Usage report","AWS CloudTrail"],
     "correct":[1],"multiple":False},
    {"q":"Um usuário tem uma conta AWS com um plano de suporte AWS Business e precisa de assistência para lidar com uma interrupção de serviço de produção.",
     "options":["Contatar o Gerente de Conta Técnica dedicado","Contatar a equipe dedicada de Suporte AWS Concierge","Abrir um caso de suporte de sistema crítico de negócios","Abrir um caso de suporte de sistema de produção fora do ar"],
     "correct":[3],"multiple":False},
    {"q":"Qual tipo de AWS Storage Gateway pode ser usado para backup de dados com software de backup popular?",
     "options":["File Gateway","Volume Gateway","Gateway Virtual Tape Library","Backup Gateway"],
     "correct":[2],"multiple":False},
    {"q":"Você gostaria de coletar métricas personalizadas de uma aplicação de produção a cada 1 minuto. Que tipo de monitoramento você deve usar?",
     "options":["CloudWatch com monitoramento detalhado","CloudTrail com monitoramento básico","CloudWatch com monitoramento básico","CloudTrail com monitoramento detalhado"],
     "correct":[0],"multiple":False},
    {"q":"Quais períodos de cobrança estão disponíveis para instâncias Amazon EC2 sob demanda? (Selecione DUAS.)",
     "options":["Por semana","Por dia","Por hora","Por minuto","Por segundo"],
     "correct":[2,4],"multiple":True},
    {"q":"Qual opção de preços Amazon EC2 fornece descontos significativos para contratos de prazo fixo?",
     "options":["Reserved Instances","Spot Instances","Dedicated Instances","Dedicated Hosts"],
     "correct":[0],"multiple":False},
    {"q":"Ao usar bancos de dados Amazon RDS, por quais itens você é cobrado? (Selecione DUAS.)",
     "options":["Transferência de dados de entrada","Multi AZ","Single AZ","Backup até o tamanho do DB","Transferência de dados de saída"],
     "correct":[1,4],"multiple":True},
    {"q":"Como as funções AWS Lambda são acionadas?",
     "options":["Eventos","Agendamentos","Métricas","Contadores"],
     "correct":[0],"multiple":False},
    {"q":"Qual ferramenta pode ser usada para fornecer orientação em tempo real sobre provisionamento de recursos seguindo as melhores práticas da AWS?",
     "options":["AWS Trusted Advisor","AWS Simple Monthly Calculator","AWS Inspector","AWS Personal Health Dashboard"],
     "correct":[0],"multiple":False},
    {"q":"Ao realizar uma análise de custo total de propriedade (TCO) entre local e a AWS Cloud, quais fatores são relevantes apenas para implantações locais? (Selecione DUAS.)",
     "options":["Equipes de aquisição de hardware","Licenciamento de sistema operacional","Custos de operação de instalações","Administração de banco de dados","Licenciamento de aplicação"],
     "correct":[0,2],"multiple":True},
    {"q":"Como a \"elasticidade\" beneficia um design de aplicação?",
     "options":["Reduzindo interdependências entre componentes de aplicação","Escalando automaticamente recursos baseado na demanda","Selecionando o nível de armazenamento correto para sua carga de trabalho","Reservando capacidade para reduzir custo"],
     "correct":[1],"multiple":False},
    {"q":"Qual é o benefício de usar serviços totalmente gerenciados comparado a implantar software de terceiros no EC2?",
     "options":["Você não precisa fazer backup de seus dados","Segurança melhorada","Redução de sobrecarga operacional","Você tem maior controle e flexibilidade"],
     "correct":[2],"multiple":False},
    {"q":"Quais são as cobranças fundamentais para uma instância Amazon EC2? (Selecione DUAS.)",
     "options":["Monitoramento básico","Armazenamento de dados","Tempo de atividade do servidor","AMI","Endereço IP privado"],
     "correct":[1,2],"multiple":True},
    {"q":"Qual serviço AWS usa um dispositivo de armazenamento de hardware altamente seguro para armazenar chaves de criptografia?",
     "options":["AWS CloudHSM","AWS IAM","Amazon Cloud Directory","AWS WAF"],
     "correct":[0],"multiple":False},
    {"q":"Qual tipo de controle de segurança pode ser usado para negar acesso de rede de um endereço IP específico?",
     "options":["AWS Shield","AWS WAF","Network ACL","Security Group"],
     "correct":[2],"multiple":False},
    {"q":"Qual serviço pode ser usado para gerenciar versões de configuração?",
     "options":["AWS Service Catalog","AWS Artifact","Amazon Inspector","AWS Config"],
     "correct":[3],"multiple":False},
    {"q":"Quais aspectos de segurança na AWS são responsabilidades do cliente? (Selecione DUAS.)",
     "options":["Configurar políticas de senha da conta","Controles de acesso físico","Criptografia do lado do servidor","Aplicação de patches em sistemas de armazenamento","Disponibilidade de regiões AWS"],
     "correct":[0,2],"multiple":True},
    {"q":"Quais das seguintes são práticas arquiteturais recomendadas para a AWS Cloud? (Selecione DUAS.)",
     "options":["Implantar em múltiplas Zonas de Disponibilidade","Implantar em uma única zona de disponibilidade","Acoplamento fechado","Projetar para tolerância a falhas","Criar arquiteturas monolíticas"],
     "correct":[0,3],"multiple":True},
    {"q":"Para reduzir o preço de suas instâncias Amazon EC2, quais comprimentos de prazo estão disponíveis para instâncias reservadas? (Selecione DUAS.)",
     "options":["4 anos","1 ano","5 anos","2 anos","3 anos"],
     "correct":[1,4],"multiple":True},
    {"q":"Quais são as cobranças fundamentais para volumes Elastic Block Store (EBS)? (Selecione DUAS.)",
     "options":["A quantidade de armazenamento de dados provisionado","A quantidade de armazenamento de dados consumido","Número de snapshots","IOPS provisionado","Transferência de dados de entrada"],
     "correct":[0,3],"multiple":True},
    {"q":"Qual é o nível de armazenamento Amazon S3 mais econômico para dados que não são acessados frequentemente, mas requerem alta disponibilidade?",
     "options":["Amazon S3 Standard-IA","Amazon S3 Standard","Amazon S3 One Zone-IA","Amazon Glacier"],
     "correct":[0],"multiple":False},
    {"q":"Qual é o principal benefício do princípio de \"acoplamento frouxo\"?",
     "options":["Reduzir complexidade operacional","Reduzir interdependências para que uma falha em um componente não se propague para outros componentes","Automatizar a implantação de infraestrutura usando código","Permitir que aplicações escalem automaticamente baseado na demanda atual"],
     "correct":[1],"multiple":False},
    {"q":"Qual opção de cobrança Amazon EC2 oferece baixo custo, máxima flexibilidade, sem custos antecipados ou compromisso, e você paga apenas pelo que usa?",
     "options":["Dedicated Host","Spot Instances","Reserved Instances","On-Demand Instances"],
     "correct":[3],"multiple":False},
    {"q":"Onde os recursos podem ser lançados ao configurar Amazon EC2 Auto Scaling?",
     "options":["Uma única subnet","Múltiplas AZs dentro de uma região","Múltiplas AZs e múltiplas regiões","Múltiplas VPCs"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço pode ser usado para melhorar a performance para usuários ao redor do mundo?",
     "options":["AWS LightSail","Amazon CloudFront","Amazon Connect","Amazon ElastiCache"],
     "correct":[1],"multiple":False},
    {"q":"Quais dos seguintes são componentes que podem ser configurados na seção VPC do console de gerenciamento AWS? (Selecione DUAS.)",
     "options":["Volumes EBS","Subnet","Endpoints","Registros DNS","Elastic Load Balancer"],
     "correct":[1,2],"multiple":True},
    {"q":"Qual das seguintes é um benefício de mover para a AWS Cloud?",
     "options":["Terceirizar todas as operações de TI","Pagar pelo que você usa","Compras de capital","Compromissos de longo prazo"],
     "correct":[1],"multiple":False},
    {"q":"Além de serviços DNS, quais outros serviços o Amazon Route 53 fornece? (Selecione DUAS.)",
     "options":["DHCP","Cache","Registro de domínio","Roteamento IP","Fluxo de tráfego"],
     "correct":[2,4],"multiple":True},
    {"q":"O que pode ser atribuído a um usuário IAM? (Selecione DUAS.)",
     "options":["Um ID de chave de acesso e chave de acesso secreta","Um certificado SSL/TLS","Um par de chaves","Uma senha para login no Linux","Uma senha para acesso ao console de gerenciamento"],
     "correct":[0,4],"multiple":True},
    {"q":"A política de uso aceitável da AWS para testes de penetração permite?",
     "options":["Clientes realizarem avaliações de segurança ou testes de penetração contra sua infraestrutura AWS sem aprovação prévia para serviços selecionados","Clientes realizarem avaliações de segurança ou testes de penetração contra sua infraestrutura AWS após obter autorização da AWS","A AWS realizar testes de penetração contra recursos do cliente sem notificação","Avaliadores de segurança autorizados realizarem testes de penetração contra qualquer cliente AWS sem autorização"],
     "correct":[0],"multiple":False},
    {"q":"Qual tipo de conexão deve ser usado para conectar um data center local com a nuvem AWS que é alta velocidade, baixa latência e não usa a Internet?",
     "options":["Direct Connect","VPC Endpoints","AWS Managed VPN","Client VPN"],
     "correct":[0],"multiple":False},
    {"q":"Qual das vantagens da nuvem listadas abaixo é mais abordada pelas capacidades do AWS Auto Scaling?",
     "options":["Beneficiar-se de economias de escala massivas","Parar de adivinhar sobre capacidade","Parar de gastar dinheiro executando e mantendo data centers","Ir global em minutos"],
     "correct":[1],"multiple":False},
    {"q":"Qual declaração está correta em relação ao Modelo de Responsabilidade Compartilhada da AWS?",
     "options":["A AWS é responsável pela segurança de regiões e zonas de disponibilidade","Clientes são responsáveis por aplicar patches em sistemas de armazenamento","A AWS é responsável por criptografar dados do cliente","Clientes são responsáveis pela segurança da nuvem"],
     "correct":[0],"multiple":False},
    {"q":"Qual das seguintes é uma vantagem da computação em nuvem comparada a implantar sua própria infraestrutura local?",
     "options":["Flexibilidade para escolher seu próprio hardware","Gastar usando um modelo CAPEX","Pagar apenas pelo que você usa","Capacidade de escolher configurações de infraestrutura personalizadas"],
     "correct":[2],"multiple":False},
    {"q":"Qual serviço pode ser adicionado a um banco de dados para fornecer performance melhorada para algumas solicitações?",
     "options":["Amazon RedShift","Amazon EFS","Amazon ElastiCache","Amazon RDS"],
     "correct":[2],"multiple":False},
    {"q":"Qual serviço pode ser usado para atribuir uma política a um grupo?",
     "options":["AWS IAM","Amazon Cognito","Amazon STS","AWS Shield"],
     "correct":[0],"multiple":False},
    {"q":"Qual serviço AWS permite adicionar registro de usuário, login e controle de acesso a aplicações web e móveis?",
     "options":["AWS Artifact","Amazon Cognito","AWS CloudHSM","AWS Directory Service"],
     "correct":[1],"multiple":False},
    {"q":"Qual é a diferença entre um volume EBS e um Instance store?",
     "options":["Volumes EBS são dispositivos de armazenamento de objeto enquanto volumes Instance store são baseados em bloco","Volumes Instance store são efêmeros enquanto volumes EBS são armazenamento persistente","Volumes Instance store podem ser usados com todos os tipos de instância EC2 enquanto EBS não pode","Volumes EBS são dispositivos de armazenamento em nível de arquivo enquanto volumes Instance store são baseados em objeto"],
     "correct":[1],"multiple":False},
    {"q":"Quais são dois componentes do Amazon S3? (Selecione DUAS.)",
     "options":["Buckets","Diretórios","Objetos","Dispositivos de bloco","Sistemas de arquivos"],
     "correct":[0,2],"multiple":True},
    {"q":"Quais dos seguintes são bons casos de uso para um modelo de preços específico do Amazon EC2? (Selecione DUAS.)",
     "options":["Instâncias reservadas para uso previsível de estado estável","Sob demanda para requisitos regulatórios que não permitem virtualização multi-tenant","Sob demanda para requisitos ad-hoc que não podem ser interrompidos","Spot para carga consistente por um longo prazo","Instâncias reservadas para aplicações com tempos de início e fim flexíveis"],
     "correct":[0,2],"multiple":True},
    {"q":"Quais das seguintes atividades relacionadas à segurança são responsabilidades dos clientes AWS? (Selecione DUAS.)",
     "options":["Descarte seguro de discos rígidos com falha","Implementar controles de acesso do data center","Instalar patches em dispositivos de rede","Instalar patches em sistemas operacionais Windows","Implementar políticas de senha IAM"],
     "correct":[3,4],"multiple":True},
    {"q":"Uma organização tem uma nuvem local e acessa sua AWS Cloud pela Internet. Como eles podem criar uma conexão híbrida privada que evita a internet?",
     "options":["AWS Direct Connect","AWS Managed VPN","AWS VPN CloudHub","AWS VPC Endpoint"],
     "correct":[0],"multiple":False},
    {"q":"Qual equipe está disponível para apoiar clientes AWS em um plano de suporte Enterprise com problemas de conta?",
     "options":["AWS Technical Support","AWS Billing and Accounts","AWS Concierge","AWS Technical Account Manager"],
     "correct":[2],"multiple":False},
    {"q":"Quais são dois exemplos das vantagens da computação em nuvem? (Selecione DUAS.)",
     "options":["Aumentar velocidade e agilidade","Trocar custos operacionais por custos de capital","Data centers seguros","Beneficiar-se de economias de escala massivas","Trocar despesa variável por despesa de capital"],
     "correct":[0,3],"multiple":True},
    {"q":"Qual das seguintes é uma prática arquitetural recomendada pela AWS?",
     "options":["Projetar para sucesso","Projetar para falha","Pensar em servidores, não serviços","Usar processos operacionais manuais"],
     "correct":[1],"multiple":False},
    {"q":"Qual é o escopo de uma Amazon Virtual Private Cloud (VPC)?",
     "options":["Ela abrange um único bloco CIDR","Ela abrange todas as Zonas de Disponibilidade dentro de uma região","Ela abrange múltiplas subnets","Ela abrange todas as Zonas de Disponibilidade em todas as regiões"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço AWS permite automatizar a avaliação de configurações gravadas contra configuração desejada?",
     "options":["AWS OpsWorks","AWS Service Catalog","AWS CloudFormation","AWS Config"],
     "correct":[3],"multiple":False},
    {"q":"Quais das opções abaixo são recomendações no pilar de confiabilidade do framework bem arquitetado? (Selecione DUAS.)",
     "options":["Testar procedimentos de recuperação","Recuperar manualmente de falhas","Gerenciar mudanças em processos manuais","Parar de adivinhar sobre capacidade","Escalar verticalmente usando sistemas grandes"],
     "correct":[0,3],"multiple":True},
    {"q":"Qual tipo de armazenamento pode ser montado usando o protocolo NFS para muitas instâncias EC2 simultaneamente?",
     "options":["Amazon Instance Store","Amazon EBS","Amazon S3","Amazon EFS"],
     "correct":[3],"multiple":False},
    {"q":"Qual tipo de implantação Amazon RDS é melhor usado para habilitar tolerância a falhas no caso de falha de uma zona de disponibilidade?",
     "options":["Múltiplas Regiões","Read Replicas","Write Replicas","Múltiplas Zonas de Disponibilidade"],
     "correct":[3],"multiple":False},
    {"q":"Qual recurso do AWS IAM permite identificar permissões desnecessárias que foram atribuídas a usuários?",
     "options":["Role Advisor","Access Advisor","Permissions Advisor","Group Advisor"],
     "correct":[1],"multiple":False},
    {"q":"Quais tipos de monitoramento o Amazon CloudWatch pode ser usado? (Selecione DUAS.)",
     "options":["Infraestrutura","Data center","Saúde operacional","Acesso à API","Performance da aplicação"],
     "correct":[2,4],"multiple":True},
    {"q":"Qual serviço AWS permite armazenamento híbrido entre local e a AWS Cloud?",
     "options":["Amazon S3 Cross Region Replication (CRR)","AWS Storage Gateway","Amazon Elastic File System (EFS)","Amazon CloudFront"],
     "correct":[1],"multiple":False},
    {"q":"O que uma organização precisa fazer para mover para outra região AWS?",
     "options":["Apenas começar a implantar recursos na região adicional","Criar uma conta IAM separada para essa região","Aplicar para outra conta AWS nessa região","Enviar uma aplicação para estender sua conta para a região adicional"],
     "correct":[0],"multiple":False},
    {"q":"Qual serviço de Computação deve ser usado para executar um sistema operacional Linux no qual você instalará software personalizado?",
     "options":["Amazon EC2","Amazon ECS","Amazon EKS","AWS Lambda"],
     "correct":[0],"multiple":False},
    {"q":"Quais dos seguintes precisam ser incluídos em uma análise de custo total de propriedade (TCO)? (Selecione DUAS.)",
     "options":["Salário do Gerente de TI","Instalação de equipamentos de instalação","Desenvolvimento de aplicação","Marketing da empresa","Custos de segurança do data center"],
     "correct":[1,4],"multiple":True},
    {"q":"O que uma organização precisa fazer no Amazon IAM para habilitar acesso de usuário a serviços sendo lançados em nova região?",
     "options":["Nada, IAM é global","Habilitar modo global no IAM para provisionar o acesso necessário","Atualizar as contas de usuário para permitir acesso de outra região","Criar novas contas de usuário na nova região"],
     "correct":[0],"multiple":False},
    {"q":"Qual declaração é verdadeira em relação aos dados armazenados dentro de uma Região AWS?",
     "options":["Dados não são replicados fora de uma região a menos que você configure","Dados são sempre replicados para outra região","Dados são automaticamente arquivados após 90 dias","Dados são sempre automaticamente replicados para pelo menos uma outra zona de disponibilidade"],
     "correct":[0],"multiple":False},
    {"q":"Uma organização tem múltiplas contas AWS e usa uma mistura de instâncias sob demanda e reservadas. Uma conta tem uma quantidade considerável de instâncias reservadas não utilizadas. Como a organização pode reduzir seus custos? (Selecione DUAS.)",
     "options":["Criar uma configuração de AWS Organization vinculando as contas","Usar instâncias Spot em vez disso","Resgatar suas instâncias reservadas","Configurar cobrança consolidada entre as contas","Mudar para usar grupos de posicionamento"],
     "correct":[0,3],"multiple":True}
]

SIMULADO_5 = [
    {"q":"Qual serviço AWS pode ser usado para preparar e carregar dados para análise usando um processo de extração, transformação e carregamento (ETL)?",
     "options":["AWS Lambda","AWS Glue","Amazon EMR","Amazon Athena"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço AWS pode ser usado para enviar notificações automatizadas para endpoints HTTP?",
     "options":["Amazon SQS","Amazon SWF","Amazon SNS","Amazon SES"],
     "correct":[2],"multiple":False},
    {"q":"Quais das seguintes constituem os cinco pilares do AWS Well-Architected Framework? (Selecione DUAS.)",
     "options":["Excelência operacional, segurança e confiabilidade","Excelência operacional, elasticidade e escalabilidade","Priorização de custos e otimização de custos","Consistência de dados e otimização de custos","Eficiência de performance e otimização de custos"],
     "correct":[0,4],"multiple":True},
    {"q":"Assumindo que você os configurou corretamente, quais serviços AWS podem escalar automaticamente sem intervenção? (Selecione DUAS.)",
     "options":["Amazon RDS","Amazon EC2","Amazon S3","Amazon DynamoDB","Amazon EBS"],
     "correct":[2,3],"multiple":True},
    {"q":"Quais componentes AWS auxiliam na construção de aplicações tolerantes a falhas? (Selecione DUAS.)",
     "options":["Endereços IP Elásticos","ARNs","AMIs","Tags","Mapeamentos de dispositivos de bloco"],
     "correct":[0,2],"multiple":True},
    {"q":"Uma empresa quer utilizar um modelo de nuvem pay-as-you-go para todas as suas aplicações sem custos CAPEX e que seja altamente elástico. Qual modelo de entrega de nuvem será mais adequado?",
     "options":["Pública","Privada","Híbrida","Local"],
     "correct":[0],"multiple":False},
    {"q":"Quais das seguintes são vantagens de usar a computação em nuvem AWS sobre TI legada? (Selecione DUAS.)",
     "options":["Você pode passar a responsabilidade pela disponibilidade de sua aplicação para a AWS","Você não precisa se preocupar com superprovisionamento pois pode escalar elasticamente","Você não precisa aplicar patches em seus sistemas operacionais","Você pode trazer novas aplicações para o mercado mais rapidamente","Você pode trazer serviços mais próximos de seus usuários finais"],
     "correct":[1,3],"multiple":True},
    {"q":"Quais serviços AWS formam os serviços voltados para aplicação da infraestrutura serverless da AWS? (Selecione DUAS.)",
     "options":["AWS Step Functions","AWS Lambda","Amazon API Gateway","Amazon DynamoDB","Amazon EFS"],
     "correct":[1,2],"multiple":True},
    {"q":"Qual é o nome do serviço de registro Docker gerenciado pela AWS usado pelo Amazon Elastic Container Service (ECS)?",
     "options":["Elastic Container Registry","ECS Container Registry","Docker Container Registry","Docker Image Repository"],
     "correct":[0],"multiple":False},
    {"q":"Quais são dois benefícios de usar AWS Lambda? (Selecione DUAS.)",
     "options":["Nenhum servidor para gerenciar","Snapshots integrados","Escalabilidade contínua (escalar horizontalmente)","Escolhas flexíveis de sistema operacional","Software de código aberto"],
     "correct":[0,2],"multiple":True},
    {"q":"Com qual serviço um desenvolvedor pode fazer upload de código usando um arquivo ZIP ou WAR e ter o serviço lidar com a implantação end-to-end dos recursos?",
     "options":["AWS CodeDeploy","AWS Elastic Beanstalk","Amazon ECS","AWS CodeCommit"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço você pode usar para monitorar, armazenar e acessar arquivos de log gerados por instâncias EC2 e servidores locais?",
     "options":["AWS CloudTrail","AWS OpsWorks","Amazon CloudWatch Logs","Amazon Kinesis"],
     "correct":[2],"multiple":False},
    {"q":"Quais ofertas estão incluídas no conjunto de produtos Amazon Lightsail? (Selecione DUAS.)",
     "options":["Servidor Privado Virtual","Banco de dados NoSQL","Banco de dados MySQL gerenciado","Armazenamento de objetos","Funções serverless"],
     "correct":[0,2],"multiple":True},
    {"q":"Qual serviço AWS faz parte do conjunto de serviços \"serverless\" e executa código como funções?",
     "options":["Amazon ECS","Amazon EKS","AWS Lambda","AWS CodeCommit"],
     "correct":[2],"multiple":False},
    {"q":"Para recompensar clientes por usar seus serviços, quais são duas maneiras que a AWS reduz preços? (Selecione DUAS.)",
     "options":["Descontos baseados em volume quando você usa mais serviços","Redução nas cobranças de transferência de dados de entrada","Custo reduzido para capacidade reservada","Descontos por usar uma variedade maior de serviços","Remoção de taxas de rescisão para clientes que gastam mais"],
     "correct":[0,2],"multiple":True},
    {"q":"Qual tipo de backup automatizado do Amazon RDS permite restaurar o banco de dados com granularidade de apenas 5 minutos?",
     "options":["Backup de snapshot","Backup completo","Backup incremental","Recuperação point-in-time"],
     "correct":[3],"multiple":False},
    {"q":"Qual recurso do DynamoDB fornece aceleração em memória para tabelas que resultam em melhorias significativas de performance?",
     "options":["Amazon ElastiCache","Amazon DynamoDB Accelerator (DAX)","Amazon EFS","Amazon CloudFront"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço AWS permite que dispositivos conectados interajam facilmente e com segurança com aplicações em nuvem e outros dispositivos?",
     "options":["Amazon Workspaces","AWS Directory Service","AWS IoT Core","AWS Server Migration Service (SMS)"],
     "correct":[2],"multiple":False},
    {"q":"Qual serviço AWS permite que desenvolvedores e cientistas de dados construam, treinem e implantem modelos de machine learning?",
     "options":["Amazon Rekognition","Amazon Comprehend","Amazon SageMaker","Amazon MQ"],
     "correct":[2],"multiple":False},
    {"q":"Qual serviço fornece alertas e orientação de remediação quando a AWS está experimentando eventos que podem impactá-lo?",
     "options":["AWS Trusted Advisor","AWS Inspector","AWS Personal Health Dashboard","AWS Shield"],
     "correct":[2],"multiple":False},
    {"q":"Quais são os benefícios primários de usar AWS Elastic Load Balancing? (Selecione DUAS.)",
     "options":["Alta disponibilidade","Elasticidade","Automação","Cache","Resiliência regional"],
     "correct":[0,1],"multiple":True},
    {"q":"O que é uma Edge location?",
     "options":["Um endpoint público para Amazon S3","Um endpoint de rede de entrega de conteúdo (CDN) para CloudFront","Um gateway privado virtual para VPN","Um endpoint de conexão de peering VPC"],
     "correct":[1],"multiple":False},
    {"q":"Qual é a relação entre subnets e zonas de disponibilidade?",
     "options":["Você pode criar uma ou mais subnets dentro de cada zona de disponibilidade","Subnets abrangem múltiplas zonas de disponibilidade","Você pode criar uma subnet por zona de disponibilidade","Subnets contêm uma ou mais zonas de disponibilidade"],
     "correct":[0],"multiple":False},
    {"q":"Como você pode configurar Amazon Route 53 para monitorar a saúde e performance de sua aplicação?",
     "options":["Usando consultas DNS","Usando verificações de saúde do Route 53","Usando a API do Route 53","Usando CloudWatch"],
     "correct":[1],"multiple":False},
    {"q":"Um desenvolvedor precisa de uma forma de provisionar automaticamente uma coleção de recursos AWS. Qual serviço AWS é usado principalmente para implantar infraestrutura como código?",
     "options":["AWS Elastic Beanstalk","AWS CloudFormation","AWS CodeDeploy","Jenkins"],
     "correct":[1],"multiple":False},
    {"q":"Como uma empresa pode conectar de sua rede local para VPCs em múltiplas regiões usando conexões privadas?",
     "options":["AWS Managed VPN","AWS Direct Connect Gateway","Amazon CloudFront","Inter-Region VPC Peering"],
     "correct":[1],"multiple":False},
    {"q":"Qual das seguintes descrições está incorreta em relação ao design das Zonas de Disponibilidade?",
     "options":["AZs têm conexões de rede diretas, de baixa latência, alta taxa de transferência e redundantes entre si","Cada AZ é projetada como uma zona de falha independente","AZs são fisicamente separadas dentro de uma região metropolitana típica e estão localizadas em planícies de inundação de baixo risco","Cada subnet em uma VPC é mapeada para todas as AZs na região"],
     "correct":[3],"multiple":False},
    {"q":"Ao projetar uma VPC, qual é o propósito de um Internet Gateway?",
     "options":["Fornece acesso à Internet para instâncias EC2 em subnets privadas","Habilita comunicações de Internet para instâncias em subnets públicas","É um host bastião para conexões de gerenciamento de entrada","É usado para fazer conexões VPN para uma VPC"],
     "correct":[1],"multiple":False},
    {"q":"Qual é o nome do portal online de autoatendimento que a AWS fornece para permitir que clientes visualizem relatórios e aceitem acordos?",
     "options":["AWS Compliance Portal","AWS Documentation Portal","AWS Artifact","AWS DocuFact"],
     "correct":[2],"multiple":False},
    {"q":"Quais são duas declarações corretas sobre AWS Organizations com cobrança consolidada? (Selecione DUAS.)",
     "options":["Múltiplas contas são fornecidas por organização","Uma conta fornecida para múltiplas contas","Contas vinculadas perdem sua independência de gerenciamento","Descontos de preços de volume aplicados em múltiplas contas","CloudTrail pode ser configurado por organização"],
     "correct":[1,3],"multiple":True},
    {"q":"Qual prática recomendada do AWS IAM recomenda aplicar as permissões mínimas necessárias para executar uma tarefa ao criar políticas IAM?",
     "options":["Criar usuários IAM individuais","Usar roles para delegar permissões","Conceder privilégio mínimo","Habilitar MFA para usuários privilegiados"],
     "correct":[2],"multiple":False},
    {"q":"Quais são os benefícios de usar roles IAM para aplicações que executam em instâncias EC2? (Selecione DUAS.)",
     "options":["Mais fácil de configurar do que armazenar chaves de acesso dentro da instância EC2","Mais seguro do que armazenar chaves de acesso dentro de aplicações","Pode aplicar múltiplas roles a uma única instância","É mais fácil gerenciar roles IAM","Credenciais de role são permanentes"],
     "correct":[1,3],"multiple":True},
    {"q":"Sob o Modelo de Responsabilidade Compartilhada da AWS, qual das seguintes NÃO é responsabilidade do cliente?",
     "options":["Adicionar regras de firewall a security groups e network ACLs","Aplicar criptografia a dados armazenados em um volume EBS","Aplicar políticas de bucket para compartilhar dados Amazon S3","Instalar atualizações de firmware em servidores host"],
     "correct":[3],"multiple":False},
    {"q":"Qual tipo de armazenamento armazena objetos compostos de pares chave-valor?",
     "options":["Amazon DynamoDB","Amazon EBS","Amazon EFS","Amazon S3"],
     "correct":[3],"multiple":False},
    {"q":"Quais tipos de volumes EBS podem ser criptografados?",
     "options":["Apenas volumes não-raiz","Tanto volumes não-raiz quanto raiz","Apenas volumes não-raiz criados de snapshots","Apenas volumes raiz podem ter criptografia aplicada no momento do lançamento"],
     "correct":[1],"multiple":False},
    {"q":"Qual recurso do Amazon S3 permite definir regras para transferir automaticamente objetos entre diferentes classes de armazenamento em intervalos de tempo definidos?",
     "options":["Elastic Data Management","Object Lifecycle Management","Auto Lifecycle Scaling","S3 Archiving"],
     "correct":[1],"multiple":False},
    {"q":"Quais cobranças são aplicáveis à classe de armazenamento Amazon S3 Standard? (Selecione DUAS.)",
     "options":["Taxa de armazenamento por GB/mês","Taxa de recuperação","Cobrança de capacidade mínima por objeto","Ingresso de dados","Egresso de dados"],
     "correct":[0,4],"multiple":True},
    {"q":"Como uma empresa pode proteger seus dados Amazon S3 de um desastre regional?",
     "options":["Arquivar para Amazon Glacier","Usar Cross-Region Replication (CRR) para copiar para outra região","Usar ações de lifecycle para mover para outra classe de armazenamento S3","Habilitar Multi-Factor Authentication (MFA) delete"],
     "correct":[1],"multiple":False},
    {"q":"Qual plano de suporte AWS fornece suporte apenas por email por Cloud Support Associates?",
     "options":["Basic","Developer","Business","Enterprise"],
     "correct":[1],"multiple":False},
    {"q":"Qual plano de suporte é a opção de menor custo que permite casos ilimitados serem abertos?",
     "options":["Basic","Developer","Business","Enterprise"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço permite que uma organização traga suas próprias licenças em hardware host que está fisicamente isolado de outras contas AWS?",
     "options":["EC2 Dedicated Instances","EC2 Spot Instances","EC2 Dedicated Hosts","EC2 Reserved Instances"],
     "correct":[2],"multiple":False},
    {"q":"Qual das seguintes é um exemplo de otimização para custo?",
     "options":["Escolher a instância EC2 mais rápida para garantir performance","Provisionar capacidade extra para permitir crescimento","Substituir uma instância de computação EC2 por AWS Lambda","Implantar recursos com AWS CloudFormation"],
     "correct":[2],"multiple":False},
    {"q":"Qual serviço é usado para cache de dados?",
     "options":["Amazon Simple Queue Service (SQS)","Amazon DynamoDB DAX","AWS Key Management Service (KMS)","Amazon Elastic File System (EFS)"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço é usado para introduzir tolerância a falhas em uma arquitetura de aplicação?",
     "options":["Amazon CloudFront","Amazon ElastiCache","Amazon Elastic Load Balancing","Amazon DynamoDB"],
     "correct":[2],"multiple":False},
    {"q":"Quais ferramentas você pode usar para gerenciar identidades no IAM? (escolha 2)",
     "options":["Amazon CloudWatch API","AWS Management Console","AWS Command Line Tools","EC2 Management Console","Amazon Workspaces"],
     "correct":[1,2],"multiple":True},
    {"q":"Quais das seguintes seriam boas razões para mover de local para a AWS Cloud? (Selecione DUAS.)",
     "options":["Ganhar acesso a serviços de suporte técnico gratuitos","Reduzir custos através de right-sizing mais fácil de cargas de trabalho","Melhorar agilidade e elasticidade","Ganhar gerenciamento operacional end-to-end de toda a pilha de infraestrutura","Terceirizar toda a responsabilidade de segurança"],
     "correct":[1,2],"multiple":True},
    {"q":"Qual serviço executa seu código de aplicação apenas quando necessário sem precisar executar servidores?",
     "options":["Amazon EC2","Amazon ECS","AWS Lambda","AWS LightSail"],
     "correct":[2],"multiple":False},
    {"q":"Qual recurso do Amazon EC2 permite que um administrador crie uma imagem padronizada que pode ser usada para lançar novas instâncias?",
     "options":["Amazon Golden Image","Amazon Block Template","Amazon Machine Image","Amazon EBS Mount Point"],
     "correct":[2],"multiple":False},
    {"q":"Que informação deve ser inserida na Calculadora TCO da AWS?",
     "options":["O número de usuários finais em sua empresa","O número de aplicações em sua empresa","O número de sistemas de armazenamento em sua empresa","O número de servidores em sua empresa"],
     "correct":[3],"multiple":False},
    {"q":"Um Endereço IP Elástico pode ser remapeado entre instâncias EC2 através de quais limites?",
     "options":["Regiões","Edge Locations","Zonas de Disponibilidade","DB Subnets"],
     "correct":[2],"multiple":False},
    {"q":"Qual serviço AWS pode auxiliar fornecendo ações recomendadas sobre otimização de custos?",
     "options":["AWS Inspector","AWS Trusted Advisor","AWS Artifact","Amazon CloudWatch Events"],
     "correct":[1],"multiple":False},
    {"q":"Como uma empresa de educação online pode garantir que seus cursos de vídeo reproduzam com latência mínima para seus usuários ao redor do mundo?",
     "options":["Usar Amazon S3 Transfer Acceleration para acelerar downloads","Usar Amazon EBS Cross Region Replication para levar o conteúdo próximo aos usuários","Usar Amazon Aurora Global Database","Usar Amazon CloudFront para levar o conteúdo mais próximo aos usuários"],
     "correct":[3],"multiple":False},
    {"q":"Qual serviço de segurança AWS fornece um firewall no nível de subnet dentro de uma VPC?",
     "options":["Security Group","IAM Policy","Bucket Policy","Network Access Control List"],
     "correct":[3],"multiple":False},
    {"q":"Quais serviços permitem que você armazene arquivos na AWS? (Selecione DUAS.)",
     "options":["AWS Lambda","Amazon LightSail","Amazon EBS","Amazon EFS","Amazon SQS"],
     "correct":[2,3],"multiple":True},
    {"q":"Qual programa AWS pode ajudar uma organização a projetar, construir e gerenciar suas cargas de trabalho na AWS?",
     "options":["APN Consulting Partners","APN Technology Consultants","AWS Business Development Manager","AWS Technical Account Manager"],
     "correct":[0],"multiple":False},
    {"q":"Qual das seguintes declarações está correta sobre replicação cross-region do Amazon S3?",
     "options":["Tanto o bucket de origem quanto o de destino S3 devem ter versionamento desabilitado","Os buckets S3 de origem e destino não podem estar em diferentes Regiões AWS","Buckets S3 configurados para replicação cross-region podem ser propriedade de uma única conta AWS ou de contas diferentes","O proprietário do bucket S3 de origem deve ter as Regiões AWS de origem e destino desabilitadas para sua conta"],
     "correct":[2],"multiple":False},
    {"q":"Qual dos seguintes modelos de preços Amazon EC2 permite que clientes usem licenças de software vinculadas a servidor existentes?",
     "options":["Spot Instances","Reserved Instances","Dedicated Hosts","On-Demand Instances"],
     "correct":[2],"multiple":False},
    {"q":"Uma empresa implantou vários bancos de dados relacionais no Amazon RDS. Todo mês, o fornecedor do software de banco de dados libera novos patches de segurança que precisam ser aplicados ao banco de dados. Qual é a maneira MAIS eficiente de aplicar os patches de segurança?",
     "options":["Conectar a cada instância de banco de dados mensalmente e baixar e aplicar os patches de segurança necessários do fornecedor","Habilitar patching automático para as instâncias usando o console Amazon RDS","No AWS Config, configurar uma regra para as instâncias e o nível de patch necessário","Usar AWS Systems Manager para automatizar patching de banco de dados de acordo com um cronograma"],
     "correct":[1],"multiple":False},
    {"q":"Um Cloud Practitioner precisa implantar rapidamente uma solução de TI popular e começar a usá-la imediatamente. O que o Cloud Practitioner deve usar?",
     "options":["Documentação do AWS Well-Architected Framework","Amazon CloudFront","AWS Elastic Beanstalk","AWS Quick Start reference deployments"],
     "correct":[3],"multiple":False},
    {"q":"Um praticante de nuvem precisa diminuir a latência da aplicação e aumentar a performance para usuários globalmente distribuídos. Quais serviços podem auxiliar? (Selecione DUAS.)",
     "options":["Amazon ECS","Amazon S3","Amazon AppStream 2.0","Amazon ElastiCache","Amazon CloudFront"],
     "correct":[1,4],"multiple":True},
    {"q":"Uma empresa precisa de proteção contra ataques de negação de serviço distribuído (DDoS) em seu site e assistência de especialistas da AWS durante tais eventos. Qual serviço gerenciado da AWS atenderá esses requisitos?",
     "options":["AWS Shield Advanced","AWS Firewall Manager","AWS Web Application Firewall","Amazon GuardDuty"],
     "correct":[0],"multiple":False},
    {"q":"Quais das seguintes devem ser usadas juntas para obter acesso programático a uma conta AWS? (Selecione DUAS.)",
     "options":["Um ID de chave de acesso","Uma chave primária","Uma chave de acesso secreta","Um ID de usuário","Uma chave secundária"],
     "correct":[0,2],"multiple":True},
    {"q":"Uma aplicação que é implantada em múltiplas Zonas de Disponibilidade pode ser descrita como:",
     "options":["Sendo altamente disponível","Tendo alcance global","Sendo segura","Tendo elasticidade"],
     "correct":[0],"multiple":False},
    {"q":"Um Cloud Practitioner está desenvolvendo um plano de recuperação de desastres e pretende replicar dados entre múltiplas áreas geográficas. Qual das seguintes atende esses requisitos?",
     "options":["Contas AWS","Regiões AWS","Zonas de Disponibilidade","Edge locations"],
     "correct":[1],"multiple":False},
    {"q":"Um usuário implanta uma instância de banco de dados Amazon Aurora em múltiplas Zonas de Disponibilidade. Esta estratégia envolve qual pilar do AWS Well-Architected Framework?",
     "options":["Eficiência de performance","Confiabilidade","Otimização de custos","Segurança"],
     "correct":[1],"multiple":False}
]

SIMULADO_6 = [
    {"q":"As ferramentas de Gerenciamento de Custos da AWS dão aos usuários a capacidade de fazer qual das seguintes? (Selecione DUAS.)",
     "options":["Encerrar todos os recursos AWS automaticamente se os limites de orçamento forem excedidos","Quebrar custos AWS por dia, serviço e conta AWS vinculada","Criar orçamentos e receber notificações se o uso atual ou previsto exceder os orçamentos","Alternar automaticamente para Reserved Instances ou Spot Instances, o que for mais econômico","Mover dados armazenados no Amazon S3 para uma classe de armazenamento mais econômica"],
     "correct":[1,2],"multiple":True},
    {"q":"Qual serviço ou recurso AWS ajuda a restringir o serviço AWS, recursos e ações de API individuais que usuários e roles em cada conta membro podem acessar?",
     "options":["Amazon Cognito","AWS Organizations","AWS Shield","AWS Firewall Manager"],
     "correct":[1],"multiple":False},
    {"q":"Sob o modelo de responsabilidade compartilhada, quais das seguintes tarefas são responsabilidade do cliente AWS? (Selecione DUAS.)",
     "options":["Garantir que dados de aplicação sejam criptografados em repouso","Garantir que servidores NTP da AWS estejam configurados com o horário correto","Garantir que usuários tenham recebido treinamento de segurança no uso de serviços AWS","Garantir que o acesso aos data centers seja restrito","Garantir que o hardware seja descartado adequadamente"],
     "correct":[0,2],"multiple":True},
    {"q":"Sob o modelo de responsabilidade compartilhada da AWS, quais das seguintes são responsabilidades do cliente? (Selecione DUAS.)",
     "options":["Configurar criptografia do lado do servidor em um bucket Amazon S3","Aplicação de patches em instâncias Amazon RDS","Configurações de rede e firewall","Segurança física das instalações do data center","Disponibilidade de capacidade de computação"],
     "correct":[0,2],"multiple":True},
    {"q":"Uma aplicação web executando na AWS recebeu solicitações maliciosas do mesmo conjunto de endereços IP. Qual serviço AWS pode ajudar a proteger a aplicação e bloquear o tráfego malicioso?",
     "options":["AWS IAM","Amazon GuardDuty","Amazon SNS","AWS WAF"],
     "correct":[3],"multiple":False},
    {"q":"Qual serviço AWS fornece a capacidade de detectar vazamentos inadvertidos de dados de informações pessoalmente identificáveis (PII) e dados de credenciais de usuário?",
     "options":["Amazon GuardDuty","Amazon Inspector","Amazon Macie","AWS Shield"],
     "correct":[2],"multiple":False},
    {"q":"De acordo com o AWS Well-Architected Framework, quais etapas de gerenciamento de mudanças devem ser tomadas para alcançar confiabilidade na AWS Cloud? (Selecione DUAS.)",
     "options":["Usar AWS Config para gerar um inventário de recursos AWS","Usar limites de serviço para impedir que usuários criem ou façam mudanças em recursos AWS","Usar AWS CloudTrail para registrar chamadas de API AWS em um arquivo de log auditável","Usar AWS Certificate Manager para criar um catálogo de serviços aprovados","Usar Amazon GuardDuty para registrar atividade de API em um bucket S3"],
     "correct":[0,2],"multiple":True},
    {"q":"Qual das seguintes atua como um firewall virtual no nível da instância Amazon EC2 para controlar tráfego para uma ou mais instâncias?",
     "options":["Tabela de rotas","Gateways privados virtuais (VPG)","Security groups","Network Access Control Lists (ACL)"],
     "correct":[2],"multiple":False},
    {"q":"Quais princípios de design da AWS Cloud podem ajudar a aumentar a confiabilidade? (Selecione DUAS.)",
     "options":["Usar arquitetura monolítica","Medir eficiência geral","Testar procedimentos de recuperação","Adotar um modelo de consumo","Recuperar automaticamente de falhas"],
     "correct":[2,4],"multiple":True},
    {"q":"Qual modelo de preços interromperá uma instância Amazon EC2 em execução se a capacidade se tornar temporariamente indisponível?",
     "options":["On-Demand Instances","Standard Reserved Instances","Spot Instances","Convertible Reserved Instances"],
     "correct":[2],"multiple":False},
    {"q":"Qual das seguintes declarações sobre o modelo de preços pay-as-you-go da AWS está correta?",
     "options":["Resulta em redução de despesas de capital","Requer pagamento antecipado para serviços AWS","É relevante apenas para Amazon EC2, Amazon S3 e Amazon DynamoDB","Reduz despesas operacionais"],
     "correct":[0],"multiple":False},
    {"q":"Qual serviço AWS pode servir um site estático?",
     "options":["Amazon S3","Amazon Route 53","Amazon QuickSight","AWS X-Ray"],
     "correct":[0],"multiple":False},
    {"q":"Uma startup de eCommerce precisa entregar rapidamente novos recursos de site de forma iterativa, minimizando o tempo para o mercado. Qual recurso da AWS Cloud permite isso?",
     "options":["Elasticidade","Alta disponibilidade","Agilidade","Confiabilidade"],
     "correct":[2],"multiple":False},
    {"q":"Qual é a maneira mais eficiente de estabelecer conectividade de rede de local para múltiplas VPCs em diferentes Regiões AWS?",
     "options":["Usar AWS Direct Connect","Usar AWS VPN","Usar AWS Client VPN","Usar um AWS Transit Gateway"],
     "correct":[3],"multiple":False},
    {"q":"Uma empresa está usando AWS CLI e acesso programático de recursos AWS de sua rede local. Qual é um requisito obrigatório neste cenário?",
     "options":["Usar uma conexão AWS Direct Connect","Usar uma chave de acesso AWS e uma chave secreta","Usar Amazon API Gateway","Usar um par de chaves Amazon EC2"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço AWS é adequado para uma carga de trabalho orientada a eventos?",
     "options":["Amazon EC2","AWS Elastic Beanstalk","AWS Lambda","Amazon Lumberyard"],
     "correct":[2],"multiple":False},
    {"q":"Com base no modelo de responsabilidade compartilhada, qual das seguintes tarefas de segurança e conformidade é responsabilidade da AWS?",
     "options":["Conceder acesso a indivíduos e serviços","Criptografar dados em trânsito","Atualizar firmware do host Amazon EC2","Atualizar sistemas operacionais"],
     "correct":[2],"multiple":False},
    {"q":"Qual serviço AWS pode ser usado para executar containers Docker?",
     "options":["AWS Lambda","Amazon ECR","AWS Fargate","Amazon AMI"],
     "correct":[2],"multiple":False},
    {"q":"Qual tipo de Elastic Load Balancer opera no nível de conexão TCP?",
     "options":["Application Load Balancer (ALB)","Network Load Balancer (NLB)","Classic Load Balancer (CLB)","Amazon Route 53 Load Balancer"],
     "correct":[1],"multiple":False},
    {"q":"Qual tecnologia AWS pode ser referida como um \"disco rígido virtual na nuvem\"?",
     "options":["Amazon EFS Filesystem","Amazon S3 Bucket","Amazon EBS volume","Amazon ENI"],
     "correct":[2],"multiple":False},
    {"q":"De que maneiras o modelo de preços da AWS beneficia organizações?",
     "options":["Elimina custos de licenciamento","Foca gastos em despesas de capital, em vez de despesas operacionais","Reduz o custo de manter recursos ociosos","Reduz o custo de pessoas de desenvolvimento de aplicações"],
     "correct":[2],"multiple":False},
    {"q":"Qual serviço permite monitorar e solucionar problemas de sistemas usando arquivos de log de sistema e aplicação gerados por esses sistemas?",
     "options":["CloudTrail Logs","CloudWatch Metrics","CloudWatch Logs","CloudTrail Metrics"],
     "correct":[2],"multiple":False},
    {"q":"De acordo com o Modelo de Responsabilidade Compartilhada da AWS, qual das seguintes é um controle compartilhado?",
     "options":["Aplicação de patches do sistema operacional","Conscientização e treinamento","Proteção da infraestrutura","Criptografia de dados do lado do cliente"],
     "correct":[1],"multiple":False},
    {"q":"Onde as contas Amazon Identity and Access Management (IAM) precisam ser criadas para uma organização global?",
     "options":["Em cada região onde os usuários estão localizados","Apenas criá-las uma vez, pois IAM é um serviço global","Criá-las globalmente e depois replicá-las regionalmente","Em cada área geográfica onde os usuários estão localizados"],
     "correct":[1],"multiple":False},
    {"q":"Qual é o nome do contêiner de nível superior usado para manter objetos dentro do Amazon S3?",
     "options":["Pasta","Diretório","Instance Store","Bucket"],
     "correct":[3],"multiple":False},
    {"q":"Quais das seguintes são exemplos de escalonamento horizontal? (Selecione DUAS.)",
     "options":["Adicionar mais CPU/RAM a instâncias existentes conforme a demanda aumenta","Adicionar mais instâncias conforme a demanda aumenta","Requer reinicialização para escalar para cima ou para baixo","Escalonamento automático usando serviços como AWS Auto Scaling","A escalabilidade é limitada pelo tamanho máximo da instância"],
     "correct":[1,3],"multiple":True},
    {"q":"Qual recurso você deve usar para acessar relatórios de segurança e conformidade da AWS?",
     "options":["AWS Artifact","AWS Business Associate Addendum (BAA)","AWS IAM","AWS Organizations"],
     "correct":[0],"multiple":False},
    {"q":"Quais métodos estão disponíveis para escalar um banco de dados Amazon RDS? (Selecione DUAS.)",
     "options":["Você pode escalar verticalmente movendo para um tamanho de instância maior","Você pode escalar horizontalmente automaticamente com EC2 Auto Scaling","Você pode escalar verticalmente aumentando a capacidade de armazenamento","Você pode escalar horizontalmente implementando Elastic Load Balancing","Você pode escalar verticalmente automaticamente usando AWS Auto Scaling"],
     "correct":[0,2],"multiple":True},
    {"q":"Qual tipo de escalonamento o Amazon EC2 Auto Scaling fornece?",
     "options":["Vertical","Linear","Horizontal","Incremental"],
     "correct":[2],"multiple":False},
    {"q":"Qual recurso do Amazon S3 permite criar regras para controlar a transferência de objetos entre diferentes classes de armazenamento?",
     "options":["Object sharing","Versioning","Lifecycle management","Bucket policies"],
     "correct":[2],"multiple":False},
    {"q":"Como um administrador de banco de dados pode reduzir sobrecarga operacional para um banco de dados MySQL?",
     "options":["Migrar o banco de dados para uma instância EC2","Migrar o banco de dados para AWS Lambda","Usar AWS CloudFormation para gerenciar operações","Migrar o banco de dados para uma instância Amazon RDS"],
     "correct":[3],"multiple":False},
    {"q":"Qual serviço de banco de dados AWS é sem esquema e pode ser escalado dinamicamente sem incorrer em tempo de inatividade?",
     "options":["Amazon RDS","Amazon Aurora","Amazon RedShift","Amazon DynamoDB"],
     "correct":[3],"multiple":False},
    {"q":"Qual tipo de banco de dados AWS é idealmente adequado para análise usando consultas SQL?",
     "options":["Amazon DynamoDB","Amazon RedShift","Amazon RDS","Amazon S3"],
     "correct":[1],"multiple":False},
    {"q":"Qual serviço AWS é projetado para ser usado para análise operacional?",
     "options":["Amazon EMR","Amazon Athena","Amazon QuickSight","Amazon Elasticsearch Service"],
     "correct":[3],"multiple":False},
    {"q":"Você precisa conectar a rede local de sua empresa à AWS e gostaria de estabelecer um serviço VPN gerenciado pela AWS. Qual dos seguintes itens de configuração precisa ser configurado no lado Amazon VPC da conexão?",
     "options":["Um Virtual Private Gateway","Um Customer Gateway","Um dispositivo Network Address Translation","Um Firewall"],
     "correct":[0],"multiple":False},
    {"q":"Onde os snapshots do Amazon EBS são armazenados?",
     "options":["Em um instance store Amazon EBS","Em um filesystem Amazon EFS","Dentro do EBS block store","No Amazon S3"],
     "correct":[3],"multiple":False},
    {"q":"Qual serviço AWS facilita a coordenação dos componentes de aplicações distribuídas como uma série de etapas em um fluxo de trabalho visual?",
     "options":["Amazon SWF","AWS Step Functions","Amazon SNS","Amazon SES"],
     "correct":[1],"multiple":False},
    {"q":"Um Cloud Practitioner está criando os fluxos de trabalho de processo de negócios associados a um sistema de cumprimento de pedidos. Qual serviço AWS pode auxiliar na coordenação de tarefas entre componentes de aplicação distribuídos?",
     "options":["AWS STS","Amazon SQS","Amazon SWF","Amazon SNS"],
     "correct":[2],"multiple":False},
    {"q":"Seu gerente pediu para você explicar alguns dos recursos de segurança disponíveis na nuvem AWS. Como você pode descrever a função do Amazon CloudHSM?",
     "options":["Fornece criptografia do lado do servidor para objetos S3","É uma Infraestrutura de Chave Pública (PKI)","Pode ser usado para gerar, usar e gerenciar chaves de criptografia na nuvem","É um firewall para uso com aplicações web"],
     "correct":[2],"multiple":False},
    {"q":"Qual opção de acesso a dados do AWS Glacier recupera dados de um arquivo em 1-5 minutos?",
     "options":["Standard","Express","Accelerated","Expedited"],
     "correct":[3],"multiple":False},
    {"q":"Como um administrador de sistemas pode especificar um script para ser executado em uma instância EC2 durante o lançamento?",
     "options":["Metadata","User Data","Run Command","AWS Config"],
     "correct":[1],"multiple":False},
    {"q":"Quais vantagens a nuvem AWS fornece em relação ao custo? (Selecione DUAS.)",
     "options":["Cobrança granular","Pagamentos únicos para recursos sob demanda","Capacidade de desligar recursos e não pagar por eles","Descontos de licenciamento empresarial","Custos de energia discriminados"],
     "correct":[0,2],"multiple":True},
    {"q":"Quais das opções de autenticação abaixo podem ser usadas para autenticar usando APIs AWS? (Selecione DUAS.)",
     "options":["Pares de chaves","Chaves de acesso","Senhas de servidor","Security groups","Certificados de servidor"],
     "correct":[1,4],"multiple":True},
    {"q":"Sob o Modelo de Responsabilidade Compartilhada da AWS, quem é responsável pelo quê? (Selecione DUAS.)",
     "options":["Clientes são responsáveis pela infraestrutura de computação","AWS é responsável pela configuração de rede e firewall","Clientes são responsáveis pela proteção de tráfego de rede","AWS é responsável pela infraestrutura de rede","Clientes são responsáveis por edge locations"],
     "correct":[2,3],"multiple":True},
    {"q":"Qual código HTTP indica um upload bem-sucedido de um objeto para Amazon S3?",
     "options":["200","300","400","500"],
     "correct":[0],"multiple":False},
    {"q":"Quais planos de suporte AWS fornecem acesso 24×7 ao atendimento ao cliente?",
     "options":["Basic","Business","Developer","Todos os planos"],
     "correct":[3],"multiple":False},
    {"q":"Quais das seguintes NÃO são recursos do AWS IAM? (Selecione DUAS.)",
     "options":["Acesso compartilhado à sua conta AWS","Login usando contas de usuário locais","Federação de identidade","Conformidade PCI DSS","Cobrança pelo que você usa"],
     "correct":[1,4],"multiple":True},
    {"q":"Como uma empresa pode facilitar o compartilhamento de dados sobre conexões privadas entre duas contas que possuem dentro de uma região?",
     "options":["Criar um ELB interno","Criar uma conexão de peering de subnet","Criar uma conexão de peering VPC","Configurar faixas de endereço CIDR correspondentes"],
     "correct":[2],"multiple":False},
    {"q":"Como você pode implantar suas instâncias EC2 para que se um único data center falhar você ainda tenha instâncias disponíveis?",
     "options":["Entre regiões","Entre subnets","Entre Zonas de Disponibilidade","Entre VPCs"],
     "correct":[2],"multiple":False},
    {"q":"Seu gerente pediu para você explicar os benefícios de usar grupos IAM. Quais das declarações abaixo são benefícios válidos? (Selecione DUAS.)",
     "options":["Você pode restringir acesso às subnets em sua VPC","Grupos permitem especificar permissões para múltiplos usuários, o que pode facilitar o gerenciamento das permissões para esses usuários","Fornece a capacidade de criar políticas de permissão personalizadas","Permite anexar políticas de permissão IAM a mais de um usuário por vez","Fornece a capacidade de aninhar grupos para criar uma hierarquia organizacional"],
     "correct":[1,3],"multiple":True},
    {"q":"Quais das seguintes são pilares dos cinco pilares do AWS Well-Architected Framework? (Selecione DUAS.)",
     "options":["Resiliência","Excelência operacional","Confidencialidade","Economia","Eficiência de performance"],
     "correct":[1,4],"multiple":True},
    {"q":"O que você precisa para fazer login no console AWS?",
     "options":["Nome de usuário e senha","Par de chaves","Chave de acesso e ID secreto","Certificado"],
     "correct":[0],"multiple":False},
    {"q":"Quais são as vantagens de executar um serviço de banco de dados como Amazon RDS na nuvem versus implantar local? (Selecione DUAS.)",
     "options":["Você tem controle total do sistema operacional e pode instalar suas próprias ferramentas operacionais","A escalabilidade é melhorada pois é mais rápido de implementar e há abundância de capacidade","Você pode usar qualquer software de banco de dados que quiser, permitindo maior flexibilidade","Alta disponibilidade é mais fácil de implementar devido à funcionalidade integrada para implantar read replicas e multi-AZ","Não há custos para replicar dados entre DBs em diferentes data centers ou regiões"],
     "correct":[1,3],"multiple":True},
    {"q":"Qual das declarações abaixo NÃO caracteriza computação em nuvem?",
     "options":["Computação em nuvem é a entrega sob demanda de poder de computação","Com computação em nuvem você se beneficia de economias de escala massivas","Computação em nuvem permite trocar despesa variável por despesa de capital","Com computação em nuvem você pode aumentar sua velocidade e agilidade"],
     "correct":[2],"multiple":False},
    {"q":"Qual tecnologia AWS permite agrupar recursos que compartilham uma ou mais tags?",
     "options":["Tag groups","Organization groups","Resource groups","Consolidation groups"],
     "correct":[2],"multiple":False},
    {"q":"Qual é a maneira mais fácil de armazenar um backup de um volume EBS no Amazon S3?",
     "options":["Escrever um script personalizado para copiar os dados para um bucket","Usar ações de lifecycle S3 para fazer backup do volume","Criar um snapshot do volume","Usar Amazon Kinesis para processar os dados e armazenar os resultados no S3"],
     "correct":[2],"multiple":False},
    {"q":"Qual ferramenta de segurança AWS usa um agente instalado em instâncias EC2 e avalia aplicações para vulnerabilidades e desvios das melhores práticas?",
     "options":["AWS Trusted Advisor","AWS Personal Health Dashboard","AWS TCO Calculator","AWS Inspector"],
     "correct":[3],"multiple":False},
    {"q":"Qual das seguintes NÃO é uma melhor prática para proteger o usuário root de uma conta AWS?",
     "options":["Não compartilhar as credenciais do usuário root","Habilitar MFA","Remover permissões administrativas","Trancar as chaves de acesso do usuário root da AWS"],
     "correct":[2],"multiple":False},
    {"q":"Você está avaliando serviços AWS que podem auxiliar na criação de ambientes de aplicação escaláveis. Qual das declarações abaixo melhor descreve o serviço Elastic Load Balancer?",
     "options":["Ajuda a garantir que você tenha o número correto de instâncias Amazon EC2 disponíveis para lidar com a carga de sua aplicação","Um serviço de Sistema de Nomes de Domínio (DNS) altamente disponível e escalável","Distribui automaticamente tráfego de aplicação de entrada entre múltiplos alvos, como instâncias Amazon EC2, containers e endereços IP","Um serviço de rede que fornece uma alternativa ao uso da Internet para conectar sites locais de clientes à AWS"],
     "correct":[2],"multiple":False},
    {"q":"Qual é um exemplo de escalonamento vertical?",
     "options":["AWS Auto Scaling adicionando mais instâncias EC2","AWS Lambda adicionando funções executando simultaneamente","Aumentar o tamanho da instância com Amazon RDS","Adicionar read replicas a um banco de dados Amazon RDS"],
     "correct":[2],"multiple":False},
    {"q":"Para reduzir custos, quais dos seguintes serviços suportam reservas? (Selecione DUAS.)",
     "options":["Amazon ElastiCache","Amazon CloudFormation","Amazon RedShift","AWS Elastic Beanstalk","Amazon S3"],
     "correct":[0,2],"multiple":True},
    {"q":"Qual tipo de serviço de computação em nuvem AWS Elastic Beanstalk e Amazon RDS correspondem?",
     "options":["IaaS","PaaS","SaaS","Híbrido"],
     "correct":[1],"multiple":False},
    {"q":"Como uma empresa pode configurar cópia automática e assíncrona de objetos em buckets Amazon S3 entre regiões?",
     "options":["Isso é feito por padrão pela AWS","Configurando replicação multi-master","Usando replicação cross-region","Usando ações de lifecycle"],
     "correct":[2],"multiple":False},
    {"q":"Sua empresa migrou recentemente para AWS. Como seu CTO pode monitorar os custos da organização?",
     "options":["AWS Cost Explorer","AWS CloudTrail","AWS Consolidated Billing","AWS Simple Monthly calculator"],
     "correct":[0],"multiple":False},
    {"q":"Sua organização tem escritórios ao redor do mundo e alguns funcionários viajam entre escritórios. Como suas contas devem ser configuradas?",
     "options":["IAM é um serviço global, apenas crie os usuários em um lugar","Criar uma conta separada no IAM dentro de cada região para a qual viajarão","Definir a conta de usuário como \"global\" quando criada","Habilitar MFA para as contas"],
     "correct":[0],"multiple":False}
]

# Dicionário com todos os simulados
SIMULADOS = {
    0: {"nome": "Simulado 0 - Prático Geral", "questoes": SIMULADO_0},
    1: {"nome": "Set 1 - Practice Questions", "questoes": SIMULADO_1},
    2: {"nome": "Set 2 - Practice Questions", "questoes": SIMULADO_2},
    3: {"nome": "Set 3 - Practice Questions", "questoes": SIMULADO_3},
    4: {"nome": "Set 4 - Practice Questions", "questoes": SIMULADO_4},
    5: {"nome": "Set 5 - Practice Questions", "questoes": SIMULADO_5},
    6: {"nome": "Set 6 - Practice Questions", "questoes": SIMULADO_6},
}

# ====== Aplicativo Tkinter ======

class SimuladoSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("Seleção de Simulados AWS")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Centralizar janela
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (600 // 2)
        y = (self.root.winfo_screenheight() // 2) - (500 // 2)
        self.root.geometry(f"600x500+{x}+{y}")
        
        self.selected_simulado = None
        self.create_widgets()
    
    def create_widgets(self):
        # Título
        title_frame = tk.Frame(self.root)
        title_frame.pack(pady=20)
        
        title_label = tk.Label(title_frame, text="AWS Cloud Practitioner", 
                              font=("Segoe UI", 20, "bold"), fg="white")
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame, text="Escolha um simulado para começar", 
                                 font=("Segoe UI", 12), fg="white")
        subtitle_label.pack(pady=(5, 0))
        
        # Frame principal com scroll
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Canvas para scroll
        canvas = tk.Canvas(main_frame, bg="#1E1E1E")
        scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#1E1E1E")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="center")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Frame centralizado para os botões
        center_frame = tk.Frame(scrollable_frame, bg="#1E1E1E")
        center_frame.pack(expand=True, fill="both", padx=50, pady=50)
        
        # Criar botões para cada simulado
        for i, (key, simulado) in enumerate(SIMULADOS.items()):
            btn = tk.Button(center_frame, text=simulado["nome"], 
                           font=("Segoe UI", 12, "bold"),
                           bg="#FF9900", fg="black", 
                           relief="flat", padx=20, pady=15,
                           command=lambda k=key: self.select_simulado(k))
            btn.pack(fill="x", pady=5)
            
            # Adicionar número de questões se disponível
            num_questoes = len(simulado["questoes"])
            if num_questoes > 0:
                info_label = tk.Label(center_frame, text=f"{num_questoes} questões", 
                                     font=("Segoe UI", 9), fg="white", bg="#1E1E1E")
                info_label.pack()
            else:
                info_label = tk.Label(center_frame, text="Em breve", 
                                     font=("Segoe UI", 9), fg="#FF6B6B", bg="#1E1E1E")
                info_label.pack()
        
        # Pack canvas e scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel para scroll
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Botão de sair
        exit_frame = tk.Frame(self.root)
        exit_frame.pack(pady=20)
        
        exit_btn = tk.Button(exit_frame, text="Sair", 
                            font=("Segoe UI", 10),
                            bg="black", fg="white",
                            relief="flat", padx=20, pady=8,
                            command=self.root.quit)
        exit_btn.pack()
    
    def select_simulado(self, simulado_id):
        if len(SIMULADOS[simulado_id]["questoes"]) == 0:
            messagebox.showinfo("Em breve", f"O {SIMULADOS[simulado_id]['nome']} será adicionado em breve!")
            return
        
        self.selected_simulado = simulado_id
        self.root.destroy()

class QuizApp:
    def __init__(self, root, simulado_id=0):
        self.root = root
        self.simulado_id = simulado_id
        self.questoes = SIMULADOS[simulado_id]["questoes"]
        self.simulado_nome = SIMULADOS[simulado_id]["nome"]
        
        self.root.title(f"{self.simulado_nome}")
        self.root.geometry("900x600")

        self.index = 0
        self.score = 0
        self.answered = [False]*len(self.questoes)

        # Header
        header = tk.Frame(root)
        header.pack(fill="x", padx=12, pady=8)

        self.lbl_title = tk.Label(header, text=self.simulado_nome, font=("Segoe UI", 14, "bold"))
        self.lbl_title.pack(side="left")
        
        # Botão para voltar à seleção
        self.btn_back = tk.Button(header, text="← Voltar", font=("Segoe UI", 10), 
                                 bg="#666666", fg="white", relief="flat", padx=10, pady=5,
                                 command=self.back_to_selection)
        self.btn_back.pack(side="right", padx=(0, 10))

        self.progress_var = tk.StringVar()
        self.progress_var.set(f"Questão 1 de {len(self.questoes)}")
        self.lbl_progress = tk.Label(header, textvariable=self.progress_var, font=("Segoe UI", 12))
        self.lbl_progress.pack(side="right")

        # Corpo
        body = tk.Frame(root)
        body.pack(fill="both", expand=True, padx=12, pady=8)

        self.txt_question = tk.Message(body, width=820, font=("Segoe UI", 12), anchor="w", justify="left")
        self.txt_question.pack(fill="x", pady=(0,10))

        self.options_frame = tk.Frame(body)
        self.options_frame.pack(fill="x")

        # Feedback
        self.feedback_var = tk.StringVar()
        self.feedback_label = tk.Label(body, textvariable=self.feedback_var, font=("Segoe UI", 12, "bold"))
        self.feedback_label.pack(pady=6)

        # Footer com botões
        footer = tk.Frame(root)
        footer.pack(fill="x", padx=12, pady=8)

        self.btn_confirm = ttk.Button(footer, text="Confirmar resposta", command=self.confirm_answer)
        self.btn_confirm.pack(side="left")

        self.btn_next = ttk.Button(footer, text="Próxima ▶", command=self.next_question, state="disabled")
        self.btn_next.pack(side="left", padx=(8,0))

        self.btn_prev = ttk.Button(footer, text="◀ Anterior", command=self.prev_question)
        self.btn_prev.pack(side="left", padx=(8,0))

        self.btn_export = ttk.Button(footer, text="Exportar TXT", command=self.export_txt)
        self.btn_export.pack(side="right")

        self.score_var = tk.StringVar(value=f"Acertos: 0")
        self.lbl_score = tk.Label(footer, textvariable=self.score_var, font=("Segoe UI", 11, "bold"))
        self.lbl_score.pack(side="right", padx=(0,12))

        # Estado das opções (radiobuttons/checkboxes)
        self.option_vars = []
        self.option_widgets = []

        self.render_question()

    def render_question(self):
        qd = self.questoes[self.index]
        self.progress_var.set(f"Questão {self.index+1} de {len(self.questoes)}")
        self.txt_question.config(text=qd["q"])

        # limpa opções
        for w in self.option_widgets:
            w.destroy()
        self.option_widgets.clear()
        self.option_vars.clear()
        self.feedback_var.set("")
        self.feedback_label.config(fg="black")
        self.btn_confirm.config(state="normal")
        self.btn_next.config(state="disabled")

        if qd["multiple"]:
            # múltipla escolha -> Checkbuttons
            for i, opt in enumerate(qd["options"]):
                var = tk.BooleanVar()
                cb = tk.Checkbutton(self.options_frame, text=opt, variable=var, font=("Segoe UI", 11), anchor="w", justify="left", wraplength=820)
                cb.pack(fill="x", pady=2, anchor="w")
                self.option_vars.append(var)
                self.option_widgets.append(cb)
        else:
            # única escolha -> Radiobuttons
            var = tk.IntVar(value=-1)
            for i, opt in enumerate(qd["options"]):
                rb = tk.Radiobutton(self.options_frame, text=opt, variable=var, value=i, font=("Segoe UI", 11), anchor="w", justify="left", wraplength=820)
                rb.pack(fill="x", pady=2, anchor="w")
                self.option_widgets.append(rb)
            self.option_vars.append(var)

        # Se já foi respondida, manter desabilitado e mostrar feedback
        if self.answered[self.index]:
            self.show_feedback(already=True)

    def get_selected_indices(self):
        qd = self.questoes[self.index]
        if qd["multiple"]:
            idxs = [i for i, var in enumerate(self.option_vars) if var.get()]
            return idxs
        else:
            val = self.option_vars[0].get()
            return [] if val == -1 else [val]

    def confirm_answer(self):
        if self.answered[self.index]:
            return

        selected = self.get_selected_indices()
        if not selected:
            messagebox.showwarning("Atenção", "Selecione ao menos uma alternativa.")
            return

        correct = set(self.questoes[self.index]["correct"])
        chosen = set(selected)

        is_correct = (correct == chosen)
        self.answered[self.index] = True

        if is_correct:
            self.score += 1
            self.feedback_var.set("✅ Correto!")
            self.feedback_label.config(fg="green")
        else:
            # mostra feedback com dica sobre múltipla
            if self.questoes[self.index]["multiple"]:
                self.feedback_var.set("❌ Incorreto. (Atenção: esta questão tem múltiplas respostas.)")
            else:
                self.feedback_var.set("❌ Incorreto.")
            self.feedback_label.config(fg="red")

        # Desabilita inputs
        for w in self.option_widgets:
            w.config(state="disabled")

        self.btn_confirm.config(state="disabled")
        # libera próxima
        if self.index < len(self.questoes) - 1:
            self.btn_next.config(state="normal")
        else:
            self.btn_next.config(state="disabled")
            # fim de prova
            acertos = self.score
            total = len(self.questoes)
            messagebox.showinfo("Simulado concluído", f"Você finalizou o simulado.\n\nAcertos: {acertos}/{total}\nAproveitamento: {acertos/total:.0%}")

        self.score_var.set(f"Acertos: {self.score}")

    def next_question(self):
        if self.index < len(self.questoes) - 1:
            self.index += 1
            self.render_question()

    def prev_question(self):
        if self.index > 0:
            self.index -= 1
            self.render_question()

    def show_feedback(self, already=False):
        # Exibe o feedback da questão já respondida (quando navega para trás)
        # e desabilita inputs
        correct = set(self.questoes[self.index]["correct"])
        # marcamos visualmente: apenas mostra msg; não reavalia escolhas antigas
        self.feedback_var.set("✅ Já respondida corretamente." if already else "")
        self.feedback_label.config(fg="green")
        for w in self.option_widgets:
            w.config(state="disabled")
        self.btn_confirm.config(state="disabled")
        if self.index < len(self.questoes) - 1:
            self.btn_next.config(state="normal")

    def export_txt(self):
        # Exporta questões (sem gabarito) para TXT
        default_name = "simulado_aws_questoes.txt"
        path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=default_name,
                                            filetypes=[("Arquivo de texto", "*.txt")])
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(f"{self.simulado_nome} ({len(self.questoes)} questões)\n\n")
                for i, qd in enumerate(self.questoes, start=1):
                    mult_tag = " (Escolha múltipla)" if qd["multiple"] else ""
                    f.write(f"{i}. {qd['q']}{mult_tag}\n")
                    for j, opt in enumerate(qd["options"]):
                        letra = chr(ord('A') + j)
                        f.write(f"   {letra}) {opt}\n")
                    f.write("\n")
            messagebox.showinfo("Exportar TXT", f"Arquivo salvo em:\n{path}")
        except Exception as e:
            messagebox.showerror("Erro ao exportar", str(e))
    
    def back_to_selection(self):
        """Volta para a tela de seleção de simulados"""
        self.root.destroy()
        # Criar nova janela de seleção
        new_root = tk.Tk()
        selector = SimuladoSelector(new_root)
        new_root.mainloop()


def main():
    """Função principal que gerencia a navegação entre telas"""
    while True:
        # Tela de seleção de simulados
        root = tk.Tk()
        selector = SimuladoSelector(root)
        root.mainloop()
        
        # Se chegou aqui, o usuário fechou a janela ou selecionou um simulado
        if selector.selected_simulado is not None:
            # Abrir o simulado selecionado
            quiz_root = tk.Tk()
            quiz_app = QuizApp(quiz_root, selector.selected_simulado)
            quiz_root.mainloop()
        else:
            # Usuário fechou a aplicação
            break

if __name__ == "__main__":
    main()
