film = input("Введите название фильма: ")
film2 = int(film)
cinema = input("Введите название кинотеатра: ")
cinema2 = int(cinema)
time = input("Введите время: ")
time1 = int(time)

words = "Билет на %i в %i на %d забронирован."
res = words % (film2, cinema2, time1)
print(res)