# 예외 case 파악하는 것이 중요

def solution(video_len, pos, op_start, op_end, commands):

    def min_to_sec(string):
        # print(string.split(':')[0])
        # print(string.split(':')[1])
        minute = string.split(':')[0]
        sec    = string.split(':')[1]
        
        return 60*int(minute) + int(sec)
        
    def sec_to_min(inteager):
        minute = inteager // 60
        sec    = inteager % 60
        
        if minute < 10:
            minute = "0" + str(minute)
        else:
            minute = str(minute)
            
        if sec < 10:
            sec = "0" + str(sec)
        else:
            sec = str(sec)   
            
        return minute + ":" + sec
        
    # print(min_to_sec(video_len))
    
    # print(sec_to_min(min_to_sec(video_len)))
    
    video_len = min_to_sec(video_len)
    pos       = min_to_sec(pos)
    op_start  = min_to_sec(op_start)
    op_end    = min_to_sec(op_end)
    
    # start_point = max(pos, op_start, op_end)
    start_point = pos
    
    for i in commands:
        if op_start <= start_point < op_end:
            start_point = op_end
        if i == "next":
            start_point += 10
        else:
            if start_point < 10:
                start_point = 0
            else:
                start_point -= 10
        
        start_point = min(start_point, video_len)

    # 중복되는 아래 두 코드를 처리하는 법?
    if op_start < start_point < op_end:
        start_point = op_end
        
    start_point = min(start_point, video_len)
        
    return sec_to_min(start_point)
