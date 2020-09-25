import os
import glob
malPath = "/home/yongbak/gym-malware/gym_malware/envs/utils/samples/"
goodPath = "./"
if __name__ == "__main__":
    # way to use glob
    # print(glob.glob(malPath+"*"))

    # memory-saved list
    # malwares = [m.split("/")[-1] for m in glob.glob(malPath+"*")]
    # goodwares = [g.split("/")[-1] for g in glob.glob(goodPath+"*")]
   
    # transparent list
    malwares = [m for m in glob.glob(malPath+"*")]
    goodwares = [g for g in glob.glob(goodPath+"*")]

    with open("train.csv", 'w') as f:
        #write malware samples
        for m in malwares:
            f.write(m + ", 1\n")
        for g in goodwares:
            f.write(g + ", 0\n")