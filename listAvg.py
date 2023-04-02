n = int(input()) 
test_list = list(map(int, input().split()))
max_score = max(test_list)
list = []
for score in test_list :
    list.append(score/max_score *100)
test_avg = sum(list)/n
print(test_avg)