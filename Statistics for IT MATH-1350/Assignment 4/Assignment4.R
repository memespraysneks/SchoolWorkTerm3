#Caleb Seeman A01315336

#1a

all_red <- 25/51 * 24/50 * 23/49 * 22/48

#1b


one_red <- 1 - (choose(26,5)/choose(52,5))

deck.cards <- c(rep("R", 26), rep("B", 26))
count = 0


for (i in 1:10^5){
  this.sample <- sample(deck.cards, 5, replace=FALSE)
  if (sum(this.sample =="R") > 0){
    count = count + 1
  }
  
}

#1c

fullhouse_hands <- (13*choose(4,3)*12*choose(4,2)/choose(52,5))

#2a

two_a <- choose(10, 1) * (0.4^1) * ((1 - 0.4)^(10 - 1))

#2b

two_b <- (1 - choose(10, 0) * (0.4^0) * ((1 - 0.4)^(10 - 0)))

#2c

two_c <- choose(10, 4) * (0.4^4) * ((1 - 0.4)^(10 - 4))

#3
n.sims <- 10^3

n.max.people <- 700

#n.people is the number of people in the room
n.people <- 2

#record the probability for each value of n.people
prob.n <- c()

while(n.people <= n.max.people){
  #checking rooms with n.people number of people
  
  #count how many simulations have two people with the same birthday
  n.successful.sims <- 0
  
  for (i.simulation in 1:n.sims){
    
    #simulate a random room with n.people
    people <- sample(1:365, n.people, replace=TRUE)
    
    #check for non-unique birthdays in the sample
    success <- max(table(people)) > 2
    
    if(success) {
      n.successful.sims <- n.successful.sims + 1
    }
  }
  prob.n[n.people] <- n.successful.sims / n.sims
  
  if (n.successful.sims/n.sims > 0.5) {
    print(paste("P(repeated birthdays) = ",
                n.successful.sims/n.sims,
                " > 0.5 for n.people = ", n.people,".",sep=""))
    break
  }else{
    print(paste("P(repeated birthdays) = ",
                n.successful.sims/n.sims,
                " < 0.5 for n.people = ", n.people,".",sep=""))
  }
  n.people <- n.people + 1
}

plot(1:length(prob.n),prob.n,xlim=c(0, 100))