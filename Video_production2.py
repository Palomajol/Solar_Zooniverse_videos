import os
import sunpy.map
import matplotlib.animation as animation

Startdir=os.getcwd()
print(Startdir)

path = 'files/generated/mp4/'

isExist=os.path.exists(path)
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
        os.chdir(directory+folder+'/')
        print(os.getcwd())
        try:
            sequence= sunpy.map.Map('*.fts',sequence=True)
        except:
            maps= []
            files=os.listdir()
            for f in files:
                try: 
                    maps.append(sunpy.map.Map(f))
                except:
                    print('error opening {:s}' .format(f))
            if len(maps)==0:
                print('No video was made due to too little frames')
                os.chdir(Startdir)
                continue
            print(maps)
            sequence=sunpy.map.Map(maps, sequence=True)
        os.chdir(Startdir)
        print(os.getcwd())
        makevideo(sequence,folder,overwrite=False)


