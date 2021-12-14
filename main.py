import time

data = {
	"meet1": {
		"code": "10",
		"name": "Яловичина",
		"price2": 25.5,
		"price10": 23.5,
		"price14": 30.8,
		"price24": 23.7,
		"months": "серпень"
},
	"pig_meet1": {
		"code": "20",
		"name": "Свинина",
		"price2": 25.0,
		"price10": 23.5,
		"price14": 25.5,
		"price24": 25.7,
		"months": "серпень"
},
	"salo1": {
		"code": "30",
		"name": "Сало",
		"price2": 14.4,
		"price10": 14.5,
		"price14": 14.5,
		"price24": 14.5,
		"months": "серпень"



},
	"meet2": {
		"code": "10",
		"name": "Яловичина",
		"price2": 23.5,
		"price10": 24.0,
		"price14": 24.0,
		"price24": 24.5,
		"months": "вересень"
},
	"pig_meet2": {
		"code": "20",
		"name": "Свинина",
		"price2": 25.5,
		"price10": 26.0,
		"price14": 26.3,
		"price24": 26.5,
		"months": "вересень"
},
	"salo2": {
		"code": "30",
		"name": "Сало",
		"price2": 14.5,
		"price10": 14.6,
		"price14": 14.8,
		"price24": 15.0,
		"months": "вересень"


},	"meet3": {
		"code": "10",
		"name": "Яловичина",
		"price2": 25.0,
		"price10": 25.0,
		"price14": 25.5,
		"price24": 25.5,
		"months": "жовтень"
},
	"pig_meet3": {
		"code": "20",
		"name": "Свинина",
		"price2": 26.6,
		"price10": 26.8,
		"price14": 27.0,
		"price24": 27.4,
		"months": "жовтень"
},
	"salo3": {
		"code": "30",
		"name": "Сало",
		"price2": 15.5,
		"price10": 15.5,
		"price14": 15.6,
		"price24": 16.0,
		"months": "жовтень"
}
}

midle_meet1 = data['meet1']['price2']+data['meet1']['price10']+data['meet1']['price14']+data['meet1']['price14']
midle_meet1 = midle_meet1//4
midle_meet2 = data['meet2']['price2']+data['meet2']['price10']+data['meet2']['price14']+data['meet2']['price14']
midle_meet2 = midle_meet2//4
midle_meet3 = data['meet3']['price2']+data['meet3']['price10']+data['meet3']['price14']+data['meet3']['price14']
midle_meet3 = midle_meet3//4

midle_pig_meet1 = data['pig_meet1']['price2']+data['pig_meet1']['price10']+data['pig_meet1']['price14']+data['pig_meet1']['price14']
midle_pig_meet1 = midle_pig_meet1//4
midle_pig_meet2 = data['pig_meet2']['price2']+data['pig_meet2']['price10']+data['pig_meet2']['price14']+data['pig_meet2']['price14']
midle_pig_meet2 = midle_pig_meet2//4
midle_pig_meet3 = data['pig_meet3']['price2']+data['pig_meet3']['price10']+data['pig_meet3']['price14']+data['pig_meet3']['price14']
midle_pig_meet3 = midle_pig_meet3//4

midle_salo1 = data['salo1']['price2']+data['salo1']['price10']+data['salo1']['price14']+data['salo1']['price14']
midle_salo1 = midle_salo1//4
midle_salo2 = data['salo2']['price2']+data['salo2']['price10']+data['salo2']['price14']+data['salo2']['price14']
midle_salo2 = midle_salo2//4
midle_salo3 = data['salo3']['price2']+data['salo3']['price10']+data['salo3']['price14']+data['salo3']['price14']
midle_salo3 = midle_salo3//4

def main():

	enter = int(input(\
"""
+------------+
|ГОЛОВНЕ МЕНЮ|
+------------+

[1]Вивести таблицю

[2]Вивести довідник

[3]Вивести аналіз

[4]Вихід


Вам потрібно: """))

	if enter == 4:
		exit()

	elif enter == 1:
		print(\
f"""

+----------+------------+---------------------------------------------------------+
|Код товару|Назва товару|на 2 число|на 10 число|на 14 число|на 24 число|  Місяць  |
+----------+------------+---------------------------------------------------------+
|    {data['meet1']['code']}    |  {data['meet1']['name']} |   {data['meet1']['price2']}   |    {data['meet1']['price10']}   |    {data['meet1']['price14']}   |     {data['meet1']['price24']}  | {data['meet1']['months']}  |
+----------+------------+---------------------------------------------------------+
|    {data['pig_meet1']['code']}    |   {data['pig_meet1']['name']}  |   {data['pig_meet1']['price2']}   |    {data['pig_meet1']['price10']}   |    {data['pig_meet1']['price14']}   |     {data['pig_meet1']['price24']}  | {data['pig_meet1']['months']}  |
+----------+----------------------------------------------------------------------+
|    {data['salo1']['code']}    |    {data['salo1']['name']}    |   {data['salo1']['price2']}   |    {data['salo1']['price10']}   |    {data['salo1']['price14']}   |     {data['salo1']['price24']}  | {data['salo1']['months']}  |
+----------+------------+---------------------------------------------------------+
|    {data['meet2']['code']}    |  {data['meet2']['name']} |   {data['meet2']['price2']}   |    {data['meet2']['price10']}   |    {data['meet2']['price14']}   |     {data['meet2']['price24']}  | {data['meet2']['months']} |
+----------+------------+---------------------------------------------------------+
|    {data['pig_meet2']['code']}    |   {data['pig_meet2']['name']}  |   {data['pig_meet2']['price2']}   |    {data['pig_meet2']['price10']}   |    {data['pig_meet2']['price14']}   |     {data['pig_meet2']['price24']}  |{data['pig_meet2']['months']}  |
+----------+----------------------------------------------------------------------+
|    {data['salo2']['code']}    |    {data['salo2']['name']}    |  {data['salo2']['price2']}   |    {data['salo2']['price10']}   |    {data['salo2']['price14']}   |     {data['salo2']['price24']}  | {data['salo2']['months']}  |
+----------+----------------------------------------------------------------------+
|    {data['meet3']['code']}    |  {data['meet3']['name']} |   {data['meet3']['price2']}  |    {data['meet3']['price10']}   |    {data['meet3']['price14']}   |     {data['meet3']['price24']}  | {data['meet3']['months']}   |
+----------+------------+---------------------------------------------------------+
|    {data['pig_meet3']['code']}    |   {data['pig_meet3']['name']}  |  {data['pig_meet3']['price2']}   |    {data['pig_meet3']['price10']}   |    {data['pig_meet3']['price14']}   |     {data['pig_meet3']['price24']}  | {data['pig_meet3']['months']}   |
+----------+----------------------------------------------------------------------+
|    {data['salo3']['code']}    |    {data['salo3']['name']}   |   {data['salo3']['price2']}   |    {data['salo3']['price10']}   |    {data['salo3']['price14']}   |     {data['salo3']['price24']}  | {data['salo3']['months']}   |
+----------+----------------------------------------------------------------------+

""")
		time.sleep(2)
		main()

	elif enter == 2:
		print(\
f"""
+----------+------------+----------------------------------+
|Код товару|Назва товару|Одиниця Виміру|Роздрібна ціна, грн|
+----------+------------+----------------------------------+
|    {data['meet1']['code']}    | {data['meet1']['name']}  |      кг      |        25.5       |
+----------+------------+----------------------------------+
|    {data['pig_meet1']['code']}    |  {data['pig_meet1']['name']}   |      кг      |        26.5       |
+----------+------------+----------------------------------+
|    {data['salo1']['code']}    |    {data['salo1']['name']}    |      кг      |        15.0       |
+----------+------------+----------------------------------+
""")
		time.sleep(2)
		main()

	elif enter == 3:
		print(\
f"""
+----------+------------+--------+------------+--------------+-----------+
|Код товару|Назва товару| Місяць |Середня ціна|Роздрібна ціна|Рівень змін|
+----------+------------+--------+------------+--------------+-----------+
|    {data['meet1']['code']}    | {data['meet1']['name']}  | {data['meet1']['months']}|    {midle_meet1}    |     25.50    |    1.01   |
+----------+------------+--------+------------+--------------+-----------+
|    {data['meet2']['code']}    | {data['meet2']['name']}  |{data['meet2']['months']}|    {midle_meet2}    |     25.50    |    1.01   |
+----------+------------+--------+------------+--------------+-----------+
|    {data['meet3']['code']}    | {data['meet3']['name']}  | {data['meet3']['months']}|    {midle_meet3}    |     25.50    |    1.01   |
+----------+------------+--------+------------+--------------+-----------+
|    {data['pig_meet1']['code']}    |   {data['pig_meet1']['name']}  | {data['pig_meet1']['months']}|    {midle_pig_meet1}    |     25.50    |    1.01   |
+----------+------------+--------+------------+--------------+-----------+
|    {data['pig_meet2']['code']}    |   {data['pig_meet2']['name']}  |{data['pig_meet2']['months']}|    {midle_pig_meet2}    |     25.50    |    1.01   |
+----------+------------+--------+------------+--------------+-----------+
|    {data['pig_meet3']['code']}    |   {data['pig_meet3']['name']}  | {data['pig_meet3']['months']}|    {midle_pig_meet3}    |     25.50    |    1.01   |
+----------+------------+--------+------------+--------------+-----------+
|    {data['salo1']['code']}    |     {data['salo1']['name']}   | {data['salo1']['months']}|    {midle_salo1}    |     25.50    |    1.01   |
+----------+------------+--------+------------+--------------+-----------+
|    {data['salo2']['code']}    |     {data['salo2']['name']}   |{data['salo2']['months']}|    {midle_salo2}    |     25.50    |    1.01   |
+----------+------------+--------+------------+--------------+-----------+
|    {data['salo3']['code']}    |     {data['salo3']['name']}   | {data['salo3']['months']}|    {midle_salo3}    |     25.50    |    1.01   |
+----------+------------+--------+------------+--------------+-----------+
""")
		time.sleep(2)
		main()




if __name__ == '__main__':
	main()