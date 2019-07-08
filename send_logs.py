import json
import requests
import time
SUMO_HTTP_ENDPOINT = 'https://endpoint4.collection.us2.sumologic.com/receiver/v1/http/ZaVnC4dhaV3N-lPxodY4J3xadi2by444XVaSboLlcbfMeGhqAnZn4PIVuJw_h3EzhhCv4jEFLfhHO3nbvfVgVSiRrB2X1hedSvXwyKB31hF3zdmR7j7mrQ=='

def send_logs(message, start_time, vendor):
    print(f'{__file__} - start send logs')
    execution_time = time.time() - start_time
    session = requests.Session()
    account_id = message.get('Account id')
    print(f'{__file__} - vendor: {vendor}')
    print(f'{__file__} - message: {message}')
    for bot in message.get('Rules violations found'):
        del bot['ID']
        del bot['Name']
    headers = {'Content-Type': 'application/json',  'Accept': 'application/json', 'X-Sumo-Name': account_id, 'X-Sumo-Category': vendor}
    data = {'msg': message,
            'execution_time': execution_time}
    print(f'{__file__} - data: {data}')
    return_sumo_status = session.post(SUMO_HTTP_ENDPOINT, headers=headers, data=json.dumps(data))
    print(f'{__file__} - status code from dome9 logs: {return_sumo_status.status_code}')
    return
