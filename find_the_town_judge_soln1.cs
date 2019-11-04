/*
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
 

Note:

1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N

Example:
truster[1] = II         trustee[3] = III (N-1)
truster[2] = II         trustee[4] = II
truster[4] = I
truster[0] = 0
*/

public class Solution {
    public int FindJudge(int N, int[][] trust) {
        // if there is only 1 person (N = 1)
        // and trust is empty, the person is the town judge
        if (N == 1 && trust.Length == 0) 
        {
            return 1;
        }

        int[] truster = new int[N+1];
        int[] trustee = new int[N+1];

        for(int i = 0; i < trust.Length; ++i) {
            truster[trust[i][0]]++;
            trustee[trust[i][1]]++;
        }

        // to satisfy to be the town judge:
        // truster of index j must b 0
        // trustee of index j must be total # of people(N)-1
        for(int j = 0; j < trustee.Length; ++j) {
            if (trustee[j] == N-1 && truster[j] == 0) 
            {
                return j;
            }
        }

        return -1;
    }
}
/*
Complexity

Time: O(N + T) where T is the trust.Length
Space: O(N)
*/