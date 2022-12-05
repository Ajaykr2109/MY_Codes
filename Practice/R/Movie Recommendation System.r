#Credit Card Fraud Detection by using R
# install.packages("caret")
# install.packages("ranger")
# install.packages("data.table")
# install.packages("caTools")
library(ranger)
library(caret)
library(data.table)
creditcard_data <- read.csv("C:\\Users\\ENGEE\\OneDrive\\Desktop\\creditcard.csv")
dim(creditcard_data)
head(creditcard_data,6)
tail(creditcard_data,6)
table(creditcard_data$Class)
summary(creditcard_data$Amount)
names(creditcard_data)
var(creditcard_data$Amount)
sd(creditcard_data$Amount)

head(creditcard_data)
creditcard_data$Amount=scale(creditcard_data$Amount)
NewData=creditcard_data[,-c(1)]
head(NewData)

library(caTools)
set.seed(123)
data_sample = sample.split(NewData$Class,SplitRatio=0.80)
train_data = subset(NewData,data_sample==TRUE)
test_data = subset(NewData,data_sample==FALSE)
dim(train_data)
dim(test_data)


Logistic_Model=glm(Class~.,test_data,family=binomial())
summary(Logistic_Model)

plot(Logistic_Model)

