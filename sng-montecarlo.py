#!/usr/bin/python
import sys
from src.montecarlo import MonteCarlo



def usage():
   print("Usage: sng-montecarclo -iterations=<iterations> -v <verbose> -s <stop at first win>")

def main(argv):
   
   # TODO: Add support for command line arguments

   mc = MonteCarlo()
   mc.run(1000000, False, False)

if __name__ == "__main__":
   main(sys.argv[1:])