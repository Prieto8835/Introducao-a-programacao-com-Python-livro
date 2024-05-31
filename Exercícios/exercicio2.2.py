#Digite a seguinte expressão no interpretador:
#10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2
#exercicio para mostrar a prioridade na resolução de expressões!

print(10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2)

# 0 --> 10 % 3 * 10 ** 2 + 1 - 10 * 4 / 2
# 1 --> 10 % 3 * 100     + 1 - 10 * 4 / 2
# 2 --> 1      * 100     + 1 - 10 * 4 / 2
# 3 -->          100     + 1 - 10 * 4 / 2
# 4 -->          100     + 1 - 40     / 2
# 5 -->          100     + 1 - 20
# 6 -->          101         - 20
# 7 -->                        81