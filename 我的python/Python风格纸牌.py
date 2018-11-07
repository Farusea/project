import collections

Card = collections.namedtuple('card', ['rank', 'huase'])

class FrenchDeck:
    # list("JQKA")是将元组转换成了列表
    ranks = [str(n) for n in range(2, 11)]  + list("JQKA") # 可以用列表["J", "Q", "k", "A"]
    # str.split()通过指定分隔符对字符串进行切片，如果参数num有指定值，则仅分割num个子字符串
    huase = "hongxin meihua fangkuai heitao".split()

# 构造函数，程序实例化的时候先执行这个函数，此函数中用元组是为了有序，两次for循环是因为有两个参数。
    def __init__(self):
        self._cards = [Card(rank, huase) for huase in self.huase
                                          for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]



beer_cards = Card('2', 'meihua')
print(beer_cards)
deck = FrenchDeck()
print(len(deck))
from  random import choice
print(choice(deck))
for card in deck:
    print(card)

for card in sorted(deck,key=spades_high):
    print(card)

