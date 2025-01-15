#!/bin/bash

cd CodeGeeX-01072025

# bash scripts/evaluate_humaneval_x.sh \
#     ../benchmark_data/humaneval-x/humaneval_python_generations.jsonl \
#     python 16

bash scripts/evaluate_humaneval_x.sh \
    ../benchmark_data/humaneval-x/generations_test_model/humaneval_cpp_generations.jsonl \
    cpp \
    16

bash scripts/evaluate_humaneval_x.sh \
    ../benchmark_data/humaneval-x/generations_test_model/humaneval_go_generations.jsonl \
    go \
    16

bash scripts/evaluate_humaneval_x.sh \
    ../benchmark_data/humaneval-x/generations_test_model/humaneval_java_generations.jsonl \
    java \
    16

bash scripts/evaluate_humaneval_x.sh \
    ../benchmark_data/humaneval-x/generations_test_model/humaneval_js_generations.jsonl \
    js \
    16

bash scripts/evaluate_humaneval_x.sh \
    ../benchmark_data/humaneval-x/generations_test_model/humaneval_python_generations.jsonl \
    python \
    16

bash scripts/evaluate_humaneval_x.sh \
    ../benchmark_data/humaneval-x/generations_test_model/humaneval_rust_generations.jsonl \
    rust \
    16
