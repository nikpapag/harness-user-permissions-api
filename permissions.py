import harnessgraphql

def get_environment_permissions_json(user_groups,accountId,api_key):
    groups_dict = {}
    for group in user_groups:
        group_name = group['name']
        for permission in group['permissions']['appPermissions']:
            actions = permission['actions']
            if permission['environments'] is not None:
                environments = permission['environments']
                if environments['envIds'] is not None:
                    for env_id in environments['envIds']:
                        env_name = harnessgraphql.get_environment(env_id, accountId, api_key)
                        env_permissions_dictionary = {env_name: actions}

                        if env_name in groups_dict:
                            perm_set = set(groups_dict[env_name])
                            perm_set.update(actions)
                            groups_dict[env_name] = list(perm_set)
                        else:
                            groups_dict = {**groups_dict, **env_permissions_dictionary}
        for key,value in groups_dict.items():
            max_length=8
            for i in range(len(value),max_length):
                value.append([None])
    return groups_dict


def get_application_permissions_json(user_groups,accountId,api_key):
    groups_dict = {}
    for group in user_groups:
        group_name = group['name']
        for permission in group['permissions']['appPermissions']:
            actions = permission['actions']

            applications = permission['applications']
            if applications['appIds'] is not None:
                for application_id in applications['appIds']:
                    application_name = harnessgraphql.get_application(application_id, accountId, api_key)
                    app_permissions_dictionary = {application_name: actions}

                    if application_name in groups_dict:
                        perm_set = set(groups_dict[application_name])
                        perm_set.update(actions)
                        groups_dict[application_name] = list(perm_set)
                    else:
                        groups_dict = {**groups_dict, **app_permissions_dictionary}
    for key,value in groups_dict.items():
        max_length=8
        for i in range(len(value),max_length):
            value.append([None])
    return groups_dict



def get_deployment_permissions_json(user_groups,accountId,api_key):
    groups_dict = {}
    for group in user_groups:
        group_name = group['name']
        for permission in group['permissions']['appPermissions']:
            actions = permission['actions']
            if permission['deployments'] is not None:
                deployments = permission['deployments']
                if deployments['envIds'] is not None:
                    for env_id in deployments['envIds']:
                        env_name = harnessgraphql.get_environment(env_id, accountId, api_key)
                        deployment_permissions_dictionary = {env_name: actions}

                        if env_name in groups_dict:
                            perm_set = set(groups_dict[env_name])
                            perm_set.update(actions)
                            groups_dict[env_name] = list(perm_set)
                        else:
                            groups_dict = {**groups_dict, **deployment_permissions_dictionary}
        for key,value in groups_dict.items():
            max_length=8
            for i in range(len(value),max_length):
                value.append([None])
    return groups_dict


def get_workflow_permissions_json(user_groups,accountId,api_key):
    groups_dict = {}
    for group in user_groups:
        group_name = group['name']
        for permission in group['permissions']['appPermissions']:
            actions = permission['actions']
            if permission['workflows'] is not None:
                workflows = permission['workflows']
                if workflows['workflowIds'] is not None:
                    for workflow_id in workflows['workflowIds']:
                        workflow_name = harnessgraphql.get_workflow(workflow_id, accountId, api_key)
                        workflow_permissions_dictionary = {workflow_name: actions}

                        if workflow_name in groups_dict:
                            perm_set = set(groups_dict[workflow_name])
                            perm_set.update(actions)
                            groups_dict[workflow_name] = list(perm_set)
                        else:
                            groups_dict = {**groups_dict, **workflow_permissions_dictionary}
        for key,value in groups_dict.items():
            max_length=8
            for i in range(len(value),max_length):
                value.append([None])
    return groups_dict



def get_account_permissions_json(user_groups):
    account_perm_set = set()
    for group in user_groups:
        group_name = group['name']
        if group['permissions']['accountPermissions'] is not None:
            if group['permissions']['accountPermissions']['accountPermissionTypes'] is not None:
                for permission in group['permissions']['accountPermissions']['accountPermissionTypes']:
                    account_perm_set.add(permission)
    return(list(account_perm_set))



