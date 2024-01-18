# 初期の方策を決定するパラメータtheta_0を定義

# 行は状態0~7、列は移動方向で⇧,⇓,⇨,⇐を表す
theta_0 = np.array([[np.nan, 1, 1, np.nan], #S0
                   [np.nan, 1, np.nan, 1],
                   [np.nan, np.nan, 1, 1],
                   [1,1,1, np.nan],
                   [np.nan, np.nan, 1, 1],
                   [1, np.nan, np.nan, np.nan],
                   [1, np.nan, np.nan, np.nan],
                   [1, 1, np.nan, np.nan],
])

# 方策パラメータthetaを行動方策piに変換する関数の定義

def simple_convert_into_pi_from_theta(theta):
    ''' 単純に割合を計算する '''

    [m, n] = theta.shape # thetaの行列サイズを取得
    pi = np.zeros((m, n))
    for i in range(0, m):
        pi[i, :] = theta[i, :] / np.nansum(theta[i, :]) #割合の計算
        """
        [i, :]では、i-1行all列の要素を抜き出している。
        つまり、[m,n]でm-1行n-1列の要素にアクセスできる。
        そして、:をすることで行の全要素か全列かに指定してアクセスできる。
        """

    pi = np.nan_to_sum(pi) # nanを0に変換

    return pi
    
