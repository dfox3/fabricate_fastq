import os
import sys
import itertools
import bisect
import argparse

#--------------------------------------------------------------------------------------------------
#Command line input parameters
parser = argparse.ArgumentParser(description='Fastq Fabricator')

parser.add_argument('--o',
                    metavar='-output',
                    required=True,
                    help='Name of fastq')
parser.add_argument('--i',
                    metavar='-input',
                    required=True,
                    help='sequence')
parser.add_argument('--d',
                    metavar='-depth',
                    required=True,
                    help='depth, number of reads')

#--------------------------------------------------------------------------------------------------
options = parser.parse_args()
with open(str(options.o), 'w') as nfq:
    for f in xrange(int(options.d)):
        nfq.write("@M03579:62:000000000-ATNDR:1:1101:18354:"+str(f)+" 1:N:0:101\n")
        nfq.write(str(options.i).upper()+"\n")
        nfq.write("+\n")
        qual = ''
        for x in xrange(len(str(options.i))):
            qual += "I"
        nfq.write(str(qual)+"\n")
    nfq.close()
   
