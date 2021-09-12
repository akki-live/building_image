# building_image
building image in docker and pushing to docker hub and creating pods in openshift with the image...


Building image in Docker:

Step 1 - Create a Directory for the Website
Make sure that you have your HTML files already in the current directory.

Step 2 - Create a file called Dockerfile
Place the following contents into the Dockerfile

-> FROM nginx:alpine

-> COPY . /usr/share/nginx/html

These lines of code represent the image we're going to use along with copying the contents of the current directory into the container.

 

Step 3 - Build the Docker Image for the HTML Server
Run the following command:

-> docker build -t html-server-image:v1 .

You can confirm that this has worked by running the command:

-> docker images
==================================================================================
need to add command for Docker to configure ports---pending
==================================================================================
push the image to "https://hub.docker.com/repository/docker/ajs3ra8/akash-app" repository

-> docker push ajs3ra8/akash-app:tagname
===================================================================================
Create deployment and services "akkihtml.yaml" and deploy in OpenShift

-> kubectl create -f akkihtml.yaml