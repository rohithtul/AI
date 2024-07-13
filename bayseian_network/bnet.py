import numpy as np
import sys

def calculate_probabilities(training_file):
    # define the conditional probability values
    p_b = np.zeros(2)
    p_bg = np.zeros((2, 2))
    p_c = np.zeros(2)
    p_gcf = np.zeros((2, 2, 2))

    # read the training data from the file
    with open(training_file, "r") as f:
        for line in f:
            b, g, c, f = map(int, line.split())
            # update the counts for each variable
            p_b[b] += 1
            p_bg[b, g] += 1
            p_c[c] += 1
            p_gcf[g, c, f] += 1

    # probability calculations
    p_b /= p_b.sum()
    p_bg /= p_bg.sum(axis=1, keepdims=True)
    p_c /= p_c.sum()
    p_gcf /= p_gcf.sum(axis=2, keepdims=True)
    return p_b, p_bg, p_c, p_gcf

def print_probabilities(p_b, p_bg, p_c, p_gcf):
    # print the conditional probability tables
    print("P(B):\nB\tP(B)")
    for i in range(2):
        print("{}\t{:.4f}".format(i, p_b[i]))
    # print P(G|B)
    print("\nP(G|B):\nB\tG=0\tG=1")
    for i in range(2):
        print("{}\t{:.4f}\t{:.4f}".format(i, p_bg[i][0], p_bg[i][1]))
    # print P(C)
    print("\nP(C):\nC\tP(C)")
    for i in range(2):
        print("{}\t{:.4f}".format(i, p_c[i]))
    # print P(F|G,C)
    print("\nP(F|G,C):"
          "\nF\tG=0,C=0\tG=0,C=1\tG=1,C=0\tG=1,C=1")
    for f in range(2):
        print("{}\t{:.4f}\t{:.4f}\t{:.4f}\t{:.4f}".format(f, p_gcf[0][0][f], p_gcf[0][1][f], p_gcf[1][0][f],
                                                          p_gcf[1][1][f]))

def compile_input(val):
    if val[-1].lower() == 't':
        return 1
    else:
        return 0
def calculate_jpd(p_b, p_bg, p_c, p_gcf, B, G, C, F):
    jpd = p_b[B] * p_bg[B, G] * p_c[C] * p_gcf[G, C, F]
    return jpd

if __name__ == "__main__":
    # read the command line arguments
    training_file = sys.argv[1]
    p_b, p_bg, p_c, p_gcf = calculate_probabilities(training_file)
    if len(sys.argv) > 2:
        # task 2 : create JPD values
        B = compile_input(sys.argv[2])
        G = compile_input(sys.argv[3])
        C = compile_input(sys.argv[4])
        F = compile_input(sys.argv[5])
        jpd = calculate_jpd(p_b, p_bg, p_c, p_gcf, B, G, C, F)
        print("Probability when \n B={}, G={}, C={}, F={}: {}".format(B, G, C, F,jpd))
    else:
        # task1 : print conditional probability values
        print_probabilities(p_b, p_bg, p_c, p_gcf)