# print("hello world!")

# variables and datatypes

# x = "Nikhil Kukreja";
# print(type(x));
# y = 56;
# print(type(y));
# z = str(y);
# print(type(z));
# d = int(z);
# print(type(d));
# x = 20;
# y = 20.5;
# print(type(x));
# print(type(y));
# x = 1j;
# print(type(x))
# z = complex(2,3);
# print(z);
# print(type(z));

# List

# l = ['apple','Banana','Orange']
# print(l[1]);
# l[2] = "kiwi"; #mutable
# print(l);

#tupple

# t = ('apple','Banana','Orange');
# print(t);
# print(t[1])
# #t[2] = "kiwi" #immutable
# print(t);

# range
# l = ['apple','Banana','Orange','kiwi']
# print(l[0:3]);

# dict
# d = {"name" : "nikhil","age" : 20}
# print(d);

# d = dict(name="john",age=22);
# # print(d);

# # print(d["name"]);
# # print(d.get("age"));
# d["name"] = "Nikhil" #mutable
# print(d);

# set

# s = {"Apple","Banana","Orange"};
# print(s);
# isKiwi = "kiwi" in s;
# print(isKiwi);
# for x in s:
#     print(x);

#frozenset

# x = frozenset({'Apple','Banana','Kiwi'})
# print(x);

# # bytes
# x=b"hello";
# print(x);

# # Functions
# def func(x,y):
#     return x+y;
# print(func(3,5));

# import

# import math as m
# print(m.sqrt(25));

# from math import sqrt 
# print(sqrt(25));

#string

# x = "python is cool"
# print(x[2:6]);
# print(x.split(" "));
# print(x.join(","))

# #file
# x = open("my.txt","w");
# x.write("this is my file");
# x.close();
print(x.closed);

y = open("my.txt",'r');
 z = "hello" +" "+ y.read();
print(z);
print(y.closed);
y.close();
print(y.closed);