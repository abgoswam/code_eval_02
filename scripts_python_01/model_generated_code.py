import json
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm

def jsonl_2_data(file_path):
    # Initialize an empty list to store the dictionaries
    list_of_dicts = []

    # Open and read the JSONL file
    with open(file_path, 'r') as file:
        for line in file:
            # Parse each line as a JSON object and append to the list
            list_of_dicts.append(json.loads(line.strip()))

    return list_of_dicts


def data_2_jsonl(list_of_dicts, file_path):
    # Writing the list of dictionaries to a JSONL file
    with open(file_path, "w") as file:
        for entry in list_of_dicts:
            json.dump(entry, file)
            file.write("\n")


def model_generate(input_text, model, tokenizer):
    inputs = tokenizer(input_text, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=256,
    )

    prompt_text_token_len = inputs['input_ids'].shape[1]
    generated_text = tokenizer.decode(outputs[0][prompt_text_token_len:], skip_special_tokens=True)
    # print(generated_text)

    return generated_text

def get_model_tokenizer(model_name):
    # load model and tokenizer
    # model_name = "mistralai/Mistral-7B-v0.1"  # Replace with the actual model name on Hugging Face Hub

    tokenizer = AutoTokenizer.from_pretrained(
        model_name,
        trust_remote_code=True)

    # Load model onto GPU
    # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto")
    
    # Retrieve and display the eos_token_id
    eos_token_id = tokenizer.eos_token_id
    eos_token = tokenizer.decode([eos_token_id]) if eos_token_id is not None else "No eos_token defined"
    print("EOS Token ID:", eos_token_id)
    print("EOS Token:", eos_token)

    return model, tokenizer


if __name__ == "__main__":

    file_name_py = r"/home/abgoswam/_hackerreborn/code_eval_01/benchmark_data/humaneval-x/humaneval_python.jsonl"
    file_name_go = r"/home/abgoswam/_hackerreborn/code_eval_01/benchmark_data/humaneval-x/humaneval_go.jsonl"
    file_name_ru = r"/home/abgoswam/_hackerreborn/code_eval_01/benchmark_data/humaneval-x/humaneval_rust.jsonl"
    file_name_ja = r"/home/abgoswam/_hackerreborn/code_eval_01/benchmark_data/humaneval-x/humaneval_java.jsonl"
    file_name_js = r"/home/abgoswam/_hackerreborn/code_eval_01/benchmark_data/humaneval-x/humaneval_js.jsonl"
    file_name_cp = r"/home/abgoswam/_hackerreborn/code_eval_01/benchmark_data/humaneval-x/humaneval_cpp.jsonl"

    file_names = [
        file_name_py,
        file_name_go,
        file_name_ru,
        file_name_ja,
        file_name_js,
        file_name_cp
    ]

    # ====================================
    # get model, tokenizer.
    model_name_or_path = "mistralai/Codestral-22B-v0.1"
    _model, _tokenizer = get_model_tokenizer(model_name_or_path)

    # ====================================
    # generate data. 
    for file_name in file_names:
        print(f"processing file: {file_name}")
        file_data = jsonl_2_data(file_name)
        
        file_data_generations = []
        for item in tqdm(file_data, desc="Processing tasks"):
            task_id = item["task_id"]
            prompt = item["prompt"]
            # print(prompt)

            generation = model_generate(prompt, _model, _tokenizer)
            d = {
                "task_id": task_id,
                "generation": generation,
                "prompt": prompt
            }
            file_data_generations.append(d)

        # Modify the file name to include "_generations" before the extension
        new_file_name = file_name.replace(".jsonl", "_generations.jsonl")
        data_2_jsonl(file_data_generations, new_file_name)

    print("done")