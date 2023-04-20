import torch
import numpy as np
import ctypes

import BAM_Feature_Store


class BAM_Tensor_Loader():
    def __init__(self, n : int, dim : int):
        self.filename = "f";
        self.cpu_tensor = torch.zeros([n,dim], dtype=torch.float)
        self.gpu_tensor = self.cpu_tensor.to('cuda:0')
        self.gpu_tensor_ptr = self.gpu_tensor.data_ptr()
    
        self.BAM_FS = BAM_Feature_Store.BAM_Feature_Store()
        self.BAM_FS.init_controllers()

    def fetch_feature(self):
        self.BAM_FS.read_feature(self.gpu_tensor_ptr)

    def print_gpuT(self):
        print(self.gpu_tensor)

    def fetch_data(self):
        cptr = self.gpu_tensor.data_ptr()
        cpu_ptr = self.cpu_tensor.data_ptr()
     #   example.set_val(cpu_ptr, 5, 8)

    def malloc(self, byte_size):
        cpu_ptr = example.c_malloc(byte_size)
        self.c_ptr = cpu_ptr
        return cpu_ptr

   # def read_ptr_val(self, ptr):
   #     return example.read_ptr_val(ptr)
   # def set_ptr_val(self, ptr, val):
   #     example.set_ptr_val(ptr, val)

    
  #  def set_cuda_val(self, idx, val):
  #      gpu_ptr = self.gpu_tensor.data_ptr()
  #      example.set_cuda_val(gpu_ptr, idx, val)

   # def print_gpu_tensor(self):
    #    print(self.gpu_tensor)




