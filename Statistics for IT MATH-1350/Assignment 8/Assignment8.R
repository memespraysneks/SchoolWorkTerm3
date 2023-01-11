data <- read_excel("SchoolWork/Statistics for IT MATH-1350/Assignment 8/F2021_MATH_1350_Data.xlsx")

#Question 1

#1a

plot(data$Siblings, data$Income.Goal,
     xlab = "Number of siblings",
     ylab = "Income goal in $",
     main = "Number of Siblings vs Income Goals")

#2a
data$Siblings[is.na(data$Siblings)] <- 0
data$Income.Goal[is.na(data$Income.Goal)] <- 0

cor.Sib.Income <- cor(data$Siblings, data$Income.Goal)

print(length(data$Siblings))

critical.value <- 1.671
