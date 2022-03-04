# crypt
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
