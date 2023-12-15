# divide doc by line
# check each line for first number, last number, if not other number is found, use first number twice
#create list with names of numbers and check for those as well
# count the double number
Code = int()
Numbers= {'one': "o1e",'two': "t2o",'three':"t3e",'four': "f4r",'five':"f5e",'six': "s6x",'seven': "s7n",'eight': "e8t",'nine': "n9e"}
with open('input.txt', 'r') as file:
    for line in file:
        print(line)
        for word_number in Numbers:
            if word_number in line:
                print(word_number)
                line=line.replace(word_number, Numbers[word_number])
        print(line)
        first_int=None
        second_int=None
        for letter in list(line):
            try:
                print(int(letter))
                if first_int==None:
                    first_int=letter
                else:
                    second_int=letter

            except ValueError:
                pass
        if second_int==None:
            second_int=first_int
        print(first_int+second_int)
        Code=Code+int(first_int+second_int)
        print(Code)

#    file.seek(0)
#    textline = 'five8btwooneight'
 #   newtextline=textline
  #  for word_number in Numbers:
   #     if word_number in textline:
    #        print(word_number)
     #       newtextline=(newtextline.replace(word_number, Numbers[word_number]))
    #print(newtextline)
    #print(textline)

