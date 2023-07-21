# ML-HW3 
## Training 
901.ckpt由以下train_tfm訓練
train_tfm = transforms.Compose([
    transforms.RandomResizedCrop((256, 256)),
    transforms.ColorJitter(),
    transforms.RandomRotation(30),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
])

## testing
並以三張test time tfm 的影像放進模型輸出，相加決定prediction

