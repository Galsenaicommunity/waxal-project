[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![Issues](https://img.shields.io/github/issues/Galsenaicommunity/waxal-project)
![PR](https://img.shields.io/github/issues-pr/Galsenaicommunity/waxal-project)

# Waxal Project
State of the art study of Keyword Spotting models to leverage the [Waxal](https://k4all.org/project/keyword-spotting-with-african-languages/) dataset.


## Running Commands

The following command shows how to fine-tune [wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the 🗣️ [Keyword Spotting](https://huggingface.co/datasets/galsenai/waxal_dataset) of the waxal dataset.

```bash
python src/run_audio_classification.py \
    --model_name_or_path facebook/wav2vec2-base \
    --dataset_name galsenai/waxal_dataset \
    --dataset_config_name waxal \
    --output_dir wav2vec2-base-ft-keyword-spotting \
    --overwrite_output_dir \
    --remove_unused_columns False \
    --do_train \
    --do_eval \
    --learning_rate 3e-5 \
    --max_length_seconds 1 \
    --validation_split_percentage 20 \
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
```
