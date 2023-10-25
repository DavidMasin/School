import Games

if __name__ == '__main__':
    for i in range(100000):
        games = Games.Games()
        games.startNewGame()
        if i % 1000 == 0:
            print(str(i / 1000) + "%")
