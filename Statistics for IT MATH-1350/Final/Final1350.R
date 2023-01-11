#This is so doomed

CPU_data <- read_excel("SchoolWork/Statistics for IT MATH-1350/Final/CPU.data.xlsx")

print(249/2)

IQR(CPU_data$MSRP.CAD)
m <- mean(CPU_data$MSRP.CAD)
quantile(CPU_data$MSRP.CAD, 0.5)
s <- sd(CPU_data$MSRP.CAD)

skew <- 3*(m-533.5)/s

hist(CPU_data$MSRP.CAD)

a3 <- 12/40*11/39*10/38*9/37*8/36+28/40*27/39*26/38*25/37*24/36

b3 <- 1-((choose(12,5)/choose(40,5))+choose(28,5)/choose(40,5))

a4 <- dbinom(28,40,0.725)

b4 <- pbinom(31,40,0.725)-pbinom(24,40,0.725)

0.7*40

c4 <- pbinom(30,40,0.725) - pbinom(28,40,0.725)

a5 <- dbinom(0,100,0.25)

b5 <- pbinom(30,100,0.25) - pbinom(9,100,0.25)

length(CPU_data$Clock.Speed.GHz)

CPU_data$Clock.Speed.GHz

a6mean <- mean(CPU_data$Clock.Speed.GHz)
a6sd <- sd(CPU_data$Clock.Speed.GHz)

prop.test(CPU_data$Clock.Speed.GHz, CPU_data$Clock.Speed.GHz, conf.level=0.9)

qt((1-0.10/2),40-1)

a6E <- 1.685*3.061/sqrt(40)
3.39+0.8155

final <- c(rep.int(TRUE,28), rep.int(FALSE,12))

sd(CPU_data$Heat.Output.Watts)

mean(CPU_data$Heat.Output.Watts)

help(t.test)

t.test(CPU_data$Heat.Output.Watts,mu=50,conf.level=0.05)

help(cor)

cor(CPU_data$Clock.Speed.GHz, CPU_data$MSRP.CAD)

cor.test(CPU_data$Clock.Speed.GHz, CPU_data$MSRP.CAD)

model <- lm(CPU_data$MSRP.CAD~CPU_data$Clock.Speed.GHz)

help(lm)

model <- lm()

help(formula)

plot(CPU_data$Clock.Speed.GHz, CPU_data$MSRP.CAD)

530-(326.5 + 83.13*3.75)

0.9332-0.0668

1-(choose(12,5)/choose(40,5))-(choose(12,4)*choose(28,1)/choose(40,5))
help(t.test)

t.test(CPU_data$Brand, mu=0.5, var.equal=TRUE, conf.level=0.05)

t.test(c(rep.int(1,28),rep.int(0,12),mu=0.5,conf.level=0.95))
       