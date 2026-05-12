# high_scores.py

def get_score(name):
    for line in open('scores.txt'):
        if name in line:
            return int(line.split()[1])
    return None

all_names = ['Bob', 'Alice', 'Charlie', 'Bev']

high_scores = [get_score(name) for name in all_names if get_score(name) is not None
                                                     if get_score(name) > 90]
# high_scores = [score for name in all_names if (score := get_score(name)) is not None 
#                                            if score > 90]
print(high_scores)
