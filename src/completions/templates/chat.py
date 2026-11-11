from completions.client import OllamaClient


def main() -> None:
    llm = OllamaClient()

    print(f"Model: {llm.model}")
    print(f"Server: {llm.client.base_url}")
    print("Waiting for a response...\n")

    response = llm.chat(
        prompt="Reply with exactly: Connection successful!",
        system="Follow the user's instructions precisely.",
    )

    print(response)


if __name__ == "__main__":
    main()