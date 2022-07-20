from RS_toolkit import RS_read
from RS_toolkit import cordinate_3D
from RS_toolkit import euclidean_distance_between_2_points
import threading

df = 0
dci = 0
ci = 0
cint = 0


def thread_function(name):

    while(True):
        global df, dci, ci, cint
        #random.random()
        df, dci, ci, cint = RS_read()
        #var_global = random.random()
        #print(var_global)

thread = threading.Thread(target=thread_function, args=(1,))
thread.start()


# x = threading.Thread(target=thread_function, args=(1,))
# x.start()

while True:

    def dis(x1, y1, x2, y2):

        global df, dci, ci, cint
        cord1 = cordinate_3D(df, cint, x1, y1)
        cord2 = cordinate_3D(df, cint, x2, y2)
        # cord1 = x1 + y1 + df
        # cord2 = x2 + y2 + cint
        #
        # dis = cord1 + cord2
        dis = euclidean_distance_between_2_points(cord1, cord2)
        print(dis)
        return dis
# x.join()

thread.join()
    # cv2.imshow("color Stream", ci)
    # cv2.imshow("depth Stream", dci)
    # cv2.waitKey(1)
