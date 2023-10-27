# Python3 program to calculate
# the average of a batsman

# Function to find the average
# of a batsman
def averageRuns(runs, matches, notout):

  # Calculate number of
  # dismissals
  out = matches - notout;

  # check for 0 times out
  if (out == 0):
    return -1;

  # Calculate batting average
  avg = runs // out;

  return avg;

# Driver Program
runs = 10000;
matches = 250;
notout = 50;

avg = averageRuns(runs, matches, notout);

if (avg == -1):
  print("NA");
else:
  print(avg);

# This code is contributed by Akanksha_rai
