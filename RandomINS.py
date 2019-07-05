import sys
import numpy as np
from BSTree import BST
from RBTree import RBT
import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt

def random_list(n):
    A = list(range(n))
    random.shuffle(A)
    return A
def sorted_list(n):
    A = list(range(n))
    return A
def main():
    sys.setrecursionlimit(10000)
    tree_BS = BST()
    tree_RB = RBT()
    number_of_node = 10
    number_of_test = 2
    matrix_of_time_BS = np.zeros((number_of_node, number_of_test))
    matrix_of_time_RB = np.zeros((number_of_node, number_of_test))
    for n in range(number_of_node):
        number = 10 + n * 100
        A = random_list(number)
        for t in range(number_of_test):
            print("Test = ", t)
            print("n = ", number)
            startInsert = timer()
            for i in range(len(A)):
                tree_BS.insert(A[i])
            endInsert = timer()
            elapsedInsert = endInsert - startInsert
            matrix_of_time_BS[n][t] =  elapsedInsert
            tree_BS = BST()
            startInsertRB = timer()
            for j in range(len(A)):
                tree_RB.insert(A[j])
            endInsertRB = timer()
            elapsedInsertRB = endInsertRB - startInsertRB
            matrix_of_time_RB [n][t]= elapsedInsertRB
            tree_RB = RBT()
    print("Matrice dei tempi di inserimento BS: \n", matrix_of_time_BS)
    print("Matrice dei tempi di inserimento RB: \n", matrix_of_time_RB)
    y_BS = []
    for a in range(number_of_node):
        y_BS.append(np.sum(matrix_of_time_BS[a]/number_of_test))
    x_BS = []
    for b in range(number_of_node):
        x_BS.append(10 + b* 100)
    y_RB = []
    for c in range(number_of_node):
        y_RB.append(np.sum(matrix_of_time_RB[c]/number_of_test))
    x_RB = []
    for d in range(number_of_node):
        x_RB.append(10 + d * 100)
    plt.scatter(x_BS, y_BS, color = 'r', s=.3, label = 'BS')
    plt.scatter(x_RB, y_RB, color = 'y', s=.3, label = 'RB')
    lineBS = plt.plot(x_BS, y_BS)
    plt.setp(lineBS, color='r', linewidth=2.0)
    lineRB = plt.plot(x_RB, y_RB)
    plt.setp(lineRB, color='y', linewidth=2.0)
    plt.ylim(0, 0.004)
    plt.ylabel("tempo")
    plt.xlabel("elementi inseriti")
    plt.title("Tempo inserim. nuovo nodo in modo casuale")
    plt.legend(loc = 'upper left')
    plt.show()

if __name__ == "__main__":
    main()