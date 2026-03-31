class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ans = []
        c = 0
        leng = len(beginWord)
        def pass_rule(a,b):
            z = 0
            for i in range(leng):
                if a[i] != b[i]:
                    z+=1
            return True if z == 1 else False
        
        if endWord not in wordList:
            return 0

        visited = set()
        def dfs(word):
            nonlocal c
            if pass_rule(word, beginWord):
                ans.append(c)
                return True
            visited.add(word)
            for w in wordList:
                if w in visited:
                    continue
                if pass_rule(word, w):
                    c+=1
                    if dfs(w) is True:
                        c-=1
                        continue
                    c-=1
            visited.remove(word)

        dfs(endWord)
        print(ans)
        if ans == []:
            return 0
        return min(ans) + 2