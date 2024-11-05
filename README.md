# Hashing

This program demonstrates how to securely implement password hashing for storage in database tables.
## Why is this better than storing passwords?


Obviously, storing passwords in plain text is bad, because someone could access the table and read them. Then they can log in as anyone, or try using that password on other sites,like banking or email accounts.

We have to assume that someone might read the table, so we use hashing to make the stored data unusable.

A password hash is a string of characters that we generate using a one-way algorithm. 
A standard hashing algorithm can take a password and generate a random-looking string. We store this in a database instead of the password.
Later on, the user enters their password, we use the same function to regenerate the hash, then compare it with the stored one.
Crucially, we can never reverse the process. A person who has the hash can not find out what the original password was.

## This program 

In this program there are two functions:

hash_password asks the user for a password. It then generates a random salt value https://auth0.com/blog/adding-salt-to-hashing-a-better-way-to-store-passwords/
The password and the salt are entered into a standard hashing algorithm to produce a new hash.
We need to store this hash and the random salt into the database, so that we can check passwords against them in the future.
For convenience, this program combines the salt and the hash into a single string, but you could store them separately.

verify_password woukld be used when someone is logging in. We enter the password guess, and we will check it against the stored value.
To do this, we get the salt we stored earlier (in this example it's the first 64 characters of the stored string) and generate a hash based on the new guess.
If all is well, this should match the hash we got before.

