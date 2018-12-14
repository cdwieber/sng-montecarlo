# Introduction
One of my hobbies is playing microstakes poker tournaments online. Recently, one of the sites that I play on added a new feature: "Spin to Get In." Essentially, they take the top 20 cards off of a standard deck (10-A of every suits), and stick them in a slot machine. You pay a penny, pull the lever, and if you get three in a row, you win! You can then enter the tournament for essentially free.

The problem is, having pulled the lever hundreds of times (and throwing away many ones of dollars), I didn't win _once_. Statistically, that didn't seem to pan out. So naturally, needing to dust off my Python anyway, I decided to write a simple _Monte Carlo_ simulation to test this. The basic idea behind a Monte Carlo simulation involves setting up a simulated scenario involving known or assumed probabilities (such as the random deck of 20 cards in deck.py), and then running that scenario over and over to guage the result (plus or minus the expected standard deviations.)

After running 100, 1000, and eventually up to 1,000,000 simulated "hands", the win rate should be around 2.8%; not exactly what I was getting at the casino. 

Wouldn't you know it. The house always wins.