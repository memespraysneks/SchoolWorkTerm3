data <- read_excel("C:/Users/caleb/Downloads/CPU.data.xlsx")

meanClock <- mean(data$Clock.Speed.GHz)


varianceClock <- var(data$Clock.Speed.GHz)

percentile80Clock <- quantile(data$Clock.Speed.GHz, 0.80)

rangeClock <- range(data$Clock.Speed.GHz)

IQRClock <- IQR(data$Clock.Speed.GHz)

IQRClock2 <- quantile(data$Clock.Speed.GHz, 0.75) - quantile(data$Clock.Speed.GHz, 0.25)

upperLimit <- quantile(data$Clock.Speed.GHz, 0.75) + 1.5*IQRClock

lowerLimit <- quantile(data$Clock.Speed.GHz, 0.25) - 1.5*IQRClock

sdCache <- sd(data$Cache.MB)

meanCache <- mean(data$Cache.MB)

zscoreCache <- (6.5-meanCache)/sdCache

zscoreAllCaches <- c()

for (i in data$CPU.Cores){
  zscoreAllCaches <- append(zscoreAllCaches, (i-meanCache)/sdCache)
}

print(zscoreAllCaches)

proportionzscore <- 0

for (i in zscoreAllCaches) {
  if (-2<= i & i<=2){
    proportionzscore <- proportionzscore + 1
  }
}


PX100 <- dbinom(100,200,0.5)

P95 <- 1- pbinom(94, 1, 5)

P105 <- pbinom(105, 1, 5)

print((28/40)^3)

prob3intel <- choose(28, 3)/choose(40,3)

permutationCPU <- (factorial(8)/6)

not8 <- 1-((choose(1,1)*choose(7,4))/choose(8,5))

dice3 <- 6^3

odds6 <- 10/216

oddless5 <- 4/216


