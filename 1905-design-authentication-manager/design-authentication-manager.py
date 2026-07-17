class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl=timeToLive
        self.d={}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.d[tokenId]=currentTime+self.ttl
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.d and self.d[tokenId]>currentTime:
            self.d[tokenId]=currentTime+self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count=0
        for key,value in self.d.items():
            if value>currentTime:
                count+=1
        return count

        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)