# Приложение СТРАХОВАЯ КОМПАНИЯ для некоторой организации. БД должна
# содержать таблицу Договор со следующей структурой записи: дата заключения, страховая
# сумма, вид страхования, тарифная ставка и филиал, в котором заключался договор.

import sqlite3 as sq

with sq.connect("company_strah.db") as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS services")
    cur.execute("""CREATE TABLE IF NOT EXISTS services(data_zak date not null,
    strah_sum decimal(10,2) not null, strah_type text not null, stavka decimal(5,2) not null,
    filial varchar(20) not null)""")

    information = [
        ("10.10.2020 10:10:10", 100000, "Страхование жизни", 30, "Первый филиал"),
        ("10.10.2020 10:10:11", 100000, "Страхование жизни", 40, "Первый филиал"),
        ("10.10.2020 10:10:12", 100000, "Страхование жизни", 50, "Первый филиал"),
        ("10.10.2020 10:10:13", 100000, "Страхование жизни", 60, "Первый филиал"),
        ("10.10.2020 10:10:14", 100000, "Страхование жизни", 70, "Первый филиал"),
        ("10.10.2020 10:10:15", 100000, "Страхование жизни", 80, "Первый филиал"),
        ("10.10.2020 10:10:16", 100000, "Страхование жизни", 90, "Первый филиал"),
        ("10.10.2020 10:10:17", 100000, "Страхование жизни", 100, "Первый филиал"),
        ("10.10.2020 10:10:18", 100000, "Страхование жизни", 110, "Первый филиал"),
        ("10.10.2020 10:10:19", 100000, "Страхование жизни", 120, "Первый филиал")
    ]
    cur.executemany("INSERT INTO services VALUES (?, ?, ?, ?, ?)", information)
    # cur.execute("SELECT * FROM services ")
    # print(cur.fetchall())
    #
    # cur.execute("SELECT * FROM services WHERE stavka = ?", (30,))
    # print(cur.fetchall())
    # cur.execute("SELECT * FROM services WHERE filial = ?", ("Первый филиал",))
    # print(cur.fetchall())
    # cur.execute("SELECT data_zak,strah_type,stavka,filial FROM services WHERE strah_sum < ?",(1000,))
    # print(cur.fetchall())
    #
    # cur.execute("DELETE FROM services WHERE data_zak = ?", ("10.10.2020 10:10:10"))
    # cur.execute("DELETE FROM services WHERE stavka < ?", (40,))
    # cur.execute("DELETE FROM services WHERE strah_sum > ?", (1000000,))
    #
    # cur.execute("UPDATE services SET filial = ? WHERE data_zak = ? AND strah_sum = ? AND strah_type = ?",("Второй филилал", "10.10.2020 10:10:10", "100000", "Страхование жизни"))
    # cur.execute("UPDATE services SET strah_sum = ? WHERE data_zak = ? AND strah_type = ? AND stavka = ?",(200000, "10.10.2020 10:10:11", "Анна", "Владимировна"))
    # cur.execute("UPDATE services SET dohod = ? + 500 WHERE notary_type = ?",(1300, "Продажа коммерческой недвижимости"))