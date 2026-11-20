# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple)


# i = (10,20,30,40,50)
# print(len(i))

# my_tuple = (10,20,30,40,50)
# # while True:
# #     print(len(my_tuple))
# #     my_tuple+=1 
# i = 0
# while i < len(my_tuple):
#         print(my_tuple[i])
        
#         i+=1

# my_tuple = [10,20,30,40,50]
# print(my_tuple[1])

# t = 2,5,6 # three values are packed in one object
# print(t)

# a,b,c = t 
# print(a,b,c) #values in t are unpacked and assigned to a,b,c

# a,b = t
# print(t) #values in t are unpacked and assigned to a,b

#write a program that convert a list into a tuple and vice 

my_list = [1, 2, 3, 4, 5]
t=()
for i in my_list:
    t = t + (i,)
print(t) #convert list into tuple    
