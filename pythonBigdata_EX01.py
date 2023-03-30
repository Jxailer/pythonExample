# 퇴근시간인 오후 6시~10시 하차 인원 최대 역 찾기
# Find the station with the maximum number of people getting off at 6-10 PM, which is the rush hour.

import csv
file = open('e:/py/subwaytime.csv', 'r')
data = csv.reader(file)
next(data)
next(data)

mx_station = ['', -1]
getOffNum = -1

for row in data:

    for i in range (4, 52) :
        row[i] = int(row[i].replace(',', ''))
        # 엑셀값에 포함된 ','를 지움
        # deleted ',' in excel chart value
    for j in range (33, 40, 2):
        getOffNum += row[j]
        # row의 33번째 값부터 39번째 값(6-10시 까지의 총 하차인원 수)까지의 합을 구함
        # Calculates the sum from the 33rd value to the 39th value of row (total number of people getting off from 6-10:00)

    if getOffNum > mx_station[1]:
        mx_station[0] = row[3]
        mx_station[1] = getOffNum
        # 기존의 값과 비교하여 하차 인원의 합이 더 크다면 최대값을 갱신함
        # compared to old value, if new value is bigger, revise max value.

print("출퇴근 시간에 하차 수가 가장 많은 역은 "+ mx_station[0] +"역 입니다.")
print("the station with the maximum number of people getting off at 6-10 PM, which is the rush hour is: "+ mx_station[0]+" station")

