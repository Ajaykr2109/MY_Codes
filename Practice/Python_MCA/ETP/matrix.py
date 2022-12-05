# Movie Recommendation System using R
# 

install.packages("tm")
install.packages("SnowballC")
install.packages("wordcloud")
install.packages("RColorBrewer")
install.packages("ggplot2")

library(tm)
library(SnowballC)
library(wordcloud)
library(RColorBrewer)
library(ggplot2)

setwd("C:/Users/Owner/OneDrive/Documents/Python_MCA/ETP")

movie_data <- read.csv("movie_metadata.csv")
install.packages("SnowballC")
install.packages("wordcloud")
install.packages("e1071")
install.packages("caret")
install.packages("ROCR")
install.packages("arules")
install.packages("arulesViz")

library(tm)
library(SnowballC)
library(wordcloud)
library(e1071)
library(caret)
library(ROCR)
library(arules)
library(arulesViz)

load the data
movies <- read.csv("movie_metadata.csv")

get a view of the data
head(movies)

get the number of rows and columns
dim(movies)

get the structure of the data
str(movies)

get the summary of the data
summary(movies)

get a list of unique genres
unique(movies$genres)

get the number of unique genres
length(unique(movies$genres))

get a list of unique directors
unique(movies$director_name)

get the number of unique directors
length(unique(movies$director_name))

get a list of unique actors
unique(movies$actor_1_name)

get the number of unique actors
length(unique(movies$actor_1_name))

get a list of unique actors
unique(movies$actor_2_name)

get the number of unique actors
length(unique(movies$actor_2_name))

get a list of unique actors
unique(movies$actor_3_name)

get the number of unique actors
length(unique(movies$actor_3_name))

get a list of unique languages
unique(movies$language)

get the number of unique languages
length(unique(movies$language))

