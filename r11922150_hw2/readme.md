# leaderboard 最高分0.8409由以下兩組hyperparameters setting 的模型ensemble，將註解 ensemble 處 uncomment即可執行
## setting A
concat_nframes = 3
train_ratio = 0.95

seed = 42     
batch_size = 8      
num_epoch = 200        
learning_rate = 1e-3    
model_path = './model.ckpt'  
early_stop = 20
drop = 0.1

input_dim = 39 * concat_nframes  
hidden_layers = 5        
hidden_dim = 128      

## setting B
concat_nframes = 3
train_ratio = 0.95


seed = 11922150     
batch_size = 8        
num_epoch = 200     
   
learning_rate = 1e-3    
model_path = './model.ckpt'  
early_stop = 20
drop = 0.5

input_dim = 39 * concat_nframes  
hidden_layers = 5        
hidden_dim = 128      
