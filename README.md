# Программа для расчета баллов по новой схеме.

На входе используются таблицы, распределенные по квартилям из выгрузок WoS(w1.xlsx, w2.xlsx, w3.xlsx, w4.xlsx, w_none.xlsx) и Scopus(s1.xlsx, s2.xlsx, s3.xlsx, s4.xlsx, s_none.xlsx), за 2020 год

На выходе программа выводит сумму баллов по рейтингу.

Используется библиотека pandas

Предполагаемый рейтинг:
- WoSQ1 = 138
- WoSQ2 = 51.1
- WoSQ3 = 18.9
- WoSQ4 = 7 
- other = 7


Алгоритм

isColaborate = FALSE // Используется для повышения балла (в 1.2) при коллабарации

total = 0

//Ni  доля ОмГТУ в каждой публикации

//Публикации по квартилям WoS загружаются в w1_list, w2_list, w3_list, w4_list, w_none_list соответственно

1. *По всем i элементам в w1_list, проверяем isCollaborate и Ni<1, то total = total + Ni * WoSQ1 * 1.2; Если нет total = total + Ni * WoSQ1*
2. *По всем i элементам в w2_list, проверяем isCollaborate и Ni<1, то total = total + Ni * WoSQ2 * 1.2; Если нет total = total + Ni * WoSQ2*
3. *По всем i элементам в w3_list, проверяем isCollaborate и Ni<1, то total = total + Ni * WoSQ3 * 1.2; Если нет total = total + Ni * WoSQ3* 
4. *По всем i элементам в w4_list, проверяем isCollaborate и Ni<1, то total = total + Ni * WoSQ4 * 1.2; Если нет total = total + Ni * WoSQ4* 
5. *Объеденить все таблицы (по Scopus и WoS) в общей DataFrame, удалить все дубликаты по ключу KEY*
6. *Из общего DataFrame вычесть данные по WoS*
7. *В полученном DataFrame, по всем элементам проверяем isCollaborate и Ni<1, то total = total + Ni * other * 1.2; Если нет total = total + Ni * other*
8. *Вывести total*

Ссылки на проекты по разбиению публикаций по квартилям WoS(w1.xlsx, w2.xlsx, w3.xlsx, w4.xlsx, w_none.xlsx) и Scopus(s1.xlsx, s2.xlsx, s3.xlsx, s4.xlsx, s_none.xlsx)

Из Scopus: https://github.com/nerudxlf/getting_quartiles_scopus

Из WoS: https://github.com/nerudxlf/getting_quartiles_wos
