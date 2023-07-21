import torch
from torchvision.utils import save_image
from stylegan2_pytorch import ModelLoader
import torchvision.transforms as transforms
import os ,sys
name = sys.argv[1]
loader = ModelLoader(
    base_dir = '.',   # path to where you invoked the command line tool
    name = name                   # the project name, defaults to 'default'
)

os.mkdir(name)
transform = transforms.Resize((64, 64))
for i in range(1000):
    noise   = torch.randn(1, 512).cuda() # noise
    styles  = loader.noise_to_styles(noise, trunc_psi = 0.7)  # pass through mapping network
    images  = loader.styles_to_images(styles) # call the generator on intermediate style vectors
    save_image(transform(images), f'./{name}/{i}.jpg') # save your images, or do whatever you desire

