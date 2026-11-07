#cos dziwnie w poleceniu zew tam zero jest przy godzinach i niby ma dac 12
def time_string(hours, minutes, time_format):
    czas = ''
    

    if time_format == '12' and hours == 0 and minutes < 10:
        czas = f'12:0{minutes}am'
    elif time_format == '12' and hours == 0:
        czas = f'12:{minutes}am'
        

    elif time_format == '12' and hours > 12 and minutes < 10:
        czas = f'{hours-12}:0{minutes}pm'
    elif time_format == '12' and hours > 12:
        czas = f'{hours-12}:{minutes}pm'
    elif time_format == '12' and hours == 12 and minutes < 10:
        czas = f'12:0{minutes}pm'
    elif time_format == '12' and hours == 12:
        czas = f'12:{minutes}pm'
        
    elif time_format == '12' and hours < 12 and minutes < 10:
        czas = f'{hours}:0{minutes}am'
    elif time_format == '12' and hours < 12:
        czas = f'{hours}:{minutes}am'
        
    elif time_format == '24' and hours < 10 and minutes < 10:
        czas = f'0{hours}:0{minutes}'
    elif time_format == '24' and minutes < 10:
        czas = f'{hours}:0{minutes}'
    elif time_format == '24' and hours < 10:
        czas = f'0{hours}:{minutes}'
    elif time_format == '24':
        czas = f'{hours}:{minutes}'
        
    return czas