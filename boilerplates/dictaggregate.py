

def solution(rollups,activity):
    output = {}
    for key ,value in activity.items():
        for key1, value1 in rollups.items():
            if key in value1:
                output[key1] = output.get(key1, 0) + sum(value)
    return output

if __name__=='__main__':
    activity = {
        'android':[1,0,0,0,0,0,1],
        'iphone':[0,1,0,1,0,0,0],
        'web':[0,1,1,1,1,0,1],
    }

    rollups = {
        'overall': ['iphone', 'android', 'web'],
        'mobile': ['iphone', 'android'],
    }

    print(solution(rollups, activity))



