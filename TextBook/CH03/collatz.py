def collatz(number):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return 3 * number + 1
while True:
    try:
        print('整数を入力してください：')
        i = int(input())
        break
    except ValueError:
        print('エラー：整数値を入力してください。')

while i > 1:
    i = collatz(i)
    print(i)
