import sys
from tkinter import filedialog
import tkinter as tk
from cryptography.fernet import Fernet
import time
import os
import ctypes

##################################################################
#                    File format for pw.txt
# Line 1: 'e' or 'd' (to denote encryption or decryption)
#
# Line 2: path to the 'hashholder.txt' file
#       (where the csv will be held to encrypt)
# Line 3: key (for decryption only; no key for encryption)
#
##################################################################

class InvalidInstructions(Exception):
  pass

class InvalidKey(Exception):
  pass


def encrypt(filename):
  # assign the key
  key = Fernet.generate_key()

  with open('filekey.key', 'wb') as filekey:
    filekey.write(key)
  fernet = Fernet(key)

  # read the file
  with open(filename, 'rb') as file:
    originalfile = file.read()
  
  # encrypt the file
  encrypted = fernet.encrypt(originalfile)

  # write the encrypted data to the file
  with open(filename, "wb") as encrypted_file:
    encrypted_file.write(encrypted)

  # prompt the user to save the file to their local machine
  savefile = filedialog.asksaveasfile(mode='wb', defaultextension=".csv", filetypes=[("csv file(*.csv)", "*.csv"), ("csv file(*.csv)", "*.csv")])
  if savefile:
    with open("hashholder.txt", "rb") as infile:
      data = infile.read()

    with open(savefile.name, "wb") as outfile:
      outfile.write(data)
  else:
    return

  # read the encryption key
  enckeyfile = open('filekey.key', "rb")
  enckey = enckeyfile.read()

  # Display the encryption key to the user
  root = tk.Tk()
  root.title("DO NOT LOSE ME")
  label = tk.Label(root, text="Your Encryption Key:")
  entry = tk.Entry(root, width=50)
  label.pack(side="left")
  entry.pack(side="right", padx=10, pady=20)
  entry.insert(0, enckey.decode("utf-8"))
  entry.configure(state='readonly')
  root.mainloop()

  print(key)


def decrypt(filename, key):

  # assign the key
  fernet = Fernet(key)

  with open(filename, 'rb') as enc_file:
    encrypted = enc_file.read()

  # decrypt the file
  decrypted = fernet.decrypt(encrypted)

  with open(filename, 'wb') as dec_file:
    dec_file.write(decrypted)



# loop until we are prompted to encrypt/decrypt

def process_instructions():
  while (os.path.getsize('pw.txt') == 0):
    time.sleep(1)
  # open the file
  f = open("pw.txt", "r")

  code = f.readline()
  if code[0] == 'e':      # encrypt the file
    fn = f.readline()
    encrypt(fn)
    f.close()

    # clear the file
    cf = open("pw.txt", "w")
    cf.write("")
    cf.close()

  elif code[0] == 'd':    # decrypt the file
    fn = f.readline()
    fn = fn[:len(fn) - 1]
    key = f.readline()
    if len(key) != 44:
      raise InvalidKey
    decrypt(fn, key)
    f.close()

    # clear the files
    cf = open("pw.txt", "w")
    cf.write("")
    cf.close()
    cf = open("filekey.key", "w")
    cf.write("")
    cf.close()


  else:                 # error
    raise InvalidInstructions

while True:
  process_instructions()
