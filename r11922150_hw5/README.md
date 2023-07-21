# run r11922150_hw5.ipynb to train the model and finish the problem1
## training back model
arch_args = Namespace( #modelhere
    encoder_embed_dim=512,
    encoder_ffn_embed_dim=2048,
    encoder_layers=6,
    decoder_embed_dim=512,
    decoder_ffn_embed_dim=2048,
    decoder_layers=6,
    share_decoder_input_output_embed=True,
    dropout=0.3,
)
## training bt model 
arch_args = Namespace( #modelhere
    encoder_embed_dim=1024,
    encoder_ffn_embed_dim=4096,
    encoder_layers=6,
    decoder_embed_dim=1024,
    decoder_ffn_embed_dim=4096,
    decoder_layers=6,
    share_decoder_input_output_embed=True,
    dropout=0.3,
)
# gradescope.ipynb is for gradescope problem2 (use rnn architechture and train only 15 epochs) 