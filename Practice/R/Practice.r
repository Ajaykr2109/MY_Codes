vlist <- list(1, TRUE, "CAP787", "CAP788", 2+5i, FALSE)
vlist[c(3, 6)]

vlist[3] <- "Hello"
vlist <- vlist[-5]
for (x in vlist) {
  print(x)
}

mat <- matrix(1:9, nrow = 3, ncol = 3)
mat

rownames(mat) <- c("A", "B", "C")
colnames(mat) <- c("a", "b", "c")
mat