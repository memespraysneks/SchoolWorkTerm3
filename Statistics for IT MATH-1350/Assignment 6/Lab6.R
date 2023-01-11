#Lab 6

#data <- read.csv("C:/Users/caobe/Downloads/W2022_MATH_1350_Lab_06_failures.txt", sep="")

#Question 1
#1a
n <- 400
p <- 0.025 #Success means need technical support

#define x = number of successes in sample
x.vals <- 0:400

#probabilities of each x values
xprobs <- dbinom(x.vals, n, p)

#plot the histogram of x
plot(x.vals, xprobs, type = "h",
     xlim=c(0,30))

p.hat.vals <- x.vals/n

plot(p.hat.vals, xprobs*100, type="h",
     xlim=c(0,0.1),
     xlab="p-hat",
     ylab="Probabilitiy density",
     main="Prob Histogram of p-hat")

#parameters
mu.phat <- p
sig.phat <- sqrt(p*(1-p)/n)

norm.x.vals <- seq(0, 0.1, 0.001)
norm.pdf.vals <- dnorm(norm.x.vals, mu.phat, sig.phat)

lines(norm.x.vals, norm.pdf.vals, col="black")

#1b
#P(2% <= p.hat <= 3%)
#P(8 <= x <= 12)

x <-  pbinom(12, n,p) - pbinom(7, n, p)
print(x)

#1c

#normal approx
without_cont <- pnorm(0.03,p, sig.phat) - pnorm(0.02, p, sig.phat)

cont <- pnorm(12.5/400, mu.phat, sig.phat) - pnorm(7.5/400, mu.phat, sig.phat)

#2a
hist(data$X.fail, freq=FALSE,
     main="Frequency of X.Fail",
     xlab = "Number of Failures")
#2b
lambda <- mean(data$X.fail)
sd(data$X.fail)

#2c
x.vals = seq(0, 8, 1)
p.vals <- dpois(x.vals, lambda)

lines(x.vals,
      p.vals,
      type="p",
      pch="x",
      col="red"
)

#3a
simsize <- 10^5
n <- 50
list_mean <- c()
for (i in 1:simsize){
  this.sample <- sample(data$X.fail, n)
  list_mean[i] <- (mean(this.sample))
}

hist(list_mean,
     breaks = seq(0.5, 2.5, 0.1),
     freq = FALSE)

x.values <- seq(0.5, 2.5, 0.01)

#3b
mu <- mean(list_mean)
sdp <- sd(list_mean)

#3c

lines(x.values,
      dnorm(x.values, mean=mu, sd=sdp),
      type="l",
      col="red")

#3d
mu-2*sdp
mu+2*sdp