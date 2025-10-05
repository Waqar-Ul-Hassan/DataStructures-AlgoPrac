class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        q = deque([(beginWord, 1)])  # (currentWord, steps)

        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        q.append((newWord, steps + 1))

        return 0