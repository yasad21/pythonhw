def cacti_number(d2):
        counter = 0
        
        for i in range(len(d2)):
            for j in range(len(d2[i])):
                if d2[i][j] == 0:
                    replace = True
                    if i > 0 and d2[i-1][j] != 0:
                        replace = False
                    if i < len(d2) - 1 and d2[i+1][j] != 0:
                        replace = False
                    if j > 0 and d2[i][j-1] != 0:
                        replace = False
                    if j < len(d2[i]) - 1 and d2[i][j+1] != 0:
                        replace = False
                    if replace:
                        d2[i][j] = 1
                        counter += 1
                        
        return counter
