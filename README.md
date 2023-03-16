# Add Azure Connector
*THIS SCRIPT IS PROVIDED TO YOU "AS IS."  TO THE EXTENT PERMITTED BY LAW, QUALYS HEREBY DISCLAIMS ALL WARRANTIES AND LIABILITY FOR THE PROVISION OR USE OF THIS SCRIPT.  IN NO EVENT SHALL THESE SCRIPTS BE DEEMED TO BE CLOUD SERVICES AS PROVIDED BY QUALYS*

## add_azzure_connector.py
Info : Python File adds the AZURE connector into CloudView w.r.t details provided in "./AZURE_CONNECTOR_INFO.csv" & "./config.yml".
       Console output as well as debug_file.txt will have both success & failure logs.

## AZURE_CONNECTOR_INFO.csv
Info : csv files contains below attributes required for AZURE connector
Script looks for AZURE_CONNECTOR_INFO.csv in the directory the script runs from

> NAME,DESC,APPLICATIONID,DIRECTORYID,AUTHKEY,SUBSCRIPTIONID

> test-ExampleAzureConnector,Some Description of the Azure Account,3723e578-15e2-11e9-ab14-d663bd873d93,3723e578-15e2-11e9-ab14-d663bd873d987,3723e578-15e2-11e9-45e6-d6634a873d93,3a23a578-15a2-11e9-ab14-d663bd873d93

CSV Variable types:

*Name*: string

*DESC*: string

*APPLICATIONID*: UUID - Create application in Azure Active Directory and you can then note the application ID.

Log on to the Microsoft Azure console. Go to Azure Active Directory in the left navigation pane, then App Registrations.
Click New application registration and provide these details:
Name: A name for the application (e.g. My_Azure_Connector)
Application Type: Select Web app/API
Sign-on URL: Enter any valid URL (e.g. https://localhost/azure_con)
Click Create. The newly created app appears in the list of applications. Copy the Application ID and paste it into the connector details.

*DIRECTORYID*: UUID - The directory ID is an unique identifier of your Azure Active Directory. Navigate to Azure Active Directory > Properties. Copy the Directory ID and paste it into the connector details.

*AUTHKEY*: UUID - Provide permission to the new application to access the Windows Azure Service Management API and create a secret key.

Provide Permission
Select the application that you created and go to Settings > Required permissions.
Click Add > Select an API > Windows Azure Service Management API and click Select.
Select required Delegated Permissions, click Select and then click Done.
Create a secret key
Select the application that you created and go to Settings > Keys.
Add a description and expiry duration for the key and click Save.
The value of the key appears in the Value field. Copy the key value at this time. You won’t be able to retrieve it later. Paste the key value as Authentication Key into the connector details.

*SUBSCRIPTIONID*: UUID - Grant permission for the application to access subscription that you want to configure. Assign a role to the new application. The role you assign will define the permissions for the new application to access subscriptions.
On the Azure portal, navigate to Subscriptions.
Select the subscription for which you want to grant permission to the application and note the subscription ID. To grant permission to the application you created, choose Access Control (IAM).
Go to Add > Select a role. Pick the role as Reader. A Reader can view everything, but cannot make any changes to the resources of a subscription.
Select Azure AD user, group, or application in Assign Access to dropdown.
Type the application name in Select drop-down and select the application you created.
Click Save to finish assigning the role. You’ll see your application in the list of users assigned to a role for that scope.
Copy the subscription ID you noted and paste it into the connector details in the Qualys Azure Connector screen and then click Create Connector.

## config.yml*
Info : Kindly provide correct correct USERNAME, PASSWORD & CloudView URL in the ./config.yml
Script looks for config.yml in the directory the script runs from
URL = Please get the proper API URL For you Qualys API connection based on your pod from the API documentation: https://qualys.com/documentation
The API user used must have manager permissions to create the Azure connector(s).

Example file contents:

    useranme
    
    password
    
    URL
    
    debug
    
    csa

 #### csa: If you want to create only Asset View Connector please mention false in csa section of the file else make it true for both Assest View and Cloud View (CSA) connector


## Script Requirements
This script requires the following PIP modules to run
Modules: json, base64, csv, os, time, urllib3

MAC/Linux "pip install urllib3"
Windows "python -m pip install urllib3"

## Debug
Set Debug True or False in config.yml
Debug file for script run, located in ./debug folder with time/date stamp


## License
## Copyright (c) 2018, Qualys All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. * Neither the name of the Qualys nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL QUALYS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED ANDON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
