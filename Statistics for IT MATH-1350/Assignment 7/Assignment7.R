data <- read.csv("~/SchoolWork/Statistics for IT MATH-1350/Assignment 7/W2022_MATH_1350_Lab_06_failures.txt", sep="")

s.var <- function (X) (1/(length(X)-1))*sum((X-mean(X))^2)
p.var <- function (X) (1/length(X))*sum((X-mean(X))^2)

#Question 1

#1a
pop.var <- p.var(data$X.fail)

#1b
sim.amount <- 10^5
n <- 5

s.current <- c()
p.current <- c()

for (i in 1:sim.amount){
  this.sample <- sample(data$X.fail, n)
  s.current[i] <- s.var(this.sample)
  p.current[i] <- p.var(this.sample)
}

#Question 2

#2a

X.example <- c(2, 2, 1, 0, 3, 1, 1, 1, 3, 2)

X.example.mean <- mean(X.example)

X.example.length <- length(X.example)

X.example.sd <- sd(X.example)

Error.95 <- qnorm(0.975)*X.example.sd/sqrt(X.example.length)

Left.95 <- X.example.mean - Error.95

Right.95 <- X.example.mean - Error.95

#2b

Error.90 <- qnorm(0.95)*X.example.sd/sqrt(X.example.length)

Left.90 <- X.example.mean - Error.90

Right.90 <- X.example.mean - Error.90

#Question 3

Defect <- c(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

#3a

Defect.mean <- mean(Defect)

Defect.sd <- sd(Defect)

Defect.length <- length(Defect)

Error.defect <- qnorm(0.995)*Defect.sd/sqrt(Defect.length)

Defect.left <- Defect.mean-Error.defect

Defect.right <- Defect.mean-Error.defect

