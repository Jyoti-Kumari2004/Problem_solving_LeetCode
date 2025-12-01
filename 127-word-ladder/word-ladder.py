class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        words=set(wordList)
        n=len(beginWord)
        q=deque()
        q.append((beginWord,1))
        
        while q:
            word,at=q.popleft()
            if (word==endWord):
                return at
            for i in range(n):
                for ch in alpha :
                    new_word=word[:i]+ch+word[i+1:]
                    if new_word in words:
                        q.append((new_word,at+1))
                        words.remove(new_word)
        return 0


        