import hashlib
MyMd5 = hashlib.md5()
MyMd5.update("AA")
MyMd5.update("BBCCDD")
print MyMd5.hexdigest()
