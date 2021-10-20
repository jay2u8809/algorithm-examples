''''
    Dictionary: https://dojang.io/mod/page/view.php?id=2307
'''

def solution(participant, completion):

    assert isinstance(participant, list), 'participant is not list'
    assert isinstance(completion, list), 'completion is not list'

    assert 1 <= len(participant) <= 100000, '1 <= participant <= 100000'
    assert len(participant) - 1 == len(completion), 'completion + 1 = participant'
    
    participant_dict = {}
    # participant_dict = dict.fromkeys(participant, 0)
    for p in participant:
        value = participant_dict.get(p, 0)
        participant_dict.update({
            p: 1 if value <= 0 else value + 1
        })

    for c in completion:
        value = participant_dict.get(c)
        participant_dict.update({
            c: value - 1
        })
    
    answer = ''
    for key in participant_dict.keys():
        if participant_dict.get(key) != 0:
            answer = key
            break

    return answer

# "leo"
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))

# "vinko"
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))

# "mislav"
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))