import os,shutil

folder={
        'images':["Image Extentions",".jpeg",".jpg",".png"],
        'audios':["Audio Extentions",".mp3",".wav",".amr"],
        'videos':["Video Extentions",".mp4",".mov",".avi",".mkv"],
        'documents':["Document Extentions",".doc",".xlsx",".ppt",".pptx",".xls",".pdf",".zip",".rar",".cvs",".docx",".txt"],
        'pythonfile':[".py"]
        }

# print(folder)
# for folder_name in folder:
#     print(folder_name,folder[folder_name])
def rename_folder():
    for folder in os.listdir(directry):
        if os.path.isdir(os.path.join(directry,folder))==True:
           os.rename(os.path.join(directry,folder),os.path.join(directry,folder.lower()))
        

def create_move(ext,file_name):
    find=False 
    for folder_name in folder:
         if"."+ext in folder[folder_name]:
             if folder_name not in os.listdir(directry):
                 os.mkdir(os.path.join(directry,folder_name))
             shutil.move(os.path.join(directry,file_name),os.path.join(directry,folder_name))
             find=True
             break
    if find!= True:
        if other_name not in os.listdir(directry):
            os.mkdir(os.path.join(directry,other_name))
        shutil.move(os.path.join(directry,file_name),os.path.join(directry,other_name))


directry="E:\\Durgesh Files\\Other\\(GUI) File Sorting Application\\files" #input("Enter The Location:")
other_name=input("Enter The Name For Unknown Files:")
rename_folder()
all_files=os.listdir(directry)
lenght=len(all_files)
count=1

for i in all_files:
    if os.path.isfile(os.path.join(directry,i))==True:
        # print("YES")
        create_move(i.split(".")[-1],i)    
    print(f"Total Files:{lenght}| Done:{count}| Left:{lenght-count}")
    count+=1    