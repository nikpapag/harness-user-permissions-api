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


###### Execution
      
    - Install and Configure the Python Script
    - Clone the github repository
      ```
        git clone https://github.com/nikpapag/harness-user-permissions-api
      ```
    - Navigate to the Repo's local directory
      ```
        cd harness-user-permissions-api
      ```
    - Provide the correct permissions to the executable files
      ```
        chmod 700 main.py
      ```
    - Run the python Script with the appropriate parameters
      ```
        --account (Harness account ID)
        --apiKey (Harness API key generated to use the graphql API)
        --user (Email of user to search)
        python3 main.py --account XXXXXXXX --apiKey XXXYYYYYYYY --user user@domain.com
      ```

