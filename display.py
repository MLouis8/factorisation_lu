import matplotlib.pyplot as plt

def display_matrix_pyplot(M):
    plt.matshow(M)
    plt.show()

def display_matrix_lateX(M):
    print("$\\begin{pmatrix}")
    epsilon = 0.01
    size = len(M.shape)
    if size == 1:
        for elem in M:
                print(f"{elem} \\\\", end='\n')
    elif size == 2:
        for l in M:
            beginning = True
            for elem in l:
                if (elem - int(elem) <= epsilon):
                    elem = int(elem)
                print(f"{elem}", end=' ') if beginning else print(f"& {elem}", end=' ')
                beginning = False
            print("\\\\", end='\n')
    else:
        raise ValueError("taille incompatible")
    print("\\end{pmatrix}$")