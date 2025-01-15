
## Prompts for HumanEval-X

- Each language has 164 prompts
- Check `benchmark_data/humaneval-x` folder for prompts. 

## Steps to get HumanEval-X scores.

#### Step 1: Get model generated responses.

```
python ./scripts_python_01/model_generated_code.py
```

- Model responses can be from any model. 
- The above script is only for reference.

#### Step 2: Execute code and get pass@1 metrics.

```
bash ./scripts_bash_01/run_evals.sh
```

- This needs to be executed inside a docker. See Dockerfile.