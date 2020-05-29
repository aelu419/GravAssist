import os
from src.body import body

class ephemeris:

    def __init__(self, sp, root_dir, METADATA='metadata.tm', mode='LT+S', observer='SOLAR SYSTEM BARYCENTER'):
        self.sp = sp
        #os.chdir(root_dir + '/src/SPICE/')
        os.listdir('.')
        self.sp.furnsh(root_dir+'/kernels/naif0012.tls')
        self.sp.furnsh(root_dir+'/kernels/pck00010.tpc')
        self.sp.furnsh(root_dir+'/kernels/gm_de431.tpc')
        self.sp.furnsh(root_dir+'/kernels/de438.bsp')
        self.sp.furnsh(root_dir+'/kernels/voyager_1.ST+1991_a54418u.merged.bsp')
        self.sp.furnsh(root_dir+'/kernels/voyager_2.ST+1992_m05208u.merged.bsp')

        os.chdir(root_dir)
        self.mode = mode
        self.observer = observer

    def get_body(self, target):
        return body(target, self.sp, self.mode, self.observer)
