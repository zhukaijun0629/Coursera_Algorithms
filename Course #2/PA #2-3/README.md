# Programming Assignment #2-3

Download the following text file:

[**Median.txt**](https://raw.githubusercontent.com/zhukaijun0629/Coursera_Algorithms/main/Course%20%232/PA%20%232-3/Median.txt)

The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 3 lecture on heap applications). The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one. Letting *x*<sub>*i*</sub> denote the *ith* number of the file, the *kth* median *m*<sub>*k*</sub> is defined as the median of the numbers *x*<sub>*1*</sub>,...,*x*<sub>*k*</sub>. (So, if *k* is odd, then *m*<sub>*k*</sub> is *(k/2)th* smallest number among *x*<sub>*1*</sub>,...,*x*<sub>*k*</sub>; if *k* is even, then *m*<sub>*k*</sub> is the *(k/2)th* smallest number among *x*<sub>*1*</sub>,...,*x*<sub>*k*</sub>.)

In the box below you should type the sum of these 10000 medians, modulo 10000 (i.e., only the last 4 digits). That is, you should compute (*m*<sub>*1*</sub>+*m*<sub>*2*</sub>+*m*<sub>*3*</sub>+ ... + *m*<sub>*10000*</sub>) mod 10000.

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and search-tree-based implementations of the algorithm.
