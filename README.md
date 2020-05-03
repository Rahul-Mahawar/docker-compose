# docker-compose
This is a TUI program build using python language. This project based on docker-compose using multitier architecture. In this project a user can launch multiple web servers according to his/her choice.
## Project Title:
This is TUI program were you can acces your data of web server using multitier architecture.  In this program user can choose from the given options to launch the web server he/she want. Here each web server is running on different port numbers , so user can launch multiple web servers simultaneously without doing it manually.

## Docker Installation  / Requirements on Redat Linux OS:
Yum configuration for adding docker repo using "https://download.docker.com/linux/centos/docker-ce.repo" put this link in the file in /etc/yum.repos.d/

![alt text](https://github.com/Rahul-Mahawar/docker-compose/blob/master/repo_directory.png)
![alt text](https://github.com/Rahul-Mahawar/docker-compose/blob/master/docker_repo.png)

Run the command given below
``` html 
yum install docker-ce
```

## Start Docker:
``` html
systemctl start docker
```

## Installing Docker Compose:
``` html
curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```
# Cloning this Project:
``` html
git clone https://github.com/Rahul-Mahawar/docker-compose.git
```
## Run the python file:
``` html
python3 myproject.py
```
![alt text](https://github.com/Rahul-Mahawar/docker-compose/blob/master/view.png)

> Now everything is set up
> choose the option to launch your web server

![alt text](https://github.com/Rahul-Mahawar/docker-compose/blob/master/web01.png)
![alt text](https://github.com/Rahul-Mahawar/docker-compose/blob/master/web02.png)
![alt text](https://github.com/Rahul-Mahawar/docker-compose/blob/master/web03.png)

## Build With:
- Redhat 8 running in virtual box
- docker
- docker-compose
- docker images
  - wordpress
  - mysql
  - joomla
  - drupal
  - nextcloud
  - owncloud
  - ghost
  
## Author:
Rahul Mahawar
