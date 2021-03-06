"""
Copyright (C) 2013 Matthew Woodruff

This script is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This script is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this script. If not, see <http://www.gnu.org/licenses/>.

===========================================================
compare_data.py

Compare two data files to see whether their data is equal to 
within a tolerance.
"""

import argparse
import sys
import numpy

def printout(ss):
    sys.stdout.write("{0}\n".format(ss))

def evaluate(left, right, sep, tol):
    """ detect differences or report that there are none"""
    ltable = numpy.loadtxt(left, delimiter=sep)
    rtable = numpy.loadtxt(right, delimiter=sep)

    ltable.sort(axis=1)
    rtable.sort(axis=1)

    if ltable.shape[1] != rtable.shape[1]:
        return "Cannot compare {0} to {1}".format(ltable.shape,rtable.shape)
    
    lmatched = []
    rmatched = []
    matches = []

    for ii in range(len(ltable)):
        for jj in range(len(rtable)):
            if jj in rmatched:
                continue
            difference = ltable[ii] - rtable[jj]
            if max(difference) < tol and min(difference) > -tol:
                lmatched.append(ii)
                rmatched.append(jj)
                matches.append((ii, jj))
                break

    if len(matches) == len(ltable):
        return "Equal within {0:.3g}".format(tol)

    message = "{0} matches of {1} rows.".format(len(matches), len(ltable))
    printout(matches)
    return message

def get_args(arguments):
    """ command-line arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument("a", help="first file to compare",
                        type=argparse.FileType("r"))
    parser.add_argument("b", help="second file to compare",
                        type=argparse.FileType("r"))
    parser.add_argument("-s", "--sep", default=" ", type=str,
                        help="field separator, default is space")
    parser.add_argument("-t", "--tol", default=1e-6, type=float,
                        help="tolerance, default is 1e-6")
    return parser.parse_args()

def cli():
    """ command-line interface """
    arguments = sys.argv
    args = get_args(sys.argv[1:])
    sys.stdout.write("{0}\n".format(str(
        evaluate(args.a, args.b, args.sep, args.tol))))
    
if __name__ == "__main__":
    cli()


# vim:ts=4:sw=4:expandtab:ai:colorcolumn=68:number:fdm=indent
