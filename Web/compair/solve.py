from itertools import product
import hashlib # Import the modules
for x in range(0, 10): # Iterate through the lengths
        for combo in product("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", repeat=x): # For each combination in this alphabet with this length
                result = hashlib.md5("mocsctf" + ''.join(combo)).hexdigest() # Generate the result
                if result.startswith("0e") and result[2:].isdigit(): # Check if result matches our requirements
                        print "mocsctf" + ''.join(combo) # If it does print out the string
                else:
                        pass #If not pass


#mocsctfPv0zY
#--- 676.12 seconds ---
#mocsctfaQaUYT
#--- 1678.66 seconds ---
#mocsctfa9Gehp
#--- 1992.91 seconds ---
#mocsctfbAjDRY
#--- 2421.78 seconds ---
#mocsctfbCKDWa
#--- 2461.01 seconds ---
#mocsctfbOegGS
#--- 2645.89 seconds ---
#mocsctfcCwWQf
#--- 3455.81 seconds ---
#mocsctfcN0BwT
#--- 3640.36 seconds ---
#mocsctfdcCZ1z
#--- 4037.41 seconds ---
#mocsctfd7VFii
#--- 4959.93 seconds ---
#mocsctfeuTeRO
#--- 5330.32 seconds ---
