import tkinter as tk
import openai

# Initialize the OpenAI API key
openai.api_key = ""  # Replace with your actual OpenAI API key

def generate_text_button_click(result_text):
    try:
        prompt = prompt_entry.get()
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Replace with the desired model
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        generated_text = response.choices[0].message.content
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, generated_text)
    except Exception as e:  # Capture the exception object
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"An error occurred: {e}")

# Create the main application window
root = tk.Tk()
root.title("Text Generator")

# Create the prompt entry widget
prompt_entry = tk.Entry(root, width=50)
prompt_entry.pack()

# Create the result text widget
result_text = tk.Text(root, width=50, height=10)
result_text.pack()

# Create the generate button
generate_button = tk.Button(root, text="Generate Text", command=lambda: generate_text_button_click(result_text))
generate_button.pack()

# Start the Tkinter main loop
root.mainloop()