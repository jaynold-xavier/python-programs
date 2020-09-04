# program to print a Mat .Size must be N X M. (N is an odd natural number, and M is 3 times N.)

def dashed_lines_prnt(length):  # method for printing dashed lines of the mat
    for j in range(length):
        print "-",


if __name__ == "__main__":

    dim = raw_input("Enter mat size(length x breadth): ")                            #raw_input("Enter N x M: ")
    dim = map(int,dim.split(" "))
    print dim,"\n"

    for i in range(dim[0]/2,0,-1):
        dashed_lines_prnt(i*3)
        for m in range(i*2,dim[0]):
            print ". | .",
        dashed_lines_prnt(i*3)
        print

    dashed_lines_prnt((dim[1]-7)/2)
    print"W E L C O M E",
    dashed_lines_prnt((dim[1]-7)/2)
    print

    for i in range(1,dim[0]/2+1):
        dashed_lines_prnt(i*3)
        for m in range(i*2,dim[0]):
            print ". | .",
        dashed_lines_prnt(i*3)
        print




