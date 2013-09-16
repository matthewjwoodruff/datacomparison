datacomparison
==============

Report whether every row of data in one text file is found in another.

Data are compared using subtraction, tolerance may be specified at the command line.  To make sure that files are actually the same, make sure they have the same number of lines.  (`wc -l filename` is a good way to do this.)  Right now, if you have only one row in file `a`, and that row is in file `b`, this utility will say that the files match, even if file `b` has 100 rows.

```
usage: compare_sets.py [-h] [-s SEP] [-t TOL] a b

positional arguments:
  a                  first file to compare
  b                  second file to compare

optional arguments:
  -h, --help         show this help message and exit
  -s SEP, --sep SEP  field separator, default is space
  -t TOL, --tol TOL  tolerance, default is 1e-6
```

Pull requests are welcome, particularly for the following features:

* Add an option for comparison using division instead of subtraction.  I.e. is abs(a/b - 1) < tol?
* Do something intelligent with columns that aren't numbers.  Either compare or ignore.  Currently causes an error.
* Handle Inf / NaN.
* Is this a one-liner in `awk` like so many other analysis tasks?  Please share.
* Sensible options for output formatting.
