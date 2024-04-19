import numpy as np # type: ignore

def calculate(list):
    calculations ={}
    if(len(list)< 9 or len(list) > 9):
        raise ValueError("List must contain nine numbers.")
    m = np.array(list).reshape(3,3)
    medias_1 = [np.mean(fila) for fila in np.transpose(m)]
    medias_2 = [np.mean(fila) for fila in m]
    media_total = np.mean(m)
    medias = [medias_1, medias_2, media_total]
    varianza = [[np.var(fila) for fila in np.transpose(m)],[np.var(fila) for fila in m], np.var(m)]
    stdDesv=[np.sqrt(i).tolist() for i in varianza]
    maxM = [[np.max(fila) for fila in np.transpose(m)],[np.max(fila) for fila in m], np.max(m)]
    minM = [[np.min(fila) for fila in np.transpose(m)],[np.min(fila) for fila in m], np.min(m)]
    sumM = [[np.sum(fila) for fila in np.transpose(m)],[np.sum(fila) for fila in m], np.sum(m)]
    calculations['mean'] = medias
    calculations['variance'] = varianza
    calculations['standard deviation'] = stdDesv
    calculations['max'] = maxM
    calculations['min'] = minM
    calculations['sum'] = sumM
    return calculations
