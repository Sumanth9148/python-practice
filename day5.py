# minimum window substring

def minimum_window_substring(s: str, t: str) -> str:
    if not s or not t:
        return ""
    
    from collections import Counter

    need=Counter(t)
    missing=len(t)

    left=0
    start=0
    min_len=float('inf')

    for right,ch in enumerate(s):
        if need[ch]>0:
            missing-=1
        need[ch]-=1

        while missing==0:
            if right-left+1<min_len:
                min_len=right-left+1
                start=left

            need[s[left]]+=1
            if need[s[left]]>0:
                missing+=1
            left+=1

    return "" if min_len==float('inf') else s[start:start+min_len]

print(minimum_window_substring(s="ADOBECODEBANC", t="ABC")) 



#decode string

def decode_string(s: str) -> str:
    stack=[]

    if not s:
        return ""
    
    for ch in s:
        if ch != ']':
            stack.append(ch)
        else:
            curr=""
            while stack and stack[-1]!='[':
                curr=stack.pop()+curr
            stack.pop()

            num=""
            while stack and stack[-1].isdigit():
                num=stack.pop()+num

            stack.append(curr*int(num))

    return "".join(stack)

print(decode_string(s="3[a2[c]]"))
