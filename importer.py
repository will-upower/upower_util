# import required module
import os
import shutil

directory = os.getcwd()
script_sample_dir = ""
sample_dir = "C:/CDNN/20230621_g4rocs_cdnn_scripting-v1.21/samples"
sample_dir_heading = "Sample_V4H1_"

# iterate over files in
# that directory
for dir in [f for f in os.listdir() if os.path.isdir(f)]:
    # print(dir)
    for f in os.listdir(dir + "/model"):
        if f.endswith(".onnx"):
            # print(f.strip(".onnx"))
            new_dir = sample_dir_heading + f.strip("*.onnx")
            new_dir = sample_dir + "/" + new_dir
            if (not os.path.exists(new_dir)):
                print("Creating directory: ", new_dir)
                os.mkdir(new_dir)
            print("Copying ", f, "to: ", new_dir)
            shutil.copy(dir+"/model/"+f, new_dir)

               