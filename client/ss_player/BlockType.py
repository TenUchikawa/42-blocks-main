from enum import Enum
from typing import Any

import numpy as np


class BlockType(Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    H = 'H'
    I = 'I'
    J = 'J'
    K = 'K'
    L = 'L'
    M = 'M'
    N = 'N'
    O = 'O'
    P = 'P'
    Q = 'Q'
    R = 'R'
    S = 'S'
    T = 'T'
    U = 'U'
    X = 'X'

    @property
    def block_map(self) -> np.ndarray[Any, np.dtype[int]]:
        if self == BlockType.A:
            ''' 
            type A:
             ■ 
            '''
            return np.array([[1]])
        elif self == BlockType.B:
            ''' 
            type B:
             ■ 
             ■ 
            '''
            return np.array([[1], [1]])
        elif self == BlockType.C:
            '''
            type C:
             ■ 
             ■ 
             ■ 
            '''
            return np.array([[1], [1], [1]])
        elif self == BlockType.D:
            '''
            type D:
             ■ 
             ■ ■ 
            '''
            return np.array([[1, 0], [1, 1]])
        elif self == BlockType.E:
            '''
            type E:
             ■ 
             ■ 
             ■ 
             ■ 
            '''
            return np.array([[1], [1], [1], [1]])
        elif self == BlockType.F:
            '''
            type F:
               ■ 
               ■ 
             ■ ■ 
            '''
            return np.array([[0, 1], [0, 1], [1, 1]])
        elif self == BlockType.G:
            '''
            type G:
             ■ 
             ■ ■ 
             ■    
            '''
            return np.array([[1, 0], [1, 1], [1, 0]])
        elif self == BlockType.H:
            '''
            type H:
             ■ ■ 
             ■ ■ 
            '''
            return np.array([[1, 1], [1, 1]])
        elif self == BlockType.I:
            '''
            type I:
             ■ ■ 
               ■ ■ 
            '''
            return np.array([[1, 1, 0], [0, 1, 1]])
        elif self == BlockType.J:
            '''
            type J:
             ■ 
             ■ 
             ■ 
             ■ 
             ■ 
            '''
            return np.array([[1], [1], [1], [1], [1]])
        elif self == BlockType.K:
            '''
            type K:
               ■ 
               ■ 
               ■ 
             ■ ■ 
            '''
            return np.array([[0, 1], [0, 1], [0, 1], [1, 1]])
        elif self == BlockType.L:
            '''
            type L:
               ■ 
               ■ 
             ■ ■ 
             ■ 
            '''
            return np.array([[0, 1], [0, 1], [1, 1], [1, 0]])
        elif self == BlockType.M:
            '''
            type M:
               ■ 
             ■ ■ 
             ■ ■ 
            '''
            return np.array([[0, 1], [1, 1], [1, 1]])
        elif self == BlockType.N:
            '''
            type N:
             ■ ■ 
               ■ 
             ■ ■ 
            '''
            return np.array([[1, 1], [0, 1], [1, 1]])
        elif self == BlockType.O:
            '''
            type O:
             ■ 
             ■ ■ 
             ■ 
             ■ 
            '''
            return np.array([[1, 0], [1, 1], [1, 0], [1, 0]])
        elif self == BlockType.P:
            '''
            type P:
               ■ 
               ■ 
             ■ ■ ■ 
            '''
            return np.array([[0, 1, 0], [0, 1, 0], [1, 1, 1]])
        elif self == BlockType.Q:
            '''
            type Q:
             ■ 
             ■ 
             ■ ■ ■ 
            '''
            return np.array([[1, 0, 0], [1, 0, 0], [1, 1, 1]])
        elif self == BlockType.R:
            '''
            type R:
             ■ ■ 
               ■ ■ 
                 ■ 
            '''
            return np.array([[1, 1, 0], [0, 1, 1], [0, 0, 1]])
        elif self == BlockType.S:
            '''
            type S:
             ■ 
             ■ ■ ■ 
                 ■ 
            '''
            return np.array([[1, 0, 0], [1, 1, 1], [0, 0, 1]])
        elif self == BlockType.T:
            '''
            type T:
             ■ 
             ■ ■ ■ 
               ■ 
            '''
            return np.array([[1, 0, 0], [1, 1, 1], [0, 1, 0]])
        elif self == BlockType.U:
            '''
            type U:
               ■ 
             ■ ■ ■ 
               ■ 
            '''
            return np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
        elif self == BlockType.X:
            '''
            type X:パスをする時用
                 
                   
                 
            '''
            return np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        
        else:
            raise NotImplementedError
