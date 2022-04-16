## Script to collect negative images

###
#   ONLY EXECUTE WHEN NEEDED
###


from icrawler.builtin import BingImageCrawler 
import os


classes=['trees','roads','cats images']
number=0
for c in classes:
    bing_crawler=BingImageCrawler(storage={'root_dir':f'n/{c.replace(" ",".")}'}) #see n is represent negaive images 
    bing_crawler.crawl(keyword=c,filters=None,max_num=number,offset=0)

def name_change(path, name):
    count = 0
    for filename in os.listdir(path): 
            dst = name + str(count) + ".jpg"
            src = path + filename 
            dst = path + dst 
            
            # rename() will rename all the files 
            os.rename(src, dst)
            count += 1

name_change("C:/Users/emree/Documents/Robotica/2/HumanMachineInterface/vision/vision/n/cats.images/", "cats")
name_change("C:/Users/emree/Documents/Robotica/2/HumanMachineInterface/vision/vision/n/roads/", "roads")
name_change("C:/Users/emree/Documents/Robotica/2/HumanMachineInterface/vision/vision/n/trees/", "trees")