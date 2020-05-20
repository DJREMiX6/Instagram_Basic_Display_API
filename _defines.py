import requests
import json


def makePostApiCall(url, endpointParams, debug='no'):
    """Make a POST API call

    url:
        Endpoint's URL (string)

    endpointParams:
        Endpoint's request params (dict)

    debug:
        Debug param for showing data 'yes/no'(string)"""

    data = requests.post(url, endpointParams)

    response = dict()
    response['url'] = url
    response['endpoint_params'] = endpointParams
    response['endpoint_params_pretty'] = json.dumps(endpointParams, indent=4)
    response['json_data'] = data.content
    response['json_data_pretty'] = json.dumps(data.content, indent=4)


def makeGetApiCall(url, endpointParams, debug='no'):
    """Make a GET API call

        url:
            Endpoint's URL (string)

        endpointParams:
            Endpoint's request params (dict)

        debug:
            Debug param for showing data 'yes/no'(string)"""

    data = requests.get(url, endpointParams)

    response = dict()
    response['url'] = url
    response['endpoint_params'] = endpointParams
    response['endpoint_params_pretty'] = json.dumps(endpointParams, indent=4)
    response['json_data'] = data.content
    response['json_data_pretty'] = json.dumps(data.content, indent=4)

    if debug == 'yes':
        displayApiCallData(response)

    return json.loads(response.content)


def getCreds():
    """Get Credentials by settings.json file

    Return: A dict with settings info"""

    f = open('settings.json', 'r')
    creds = json.load(f)
    f.close()
    return creds


def changeCreds(credNames = list(), values = list()):
    """Change credentials values by settings.json file

    credName:
        Credentials's names

    value:
        New Credentials's values"""

    creds = getCreds()
    for n,v in zip(credNames, values):
        creds[n] = v
    f = open('settings.json', 'w')
    f.write(json.dumps(creds, indent=4))
    return


def addCreds(credNames = list(), values = list()):
    """Add credentials and values on settings.json file

        credName:
            Credentials's name

        value:
            New Credentials's value"""
    
    creds = getCreds()
    for n,v in zip(credNames, values):
        creds[n] = v
    f = open('settings.json', 'w')
    f.write(json.dumps(creds, indent=4))
    return


def delCreds(credNames = list()):
    """Delete credentials and values on settings.json file

           credNames:
               Credentials's name"""

    creds = getCreds()
    for n in credNames:
        del(creds[n])
    f = open('settings.json', 'w')
    f.write(json.dumps(creds, indent=4))
    return


def displayApiCallData(response):
    print('\nURL: ' + response['url'])
    print('Endpoint Params: ')
    print(response['endpoint_params_pretty'])
    print('Response Data:')
    print(response['json_data_pretty'])


def displayCreds():
    creds = getCreds()
    print('\nSettings:')
    for k, i in zip(creds.keys(), creds.values()):
        print(k + ': ' + i)


"""
displayCreds()
addCreds(['ciaone'], ['test'])
displayCreds()
changeCreds(['ciaone'], ['ciccino'])
displayCreds()
delCreds(['ciaone'])
displayCreds()
"""
