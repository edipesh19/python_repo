#-------------------------------------------------------------------------------
# Name:        CommandLineParsing.py
# Purpose:
#
# Author:     Dipesh Kumar Dutta 
#
# Created:     06/05/2014
# Copyright:   (c) dkdutta 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys;
import getopt;

def main():
    sys.stdout.write("Number of arguments = " + str(len(sys.argv)) + "\n")
    sys.stdout.write("Argument list = " + str(sys.argv)+"\n")

    input_file='';
    ouput_file='';
    try:
        opts, args = getopt.getopt(sys.argv, "hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        sys.stdout.write("CommandLineParsing.py -i <inputfile> -o <outputfile>'\n")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            sys.stdout.write("CommandLineParsing.py -i <inputfile> -o <outputfile>'\n")
            sys.exit();
        if opt in ("-i","-ifile"):
            input_file = arg
        if opt in ("-o","-ofile"):
            ouput_file = arg
    sys.stdout.write("Input File = " + input_file)
    sys.stdout.write("Output File = " + ouput_file)

if __name__ == '__main__':
    main()
