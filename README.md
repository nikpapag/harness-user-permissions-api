# Harness API User Permissions (harness-user-permissions-api)
Python script to present user permissions for a given user


###### Metric Types
This script utilises the Harness graphql APIs 
```
https://app.harness.io/gateway/api/graphql
```


###### Installation
1. Centos
    - Install centos prereqs
      ```
        sudo yum install -y git
        sudo yum install -y python3-pip
        pip3 install requests
        pip3 install pandas
      ```
2. Ubuntu
    - Install ubuntu prereqs
      ```
        sudo apt-get update -y
        sudo apt-get install -y git
        sudo apt-get install -y python3-pip
        pip3 install requests
        pip3 install pandas
      ```

###### Clone and prepare script

1. Clone the github repository

        git clone https://github.com/nikpapag/harness-user-permissions-api

2. Navigate to the Repo's local directory

        cd harness-user-permissions-api

      
3. Provide the correct permissions to the executable files

        chmod 700 main.py


###### Startup Options
1. Script takes three arguments
      -Account  --account (Harness account ID)
      -Api Key  --apiKey (Harness API key generated to use the graphql API)
      -User Email  --user (Email of user to search)


###### Execution
      
1. Run the python Script with the appropriate parameters

        python3 main.py --account XXXXXXXX --apiKey XXXYYYYYYYY --user user@domain.com


