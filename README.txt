----------------------
     Test Cases
----------------------
With reference to the problem statement and sample inputs the following assumptions are made

  # Message should contain the name of the kingdom and message to it(comma separated and case in-sensitive). So the program accepts the following inputs.
     a. air,Owler (small 'a', capital 'O', without quotes)
     b. Air, "lets bowl"

  # The following inputs are considered invalid and handled with appropriate error messages
     a. air owl (kingdom and message are not separated) this error is handled. (Prints 'Error: Invalid input!')
     b. Sand, Tyene (Prints 'Error: Invalid kingdom!')
     c. Bravoos, valar, morghulis (Too many inputs, Prints 'Error: Invalid input!')

  # Program accepts lines until getting an empty line.

---------------------
      Output
---------------------
  # If the King wins over 3 or more kingdoms, he is declared as ruler.
  # Order of allies is preserved according to the order of the messages sent. (Observed from the sample input)
  # Though the King does not get enough allies to become ruler, the Allies of the King are printed as allies in the output.

# No third party libraries are used.
