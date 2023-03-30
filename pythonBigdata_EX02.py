# 새벽 3시부터 익일 새벽 4시까지 승차한 사람의 총 합이 가장 큰 역 이름 및 승차 인원 출력
# printing the station with a maximum number of people getting on between 4 am to 3 am (11hours) and how many are they.


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
    for j in range (4, 49, 2):
        getOffNum += row[j]
        # row의 4번째 값부터 49번째 값(4시-익일 3시 까지의 총 승차인원 수)까지의 합을 구함
        # Calculates the sum from the 5th value to the 49th value of row (total number of people getting on subway from 4am to 3am(for 11 hours))

    if getOffNum > mx_station[1]:
        mx_station[0] = row[3]
        mx_station[1] = getOffNum
        # 기존의 값과 비교하여 하차 인원의 합이 더 크다면 최대값을 갱신함
        # compared to old value, if new value is bigger, revise max value.

print("새벽 3시부터 익일 새벽 4시까지 승차한 사람의 총 합이 가장 큰 역 이름은 " + str(mx_station[0]) + "역 이고, 총 승차 인원은 " +  str(mx_station[1]) +"명 입니다.")
print("the name of the station with a maximum number of people getting on between 4 am to 3 am (11hours) is " + str(mx_station[0]) + " and how many are they is: " + str(mx_station[1]))

