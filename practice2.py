# Дан словарь с балансом пользователей, пример:
# balance = { 'user1': 100, 'user2': 500 }
# В примере у user1 - 100 "денег", у user2 - 500.
# Так же дан список transactions состоящий из словарей, каждый из которых транзакция.
# Ключ транзакции - имя пользователя,
# значение - количество "денег". Положительное значение добавляет деньги к балансу, отрицательное - убавляет. Пример:
# transactions = [ {'user1': -10}, {'user2': -20}, {'user1': 50}, {'user2': -20}, {'user2': -100}, ]
# Написать фунцкию apply_transactions(balance, transactions) которая принимает эти данные и вычисляет финальный баланс
# пользователей после всех транзакций. Гарантировано, что все пользователи указанные в транзакциях существуют в словаре
# balance.
# Для нашего примера после вызова функции balance должен содержать в себе:
# { 'user1': 140, 'user2': 360 }

balance = {'user1': 100, 'user2': 500}
transactions = [{'user1': -10}, {'user2': -20}, {'user1': 50}, {'user2': -20}, {'user2': -100}]


# def apply_transactions(balance: dict, transactions: [dict]):
#     for transaction in transactions:
#         transaction_user = list(transaction.keys())
#         if transaction_user[0] == "user1":
#             balance['user1'] += transaction['user1']
#         else:
#             balance['user2'] += transaction['user2']#

# print(apply_transactions(balance1, transactions1))

def apply_transactions(balance: dict, transactions: [dict]):
    for transaction in transactions:
        for user, spendings in transaction.items():
            balance[user] += spendings


print(apply_transactions(balance, transactions))
print(balance)

