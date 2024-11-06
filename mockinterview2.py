

def encodelog (logfile):
    print_slices = lambda logfile: [(logfile[i:]) for i in range(len(logfile))]
    
    # Call the lambda function and store the result
    slices = print_slices(logfile)

    for val in slices:
        for char in logfile:
            n = logfile.count(char)
            print(n)
    # print(slices)
logfile = str(input())
encodelog(logfile)

