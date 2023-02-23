def gulden_snede(n1, n2):
    return n2 / n1

def main(num_termen):
    eerste_term = 0
    tweede_term = 1

    for i in range(num_termen):
        print(eerste_term)

        volgende_term = eerste_term + tweede_term
        eerste_term = tweede_term
        tweede_term = volgende_term

    de_gulde_snede = gulden_snede(eerste_term, tweede_term)
    print("De gulden snede is:", de_gulde_snede)

if __name__ == "__main__":
    main(10) 