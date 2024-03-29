import csv
import openai
import os
import sys

# Safe way to set up OpenAI API key
openai.api_key = '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'
if not openai.api_key:
    print("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    sys.exit(1)

# Function to generate response using ChatGPT
def generate_response(prompt, model="gpt-3.5-turbo-1106"):
    try:
        response = openai.Completion.create(
            engine=model,  # Dynamically set the model
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"An error occurred while generating a response with {model}: {e}")
        return ""


# Function to fill CSV with responses
def fill_csv(input_file, output_file):
    # Open the CSV file
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

    # Iterate over rows and generate responses
    for row_index, row in enumerate(rows):
        token = row[0]  # Assuming token is in the first column
        # Iterate over labels (remaining columns)
        for col_index, label in enumerate(row[1:]):
            # Construct prompt
            prompt = f"What are the {token}'s {label}?"
            # Generate response
            response = generate_response(prompt)
            # Update the CSV rows with the generated response
            rows[row_index][col_index + 1] = response  # adding 1 because of skipping token column
    
    # Write the updated rows back to the CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(rows)

# Main function
def main():
    input_file = 'nyc-gpt - sheet1.csv'  # Make sure the filename matches exactly
    output_file = 'output.csv'  # Output filename
    fill_csv(input_file, output_file)

if __name__ == "__main__":
    main()
