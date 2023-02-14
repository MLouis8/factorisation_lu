import numpy as np

def factorisation_lu(A):
    L = np.diag(np.ones((A.shape[0])))
    for id_act, line_act in enumerate(A):
        L1 = np.diag(np.ones((A.shape[0])))
        if A[id_act, id_act] == 0:
            return
        diag_elem = A[id_act, id_act]
        for ind, line in enumerate(A[id_act+1:]):
            real_id = ind+id_act+1
            temp_elem = A[real_id, id_act]
            factor = temp_elem/diag_elem
            A[real_id] = A[real_id] - factor * A[id_act]
            L1[real_id, id_act] += factor
        L = np.matmul(L, L1)
    U = A
    return L, U