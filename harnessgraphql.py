import requests
import json


def get_application(appId,accountId, api_key):
    application_query="""query ($appId: [String]!){
    applications(filters:{
    application:{
      operator: EQUALS
      values: $appId
    }
  }
    limit: 10
    offset: 0
  )
  {
      nodes{
      	name
      }
  }
}"""
    variables = {'appId': appId}
    url = 'https://app.harness.io/gateway/api/graphql'
    headers = {
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'x-api-key': api_key
    }
    params = {'accountId': accountId}
    response = requests.post(url, headers=headers, params=params, json={'query': application_query, 'variables': variables})
    application_name = json.loads(response.text)
    return application_name['data']['applications']['nodes'][0]['name']




def get_environment(envId,accountId, api_key):
    application_query="""query ($envId: [String]!){
    environments(filters:{
    environment:{
      operator: EQUALS
      values: $envId
    }
  }
    limit: 10
    offset: 0
  )
  {
      nodes{
      	name
      }
  }
}"""
    variables = {'envId': envId}
    url = 'https://app.harness.io/gateway/api/graphql'
    headers = {
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'x-api-key': api_key
    }
    params = {'accountId': accountId}
    response = requests.post(url, headers=headers, params=params, json={'query': application_query, 'variables': variables})
    application_name = json.loads(response.text)
    return application_name['data']['environments']['nodes'][0]['name']




def get_workflow(workflowId,accountId, api_key):
    application_query="""query ($workflowId: [String]!){
    workflows(filters:{
    workflow:{
      operator: EQUALS
      values: $workflowId
    }
  }
    limit: 10
    offset: 0
  )
  {
      nodes{
      	name
      }
  }
}"""
    variables = {'workflowId': workflowId}
    url = 'https://app.harness.io/gateway/api/graphql'
    headers = {
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'x-api-key': api_key
    }
    params = {'accountId': accountId}
    response = requests.post(url, headers=headers, params=params, json={'query': application_query, 'variables': variables})
    workflow_name = json.loads(response.text)
    return workflow_name['data']['workflows']['nodes'][0]['name']







def get_user_by_email(user_email,accountId, api_key):
    query = """query ($userEmail: String!){
      userByEmail(email:$userEmail){
        id,
        name
        userGroups(limit: 100) {
          nodes {
            id
            name
            permissions {
              appPermissions {
                actions
                applications {
                  appIds
                }
                environments {
                  envIds
                }
                deployments {
                  envIds
                }
                workflows {
                  workflowIds
                }
               }
              accountPermissions{
                accountPermissionTypes
              }
            }
          }
        }
      }
    }
    """
    variables = {'userEmail': user_email}
    url = 'https://app.harness.io/gateway/api/graphql'
    headers = {
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'x-api-key': api_key
    }

    params = {'accountId': accountId}
    r = requests.post(url, headers=headers, params=params, json={'query': query, 'variables':variables})
    json_data = json.loads(r.text)
    user_groups = json_data['data']['userByEmail']['userGroups']['nodes']
    return user_groups
