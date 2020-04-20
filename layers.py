import numpy as np

def affine_forward(x, w, b):
    '''
    fully connected layer
    :param x: (N,d_1,d_2,...,d_k)->(N,D)
    :param w: (D, M)
    :param b: (M,)
    :return: out (N,M)
    '''
    out = x.reshape(x.shape[0], -1).dot(w) + b
    cache = (x, w, b)
    return out, cache

def affine_backward(dout, cache):
    '''
    BP fully connected layer
    :param dout: Upstream derivative (N,M)
    :param cache: x, w, b
    :return: dx (N,d1,...,d_k)
            dw (D,M)
            db (M,)
    '''
    x, w, b = cache
    dx = dout.dot(w.T).reshape(x.shape)
    dw = x.reshape(x.shape[0],-1).T.dot(dout)
    db = np.sum(dout,axis=0)
    return dx, dw, db

def relu_forward(x):
    out = np.maximum(0, x)
    cache = x
    return out, cache

def relu_backword(dout, cache):
    x = cache
    dx = np.where(x > 0, dout, 0)
    return dx

def batchnorm_forward(x, gamma, beta, bn_param):
    mode = bn_param['mode']
    eps = bn_param.get('eps', 1e-5)
    momentum = bn_param.get('momentum', 0.9)

    N ,D = x.shape
    running_mean = bn_param.get('running_mean', np.zeros(D, dtype=x.dtype))
    running_var = bn_param.get('running_var', np.zeros(D, dtype=x.dtype))

    out, cache = None, None
    if mode == 'train':
        mu = x.mean(axis=0)
        xc = x - mu
        var = np.mean(xc**2, axis=0)
        std = np.sqrt(var+eps)
        xn = xc / std
        out = gamma * xn + beta
        cache = (mode, x, gamma, xc, std, xn, out)
        pass #TODO

def batchnorm_backward(dout, cache):
    pass

def dropout_forward(x, parameters, keep_prob=0.5):
    np.random.seed(1)
    W1 = parameters['W1']
    b1 = parameters['b1']

    Z1 = np.dot(W1, x) + b1
    A1 = relu_forward(Z1)
    D1 = np.random.rand(Z1.shape[0],Z1.shape[1])
    D1 = D1< keep_prob # 根据概率将D1中的元素设为0或1
    A1 = A1 * D1
    A1 = A1 / keep_prob
    return A1