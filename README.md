# crypto

Read - https://cryptohack.gitbook.io/cryptobook/fundamentals/

Read - https://bitsdeep.com/posts/attacking-rsa-for-fun-and-ctf-points-part-2/

Euclidean Alogrithm - https://www.freecodecamp.org/news/euclidian-gcd-algorithm-greatest-common-divisor/

The Extended Euclidean Algorithm - http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html

Phi Exploration - https://www.khanacademy.org/computing/computer-science/cryptography/modern-crypt/pi/euler-totient-exploration

Factoring - http://factordb.com/ , https://www.alpertron.com.ar/ECM.HTM

`>>> from sympy import *`
`>>> factorint(value)`
- Use the above module for factoring!

https://github.com/ryosan-470/factordb-python

Read - https://github.com/ashutosh1206/Crypton

Notes:

### part1: Key Generation

Select  p,q                 p and q are prime numbers; p!=q

Calculate n               n = p * q

Calculate phi(ϕ)       ϕ = ( p - 1 ) * ( q - 1 )

Select integer e       GCD ( ϕ(n) , e ) = 1; 1 < e < ϕ(n)

Calculate d               d = inverse(e) % ϕ(n)

Public Key (Pk)         {e,n}

Private Key (Pr)        {d,n}


### Part2: Encryption       

Plain Text (M)           M < n

Cipher Text (C)         C = pow( M , e) % n

Part3: Decryption

Cipher Text (C)          C

Plain Text (M)            M = pow(C , d) % n
