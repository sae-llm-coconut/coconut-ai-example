import os

import coconut_ai

if __name__ == '__main__':
    input_story_theme = "Coconut"
    steps = 20

    model_path = os.path.abspath(os.path.join("data", "llama-2-7b.Q5_K_M.gguf"))
    comic_prompts = coconut_ai.text_to_text({
        'input_text': "You will make up the description of a 3 panel comic, telling a specific story. You will describe every panel visually one by one, each one with a single sentence ending with a point. Your response will need to contain nothing other than those four visual description. The story will be of the following theme: " + input_story_theme + ".",
        'max_tokens': 1000,
        'model_path': model_path
    }).split(".")
    prompt_number = 0
    for prompt in comic_prompts:
        print("prompt_number: " + str(prompt_number) + ", prompt: " + prompt)
        output_path = os.path.abspath(os.path.join("data", "comic" + "-" + str(prompt_number) + ".png"))
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        coconut_ai.text_to_image({
            "input_text": prompt,
            "output_path": output_path,
            "steps": steps
        })
        prompt_number = prompt_number + 1
