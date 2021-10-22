# Week2
### Naive Cipher:
used rot5 for dixoae{oczz_ocz_hvnozm_ja_xvznzm_xdkczm}
flag: `inctfj{thee_the_master_of_caeser_cipher}`

### Multi encoder:
I can see there's a loop that repeats 5 times, encoding the flag to base64 and then to hex.To undo the process, we need to decode in reverse order, from hex and then from base64.And repeat it 5 times as it was done to encrypt
```python
f=b'textinthefile'
from codecs import decode
for i in range(5):
    f=decode(f, 'hex')
    f=decode(f, 'base64')
print(f)
flag: b'inctfj{Y0u_@re_Qu1t3_th3_D3c0d3r}'
```
### Angry Steves
i just used strings <image name>
and got the flag: `inctfj{string5_m4keth_fl4gs}`

### can-the-cat
used foremost and opened output files and found the flag
`inctfj{y0u_c4nt_s33_m3!!}`

### base base base
R1k0U0FOVEZFQTNER0lCWEdRUURNTlJBR1pRU0FOM0NFQTNERUlCVEdRUURPTVpBR01aU0FOWlRFQTJXTUlCVEdRUURPTVJBR01aU0FOTEdFQTNER0lCVEdBUURHTUJBR01ZQ0FNWlFFQVpUQUlCVEdBUURHTUJBR01ZQ0FOVERFQTNXST09PQ==
first base64 and again base64 i found some numbers 69 6e 63 74 66 6a 7b 62 34 73 33 73 5f 34 72 33 5f 63 30 30 30 30 30 30 30 30 6c 7d
it seems to be hexedit 
on decoding it 
`inctfj{b4s3s_4r3_c00000000l}`

### Snow Snow
used stegsnow -C
$stegsnow -C -p thisiseasy flag.txt
aW5jdGZqe2g0aDRfc3QzZ3NuMHdfaTVfYzAwMDAwMDAxfQ==
$echo 'aW5jdGZqe2g0aDRfc3QzZ3NuMHdfaTVfYzAwMDAwMDAxfQ==' | base64 -d
`inctfj{h4h4_st3gsn0w_i5_c00000001}`

### Single Byte XOR
used https://www.dcode.fr/xor-cipher and put the ascii key as z
`flag: inctfj{x0r_c4n't_b3_e4sily_br0k3n}`

### Mischief Kid
I compared the hex bytes from the other image with that one
Found some missing bytes....To correct the image we added them back
Used hexeditor -b busted.png
`flag : inctfj{_4Ye_@aRrAmbB4_u_g0T_m3!}`

## C programming
1.Learn about Caesar cipher and implement it in C.
Encryption:
```cpp
#include<stdio.h>
int main()
{
      int i, key;
      char text[100],c;
      printf("\nCaesar Cipher - Encryption");
      printf("\nEnter Message To Encrypt : ");
      gets(text);
      printf("\nEnter Key : ");
      scanf("%d", &key);
      for(i=0;text[i]!='\0';++i)
      {
            c=text[i];
      if(c>='a'&&c<= 'z')
            {
                  c=c+key;
                  if(c>'z')
                  {
                        c=c-'z'+'a'-1;
                  }
                  text[i]=c;
            }
            else if(c>='A'&&c<='Z')
            {
                  c=c+key;
                  if(c>'Z')
                  {
                        c=c-'Z'+'A'-1;
                  }

            text[i]=c;
            }
      }
      printf("\nEncrypted Message : %s", text);
	  return 0;
}
```

Decrytion:
```cpp
#include<stdio.h>
void main()
{
    int i, key;
    char text[100],c;
    printf("\nCaesar Cipher- Decryption");
    printf("\nEnter Message To Decrypt : ");
    gets(text);
    printf("\nEnter Key : ");
    scanf("%d", &key);
    for(i = 0; text[i] != '\0'; ++i)
    {
        c = text[i];
        if(c >= 'a' && c <= 'z')
        {
            c = c - key;
            if(c < 'a')
            {
                c = c + 'z' - 'a' + 1;
            }
            text[i] = c;
        }
        else if(c >= 'A' && c <= 'Z')
        {
            c = c - key;
            if(c < 'A')
            {
                c = c + 'Z' - 'A' + 1;
            }
            text[i] = c;
        }
    }
    printf("Decrypted text: %s", text);
}
```

2.Learn about XOR, Implement Single Byte XOR encryption in C.
Encryption:
```cpp
#include <stdio.h>
#include <math.h>
#include <string.h>
int main()
{
    char x[]="Hello";
    char y='s';
    int a=0;

    while (a!=strlen(x))
    {
        int z=x[a]^y;
        printf("%c",z);
        printf("%c",x[0]);
        a++;
    }
    return 0;
}
```

