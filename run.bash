model_name_or_path=facebook/wav2vec2-base
# dataset_name=Tevatron/wikipedia-nq+
dataset_name=squad_v2
output_dir=models
batch_size=64
num_train_epochs=5
max_seq_length=384
save_steps=10000

CUDA_VISIBLE_DEVICES=0 python src/run_audio_classification.py \
    --model_name_or_path $model_name_or_path \
    --dataset_name $dataset_name \
    --dataset_config_name waxal \
    --output_dir wav2vec2-base-ft-keyword-spotting \
    --overwrite_output_dir \
    --remove_unused_columns False \
    --do_train \
    --do_eval \
    --learning_rate 3e-5 \
    --max_length_seconds 1 \
    --validation_split_percentage 20 \
    --report_to_wandb \
    --attention_mask False \
    --warmup_ratio 0.1 \
    --num_train_epochs 5 \
    --per_device_train_batch_size 4 \
    --gradient_accumulation_steps 4 \
    --per_device_eval_batch_size 4 \
    --logging_strategy steps \
    --logging_steps 10 \
    --evaluation_strategy epoch \
    --save_strategy epoch \
    --load_best_model_at_end True \
    --metric_for_best_model accuracy \
    --save_total_limit 3 \
    --seed 0