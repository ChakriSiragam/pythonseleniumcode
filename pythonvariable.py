varl1 = 10
varl2 = 20

print(varl1)
print(id(varl1))
# = assignment operator
# + plus operator

varl3 = varl1 + varl2
print(varl3)


# rules to decalre variable
# 1. there should not be space in variable name
# var 1 : wrong
# varl : correct

#2. can not use number at begining of the var name
# 245var = 800 ; wrong
# chakri21 = 800 ; correct

#python is case sensitive languge
name = 'chakri'
Name = 'sainath'
NAME = 'ramu'
print(name, NAME, Name)

#4  special charcter also not allowed in variable name
# chakri@ = 800 : wrong

#############################################
# assign one value to multiple varibale
p = q = r = 90
print(p,q, r)

# assign different vaues to different at a time
x, y, z = 50, 60, 70
print(x, y, z)


var1 = 100
var2 = 103
print('var1 : address : ', id(var1))
print('var2 : address : ', id(var2))






















