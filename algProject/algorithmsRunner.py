from algorithms import algorithm_1, algorithm_2, algorithm_4, maxSum
import random, time, math

with open('phw_input.txt', 'r') as file:                        # Specifies the file
    content = file.read()                                       # Reads contents of the file
    content_list = content.split(",")                           # Splits contents using a comma-delimiter
content_list = [int(i) for i in content_list]                   # Converts list of strings into ints

L, U = 0, len(content_list)-1
print("algorithm_1: " + str(algorithm_1(content_list)) + "\nalgorithm_2: " + str(algorithm_2(content_list))
    + "\nalgorithm_3: " + str(maxSum(content_list, L, U)) 
    + "\nalgorithm_4: " + str(algorithm_4(content_list)))       # Prints MSCS of all algs with array in phw_input file

intSeq = []                                                     # The double for loop generates 19 integer sequences
for i in range(10, 101, 5):                                     # stored in the list 'intSeq.' Essentially arrays in a
    tempArr = []                                                # list.
    for p in range(i):
        randInt = random.randint(-100, 100)                     # Generates random ints from 100 to -100 and stores in
        tempArr.append(randInt)                                 # tempArr. TempArr is then added to intSeq.
    intSeq.append(tempArr)

f = open("joshuaKim_phw_output.txt", "a")                       # Opens output file
f.write("\nalgorithm-1, algorithm-2, algorithm-3, algorithm-4, T1(n), T2(n), T3(n), T4(n)")

matrixArr = []                                                  # Array which will create the matrix                          
for i in range(len(intSeq)):                                    # ^19 elements of 8 element arrays
    tempArr = []
    start = time.time()                                         # Breakpoint on time in the program
    for p in range(0, 500):                                     # Running an alg of N=500 times on an element in intSeq
        algorithm_1(intSeq[i])                                  # Runs alg on single element
    elapsed = (time.time() - start)                             # Records running time of the alg on the element
    elapsed = round((elapsed * 1000000)/500, 7)                 # Finds average running time in microseconds
    tempArr.append(elapsed)                                     # Adds first element into matrixArr (algorithm 1 run)

    start = time.time()
    for p in range(0, 500):                                     # For loop runs 500 times on all elements in intSeq
        algorithm_2(intSeq[i])                                  # Runs using alg 2
    elapsed = (time.time() - start)                             # Records running time of alg 2
    elapsed = round((elapsed * 1000000)/500, 7)                 # Finds average running time in microseconds
    tempArr.append(elapsed)                                     # Adds second element to each element in matrixArr

    start = time.time()
    for p in range(0, 500):                                     # For loop runs 500 times on all elements in intSeq
        maxSum(intSeq[i], 0, len(intSeq[i])-1)                  # Runs using alg 3
    elapsed = (time.time() - start)                             # Records running time of alg 3
    elapsed = round((elapsed * 1000000)/500, 7)                 # Finds average running time in microseconds
    tempArr.append(elapsed)                                     # Adds third element to each element in matrixArr

    start = time.time()
    for p in range(0, 500):                                     # For loop runs 500 times on all elements in intSeq
        algorithm_4(intSeq[i])                                  # Runs using alg 4
    elapsed = (time.time() - start)                             # Records running time of alg 4
    elapsed = round((elapsed * 1000000)/500, 7)                 # Finds average running time in microseconds
    tempArr.append(elapsed)                                     # Adds second element to each element in matrixArr

    n = len(intSeq[i])                                          # Fills in last 4 elements with theoretical time complexities
    equation1 = math.ceil((7/6)*(n**3)+7*(n**2)+(47/6)*n+3)     # which were calculated on instructions sheet
    tempArr.append(equation1)
    equation2 = math.ceil((11/2)*(n**2)+(17/2)*n+3)
    tempArr.append(equation2)
    equation3 = math.ceil(11*n*math.log(n)+11*n)
    tempArr.append(equation3)
    equation4 = math.ceil(12*n+12)
    tempArr.append(equation4)

    matrixArr.append(tempArr)
    f.write("\n" + str(matrixArr[i][0]) + ", " + str(matrixArr[i][1]) + ", " + str(matrixArr[i][2]) + ", " + str(matrixArr[i][3])
        + ", " + str(matrixArr[i][4]) + ", " + str(matrixArr[i][5])
        + ", " + str(matrixArr[i][6]) + ", " + str(matrixArr[i][7]))
f.close()
print("Output file is complete")