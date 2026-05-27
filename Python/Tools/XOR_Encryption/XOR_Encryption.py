print("Enter the word :")
Word = input()
print("Enter the key :")
Key = input()
def Encryption(Word,key):
    Encrypted_Word = ""
    for i in range (len(Word)):
       Encrypted_Word += chr(ord(Word[i]) ^ ord(Key[i % len(Key)])) 
    return Encrypted_Word
Encrypted_Word = Encryption(Word,Key)
print("Encrypted Word : " + Encrypted_Word)
def Decryption(Encrypted_Word,key):
    Decrypted_Word = ""
    for i in range (len(Encrypted_Word)):
       Decrypted_Word += chr(ord(Encrypted_Word[i]) ^ ord(Key[i % len(Key)])) 
    return Decrypted_Word

Decrypted_Word = Decryption(Encrypted_Word,Key)
print("Decrypted Word : " + Decrypted_Word)