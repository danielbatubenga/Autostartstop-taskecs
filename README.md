# Autostartstop-taskecs

Esse pequeno programa foi feito para ser usado no lambda, de forma parar programáticamente
as tasks do ecs fargate.

## Como funciona.

1. Ter uma conta aws
2. Criar  função lambda com python 3.8.
3. Criar um evento no amazon eventbridge, com disparos programatico via cron.
4. definir target no eventbridge usando os modelos em json [aqui](https://github.com/danielbatubenga/Autostartstop-taskecs/tree/main/comandos)
