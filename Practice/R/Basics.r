t <- c(1, 2, 3, 4, 5)
length(t)

strvector <- c("Hello", "Ajay", "Kumar", "gautam", "Holllaa")
rep(strvector, each = 5)
strvector
t <- rep(2:5, 10)
t

t <- rep(t, times = 4)
t

rep(strvector, each = 5)

# arithmetic operators
i <- c(2, 6, 8, 7, 8, 9)
j <- c(8, 5, 6, 4, 7, 8)
i %% j
i - j
i + j
i * j
i / j
x <- c(5, 6, 7, 8, 10, 19)
sd(x)

# for loop
for (i in 1:5) {
  print(i)
}

for (i in range(1, 5)) {
  print(i)
}

# while loop
while (i < 5) {
  print(i)
  i <- i + 1
}

# repeat loop
im <- 1
repeat {
  print(im)
  im <- im + 1
  if (im > 5) {
    break
  }
}

# ^ power symbol
for (n in 1:5) {
  print(n^2)
}

num <- c(1, 2, 3, 4, 5)
for (n in num) {
  print(n^2)
}

print(num)

x <- c(37, 52, 2, 4, 36, 5, 6, 8)
for (i in x) {
  print(x[i])
}

# in-built functions
sum(i)
mean(i)
max(i)
min(i)
length(i)
sd(i)
mode(strvector)
sort(strvector)
sort(strvector, decreasing = TRUE)
order(strvector)
# it will print the index from smallest to largest


# if else
x <- c(5)
if (x > 0) {
  print("Positive")
} else if (x < 0) {
  print("Negative")
} else if (x == 0) {
  print("Zero")
} else {
  print("Invalid")
}

# gratest among three numbers
x <- c(5)
y <- c(6)
z <- c(7)
if (x > y & x > z) {
  print("x is greater")
} else if (y > x & y > z) {
  print("y is greater")
} else if (z > x & z > y) {
  print("z is greater")
} else {
  print("Invalid")
}

# 1.print the name of the day if elseif
# 2.program to print name of the month
# 3.number is even and greater than 20

letters[1:5]
# to print the consecutive letters

# checking the location of the elements
which.min(i)
which.max(i)

# passing negative value to the vector will remove the element from passed argument
t <- c(1, 2, 3, 4, 5, 6, 7, 8, 9)
t[-2]
t
t[c(TRUE, FALSE, TRUE, FALSE, FALSE)]
t[c(1, 5, 8)]
strvector[c(TRUE, FALSE)]

# rep() with both parameters as vectors
rep(strvector, c(1, 2, 3, 4, 5))


which.min(t)
min(which.max(t))

x[2] <- 9
x # inserting a value at an index
x[3] <- NA
sum(t, na.rm = TRUE)

# list in R its a hetrogenous type of datatype which can store string or integral value
numlist <- list(1, 3, 4, 5, 7, 8, 9)
numlist

list1 <- list("a", "b", "c")
list1

strlist <- list("pen", "book", "laptop")
strlist

loglist <- list(TRUE, FALSE, FALSE, FALSE, TRUE)
loglist

comlist <- list(3 + 4i, 7 + 3i)
comlist

mlist <- list("laptop", "pen", 2, 4, 7, 5, TRUE, c(24, 45, 67))
mlist
45 %in% mlist


vlist <- list("mac", "phone", seq(1, 5, by = 2), 3:7, FALSE)
vlist
vlist[3]
vlist[3] <- TRUE
length(vlist)
"phone" %in% vlist # to check its in the list or not element(%in%)list_name

vlist <- append(vlist, "welcome", after = 2)
vlist

vlist <- vlist[-2]
vlist

# converting the list into vector
unlist(vlist)

vlist[c(1, 2, 3)]
vlist[2:5]

# looping concepts
for (y in vlist) {
  print(vlist[y])
}

# matrix
# two dimensional arrya
# it will only store homogenous type of data

# matrix(data,nrow,ncol,byrow,dimnames)

# data; is the value
# nrow: number of rows
# ncol: number of columns
# byrow: TRUE or FALSE to save the records in row wie or column wise



matrix(1:9, nrow = 3, ncol = 3)
matrix(
  c(22, 33, 99, 1, 2, 3, 55, 100, 4),
  nrow = 3,
  ncol = 3,
  byrow = TRUE
)
matrix(seq(1:12), nrow = 4, ncol = 3)
matrix(seq(1:12), nrow = 3, ncol = 4)
matrix(seq(1:12), nrow = 6, ncol = 2)
matrix(seq(1:12), nrow = 2, ncol = 6)

m <- matrix(
  1:12,
  nrow = 3,
  ncol = 4,
  byrow = FALSE,
  dimnames = list(c("ROw1", "ROW2", "ROW3"), c("a", "b", "c", "d"))
)

rownames(m) <- c("R1", "R2", "R3")
colnames(m) <- c("C1", "C2", "C3", "C4")
m

cbind(c(1, 2, 3, 4), c(4, 5, 6, 7))
rbind(c(1, 2, 3, 4), c(4, 5, 6, 7))

# matrix(i, nrow = 2)
# i <- dim(i) <- c(3, 2)
# i

print(m[1, 2])
print(m[, 2])
print(m[1, ])

# merge two matrix
m1 <- matrix(1:12, nrow = 3, ncol = 4, byrow = FALSE)
m2 <- matrix(1:12, nrow = 3, ncol = 4, byrow = FALSE)
m3 <- cbind(m1, m2)
m3

# data frames hetrogenous type
a <- c(1, 2, 3, 4, 5)
b <- c(2 + 3i, 5 + 1i, 6 + 8i, 3 + 5i, 6 + 8i)
c <- c(TRUE, FALSE, TRUE, FALSE, FALSE)
d <- c(1L, 2L, 3L, 4L, 5L)
e <- c("ajay", "kumar", "chaturvedi", "D2117", "A01")

df <- data.frame(a, b, c, d, e)
summary(df) #
str(df) # structure of the data frame


df1 <- data.frame(Training = c("Strength", "Stamina", "Other"), Pulse = (c(100, 150, 120)), Duration = c(60, 30, 45))
df1[1] # to print the first row
df1[["Training"]] # to print the column
df1$Training # to print the column

newdf <- rbind(df1, c("ABC", 140, 25))
newdf
df1

nncol <- cbind(df1, Result = c(TRUE, FALSE, TRUE))
nncol
df1[-c(1), -c(1)] # to remove the row and column

dim(df1) # to print the dimension of the data frame'
nrow(df1) # to print the number of rows
ncol(df1) # to print the number of columns
length(df1) # to print the column numbers

# stats
# # b <- c(82, 83, 97, 55, 67, 53) #front
# # sd(b)
# # mean(b)
# # var(b)

# # a <- c(83, 78, 68, 61, 77, 54, 69, 51, 63) #middle
# # sd(a)
# # mean(a)
# # var(a)

# # c <- c(38, 59, 55, 66, 45, 52, 52, 61)
# # sd(c)
# # mean(c)
# # var(c)

# install.packages()
.libPaths()


x <- c(10, 20, 30, 40)
pie(x)

# pie(variable,label,main(title),)
barplot(x)

 data <- read.csv("C:/Users/ajay/Desktop/ajay.csv") #to read the csv file
# data1 <- read.excel("C:/Users/ajay/Desktop/ajay.xlsx") #to read the excel file

install.packages("rmarkdown")
``