"""
Problem: Count Peaks

A sensor outputs radioactivity values every second.

A value is called:

1. Top Peak
   - if it is at least 5 greater than BOTH neighbors

2. Bottom Peak
   - if it is at least 5 smaller than BOTH neighbors

The first and last elements can never be peaks.

Return the total number of peaks.

Example:
values = [8, 10.7, 17.1, 11.2, 13.5, 9.9, 14.9, 9.4, 9.4, 3.1, 12.7]

Output:
3
"""

#Solution

values = [8, 10.7, 17.1, 11.2, 13.5, 9.9, 14.9, 9.4, 9.4, 3.1, 12.7]

def count_peaks(values):
    peaks = 0

    for i in range(1, len(values)-1):

        #top_peaks
        if values[i] >= values[i-1] + 5 and values[i] >= values[i+1] + 5:
            peaks += 1
        
        #bottom_peaks
        elif values[i] <= values[i-1] - 5 and values[i] <= values[i+1] - 5:
            peaks += 1

    return peaks

print(count_peaks(values))