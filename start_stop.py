import boto3

def stop_ecs_service(cluster, service_name):
    # Cria uma instância do cliente ECS
    ecs = boto3.client('ecs')

    # Para o serviço especificado
    response = ecs.update_service(cluster=cluster, service=service_name, desiredCount=0)

    # Verifica se o serviço foi parado com sucesso
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return True
    else:
        return False

def start_ecs_service(cluster, service_name):
    # Cria uma instância do cliente ECS
    ecs = boto3.client('ecs')

    # Inicia o serviço especificado
    response = ecs.update_service(cluster=cluster, service=service_name, desiredCount=1, healthCheckGracePeriodSeconds=100)

    # Verifica se o serviço foi iniciado com sucesso
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return True
    else:
        return False

def lambda_handler(event, context):
    try:
        cluster = 'CLUSTER_NAME'
        service_name = 'SERVICE_NAME'

        # Verifica se a ação é de parar ou iniciar o serviço
        action = event['action'].lower()

        if action == 'parar':
            # Para o serviço do ECS
            stopped = stop_ecs_service(cluster, service_name)
            if stopped:
                return {
                    'statusCode': 200,
                    'body': f'O serviço "{service_name}" no cluster "{cluster}" foi parado com sucesso.'
                }
            else:
                return {
                    'statusCode': 500,
                    'body': f'Ocorreu um erro ao parar o serviço "{service_name}" no cluster "{cluster}".'
                }
        elif action == 'iniciar':
            # Inicia o serviço do ECS
            started = start_ecs_service(cluster, service_name)
            if started:
                return {
                    'statusCode': 200,
                    'body': f'O serviço "{service_name}" no cluster "{cluster}" foi iniciado com sucesso.'
                }
            else:
                return {
                    'statusCode': 500,
                    'body': f'Ocorreu um erro ao iniciar o serviço "{service_name}" no cluster "{cluster}".'
                }
        else:
            raise ValueError('Ação inválida. Use "parar" ou "iniciar" como ação.')

    except Exception as e:
        print('Erro:', e)
        return {
            'statusCode': 500,
            'body': 'Ocorreu um erro ao executar a ação de modificar o serviço.'
        }