#Insertion Sort:
"""
Insertion sort works by trying to find the smallest value in the array and bring it to position 1
"""

Starting point: 0[2, 7, 9, 4, 1, 5, 3, 6, 0, 8] 
                1[2, 4, 7, 9, 1, 5, 3, 6, 0, 8]
                2[1, 2, 4, 7, 9, 5, 3, 6, 0, 8]
                3[1, 2, 4, 5, 7, 9, 3, 6, 0, 8]
                4[1, 2, 3, 4, 5, 7, 9, 6, 0, 8]
                5[1, 2, 3, 4, 5, 6, 7, 9, 0, 8]
                6[0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
                7[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#Bubble Sort:
"""
Bubble sort works by comparing two vales in the array and then moving the one smaller to the left
and then it wil repeat ubtil it is on order
"""
Starting point: 0[2, 7, 9, 4, 1, 5, 3, 6, 0, 8]
                1[2, 7, 4, 1, 5, 3, 6, 0, 8, 9]
                2[2, 4, 1, 5, 3, 6, 0, 7, 8, 9]
                3[2, 1, 4, 3, 5, 0, 6, 7, 8, 9]
                4[1, 2, 3, 4, 0, 5, 6, 7, 8, 9]
                5[1, 2, 3, 0, 4, 5, 6, 7, 8, 9]
                6[1, 2, 0, 3, 4, 5, 6, 7, 8, 9]
                7[1, 0, 2, 3, 4, 5, 6, 7, 8, 9]
                8[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Selection Sort:
"""
Selectin sort works by comparing the first value to the next value in the array until it swaps with a smaller
value. Then it will carry on comparing until it has reached the end.
WHen it reaches the end it till carry on comparing with the second value now
"""

Starting Point: 0[2, 7, 9, 4, 1, 5, 3, 6, 0, 8]
                1[0, 7, 9, 4, 2, 5, 3, 6, 1, 8]
                2[0, 1, 9, 7, 4, 5, 3, 6, 2, 8]
                3[0, 1, 2, 9, 7, 5, 4, 6, 3, 8]
                4[0, 1, 2, 3, 9, 7, 5, 6, 4, 8]
                5[0, 1, 2, 3, 4, 9, 7, 6, 5, 8]
                6[0, 1, 2, 3, 4, 5, 9, 7, 6, 8]
                7[0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
                8[0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
                9[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

