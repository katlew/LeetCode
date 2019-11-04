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
[1,1] -> [1,-1]
[2,1] -> [2,-1]
[3,1] -> [3,4]
[4,1] -> [4,1]
*/

/**
 * @param {number} N
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function(N, trust) {
    const map = new Map();
    for(let nums=1; nums<=N; nums++)
    {
        map.set(nums,1);
    }

    for(let t=0; t<trust.length; t++)
    {
        //judge trusts nobody
        map.set(trust[t][0],map.get(trust[t][0])-1); 
        
        //everyone trusts the judge
        map.set(trust[t][1],map.get(trust[t][1])+1); 
    }

    for (const [k, v] of map.entries()) {
      if(v==N) return k;
    }
    return -1;
};

/*
Complexity

Time Complexity: O(2N+T)
Space Complexity: O(N)
*/