## Overview:

This is a deployment of a sample application via AWS Fargate that utilizes Secretmanager

ansible-playbook site.yml -i inventory/dev -vv

Dockerfile in the repository root is used to containerize the application, called `task-app`.

Environment is usually added as a resource tag where possible, and also added to the name of the resource.

The initial modules builds the docker image and pushes to the ECR repository it creates. 

This playbook has modules then that create VPC, subnets for DB and web(ECS fargate cluster and ECS service), the RDS database and creates security groups for access between them. It also creates an ALB with target groups that are registered by Fargate ECS service.

The URL for ALB is given out in the `Output ecs_elb` task.

### Secret management:

DB passwords are pushed via aws cli to AWS secretmanager to the respective env/regions, and a lookup is used from ansible to retrieve. The AWS credentials are repository secrets accessible for Github actions.

### Deletion:

All resources can be deleted from ansible if "state" is set to "absent" instead of "present". For the resources that do not have a "state" argument, then those would have to be deleted using CLI or AWS console.

### TO DO:
Clamping down access between Frontend ECS and Backend database as well as access from internet
