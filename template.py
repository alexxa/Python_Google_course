#!/usr/bin/python
#AUTHOR: alexxa
#DATE: 19.12.2013
#SOURCE: Google Python course 
# https://developers.google.com/edu/python/
#PURPOSE: Basics. Stings

# The original course is dedicated to Python 2.4
# All exercises were written in Python 3

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
