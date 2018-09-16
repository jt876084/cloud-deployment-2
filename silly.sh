#!/bin/bash

echo "This is a silly script" > /tmp/silly.txt

sudo yum clean all
suo yum -y update
sudo yum -y install httpd

sudo firewall-cmd --permanent --add-port=80/tcp
sudo firewall-cmd --permanent --add-port=443/tcp
sudo firewall-cmd --reload

sudo systemct1 start httpd

echo "Successfully installed and running apache2"
