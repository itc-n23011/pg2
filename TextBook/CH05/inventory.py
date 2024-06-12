def display_inventory(inventory):
    print("持ち物リスト:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("アイテム総数: " + str(item_total))

if __name__ == "__main__":
    stuff = {'ロープ': 1, 'たいまつ': 6, '金貨': 42, '手裏剣': 1, '矢': 12}
    display_inventory(stuff)
