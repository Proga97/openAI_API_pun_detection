import openai
from dotenv import load_dotenv
import os

load_dotenv('.env')

openai.api_key = os.getenv('OPENAI_API_KEY')

def detect_wordplay(text):
    # The prompt to detect wordplay and explain its meanings and age appropriateness
    prompt = f"""
    Analyze the following text and detect only one word which is the most probable word or phrase that have multiple meanings. For each word or phrase with multiple meanings, list the word, describe each meaning, and determine whether the meanings are age-appropriate. If there is no wordplay, respond with "No wordplay detected."

    Text: "{text}"

    Output format:
    Word: <word>
    Sense 1: <description of meaning 1>
    Sense 2: <description of meaning 2>
    Age Appropriateness: <give age of aquisition>

    If there is no wordplay, simply state: "No wordplay detected."

    like below:
    Example 1:
    From 3650 Jokes, Puns & Riddles, p.65, section on Bad Medicine:
    Danny: Why so glum?
    Gerry: I've got a bad case of shingles.
    Danny: Did you see a doctor?
    Gerry: Yeah, and he prescribed aluminum siding.
    Explanation: The word with multiple meanings: shingles.
    Sense 1: Viral infection that causes a painful rash.
    Sense 2: Building material, used here in plural.
    According to X source, the word "shingles" is (not) acquired around Y years of age, and thus this text will not be understood by a Z-year-old.

    Example 2:
    Autobiography: when your car starts telling you about its life.
    Explanation: Word/phrase: autobiography.
    Sense 1: An account of a person's life written by that person.
    Sense 2: Auto (car) biography.
    According to X source, age of acquisition for "auto" is Y, age of acquisition of "autobiography" is Z.

    Example 3:
    Why do elephants have a trunk? Because they don’t have pockets to put stuff in.
    Explanation: The word "trunk" has several meanings, including a body part of an elephant and a container.
    According to X source, age of acquisition for the term "trunk" is Y years of age.
    """

    # API call to OpenAI GPT-4 to detect wordplay
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # Ensure you're using the GPT-4 model
        messages=[
            {"role": "system", "content": "You are a wordplay detector and age appropriateness evaluator."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.5
    )

    # Extract and return the response from the assistant
    return response['choices'][0]['message']['content']

# Test the function with an example joke
examples = [
    "Why so glum? I've got a bad case of shingles. Did you see a doctor? Yeah, and he prescribed aluminum siding.",
    "Autobiography: When your car starts telling you about its life.",
    "Why do elephants have a trunk? Because they don’t have pockets to put stuff in.",
    "The teddy bear was stuffed and he said no the desert",
    "why did the imagination go to school? To become little more thoughful"
]
# Call the function and display the result
for joke in examples:
    wordplay_result = detect_wordplay(joke)
    print(wordplay_result)

