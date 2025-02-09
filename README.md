# flask-microservice-deploymentment
Deploying flask api using multiple VMS

Download virtual box based on your os host from here https://www.virtualbox.org/wiki/Downloads
Install it
Download SHO file from here
https://puppylinux-woof-ce.github.io/

Create a new VM (PUPPY LINUX) on virtual box 
Config: 2 GM RAM
16 GB DISK
2 Cores
Add SHO file
Start

Clone another VM (PUPPY LINUX)

Connect network using settings network bridged adapter. 
Create app.py using flask and python in one VM
Create client.py using request module and python in another VM

app.py client.py are present in the git.

