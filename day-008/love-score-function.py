def calculate_love_score(name1, name2):
    combined_name = name1 + name2
    lower_names = combined_name.lower()
    t = lower_names.count('t')
    r = lower_names.count('r')
    u = lower_names.count('u')
    e = lower_names.count('e')
    true_total = t + r + u + e
    l = lower_names.count('l')
    o = lower_names.count('o')
    v = lower_names.count('v')
    e = lower_names.count('e')
    love_total = l + o + v + e
    love_score = int(str(true_total) + str(love_total))
    print(love_score)
    
calculate_love_score("Dylan", "Jessica")