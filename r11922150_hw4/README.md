## Training
以此組參數並改變weight decay進行訓練
	"batch_size": 32,
	"n_workers": 8,
	"valid_steps": 2000,
	"warmup_steps": 1000,
	"save_steps": 10000,
	"total_steps": 10000000,
	d_model=256, n_spks=600, dropout=0.1):
	d_model=d_model, dim_feedforward=256, nhead=16

## Testing
kaggle最高成績為no weight decay 與 weight decay = 1e-2 兩個模型ensemble