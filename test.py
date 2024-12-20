# import os
# os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
# import torch
# print(torch.cuda.is_available())
# print(torch.version.cuda)
# print(torch.backends.cudnn.enabled)


import pickle


with open('stubs/track_stubs.pkl', 'rb') as f:
    try:
        data = pickle.load(f)
        print(data)  # Check the loaded data
    except EOFError:
        print("File is empty or corrupted.")