'''
2018 KAKAO BLIND RECRUITMENT
#을 처리하기가 까다로움 -> replace 활용
'''
def solution(m, musicinfos):
    music = list()
    result = list()
    
    m = m.replace('C#', 'c', len(m))
    m = m.replace('D#', 'd', len(m))
    m = m.replace('F#', 'f', len(m))
    m = m.replace('G#', 'g', len(m))
    m = m.replace('A#', 'a', len(m))
    
    for i in musicinfos:
        tmp = i.split(',')
        tmp[3] = tmp[3].replace('C#', 'c', len(tmp[3]))
        tmp[3] = tmp[3].replace('D#', 'd', len(tmp[3]))
        tmp[3] = tmp[3].replace('F#', 'f', len(tmp[3]))
        tmp[3] = tmp[3].replace('G#', 'g', len(tmp[3]))
        tmp[3] = tmp[3].replace('A#', 'a', len(tmp[3]))
        hour = int(tmp[1][:2]) - int(tmp[0][:2])
        minute = int(tmp[1][3:]) - int(tmp[0][3:])
        minute += 60*hour
        mod = minute % len(tmp[3])
        music.append([minute, tmp[2], tmp[3]*(minute//len(tmp[3])) + tmp[3][:mod]])
        
    for k, i in enumerate(music):
        if m in i[2]:
            result.append([i[0], k, i[1]])
            
    if result:
        result.sort(key = lambda x: (x[0], -x[1]))
        return result[-1][-1]
    else:
        return '(None)'
