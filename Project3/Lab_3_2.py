from Comb import Factorial


class get_combinations(Factorial):

    def get_all_perms(self):
        print("Your array:\n ")

        A = [int(x) for x in input().split(", ")]
        print('Entered array:')
        print(A)
        print('-----------------')
        print('All permutations:')
        for i in range(1, self.factorial(len(A))):
            A = self.gen_perm(A)
            print(A)

    def gen_all_combs(self):
        print("Your array:\n ")

        A = [int(x) for x in input().split(", ")]
        print("n = ", end="")
        n = int(input())
        print("k = ", end="")
        k = int(input())
        first_elem = A[0]
        print('----------------')
        print('All combinations: ')
        print(A[0:k])
        for i in range(1, self.C(n, k)):
            A = self.gen_comb(A, n, k, first_elem)

            print(A)

combs = get_combinations()

combs.get_all_perms()


combs.gen_all_combs()
