class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 == 1:
            return False

        open_bracket = ['(','{','[']
        close_bracket = [')','}',']']
        
        fake_stack_open = []
        fake_stack_close = []
        for i in range(len(s)):
            if s[i] in open_bracket:
                fake_stack_open.append(s[i])
                print(f"open round {i} :", fake_stack_open)
                if not close_bracket[open_bracket.index(s[i])] in s:
                    return False
            else:
                if i == 0:
                    return False
                fake_stack_close.append(s[i])
                print(f"close round {i} :", fake_stack_close)
                if fake_stack_open == []:
                    return False
                if open_bracket[close_bracket.index(s[i])] != fake_stack_open[-1]:
                    return False
                else:
                    fake_stack_open.pop()
        
        if (fake_stack_open != []):
            return False
        
        return True
        