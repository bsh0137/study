array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start_idx = commands[i][0] - 1
        end_idx = commands[i][1]
        goal_idx = commands[i][2] - 1
        split_array = array[start_idx:end_idx]
        split_array.sort()
        answer.append(temp_array[goal_idx])
    return answer
answer = solution(array,commands)
print(answer)
