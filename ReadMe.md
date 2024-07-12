# Fenwick Trees

In ``fenwick.py`` there is a basic implementation of a Fenwick tree.  The ``treeify`` method is an alternative constructor that runs in time $O(n)$ and is as such faster than entering the initial entries one at a time.  The file ``countInversions.py`` uses this structure to count the number of inversions in a permutation in time $O(n \log(n))$.  

The other files are tests.  
