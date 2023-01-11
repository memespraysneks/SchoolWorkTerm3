#lab 6 - Caleb Seeman A01315336

data <- read.csv("~/SchoolWork/Statistics for IT MATH-1350/Assignment 6/W2022_MATH_1350_Lab_06_failures.txt", sep="")

#Question 1
#1a
n <- 400
p <- 0.025

x.vals <- 0:400

x.probs <- dbinom(x.vals, n, p)

plot(x.vals, x.probs, type = "h",
     xlim=c(0,25))

p.hat.vals <- x.vals/n

plot(p.hat.vals, x.probs*100, type = "h",
     xlim=c(0,0.1),
     xlab="p-hat",
     ylib="probability density",
     main="p-hat probability histogram")

mu.p.hat <- p
sig.p.hat <- sqrt(p*(1-p)/n)

norm.x.vals <- seq(0,0.1,0.0001)
norm.pdf.vals <- dnorm(norm.x.vals,mu.p.hat,sig.p.hat)
lines(norm.x.vals, norm.pdf.vals,col="black")

#1b
x <- pbinom(12, n, p) - pbinom(7, n, p)
print(x)

#1c

no_cont <- pnorm(0.03, p, sig.p.hat) - pnorm(0.02, p, sig.p.hat)

cont <- pnorm(12.5/400, p, sig.p.hat) - pnorm(7.5/400, p, sig.p.hat)

#Question 2
#2a

hist(data$X.fail,
     freq=FALSE,
     main="Frequences of X fail",
     xlab="Number of failures")
#2b

lambda <- mean(data$X.fail)
sd.X.fail <- sd(data$X.fail)
#2c

x.vals = seq(0,8,0.1)

p.vals <- dpois(x.vals, lambda)

lines(x.vals,
      p.vals,
      type="p",
      pch="x",
      col="blue")
#Question 3
#3a

simamount <- 10^5
n <- 50
list.mean <- c()
for (i in 1:simamount){
  current.sample <- sample(data$X.fail, n)
  list.mean[i] <- (mean(current.sample))
}
hist(list.mean,
     breaks = seq(0.5,2.5,0.1),
     freq = FALSE)
x.values <- seq(0.5,2.5,0.1)
#3b

mu <- mean(list.mean)
sdp <- sd(list.mean)

#3c

lines(x.values,
      dnorm(x.values,mean=mu,sd=sdp),
      type="l",
      color="red")

#3d

mu-2*sdp
mu+2*sdp
