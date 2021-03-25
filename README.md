# Программа для расчета баллов по новой схеме.

На входе используются таблицы, распределенные по квартилям из выгрузок WoS и Scopus:

w1.xlsx, w2.xlsx, w3.xlsx, w4.xlsx, w_none.xlsx, s1.xlsx, s2.xlsx, s3.xlsx, s4.xlsx, s_none.xlsx

На выходе программа выводит сумму баллов на экран

Используется библиотека pandas

Предполагаемый рейтинг:
- WoS Q1 = 138
- WoS Q2 = 51.1
- WoS Q3 = 18.9
- WoS Q4 = 7 
- other = 7

Даны публикации по квартилям WOS( w1,w2,w3,w4,w_none) и по квартилям Scopus (s1,s2,s3,s4,s_none).

Алгоритм
isColaborate = FALSE, total = 0 // N - доля ОмГТУ
1. *По всем элементам в w1_list, проверяем isCollaborate и N<1, то total = total + N * WoSQ1 * 1.2; Если нет total = total + N * WoSQ1*
2. *По всем элементам в w2_list, проверяем isCollaborate и N<1, то total = total + N * WoSQ2 * 1.2; Если нет total = total + N * WoSQ2*
3. *По всем элементам в w3_list, проверяем isCollaborate и N<1, то total = total + N * WoSQ3 * 1.2; Если нет total = total + N * WoSQ3* 
4. *По всем элементам в w4_list, проверяем isCollaborate и N<1, то total = total + N * WoSQ4 * 1.2; Если нет total = total + N * WoSQ4* 
5. *Объеденить все таблицы в общей DataFrame, удалить все дубликаты по ключу KEY*
6. *Из общего DataFrame вычесть данные по WoS*
7. *В полученном DataFrame, по всем элементам проверяем isCollaborate и N<1, то total = total + N * other * 1.2; Если нет total = total + N * other*
8. *Вывести total*

Ссылкы на проекты с получением квартилей

Из Scopus: https://github.com/nerudxlf/get_affilietions_and_names_from_scopus

Из WoS: https://github.com/nerudxlf/getting_quartiles_wos
