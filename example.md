## encryption
~/crypt$ ls

```README.md  requirements.txt  script.py```

~/crypt$ python3 script.py 

```Choose an option: [0]=Encrypt Message, [1]=Decrypt Message```

```0```

```Input the message you want to encrypt:```

```hello```

```- Your encrypted message is as follows -```

```119:310:186:520:660```

```- Your key is as follows -```

```15:209:78:412:549```

~/crypt$ 

## encryption with -i flag
~/crypt$ ls

```example.md  README.md  requirements.txt  script.py  txt.txt```

~/crypt$ tail txt.txt 

```hello```

~/crypt$ python3 script.py -i txt.txt 

```- Your encrypted message is as follows -```

```378:193:642:517:814:629```

```- Your key is as follows -```

```274:92:534:409:703:619```

~/crypt$ 

## decryption

~/crypt$ python3 script.py 

```Choose an option: [0]=Encrypt Message, [1]=Decrypt Message```

```1```

```Input the encrypted message you want to decrypt. It should only contain numbers and colons. (Ex = 111:2:333)```

378:193:642:517:814:629

```Input your key. It should only contain numbers and colons. (Ex = 111:2:333)```

274:92:534:409:703:619

```- Your decrypted message is below -```

```hello```

~/crypt$ 