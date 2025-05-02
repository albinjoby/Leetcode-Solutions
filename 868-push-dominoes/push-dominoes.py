class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        n = len(dominoes)
        q = deque()

        for i, domino in enumerate(dominoes):
            if domino != ".":
                q.append((domino,i))

        while q:
            domino, i = q.popleft()

            if domino == "L":
                if i > 0 and dominoes[i-1] == '.':
                    dominoes[i-1] = "L"
                    q.append(("L",i-1))

            elif domino == "R":
                if i+1 < n and dominoes[i+1] == '.':
                    if i+2 < n and dominoes[i+2] == "L":
                        q.popleft()
                    else:
                        dominoes[i+1] = "R"
                        q.append(("R",i+1))
                
        return "".join(dominoes)
                    