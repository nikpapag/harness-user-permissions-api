import argparse
import logging
import sys
from logging.config import dictConfig

import harnessgraphql
import pandas as pd
import permissions



#Get all command line arguments
full_cmd_arguments=sys.argv

argument_list= full_cmd_arguments[1:]

parser = argparse.ArgumentParser()
parser.add_argument('--account', help='Harness account id')
parser.add_argument('--apiKey', help='Harness api key')
parser.add_argument('--user', help='user')
args = vars(parser.parse_args())

accountId=args['account']
api_key=args['apiKey']
user_email=args['user']




logger = logging.getLogger(__name__)
DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
}
def configure_logging(logfile_path):
    dictConfig(DEFAULT_LOGGING)
    default_formatter = logging.Formatter(
        " %(message)s",
        "%d/%m/%Y %H:%M:%S")
    file_handler = logging.handlers.RotatingFileHandler(logfile_path, maxBytes=(1048576*5), backupCount=7)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(default_formatter)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    console_handler.setFormatter(default_formatter)
    logging.root.setLevel(logging.INFO)
    logging.root.addHandler(file_handler)
    logging.root.addHandler(console_handler)
configure_logging('permissions.log')

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

user_groups = harnessgraphql.get_user_by_email(user_email,accountId,api_key)
application_permissions = permissions.get_application_permissions_json(user_groups,accountId,api_key)
environment_permissions = permissions.get_environment_permissions_json(user_groups,accountId,api_key)
deployment_permissions = permissions.get_deployment_permissions_json(user_groups,accountId,api_key)
workflow_permissions = permissions.get_workflow_permissions_json(user_groups,accountId,api_key)
account_permissions = permissions.get_account_permissions_json(user_groups)




logger.info("---------------------------------------")
logger.info(user_email)
logging.info('\n')
logger.info("********Application Permissions********")
df=pd.DataFrame(application_permissions).transpose()
logger.info(df)
df.head()

logging.info('\n')
logger.info("********Environment Permissions********")
df=pd.DataFrame(environment_permissions).transpose()
logger.info(df)
df.head()

logging.info('\n')
logger.info("********Deployment Permissions********")
df=pd.DataFrame(deployment_permissions).transpose()
logger.info(df)
df.head()

logging.info('\n')
logger.info("********Workflow Permissions********")
df=pd.DataFrame(workflow_permissions).transpose()
logger.info(df)
df.head()

logging.info('\n')
#Account permissions
logger.info("********Account Permissions********")
df= pd.DataFrame(account_permissions)
logger.info(df)


