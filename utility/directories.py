class directory: 
    def __init__(self):
        pass 

    def codedir(self, project='qfenv', plot=''): 
        if project == 'qfenv': 
            self.dir = '/home/users/hahn/research/pro/blanton/qf_environment/'
        elif project == 'sfrevol': 
            self.dir = '/home/users/hahn/research/pro/tinker/wetzel_tree/'
        elif project == 'fibcol': 
            self.dir = '/home/users/hahn/powercode/fiber_collision/'
        elif project == 'bispec': 
            self.dir = '/home/users/hahn/powercode/bispectrum/'
        elif project == 'powerspec': 
            self.dir = '/home/users/hahn/powercode/powerspectrum/'
        return self.dir 

    def figdir(self, project='qfenv'): 
        if project == 'qfenv': 
            self.dir = '/home/users/hahn/research/figures/primus/'
        elif project == '': 
            self.dir = '/home/users/hahn/research/figures/' 
        elif project == 'sfrevol': 
            self.dir = '/home/users/hahn/research/figures/tinker/'
        elif project == 'fibcol': 
            dir = '/home/users/hahn/research/figures/boss/fiber_collision/'
        elif project == 'bispec': 
            dir = '/home/users/hahn/research/figures/boss/bispectrum/'
        elif project == 'powerspec': 
            dir = '/home/users/hahn/research/figures/boss/powerspectrum/'
        return self.dir 

    def addsubdir(self, subdir):
        self.dir = ''.join([self.dir, subdir])

    def addfile(self, file): 
        self.dir = ''.join([self.dir, file])
