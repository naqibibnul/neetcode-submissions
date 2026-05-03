class Solution:

    def encode(self, strs: List[str]) -> str:
        
        send = ""
        
        for i in range(len(strs)):
            send += str(len(strs[i]))
            send += '@'
            send += strs[i]
        print(send)
        return send

    def decode(self, s: str) -> List[str]:
          
        output = []  
        i = 0
        
        while i < len(s):
            j = i

            while s[j] != '@':
                j+=1
            print(s[i:j])
            length = int(s[i:j])

            start = j + 1
            end = start + length

            word = s[start:end]

            output.append(word)

            i = end

        return output


        

        
        # for i in range(len(temp)):
        #     if temp[i] != '@':
        #         current += temp[i]
        #     else:
        #         output.append(current)
        #         current = ""
        # return output