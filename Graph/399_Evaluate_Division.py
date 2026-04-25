from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]

        {
        "a": {"b": 2.0, "c": 3.0},
        "b": {"a": 0.5}
        }

        time: O(M * N), N: equations, M: queries, when we build graph, takes O(N), for each query, in worst case we need 
        to traverse the whole graph O(N) to find the path from divended to divisor, so total is O(M * N). Overall, the time
        complexity is O(M * N) + O(N) = O(M * N)

        space: O(N), store graph we need O(N) space, recursion call stack can grow up to O(N) in worst case when the graph is 
        a chain, visited set can grow up to O(N), so overall space complexity is O(N)


        """
        
        graph = defaultdict(dict)

        result = []
        
        for (divended, divisor), value in zip(equations, values):
            graph[divended][divisor] = value
            graph[divisor][divended] = 1 / value

        def backtrack(curr_node, target_node, acc_product, visited):
            visited.add(curr_node)
            # ret means can't find path, value is -1
            ret = -1.0
            neighbors = graph[curr_node]

            if target_node in neighbors:
                ret = acc_product * neighbors[target_node]
            # if can't find in neighbor, search in neighbor's neighbor
            else:
                for neighbor, value in neighbors.items():
                    # if neighbor is alreay in path, skip, avoid ring
                    if neighbor in visited:
                        continue
                    ret = backtrack(neighbor, target_node, acc_product * value, visited)
                    # if we find value stop
                    if ret != -1.0:
                        break
            
            return ret

        
        for divended, divisor in queries:
            # case 1, either node not exsits
            if divended not in graph or divisor not in graph:
                ret = -1.0
            # case 2, curr and target are same
            elif divended == divisor:
                ret = 1.0
            else:
                visited = set()
                ret = backtrack(divended, divisor, 1, visited)
            result.append(ret)

        return result





