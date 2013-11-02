import hashlib

m = hashlib.md5()
sig = '80188fae05444929' + 'api_key' + '4742b7951c4eb4932ac58150295f8902' + 'perms' + 'read'
m.update(sig)


hashSig = m.hexdigest()
url = 'http://flickr.com/services/auth/?api_key=4742b7951c4eb4932ac58150295f8902&perms=read&api_sig=' + hashSig
print hashSig
