'''
Created on Sep 08, 2014

@author: raniba
'''

import argparse

__version__ = '0.0.1'


#==============================================================================
# make a UI
#==============================================================================
parser = argparse.ArgumentParser(
    prog='create_targets',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='''This component is used to create targets to be realigned
                It takes a sorted alignment and produces a target list''')

# required arguments
parser.add_argument('--infile', metavar='INPUT',
                    help='A BAM file to be reheaded')

parser.add_argument('--indexed_bam', metavar='INDEXED_BAM',
                    help='index of the bam input (forcing task dependencies')

parser.add_argument('--ref_genome', metavar='REF_GENOME',
                    help='A BAM file to be reheaded')

parser.add_argument('--outfile', metavar='OUTPUT',
                    help='Reheaded BAM file')


args, x = parser.parse_known_args()
