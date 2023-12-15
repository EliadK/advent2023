#load 3 lines
#find in string anything that's not a digit or a .
#get the location
#look for the location +-=1 in row above
#look for the location +-1 in same row
#look for the location +-=1 in row below
#if any of the is a digit add the number
#how to ensure no dupes? Replace with ...

parsed_lines= {"line 1":0,"line 2":0, "line 3":0}
code = 0

def number_cruncher(string,index):
    # runs on a specific point and returns a whole number touching this point, whether it's to the left, right,
    # or between. Then deletes it. Will only return "complete" number at ANY length which fulfils conditions.
    n = "" # The number tallied
    i=index # Temporary variable for indexing the search
    if string[i].isdigit(): # Checks if it's a digit to save time and prevent errors
        while i <= 140 and string[i].isdigit():
            n = n + string[i]
            string[i] = '.'
            i+=1
        i=index-1 # must now be reset as the scan proceeds to the left of index point
        while i >= 0 and string[i].isdigit():
            n=string[i]+n
            string[i] = '.'
            i-=1
    if n.isdigit(): # returning n as an empty string created lots of errors... how to avoid this? not sure
        return int(n)
    else:
        return 0

with open('input 3.txt', 'r') as file:
    for line in file:
        # Loads up the lines.. There's probably a better way to do this that would eliminate the need for code later
        if parsed_lines["line 1"] == 0:
            parsed_lines["line 1"] = list(line)
            print(parsed_lines)
        elif parsed_lines["line 2"] == 0:
            parsed_lines["line 2"] = list(line)
            print(parsed_lines)
        elif parsed_lines["line 3"] == 0:
            parsed_lines["line 3"] = list(line)
            print(parsed_lines)
        else: # When all loaded, begin to run on middle line, looking for those special chars
            for parsed_character in enumerate(parsed_lines["line 2"]):
                if parsed_character[1] != "." and not parsed_character[1].isdigit() and parsed_character[0] < 140:
                    # When found (I'm now thinking this could've been a while?) it'll look around the char using my function
                    print(f"special {parsed_character[1]} at {parsed_character[0]}")
                    # And now my neighborhood way of looking at every point around special char
                    code += number_cruncher(parsed_lines["line 1"], parsed_character[0] - 1)
                    print(code)
                    code += number_cruncher(parsed_lines["line 1"], parsed_character[0])
                    print(code)
                    code += number_cruncher(parsed_lines["line 1"], parsed_character[0] + 1)
                    print(code)
                    code += number_cruncher(parsed_lines["line 2"], parsed_character[0] - 1)
                    print(code)
                    code += number_cruncher(parsed_lines["line 2"], parsed_character[0] + 1)
                    print(code)
                    code += number_cruncher(parsed_lines["line 3"], parsed_character[0] - 1)
                    print(code)
                    code += number_cruncher(parsed_lines["line 3"], parsed_character[0])
                    print(code)
                    code += number_cruncher(parsed_lines["line 3"], parsed_character[0] + 1)
                    print(f"total is {code}")
            # finally we cycle the lines.. I do wonder if I could put this on the top and somehow get rid of an elif?
            parsed_lines["line 1"] = parsed_lines["line 2"]
            parsed_lines["line 2"] = parsed_lines["line 3"]
            parsed_lines["line 3"] = list(line)
            print(parsed_lines)
# finally another neighborhood way of running on the last few lines.. I'm sure I can do better if I think about it
# a bit more. This could also go up into the elif.. or perhaps made into a function for "elegance"..?
for parsed_character in enumerate(parsed_lines["line 2"]):
    if parsed_character[1] != "." and not parsed_character[1].isdigit() and parsed_character[0] < 140:
        print(f"special {parsed_character[1]} at {parsed_character[0]}")
        code += number_cruncher(parsed_lines["line 1"], parsed_character[0] - 1)
        print(code)
        code += number_cruncher(parsed_lines["line 1"], parsed_character[0])
        print(code)
        code += number_cruncher(parsed_lines["line 1"], parsed_character[0] + 1)
        print(code)
        code += number_cruncher(parsed_lines["line 2"], parsed_character[0] - 1)
        print(code)
        code += number_cruncher(parsed_lines["line 2"], parsed_character[0] + 1)
        print(code)
        code += number_cruncher(parsed_lines["line 3"], parsed_character[0] - 1)
        print(code)
        code += number_cruncher(parsed_lines["line 3"], parsed_character[0])
        print(code)
        code += number_cruncher(parsed_lines["line 3"], parsed_character[0] + 1)
        print(f"total is {code}")