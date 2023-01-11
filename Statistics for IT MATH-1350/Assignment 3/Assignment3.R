library(readxl)
Data <- read_excel("SchoolWork/Statistics for IT MATH-1350/Assignment 2/F2021_MATH_1350_Data.xlsx")

#Part 1

brown_and_car = length(Data$Set[Data$Eye.Colour == "Brown" & Data$Owns.Car == "Yes"])/ nrow(Data)

brown_and_car

brown_with_car = length(Data$Set[Data$Eye.Colour == "Brown" & Data$Owns.Car == "Yes"])/ length(Data$Set[Data$Eye.Colour == "Brown"])

brown_with_car

two_glasses = (sum(Data$Wears.Glasses == "Yes") / nrow(Data)) * ((sum(Data$Wears.Glasses == "Yes") - 1) / (nrow(Data) - 1))

two_glasses

#Part 2


die1 <- sample(c(1,2,3,4,5,6), 10^6, replace = TRUE)
die2 <- sample(c(1,2,3,4,5,6), 10^6, replace = TRUE)
die3 <- sample(c(1,2,3,4,5,6), 10^6, replace = TRUE)
die4 <- sample(c(1,2,3,4,5,6), 10^6, replace = TRUE)

X = (die1 + die2 + die3 + die4)/4

hist(X, freq=FALSE, breaks = seq(0.875, 6.125, 0.25), col = "Purple",
     xaxp = c(1,6,20),
     main = "Histogram of the average of 4 dice after being rolled 10^6 times",
     xlab = "Average of 4 dice"
)

getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}

mode <- getmode(X)
mode

X_between_three_and_four = sum(X >= 3 & X <= 4)
X_between_three_and_four/10^6

#part 3
ages = c(21,19,19,25,23,27,43,24,19,22)

younger_22 = sum(ages <= 22) / length(ages)

younger_22_all = choose(sum(ages <= 22), 4)/choose(length(ages), 4)

answer_3c = c()

all_unique = 0

for (i in 1:10^5){
  new_itteration = sample(ages, 4)
  answer_3c <- append(answer_3c, mean(new_itteration))
  if (length(unique(new_itteration)) == 4){
    all_unique = all_unique + 1
  }
}

hist(answer_3c,
     col = "Purple",
     xlab='Mean of 4 Samples',
     main='Histogram of a 10^5 Samples of Mean Age of Sample Size 4')

under_22 = sum(answer_3c <= 22)/ length(answer_3c)

unique_prob = all_unique/length(answer_3c)