import os
import argparse

import coconut_ai

if __name__ == '__main__':
    parser = argparse.ArgumentParser("coconut-ai")
    parser.add_argument("--type", help="The types of conversion you want to do.", choices=["text_to_image", "image_to_text", "text_to_text", "image_to_image", "BD"], required=True)
    parser.add_argument("--input", help="The prompt or image input.", type=str, required=True)
    parser.add_argument("--output", help="The output path.", type=str, required=True)
    parser.add_argument("--steps", help="The number of steps.", type=int, default=5, required=False)
    arguments = parser.parse_args()

    steps = arguments.steps

    if arguments.type == "text_to_image":
        output_path = os.path.abspath(arguments.output)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        print("---Text To Image---")
        print(f"Text: \"{arguments.input}\"")
        print(f"Image Output Path: \"{output_path}\"")
        print(f"Steps: {steps}")
        coconut_ai.text_to_image({
            "input_text": arguments.input,
            "output_path": output_path,
            "steps": steps
        })
    elif arguments.type == "image_to_image":
        input_path = os.path.abspath(arguments.input)
        output_path = os.path.abspath(arguments.output)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        print("---Image To Image---")
        print(f"Image Input Path: \"{input_path}\"")
        print(f"Image Output Path: \"{output_path}\"")
        print(f"Steps: {steps}")
        coconut_ai.image_to_image({
            "input_path": input_path,
            "output_path": output_path,
            "steps": steps
        })
    elif arguments.type == "BD":
        bd_prompts = coconut_ai.text_to_text({
            'input_text': "You will make up the description of a 3 panel comic, telling a specific story. You will describe every panel visually one by one, each one with a single sentence ending with a point. Your response will need to contain nothing other than those four visual description. The story you need to adapt is the following: " + arguments.input,
            'max_tokens': 1000,
            'model_path': model_path
        }).split(". ")
        prompt_number = 0
        for prompt in bd_prompts:
            print("prompt_number: " + prompt_number + ", prompt is " + prompt)
            output_path = os.path.abspath(arguments.output + "-" + prompt_number)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            coconut_ai.text_to_image({
                "input_text": bd_prompts[prompt_number]
                "output_path": output_path,
                "steps": steps
            })
            prompt_number = prompt_number + 1