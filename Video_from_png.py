import os 
path='files/generated/mp4/'
if not os.path.exists(path):
    os.makedirs(path)
    print("The mp4 directory is created")
def makevideo(vidname):
    if os.path.exists(path+vidname+'.mp4')==True:
        print(vidname,'.mp4 already exists so I am going to continue')
        return
    os.system('ffmpeg -r 10 -f image2 -pattern_type glob -i "files/generated/png/{}/*?png" -vcodec libx264 -crf 20 -pix_fmt yuv420p files/generated/mp4/{}.mp4'.format(vidname,vidname))
    return

for folder in os.listdir('files/generated/png/'):
    if 'SOL' in folder:
        print(folder)
        makevideo(folder)

