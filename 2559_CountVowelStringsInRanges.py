class Solution:
    def vowelStrings(self, words, queries):
        # trues = set()
        trues = []
        vowels = {"a","e","i","o","u"}
        for w,word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                trues.append(w)

        totals = []
        count=0
        print(trues)
        for l,r in queries:

            # if [l,r] != queries[14]:
                # continue
            #binary search for the first true >=l
            #and the last true <=r

            front,back = 0,len(trues) - 1
            firstT,lastT=-1,-1
            while front <= back:
                if front == back:
                    if trues[front] >= l:
                        firstT=front
                        break
                middle = (front + back) // 2
                if trues[middle] == l:
                    firstT = middle
                    break
                elif trues[middle] > l:
                    back = middle
                    # print(front,back)


                else:
                    front = middle + 1
            front,back = 0,len(trues) - 1
            while front <= back:
                if front == back:
                    if trues[front] <= r:
                        lastT=front
                        break
                middle = (front + back + 1) // 2 #increase by 1 because stupid
                if trues[middle] == r:
                    lastT = middle
                    break
                elif trues[middle] > r:
                    back = middle - 1
                else:
                    front = middle

            if firstT != -1 and lastT != -1:
                totals.append(1+lastT-firstT)
            else:
                totals.append(0)
        return totals

solver = Solution.__new__
words,queries = ["aba","bcb","ece","aa","e"],[[0,2],[1,4],[1,1]]
# words, queries = ["a","e","i"] , [[0,2],[0,1],[2,2]]
words=["b","rmivyakd","kddwnexxssssnvrske","vceguisunlxtldqenxiyfupvnsxdubcnaucpoi","nzwdiataxfkbikbtsjvcbjxtr","wlelgybcaakrxiutsmwnkuyanvcjczenuyaiy","eueryyiayq","bghegfwmwdoayakuzavnaucpur","ukorsxjfkdojcxgjxgmxbghno","pmgbiuzcwbsakwkyspeikpzhnyiqtqtfyephqhl","gsjdpelkbsruooeffnvjwtsidzw","ugeqzndjtogxjkmhkkczdpqzwcu","ppngtecadjsirj","rvfeoxunxaqezkrlr","adkxoxycpinlmcvmq","gfjhpxlzmokcmvhjcrbrpfakspscmju","rgmzhaj","ychktzwdhfuruhpvdjwfsqjhztshcxdey","yifrzmmyzvfk","mircixfzzobcficujgbj","d","pxcmwnqknyfkmafzbyajjildngccadudfziknos","dxmlikjoivggmyasaktllgmfhqpyznc","yqdbiiqexkemebyuitve"]
queries=[[5, 21],[17, 22],[19, 23],[13, 15],[20, 23],[21, 23],[6, 20],[1, 8],[15, 20],[17, 22],[6, 6],[1, 2],[4, 11],[14, 23],[7, 10],[16, 22],[20, 22],[21, 22],[15, 18],[5, 16],[17, 23]]
print(Solution.vowelStrings(solver,words,queries))