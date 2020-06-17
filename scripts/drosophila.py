import numpy as np
def conn_mat(conn):
    map_neurons_to_inds={}
    uniq=np.array(list(set(np.union1d(conn[:,0],conn[:,1]))))
    for j in range(0,uniq.shape[0]):
        map_neurons_to_inds[uniq[j]]=j
    #print(map_neurons_to_inds)
    conn_m=np.zeros((uniq.shape[0],uniq.shape[0]))
    for row in range(0,conn.shape[0]):
        pre=map_neurons_to_inds[conn[row,0]]
        post=map_neurons_to_inds[conn[row,1]]
        weight=conn[row,2]
        conn_m[pre,post]=weight
    return conn_m

def depth_first_search(con_mat,v,visited_arr):
    to_visit=np.nonzero(con_mat[v,:].flatten())[0]
    visited_arr[v]=1
    for j in range(0,to_visit.shape[0]):
        u=to_visit[j]
        if visited_arr[u]==0:
            depth_first_search(con_mat,u,visited_arr)
    return visited_arr
