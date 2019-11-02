/*
You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.

paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.

Also, there is no garden that has more than 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, 
for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.

 

Example 1:

Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Example 2:

Input: N = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
Example 3:

Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
 

Note:

1 <= N <= 10000
0 <= paths.size <= 20000
No garden has 4 or more paths coming into or leaving it.
It is guaranteed an answer exists.
*/

public class Solution {
    public int[] GardenNoAdj(int N, int[][] paths) {
        var dict = new Dictionary<int, HashSet<int>>();
        var gardens = new int[N];
        
        //build map of paths
        foreach (int[] path in paths)
        {
            int p1 = path[0];
            int p2 = path[1];
            
            if (!dict.ContainsKey(p1))
                dict.Add(p1, new HashSet<int>());
            
            if (!dict.ContainsKey(p2))
                dict.Add(p2, new HashSet<int>());
            
            dict[p1].Add(p2);
            dict[p2].Add(p1);
        }
        
        for (int i = 0; i < N; i++)        
            gardens[i] = DetermineType(i + 1, gardens, dict);
        
        return gardens;
    }
    
    private int DetermineType(int gardenNum, int[] gardens, Dictionary<int, HashSet<int>> dict)
    {        
        if (dict.ContainsKey(gardenNum))
        {
            HashSet<int> neighbors = dict[gardenNum];
            int[] usedTypes = new int[] {0,0,0,0};

            // loop thru neighbors and mark the used types
            foreach(int neighbor in neighbors)
            {
                int index = neighbor - 1;
                int type = gardens[index];

                if (type > 0)
                {
                    int markUsed = type-1;
                    usedTypes[markUsed] = 1;
                }
            }

            // find the first non-used type
            for(int i = 0; i < 4; ++i)
            {
                if (usedTypes[i] == 0)
                {
                    return i+1;
                    // return type 1,2,3,4
                }
            }
        } 
        else 
        {
            return 1; //nothing connects to this garden, so its safe to be just be type 1
        }
        
        return 0;
    }
}

/*
Intuition
Greedily paint nodes one by one.
Because there is no node that has more than 3 neighbors,
always one possible color to choose.

Complexity
Time O(N) with O(paths) -> O(N)
Space O(N)
*/