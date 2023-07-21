# training 
num_epoch = 10
validation = True
logging_step = 100
learning_rate = 1e-5
wd = 1e-3
optimizer = AdamW(model.parameters(), lr=learning_rate,weight_decay = wd)
train_batch_size = 8
scheduler = LinearLR(optimizer, start_factor=1.0, end_factor=1/100, total_iters=num_epoch, verbose = True)
gradient_accumulation_steps = 16
用以上config 改變 random seed 得到3個模型的ensembel結果 