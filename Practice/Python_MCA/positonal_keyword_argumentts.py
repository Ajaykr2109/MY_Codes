# #Positional Parameter: Message that has to be printed
# #Keyword Parameters: Times that the message has to be printed
# ###################################################################


# # Positional Arguments
# def nprintn(message, n):  # n: numer of times.
#     for i in range(0, n):
#         print(message)  # printing the message n times.


# nprintn("Hello", 3)  # correct
# # in this case error would be there because paramters are reversed.
# nprintn(3, "Hello")

# #Keyword arguements
# # by mentioning the parameters name it'll self organise everything by its own.
# nprintn(n=6, message="hello")


# implimenting by both arguments
x=100
print(id(x))
def si(p,r,t):
    #x=(p*r*t)/100
    x=100
    print(id(x))
    return x
print(si(p=100,r=10,t=2))
#print(si(200,20,5))

#for global use we need write //global// keyword infront of the local variable so that we can access and perform on global variable.