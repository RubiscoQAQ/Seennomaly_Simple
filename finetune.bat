set MODEL_NAME=vaegan
set TRAINSET_NAME=rico_gif
set TRAIN_DIR=G:\\models\\vaegan
set TRAINSET_DIR=G:\\tf_record\\rico_gif

python main.py --train_dir=G:\\models\\vaegan --dataset_split_name=train --dataset_dir=G:\\tf_record\\rico_gif --model_name=vaegan --max_number_of_steps=1000000 --batch_size=8 --learning_rate=0.01 --learning_rate_decay_type=fixed --save_interval_secs=600 --save_summaries_secs=300 --max_to_keep=3 --log_every_n_steps=10 --optimizer=adam --weight_decay=0.00004
pause