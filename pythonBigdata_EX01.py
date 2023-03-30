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
    print(getOffNum)
    print(row[3])
    #퇴근 시간에 지하철에서 내린 사람 수의 합
    #sum of the number of people who get off the subway in rush time
    if getOffNum > mx_station[1]:
        mx_station[0] = row[3]
        mx_station[1] = getOffNum

print("출퇴근 시간에 하차 수가 가장 많은 역은 "+ mx_station[0] +"역 입니다.")
print("the station with the maximum number of people getting off at 6-10 PM, which is the rush hour is: "+ mx_station[0]+" station")

