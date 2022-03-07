## Crypt
Python version of Crypt (iOS Shortcut), a OTP concept.

The iOS shortcut equivalent for this script may be found on routinehub [https://routinehub.co/shortcut/10927/].

## Usage
This script relies on numpy as a dependency. Install it first with ```pip3 install numpy``` Download the script. Run python3 script.py in a terminal. Follow the prompts given. If you want to pass in a text file to encrypt, use the ```-i``` flag.

## About
This script is meant to provide a sort of encryption for simple messages. Say you want to send someone a text message without someone else being able to read it. You can use this shortcut to send a string of numbers containing the message.

This shortcut was based off of the concept of OTP (One Time Pad), so each letter of message is randomly altered; this shortcut uses addition. As I have not extensively studied encryption methods, I could be completely wrong about OTP. The shortcut seems to work anyway.

The TLDR of the mechanism:

- Split message into letters, spaces, basic punctuation

- Assign numeric value to each split item (ASCII)

- Randomly generate number as key

- Add said random key to aforementioned number


## Example
For example, let's encrypt the string "hello". The shortcut will split each letter apart, creating a list of 

```
h
e
l
l
o
```

Each character is then converted to ASCII, which becomes 

```
104
101
105
105
111
```

For each number, a random "key" is generated, which is a random integer from 2 to 750, wihch is then added to the number in the ASCII list. If for example our keys were generated as 

```
1
2
1
3
4
```

and the shared key was 2, then our final encrypted message is:

```
104 + 1 = 105
101 + 2 = 103
105 + 1 = 106
105 + 3 = 108
111 + 4 = 115
```

Then the encrypted message and the key are combined with colons and exported.

```
encrypted message = 105:103:106:108:115
final key = 1:2:1:3:4
```

To decrypt, run the process in reverse.

```
105 - 1 = 104 = h
103 - 2 = 101 = e
106 - 1 = 105 = l
108 - 3 = 105 = l
115 - 4 = 111 = o
```
