/*
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Approach 2: Sorting
Intuition

If we sort the intervals by their start value, then each set of intervals that can be merged will appear as a contiguous "run" in the sorted list.

Algorithm

First, we sort the list as described. Then, we insert the first interval into our merged list and continue considering each interval in turn as follows: If the current interval begins after the previous interval ends, then they do not overlap and we can append the current interval to merged. Otherwise, they do overlap, and we merge them by updating the end of the previous interval if it is less than the end of the current interval.

A simple proof by contradiction shows that this algorithm always produces the correct answer. First, suppose that the algorithm at some point fails to merge two intervals that should be merged. This would imply that there exists some triple of indices ii, jj, and kk in a list of intervals intsints such that i < j < ki<j<k and (ints[i]ints[i], ints[k]ints[k]) can be merged, but neither (ints[i]ints[i], ints[j]ints[j]) nor (ints[j]ints[j], ints[k]ints[k]) can be merged. From this scenario follow several inequalities:

\begin{aligned} ints[i].end < ints[j].start \\ ints[j].end < ints[k].start \\ ints[i].end \geq ints[k].start \\ \end{aligned} 
ints[i].end<ints[j].start
ints[j].end<ints[k].start
ints[i].end≥ints[k].start
​	
 

We can chain these inequalities (along with the following inequality, implied by the well-formedness of the intervals: ints[j].start \leq ints[j].endints[j].start≤ints[j].end) to demonstrate a contradiction:

\begin{aligned} ints[i].end < ints[j].start \leq ints[j].end < ints[k].start \\ ints[i].end \geq ints[k].start \end{aligned} 
ints[i].end<ints[j].start≤ints[j].end<ints[k].start
ints[i].end≥ints[k].start
​	
 

Therefore, all mergeable intervals must occur in a contiguous run of the sorted list.

Sorting Example

Consider the example above, where the intervals are sorted, and then all mergeable intervals form contiguous blocks.

*/
/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    if (intervals.length < 2) {
        return intervals.map((item) => item.slice());
    }

    intervals = intervals.sort((a,b) => a[0] - b[0]);

    const solArr = [];
    let [prevStart, prevEnd] = intervals[0];

    for(let i = 1; i < intervals.length; ++i) {
        const [currStart, currEnd] = intervals[i];

        if (prevEnd < currStart) {
            solArr.push([prevStart, prevEnd]);

            prevStart = currStart;
            prevEnd = currEnd;
        }
        else {
            prevEnd = Math.max(prevEnd, currEnd);
        }
    }
    sollArr.push([prevStart, prevEnd]);

    return solArr;
};

/*
Complexity Analysis

Time complexity : O(nlogn)

Other than the sort invocation, 
we do a simple linear scan of the list, 
so the runtime is dominated by the O(nlgn) complexity of sorting.

Space complexity : O(1) (or O(n)

If we can sort intervals in place, 
we do not need more than constant additional space. 
Otherwise, we must allocate linear space to store 
a copy of intervals and sort that.
*/