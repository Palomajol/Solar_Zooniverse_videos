import os
import sunpy.map
import matplotlib.animation as animation

path = 'files/generated/mp4/'

def Exists(path):
    ans = os.path.exists(path)
    return ans

isExist=Exists(path)
if not isExist:
    os.makedirs(path)
    print("The mp4 directory is created")

directory = 'files/fits/'

def makevideo(aia_map_sequence,vidname,overwrite=False):
    if overwrite==False and os.path.exists(path+vidname+'.mp4')==True:
        print('Video {} already exists, so I am not going to continue'.format(vidname))
        return
    ani = aia_map_sequence.plot()
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=10, metadata=dict(artist='SunPy'), bitrate=1800)
    ani.save(path+vidname+'.mp4', writer=writer)

for folder in os.listdir(directory):
    if 'SOL' in folder:
        print(folder)
        sequence= sunpy.map.Map(directory+folder+'/'+'*.fts',sequence=True)
        makevideo(sequence,folder)

