def calculate_love_score(name1, name2):
    word1 = "true"
    word2 = "love"
    count1 = 0
    for letter in word1:
        if letter in name1:
            count1 += 1
        if letter in name2:
            count1 += 1
    
    count2 = 0
    for letter in word2:
        if letter in name1:
            count2 += 1
        if letter in name2:
            count2 += 1 
                
    total_score = str(count1) + str(count2)
    
    print(total_score)
    
calculate_love_score("yasin", "gonca")   