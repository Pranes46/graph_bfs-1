class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        
        m = len(wordList[0])  #calculating the len of wordlist
        
        wordList = set(wordList)  #using set
        
        wordList.add(beginWord)  #adding the begin word in the wordlist 
        
        adj = defaultdict(list)  #creating adj list
        
        for word in wordList:
            for i in range(m):
                s = word[:i]+"_"+word[i+1:]  #appending the word with _on it by replacing the ith index
                
                adj[s].append(word)
                
                
        q = deque()  #creating queue
        
        q.append(beginWord)  #appending the begin word in queue
        
        visited = set()  #crreating a visited hashset
        dist = 0  #counter
        visited.add(beginWord) #adding the begin word in the visited set
        
        while q: #the loop wil run until the queue is empty
            dist+=1  #increasing the counter
            size = len(q)  #level order
            
            for _ in range(size):
                currword = q.popleft()  #popping the queue first element 
                for i in range(m):
                    s = currword[:i]+"_"+currword[i+1:]
                    for nextWord in adj[s]:  #if the word is in the visited we are adding the next word in the set
                        if nextWord not in visited:
                            visited.add(nextWord)
                            q.append(nextWord)  #and adding it in the queue
                            if nextWord == endWord:  #if the next word is same as ending word we are returning dist+1
                                return dist+1  
                                
        return 0  #if there is no match we are returning 0
                            
        
        