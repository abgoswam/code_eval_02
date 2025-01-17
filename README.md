
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

- This needs to be executed inside a docker. See Dockerfile.

- Do pip uninstall codegeex which comes with the image.

```
pip uninstall codegeex
```

- Install codegeex from locaal folder `CodeGeeX-01072025`

```
cd CodeGeeX-01072025/
pip install -e .
```

- Run the eval.

```
bash ./scripts_bash_01/run_evals.sh
```

##### Appendix.

docker run --gpus all -it --name container_4_code_eval_02 -v $(pwd):/workspace rishubi/codegeex
