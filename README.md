# AE3KR-task02-RSAcipher

## task description

RSA is the asymmettric cipher from asymmetric cryptology
Be careful, the principle is so easy, but for implementation there some „traps“
The basic descirption you can of course find on Wikipedia. Base on it you should implemented 
following 5:
1. Generating the public and private key pair
2. Transformation the open text to numeric form
3. Encryption using public key
4. Decryption using private key
5. Transofrmation back from numeric form to text form of open-text
For this cipher is not necessary to ommit any special characters on trasnfer letter to capitalized -> it 
can také anything as input.
Key generating:
1. Two big prime numbers are chosen -> p and q (randomly generated and different)
2. The number n is counted as n = p*q
3. The number phi(n) is counted as from Euler function -> phi(n) = (p-1)*(q-1)
4. The random number e is chosen on the interval (1; phi(n)) -> 1 < e < phi(n), when the 
GCD(e, phi(n) should be equal to 1.
5. Number d is chosen as inverse modulo number to the number e when i sis moduled by 
phi(n) -> similar function to PowerMod from wolfram mathematica should be used.
Public key will be numbers (n, e)
Private key will be numbers (n, d)
Encryption is simple function c = me mod n
Where m - message, c - ciphertext
Decryption is analogious m = cd mod n
kde m - message, c – ciphertex
