# 퇴근시간인 오후 6시~10시 하차 인원 최대 역 찾기
# Find the station with the maximum number of people getting off at 6-10 PM, which is the rush hour.

import csv
file = open('e:/py/subwaytime.csv', 'r')
data = csv.reader(file)
next(data)
next(data)

mx_station = ['stationName', -1]

for row in data:
    print(row)

    for i in range (4, 52) :
        row[i] = row[i].replace((',', ''))

        # if row[i] > mx_station[1]:
        #     mx_station[1] = row[i]
        #     mx_station[0] =

    row[4:] = map(int, row[4:])

    print(row)
    break



