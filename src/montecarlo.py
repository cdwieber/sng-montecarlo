from deck import Deck

class MonteCarlo:

    def run(self, iterations, stop_at_win = False, verbose = False):
        i = 1
        win_count = 0
        while i < iterations:
            # Get a new shuffled deck
            d = Deck()
            cards = d.draw(3)
            # Second condition will stop hand from displaying twice in verbose mode
            if verbose == True and cards[0][0] != cards[1][0]:
                print(cards[0][0] + cards[0][1] + 
                ", " + cards[1][0] + cards[1][1] + 
                ", " + cards[2][0] + cards[2][1])
            
            if cards[0][0] == cards[1][0] == cards[2][0]:
                print(cards[0][0] + cards[0][1] + 
                ", " + cards[1][0] + cards[1][1] + 
                ", " + cards[2][0] + cards[2][1])
                print("It's a match! Three of a kind after " + str(i) + " iterations.")
                win_count += 1
                if stop_at_win == True:
                    break
            # Advance iterator.
            i += 1

        # Calculate win rate.
        win_rate = 100 * float(win_count)/float(i)
        # Success message.
        print("Simulation complete. Won " + 
        str(win_count) + 
        " in " + str(i) 
        + " iterations. " + "(" + str(win_rate) + "%)" )