a = 1234
b = 1234
c = a
print(id(1234), id(a), id(b), id(c))
 
a += 1
b += 1
c = 1235
print(id(1235), id(a), id(b), id(c))
 
#a jak zachowują się zmienne o innych wartościach?
a = 123
b = 123
c = a
print(id(123), id(a), id(b), id(c))
 
#co ze stringami?
s1 = "alamakota"
s2 = "alamakota"
print(id(s1), id(s2))

s3 = "ala ma kota"
s4 = "ala ma kota"
print(id(s3), id(s4))
