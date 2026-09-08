from collections import Counter, deque
import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int

        N = len(tasks), K = different type of tasks, k <= 26, T = final CPU 
        intervals, include idle

        time: O(N + K log K + T log K), we can say is O(T). For counter will takes O(N), iterate all tasks to get frequency. 
        Next for heap, we have k different type(k <= 26), thus over all is O(KlogK). For while, will either excute tasks or 'idle', 
        total will be T times(size for final ans), each 'heappop' will takes O(logK) times, so overall is O(TlogK).

        space: O(26) = O(1)
        """
        
        # 1. count frequency for each tasks
        count = Counter(tasks)

        # 2. store tasks sort base on frequency into heap (-freq, letter)
        heap = []
        for letter, freq in count.items():
            heapq.heappush(heap, (-freq, letter))

        # 3. cretate queue, first in first out (ready_time, remain_freq, letter)
        cooldown = deque()

        time = 0

        while heap or cooldown:
            # MUST check cooldown first, make sure 'ready' task move to queue
            if cooldown and cooldown[0][0] <= time:
                ready_time, freq, letter = cooldown.popleft()

                # put it back to heap
                heapq.heappush(heap, (freq, letter))

            # if there's task in heap, deal the top tasks
            if heap:
                freq, letter = heapq.heappop(heap)

                # let freq of curr task -= 1
                freq += 1

                # if still remain freq, we need to append to queue waiting for next round
                if freq < 0:
                    ready_time = time + n + 1
                    cooldown.append((ready_time, freq, letter))
            # nothing can be excuted, all tasks in cooldown can't process now
            else:
                # if not heap, means place 'IDLE'
                pass

            time += 1

        return time