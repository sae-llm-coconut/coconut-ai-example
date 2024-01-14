# coconut-ai-example

Example usage of [`coconut-ai` Python library](https://github.com/sae-llm-coconut/coconut-ai/).

## Getting Started

### Prerequisites

- [Python](https://www.python.org/) v3.10
- [Pipenv](https://pipenv.pypa.io/)
- [AUTOMATIC1111/Stable Diffusion Web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) v1.6.0

### Usage

```sh
# Go to AUTOMATIC1111/Stable Diffusion web UI source code
cd stable-diffusion-webui

# Run the AUTOMATIC1111/Stable Diffusion Web API
./webui.sh --api --nowebui

# Go to coconut-ai-example source code
cd ../coconut-ai-example
pipenv install

# Run the coconut-ai example script
pipenv run start --type="text_to_image" --input="Coconut" --output="./data/output.png"
```

## 💡 Contributing

Anyone can help to improve the project, submit a Feature Request, a bug report or even correct a simple spelling mistake.

The steps to contribute can be found in the [CONTRIBUTING.md](./CONTRIBUTING.md) file.

## 📄 License

[MIT](./LICENSE)
