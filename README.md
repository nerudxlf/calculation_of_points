# Программа для расчета баллов по новой схеме.

На входе используются таблицы, распределенные квартилям WOS( w1,w2,w3,w4,w_none) и по квартилям Scopus (s1,s2,s3,s4,s_none):

w1.xlsx, w2.xlsx, w3.xlsx, w4.xlsx, w_none.xlsx, s1.xlsx, s2.xlsx, s3.xlsx, s4.xlsx, s_none.xlsx

Ссылкы на проекты с получением квартилей
* Из Scopus: https://github.com/nerudxlf/get_affilietions_and_names_from_scopus
* Из WoS: https://github.com/nerudxlf/getting_quartiles_wos

На выходе программа выводит сумму баллов на экран

Используется библиотека pandas

Баллов по рейтингу (задаётся в коде):
* WoSQ1 = 138 (первый квартиль Q1 в системе Web of Science)
* WoSQ2 = 51.1
* WoSQ3 = 18.9
* WoSQ4 = 7 
* other = 7

Алгоритм

isColaborate = FALSE, 

total = 0 

// Ni - доля ОмГТУ в каждой конкретной публикации

1. *По всем i элементам в w1_list, проверяем isCollaborate и Ni<1, то total = total + Ni * WoSQ1 * 1.2; Если нет total = total + Ni * WoSQ1*
2. *По всем элементам в w2_list, проверяем isCollaborate и Ni<1, то total = total + Ni * WoSQ2 * 1.2; Если нет total = total + Ni * WoSQ2*
3. *По всем элементам в w3_list, проверяем isCollaborate и Ni<1, то total = total + Ni * WoSQ3 * 1.2; Если нет total = total + Ni * WoSQ3* 
4. *По всем элементам в w4_list, проверяем isCollaborate и Ni<1, то total = total + Ni * WoSQ4 * 1.2; Если нет total = total + Ni * WoSQ4* 
5. *Объеденить все таблицы в общей DataFrame, удалить все дубликаты по ключу KEY*
6. *Из общего DataFrame вычесть данные по WoS*
7. *В полученном DataFrame, по всем i элементам проверяем isCollaborate и Ni<1, то total = total + Ni * other * 1.2; Если нет total = total + Ni * other*
8. *Вывести total*


