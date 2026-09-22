        vowel={"a","e","i","o","u","A","E","I","O","U"}
        i=len(s)-1
        while i>=0 and s[i] in vowel:
            i-=1
        return s[:i+1] 