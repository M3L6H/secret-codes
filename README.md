<h1 align="center">Secret Codes</h1>

Repository containing a number of encoding/decoding programs.

Currently implemented are:

- [Caesar Cipher](https://github.com/M3L6H/secret-codes/blob/main/caesar_cipher.rb)
- [Vigenere Cipher](https://github.com/M3L6H/secret-codes/blob/main/vigenere_cipher.rb)

## Caesar Cipher

A Caesar Cipher is one of the most common forms of ciphers. It is a form of substitution cipher in which each letter is replaced with the corresponding letter some offset away. An example would be if we wanted to transform "cat" with an offset of 3, we would end up with "fdw". Decoding the message follows the same process, but with a negative version of the original offset. 

The Caesar Cipher is a relatively weak cipher. One of the issues is that if one correct mapping is discovered (i.e. "a" is found to map to "h"), then the entire message can be decoded. Furthermore, it is also problematic in that the mapping rule is so simple. Because each letter is mapped by a fixed offset, even when encrypted, the words in the message still retain their patterns (i.e. "vacuum" mapped with an offset of 5 becomes "afhzzr"), which also makes the code easier to crack.

Despite these flaws, the Caesar Cipher is still a very good way to introduce the idea of encrypting messages because of its simplicity and ease of use. Additionally, a physical solution can be made by creating two discs - one smaller than the other - with the alphabet on their perimeter. By rotating the discs, one can create a mapping of letters which is itself a Caesar Cipher.
