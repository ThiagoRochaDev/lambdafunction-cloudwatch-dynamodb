# lambdafunction-cloudwatch-dynamodb

## Etapas :

1- instalar serverless `serverless create --template aws-python3`

2 - Fazer os vinculos da cloudwatch com a função lambda pelo controle aws

3 - Criar as politicas e serviços: cloudwatchlogs , dynamodb , s3 (all resources, all actions)

4 - Criar função lambda e vincular a politica.

5 - Não inserir arquivos com caracteres especiais, ainda não validado