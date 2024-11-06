class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        l=[str(x) for x in range(10)]
        lSymbols=['-','+']
        out=''
        if len(s) == 0: return 0
        for i in range(len(s)):
            if i ==0 and (s[i] not in l or s[i] not in lSymbols):
                return 0
            if s[i] in l:
                out+=s[i]
            else:
                break
        if out[0:2] in ['-+','+-'] or (len(out) == 1 and out in ['-','+','.']):
            return 0
        if out.find("-",1) > 0:
            out="-"+out.split("-")[1]
        if out.find("+",0) > 0:
            out=out.split("+")[0]
        if  int(out) < 0 and int(out) < -2147483648:
            return -2147483648
        elif int(out) > 2147483647:
            return 2147483647
        return int(out)
        
s=Solution()
print(s.myAtoi("-5-"))

        