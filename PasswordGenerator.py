# Last Update: 2024/05/04
# Author: Luke Kaser
# Description: A simple password generator program 
# E-mail: qaz442200156@gmail.com
import secrets

sample_to_generate = 11
while True:
    command = input("How long does generator to crate password ?")
    
    if command.isnumeric():
        length = int(command)
        if length <= 0:
            print("Input length must large than 0")
            continue
        for x in range(sample_to_generate):
            # API , Generate result
            # secrets.token_urlsafe => 'Drmhze6EPcv0fN_81Bj-nA'
            print(secrets.token_urlsafe(length)[:length])
            # secrets.token_hex => 'f9bf78b9a18ce6d46a0cd2b0b86df9da'
            #print(secrets.token_hex(length)[:length])
            # secrets.token_urlsafe => b'\xebr\x17D*t\xae\xd4\xe3S\xb6\xe2\xebP1\x8b'
            #print(secrets.token_bytes(length)[:length])
        break