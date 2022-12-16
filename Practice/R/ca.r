#create a data frame and read it. Show rbind and cbind functions
#CA 2

data_frame <- data.frame(
  Numeric = c(1, 2, 3, 4, 5),
  Complex = c(2+3i, 5+1i, 6+8i, 3+5i, 6+8i),
  Logical = c(TRUE, FALSE, TRUE, FALSE, FALSE),
  Long = c(1L, 2L, 3L, 4L, 5L),
  Character = c("ajay", "kumar", "CA2", "D2117", "A01")
)
data_frame
df1 <- rbind(data_frame, c(6, 5+3i, TRUE, 6L, "D2117"))
df2 <- cbind(data_frame, Numeric10s = c(10, 20, 30, 40, 50))

data_frame
df1
df2

#installing package to read excel file
# install.packages("readxl")
# excel_file <- read.csv("C:/Users/ENGEE/Desktop/CA2.csv")
# excel_file
# excel_file[["CCA3"]]

# install.packages("rmarkdown")
