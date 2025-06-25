import torch
from train import train
from utils import AttrDict
import yaml
import os
import pandas as pd

def get_config(file_path):
    with open(file_path, 'r', encoding="utf8") as stream:
        opt = yaml.safe_load(stream)
    opt = AttrDict(opt)
    if opt.lang_char == 'None':
        characters = ''
        for data in opt['select_data'].split('-'):
            csv_path = os.path.join(opt['train_data'], data, 'labels.csv')
            df = pd.read_csv(csv_path, sep='^([^,]+),', engine='python', usecols=['filename', 'words'], keep_default_na=False)
            all_char = ''.join(df['words'])
            characters += ''.join(set(all_char))
        characters = sorted(set(characters))
        opt.character= ''.join(characters)
    else:
        opt.character = opt.number + opt.symbol + opt.lang_char
    os.makedirs(f'./saved_models/{opt.experiment_name}', exist_ok=True)
    return opt

# Load configuration
opt = get_config('config_files/ja_custom local.yaml')

# Modify for quick test
opt.num_iter = 10
opt.valInterval = 5

print("Starting training test...")
print(f"Device: {'cuda' if torch.cuda.is_available() else 'cpu'}")
print(f"Model path: {opt.saved_model}")

# This should work now with our fix
train(opt, amp=False) 