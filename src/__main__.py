import os

import coconut_ai

if __name__ == '__main__':
    input_story_theme = "Create a story for children, featuring a little girl named Agathe, who takes the throne of the Snow Queen."
    input_story_name = "agathe-story"
    steps = 15

    output_folder_path = os.path.abspath(os.path.join("data", input_story_name))
    os.makedirs(output_folder_path, exist_ok=True)

    model_path = os.path.abspath(os.path.join("data", "models", "llama-2-7b.Q5_K_M.gguf"))
    comic_prompts = coconut_ai.text_to_text({
        'input_text': "You will make up the description of a 3 panel comic, telling a specific story. You will describe every panel visually one by one, each one with a single sentence ending with the character \"-\" to clearly separate every description of each panel. Your response will need to contain nothing other than those 3 visual descriptions. No more than 3 sentences to describe this comic. Also, the description of each panel will need to contain every information needed to indenpendently create the visual representation of them, so dont replace nouns with personal pronouns. The story will be about the following theme: " + input_story_theme + ".",
        'max_tokens': 1000,
        'model_path': model_path
    }).split("-")

    with open(os.path.join(output_folder_path, "story.txt"), "w", encoding="utf-8") as file:
        file.write(input_story_theme + "\n\n")
        for prompt_index in range(len(comic_prompts)):
            prompt = comic_prompts[prompt_index]
            output_text = "prompt_number: " + str(prompt_index + 1) + ", prompt: " + prompt + "\n"
            print(output_text)
            file.write(output_text)

            output_image_path = os.path.abspath(os.path.join(output_folder_path, "comic" + "-" + str(prompt_index + 1) + ".png"))
            coconut_ai.text_to_image({
                "input_text": prompt,
                "output_path": output_image_path,
                "steps": steps
            })
