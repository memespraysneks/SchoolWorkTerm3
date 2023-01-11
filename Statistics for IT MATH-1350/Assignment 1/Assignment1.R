library(moments)

library(readxl)

Data <- read_excel("SchoolWork/Statistics for IT MATH-1350/MATH_1350_Lab_01_Data (2).xlsx")


hist(Data$Age, col ="pink",breaks=seq(17.5,35.5,2), xlim=c(15,40),
     xlab="Age (years)", xaxp=c(15,39,24), 
     ylim=c(0,20), main="Histogram of Age (n=58)")

table(Data$Age)

table(Data$Phone.Brand)

pie(table(Data$Phone.Brand), main = "Phone Brands Used (n = 59)",
    col = c("pink", "purple", "red", "blue", "green", "yellow", "orange", "cyan"))
mean(Data$Siblings)
mean(Data$Income.Goal, na.rm = TRUE)
median(Data$Siblings)
median(Data$Income.Goal, na.rm = TRUE)

getmode <- function(v) {
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]
}

getmode(Data$Siblings)
getmode(Data$Income.Goal)

range(Data$Siblings)
range(Data$Income.Goal, na.rm = TRUE)

sd(Data$Siblings)
sd(Data$Income.Goal, na.rm = TRUE)

var(Data$Siblings)
var(Data$Income.Goal, na.rm = TRUE)

skewness(Data$Siblings)
skewness(Data$Income.Goal, na.rm = TRUE)

quantile(Data$Siblings, 0.30)
quantile(Data$Income.Goal, na.rm = TRUE, 0.30)

IQR(Data$Siblings)
IQR(Data$Income.Goal, na.rm=TRUE)