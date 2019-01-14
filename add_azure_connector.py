
import sys, requests, datetime, os, time, yaml, json, csv, base64

def config():
    with open('config.yml', 'r') as config_settings:
        config_info = yaml.load(config_settings)
        username = str(config_info['defaults']['username']).rstrip()
        password = str(config_info['defaults']['password']).rstrip()
        URL = str(config_info['defaults']['apiURL']).rstrip()
        debug = config_info['defaults']['debug']
        if username == '' or password == '' or URL == '':
            print "Config information in ./config.yml not configured correctly. Exiting..."
            sys.exit(1)
    return username, password, URL, debug

def Post_Call(username,password,URL,data_connector):

    usrPass = str(username)+':'+str(password)
    b64Val = base64.b64encode(usrPass)
    headers = {
        'Accept': '*/*',
        'content-type': 'application/json',
        'Authorization': "Basic %s" % b64Val

    }

    r = requests.post(URL, data=data_connector, headers=headers)
    return r.raise_for_status()


def Add_AZURE_Connector():
    username, password, URL, debug = config()
    URL = URL + "/cloudview/rest/1.0/azure/connectors"

    if debug:
        print '------------------------------AZURE Connectors--------------------------------'
        if not os.path.exists("debug"):
            os.makedirs("debug")
        debug_file_name = "debug/debug_file"+ time.strftime("%Y%m%d-%H%M%S") + ".txt"
        debug_file = open(debug_file_name, "w")
        debug_file.write('------------------------------AZURE Connectors--------------------------------' + '\n')
    #df = pd.read_excel('AZURE_CONNECTOR_INFO.xlsx', sheet_name='Sheet1')
    with open('AZURE_CONNECTOR_INFO.csv', 'rb') as f:
        reader = csv.DictReader(f)
        a = list(reader)
        f.close()
    counter=0
    for i in a:
        counter += 1
        AppID = i['APPLICATIONID']
        AzureAuthKeyID = i['AUTHKEY']
        SubID = i['SUBSCRIPTIONID']
        DirectoryID = i['DIRECTORYID']
        DESC = i['DESC']
        NAME = i['NAME']
        if debug:
            print str(counter) + ' : AZURE Connector'
            debug_file.write(str(counter) + ' : AZURE Connector' + '\n')
            print '---' + 'NAME  : ' + str(NAME)
            print '---' + 'DESC : ' + str(DESC)
            print '---' + 'Application ID : ' + str(AppID)
            print '---' + 'Subscription ID: ' + str(SubID)
            print '---' + 'Authentication Key : ' + str(AzureAuthKeyID)
            print '---' + 'Directory ID: ' + str(DirectoryID)
            debug_file.write('---' + 'NAME : ' + str(NAME) + '\n')
            debug_file.write('---' + 'DESC : ' + str(DESC) + '\n')
            debug_file.write('---' + 'Application ID : ' + str(AppID) + '\n')
            debug_file.write('---' + 'Subscription ID : ' + str(SubID) + '\n')
            debug_file.write('---' + 'Authentication Key : ' + str(AzureAuthKeyID) + '\n')
            debug_file.write('---' + 'Directory ID : ' + str(DirectoryID) + '\n')

        data_connector = {
            "applicationId": str(AppID),
            "description": str(DESC),
            "key": str(AzureAuthKeyID),
            "name": str(NAME),
            "subscriptionId": str(SubID),
            "tenantId": str(DirectoryID)
        }

        try:
            Post_Call(username, password, URL, data_connector)
            if debug:
                print str(counter) + ' : Connector Added Successfully'
                print '-------------------------------------------------------------'
                debug_file.write(str(counter) + ' : Connector Added Successfully' + '\n')

        except requests.exceptions.HTTPError as e:  # This is the correct syntax
            print str(counter) + ' : Failed to Add Azure Connector'
            print e
            print '-------------------------------------------------------------'
            if debug:
                debug_file.write(str(counter) + ' : Failed to Add Azure Connector' + '\n')
                debug_file.write(str(e) + '\n')
    if debug:
        debug_file.close()

Add_AZURE_Connector()
