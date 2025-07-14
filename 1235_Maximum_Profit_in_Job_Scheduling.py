class Solution:
    def jobScheduling(self, inicio: list[int], fim: list[int], lucro: list[int]) -> int:
        trabalhos = sorted(zip(fim, inicio, lucro))

        tempos_dp = [0]       # Lista dos tempos de término considerados
        lucros_dp = [0]       # Lista dos lucros acumulados máximos até cada tempo

        for fim_trabalho, inicio_trabalho, lucro_atual in trabalhos:

            idx = bisect.bisect_right(tempos_dp, inicio_trabalho) - 1

            lucro_com_trabalho = lucros_dp[idx] + lucro_atual

            if lucro_com_trabalho > lucros_dp[-1]:
                lucros_dp.append(lucro_com_trabalho)
                tempos_dp.append(fim_trabalho)
            else:
                lucros_dp.append(lucros_dp[-1])
                tempos_dp.append(fim_trabalho)

        # O último valor em lucros_dp é o lucro máximo possível
        return lucros_dp[-1]