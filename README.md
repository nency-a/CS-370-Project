# CS-370-Project
## GitHub ID
- Devan Desai : devdes338
- Nency Ajmera : nency-a

## HuggingFace
- Devan Desai : drd38
- Nency Ajmera : nencya

### Commands to Build Image and Compose
- **Refer to https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_linux_mac/ for more information**
- Make sure directories on local are same as in this repository
- echo "vm.max_map_count=262144" > /tmp/99-clearml.conf
- sudo mv /tmp/99-clearml.conf /etc/sysctl.d/99-clearml.conf
- sudo sysctl -w vm.max_map_count=262144
- sudo service docker restart
- sudo chown -R 1000:1000 /opt/clearml
- export CLEARML_AGENT_ACCESS_KEY=generate_access_key_here
- export CLEARML_AGENT_SECRET_KEY=generate_secret_key_here
- export CLEARML_HOST_IP=server_host_ip_here
- export CLEARML_AGENT_GIT_USER=git_username_here
- export CLEARML_AGENT_GIT_PASS=git_password_here
- **To start:** docker-compose -f /opt/clearml/docker-compose.yml up -d
- visit http://localhost:8080 to view local clearml GUI after container is running
- **To stop:** docker-compose -f /opt/clearml/docker-compose.yml down
