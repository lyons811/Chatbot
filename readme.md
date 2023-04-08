This is a simple Tkinter graphical user interface(GUI) based chatbot that leverages OpenAI GPT-4 to generate conversation responses. The chatbot allows you to customize the type of chatbot you want to create and provides a dark mode theme toggle.

## Requirements

- Python 3.x
- `openai` package: Install it using pip:
  ```
  pip install openai
  ```

## Configuration

1. Set your OpenAI API key:

   ```
   openai.api_key = "your-api-key-here"
   ```

   Replace `your-api-key-here` with your OpenAI API key.

## Usage

Run the script, and enter the chatbot characteristics in the input field, e.g., "A helpful assistant."

Click the "Create" button to initialize the chatbot. The assistant will greet you with a system message.

Type your message in the lower input box and click "Send" to interact with the chatbot.

You can toggle the dark mode by clicking the "Toggle Dark Mode" button.

## Features

- Create a custom chatbot by specifying its characteristics.
- Send and receive messages between the user and the chatbot.
- A simple GUI for a smooth user experience.
- Toggle between dark mode and light mode.

## Code Components

- `send_message()`: Collects the user's message, and generates assistant's response using OpenAI GPT-4.
- `create_chatbot()`: Initializes the chatbot with the specified characteristics provided by the user.
- `toggle_dark_mode()`: Toggles the dark mode theme for the chatbot interface.

Enjoy chatting with your AI-powered assistant!