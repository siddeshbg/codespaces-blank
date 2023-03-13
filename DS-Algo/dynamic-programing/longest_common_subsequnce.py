"""
Write a function to find the length of the longest common subsequence between two sequences. 
E.g. Given the strings "serendipitous" and "precipitation", 
the longest common subsequence is "reipito" and its length is 7.

Problem statement: We are given 2 sequences and we need to 
find the length of longest subsequence between them

Input: 
seq1 = "serendipitous"
seq2 = "precipitation"

Ouput:
Len of longets subsequence i.e 7 (reipito)

Test cases
1. General case (string)
2. General case (list)
3. No common subsequence
4. One is a subsequence of the other
5. One sequence is empty
6. Both sequences are empty
7. Multiple subsequences with same length (ex. "abcdef" and "badcfe")

Algo (recursive):
1. Create 2 counters idx1 & idx2 starting at 0. Our recursive function will compute the LCS of seq1(idx:) and seq2[idx:]
2. if seq1[idx1] and seq2[idx2] are equal, then this char belongs to LCS of seq1[idx1:] & seq2[idx2:]. 
   Determine LCS of seq1[idx1+1:] & seq2[idx2+1:]
3. If not, then the LCS of seq1[idx1:] & seq2[idx2:] is the longer among the LCS of seq1[idx1+1:],
   seq2[idx2:] & the LCS of seq1[idx1:], seq2[idx2+1:]
4. If either seq1[idx1:] or seq2[idx2:] is empty, then their LCS is empty.
"""

def lcs_recursive( seq1, seq2, idx1=0, idx2=0):
    """
    Time complexity is 2**(m+n) 
    """
    if idx1 == len(seq1) or idx2 == len(seq2):
      return 0
    elif seq1[idx1] == seq2[idx2]:
       return 1 + lcs_recursive(seq1,seq2, idx1+1, idx2+1)
    else:
       option1 = lcs_recursive(seq1,seq2,idx1+1,idx2)
       option2 = lcs_recursive(seq1,seq2,idx1,idx2+1)
       return max(option1, option2)
      
   
def lcs_memo(seq1, seq2):
   """
   Time complexity is O(m*n)
   """
   memo = {}
   def recurse(idx1=0, idx2=0):
      key = (idx1, idx2)
      if key in memo:
         return memo[key]
      elif idx1 == len(seq1) or idx2 == len(seq2):
         memo[key] = 0
      elif seq1[idx1] == seq2[idx2]:
         memo[key] = 1 + recurse(idx1+1,idx2+1)
      else:
         memo[key] = max(recurse(idx1+1, idx2), recurse(idx1,idx2+1))
      return memo[key]
   return recurse(0, 0)

def lcs_dp(seq1, seq2):
   """
   Algo:
   2. If seq1[i] and seq2[j] are equal, then table[i+1][j+1] = 1 + table[i][j]
   3. If seq1[i] and seq2[j] are not equal, then table[i+1][j+1] = max(table[i][j+1],table[i+1][j])

   Time complexity is O(N1*N2)
   """
   n1, n2 = len(seq1), len(seq2)
   # Initialize table with 0's
   table = [[0 for x in range(n2+1)] for x in range(n1+1)]
   for i in range(n1):
      for j in range(n2):
         if seq1[i] == seq2[j]:
            table[i+1][j+1] = 1 + table[i][j] # diagonally opposite value
         else:
            # max of previous row or column
            table[i+1][j+1] = max(table[i][j+1], table[i+1][j])
   # return last element in the table
   return table[-1][-1]


if __name__ == "__main__":
   #  print(lcs_recursive("serendipitous", "precipitation") == 7)
   #  print(lcs_recursive([1,3,5,6,7,2,5,2,3], [6,2,4,7,1,5,6,2,3]) == 5)
   #  print(lcs_recursive('longest', 'stone') == 3)
   #  print(lcs_recursive('asdfwevad','opkpoiklklj') == 0)
   #  print(lcs_recursive('dense', 'condensed') == 5)
   #  print(lcs_recursive('', 'opkpoiklklj') == 0)
   #  print(lcs_recursive('','') == 0)
   #  print(lcs_recursive('abcdef','badcfe') == 3)

   #  print(lcs_memo("serendipitous", "precipitation") == 7)
   #  print(lcs_memo([1,3,5,6,7,2,5,2,3], [6,2,4,7,1,5,6,2,3]) == 5)
   #  print(lcs_memo('longest', 'stone') == 3)
   #  print(lcs_memo('asdfwevad','opkpoiklklj') == 0)
   #  print(lcs_memo('dense', 'condensed') == 5)
   #  print(lcs_memo('', 'opkpoiklklj') == 0)
   #  print(lcs_memo('','') == 0)
   #  print(lcs_memo('abcdef','badcfe') == 3)

   print(lcs_dp("serendipitous", "precipitation") == 7)
   print(lcs_dp([1,3,5,6,7,2,5,2,3], [6,2,4,7,1,5,6,2,3]) == 5)
   print(lcs_dp('longest', 'stone') == 3)
   print(lcs_dp('asdfwevad','opkpoiklklj') == 0)
   print(lcs_dp('dense', 'condensed') == 5)
   print(lcs_dp('', 'opkpoiklklj') == 0)
   print(lcs_dp('','') == 0)
   print(lcs_dp('abcdef','badcfe') == 3)