def time_string(hours, minutes, time_format):
    czas=''
    if time_format=='12' and hours>12 :
        czas=f'{hours-12}:{minutes}pm'
    elif time_format=='12' and hours<=12 :
        czas=f'{hours}:{minutes}am'
    elif time_format=='24' and hours:
        czas=f'{hours}:{minutes}'
    return czas

print(time_string(15, 38, '24'))
print(time_string(8, 3, '24'))