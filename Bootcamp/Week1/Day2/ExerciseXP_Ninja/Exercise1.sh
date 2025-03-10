#!/bin/bash

# Exercise 1 : Use the terminal
#Instructions
#
#    Run this command in the terminal to open a python console:
#
#$ python3
#
#    Read about the PATH variable. Try to explain why you can call python3 if you aren’t in the executable directory.

echo $PATH
#/home/liliane/perl5/bin:/home/liliane/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin:/home/liliane/.local/share/JetBrains/Toolbox/scripts
whereis python3
#python3: /usr/bin/python3 /usr/lib/python3 /etc/python3 /usr/share/python3 /usr/share/man/man1/python3.1.gz

#The PATH variable is an environment variable that contains directories where executable are.+