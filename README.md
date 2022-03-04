## crypt
Python version of Crypt (iOS Shortcut).

The iOS shortcut equivalent for this script may be found on routinehub [https://routinehub.co/shortcut/10927/].

This script is meant to provide a sort of encryption for simple messages. Say you want to send someone a text message without someone else being able to read it. You can use this shortcut to send a string of numbers containing the message.

This shortcut was based off of the concept of OTP (One Time Pad), so each letter of message is randomly altered; this shortcut uses simple math. As I have not extensively studied encryption methods, I could be completely wrong about OTP. The shortcut seems to work anyway.

The TLDR of the mechanism:

- Split message into letters, spaces, basic punctuation

- Assign numeric value to each split item (ASCII)

- Randomly generate number as key

- Multiply said random key with aforementioned number

- Implementation of shared key, derived from previous work and concepts of my shortcut “Encrypt”. The key generated from the shortcut cannot decrypt correctly without the use of a shared and preset numeric key. This was implemented to enhance key security.

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

For each number, a random "key" is generated, which is a random integer from 2 to 350. The shared private key is multiplied to that random number to create a final key, wihch is then multiplied to the number in the ASCII list. If for example our keys were generated as 

```
1
2
1
3
4
```

and the shared key was 2, then our final encrypted message is:

```
104 * 1 * 2 = 208
101 * 2 * 2 = 404
105 * 1 * 2 = 210
105 * 3 * 2 = 630
111 * 4 * 2 = 888
```

Then the encrypted message and the key are combined with colons and exported.

```
encrypted message = 208:404:210:630:888
final key = 2:4:2:6:8
```

To decrypt, run the process in reverse.
