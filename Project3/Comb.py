

class Factorial():

    def factorial(self, n):
        if n == 0:
            return 1

        res = 1
        for i in range(2, n + 1):
            res *= i

        return res

    def A(self, n, k):
        return int(self.factorial(n) / self.factorial(n - k))

    def A1(self, n, k):
        return int(n ** k)

    def C(self, n, k):
        return int((self.factorial(n)) / (self.factorial(k) * self.factorial(n - k)))

    def C1(self, n, k):
        return int((self.factorial(n + k - 1)) / (self.factorial(k) * self.factorial(n - 1)))

    def gen_perm(self, lst):
        x = -1
        y = -1
        for i in range(0, len(lst) - 1):
            if lst[i] < lst[i + 1]:
                x = i
                y = i + 1

        min_in_end = y
        for i in range(y, len(lst)):
            if lst[i] < lst[min_in_end] and lst[x] < lst[i]:
                min_in_end = i

        lst[x], lst[min_in_end] = lst[min_in_end], lst[x]

        lst_end = lst[y:len(lst)]
        lst_end.sort()
        lst = lst[0:y]
        lst += lst_end

        return lst

    def gen_comb(self, lst, n, k, first_elem):
        res_lst = lst[0:k]

        ai = 0
        for i in range(0, k):
            if res_lst[i] != n - k + i + first_elem:
                ai = i

        res_lst[ai] += 1

        for j in range(ai + 1, k):
            res_lst[j] = res_lst[j - 1] + 1

        return res_lst





