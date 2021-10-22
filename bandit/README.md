### bandit0:

ssh bandit0@bandit.labs.overthewire.org -p 2220

connect to the above port and gave password bandit0

### bandit0:

there is a readme file : `boJ9jbbUNNfktd78OOpsqOltutMc3MY1`

this is the password for the bandit2

### bandit1:

there is a file but named as "-" so used command cat < - to read the file

got new password `CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9`

### bandit2:

here there is a fie but with spaces in between so added \ insted of spaces cat spaces\ in\ this\ filename

the password is `UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK`

### bandit3:

had a folder cd inhere | ls -la(for the hidden files) | cat .hidden

the password is `pIwrPrtPN36QITSp3EQaw936yaFoFgAB`

### bandit4:

cd inhere | ls | cat ./-file00 viewed all the files and found the psasword in file 7

the password is `koReBOKuIDDepwhWk7jZC0RTdopnAYKh`

### bandit5:

find ./ -type f -size 1033c this is used to fing the the file with the specified requirements

it showed the directory as ./maybehere07/.file2 from there cd and cat command will help

password: `DXjZPULLxYr17uwoI01bNLQbtFemEgo7`

### bandit6:

first went to root directory adn then started finding for the file with find command

find . -size 33c -user bandit7 -group bandit6

./var/lib/dpkg/info/bandit7.password(this doesn't required any premissions)

so cat ./var/lib/dpkg/info/bandit7.password got the password: `HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs`

### bandit7:

cat data.txt | gerp millionth

directly got the password : `cvX2JJa4CFALtqS87jk27qwqGhBM9plV`

###bandit8:

sort data.txt | uniq -u

sort - sort lines of text files

uniq - report or omit repeated lines and -u, --unique only print unique lines

password: `UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR`

### bandit9:

strings data.txt | grep =

as there are non printable characters in the file used strings insted of cat

strings - print the strings of printable characters in files.

password:`truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk`

### bandit10:

cat data.txt | base64 -d

when we cat the file it seems to be encoded to base64

base64 - base64 encode/decode data and print to standard output

-d, --decode

The password is `IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR`

### bandit11:

cat data.txt copied and used online decoder for rot13

The password is `5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu`

we can also use tr command cat data.txt | tr 'n-za-mN-ZA-M' 'a-zA-Z'

### bandit12:

too much of unzipping followed online soln

The password is `8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL`

### bandit13:

ssh -i sshkey.private bandit14@localhost

bandit14@bandit:/$ cd /etc/bandit_pass/

bandit14@bandit:/etc/bandit_pass$ cat bandit14

`4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e`

### bandit15:

To submit the password to localhost I used nc command

bandit14@bandit:/etc/bandit_pass$ echo 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e | nc localhost 30000

Correct!

`BfMYroe26WYalil77FoDi9qh59eK5xNr`
