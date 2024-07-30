from openai import AzureOpenAI
import base64
import os

os.environ['AZURE_OPENAI_API_KEY'] = ''
os.environ['AZURE_OPENAI_ENDPOINT'] = ''
os.environ['OPENAI_API_VERSION'] = ""

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version=os.getenv("OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

#-------------------------------------------------------------------------------------------------------------------------
#----------------------------------------- TEXT --------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------

with open('final_output_txt_10_gram\\merged_output11.txt', 'r', encoding='latin-1') as file:
    merged_output11_txt = file.read()

with open('final_output_txt_10_gram\\merged_output12.txt', 'r', encoding='latin-1') as file:
    merged_output12_txt = file.read()

with open('final_output_txt_10_gram\\merged_output13.txt', 'r', encoding='latin-1') as file:
    merged_output13_txt = file.read()

with open('final_output_txt_10_gram\\merged_output14.txt', 'r', encoding='latin-1') as file:
    merged_output14_txt = file.read()

with open('final_output_txt_10_gram\\merged_output15.txt', 'r', encoding='latin-1') as file:
    merged_output15_txt = file.read()

with open('final_output_txt_10_gram\\merged_output16.txt', 'r', encoding='latin-1') as file:
    merged_output16_txt = file.read()

with open('final_output_txt_10_gram\\merged_output17.txt', 'r', encoding='latin-1') as file:
    merged_output17_txt = file.read()

with open('final_output_txt_10_gram\\merged_output18.txt', 'r', encoding='latin-1') as file:
    merged_output18_txt = file.read()

with open('final_output_txt_10_gram\\merged_output19.txt', 'r', encoding='latin-1') as file:
    merged_output19_txt = file.read()

with open('final_output_txt_10_gram\\merged_output20.txt', 'r', encoding='latin-1') as file:
    merged_output20_txt = file.read()

#-------------------------------------------------------------------------------------------------------------------------
#----------------------------------------- IMAGE -------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------

with open('final_output_jpg_10_gram\\merged_output11.txt', 'r', encoding='latin-1') as file:
    merged_output11_jpg = file.read()

with open('final_output_jpg_10_gram\\merged_output12.txt', 'r', encoding='latin-1') as file:
    merged_output12_jpg = file.read()

with open('final_output_jpg_10_gram\\merged_output13.txt', 'r', encoding='latin-1') as file:
    merged_output13_jpg = file.read()

with open('final_output_jpg_10_gram\\merged_output14.txt', 'r', encoding='latin-1') as file:
    merged_output14_jpg = file.read()

with open('final_output_jpg_10_gram\\merged_output15.txt', 'r', encoding='latin-1') as file:
    merged_output15_jpg = file.read()

with open('final_output_jpg_10_gram\\merged_output16.txt', 'r', encoding='latin-1') as file:
    merged_output16_jpg = file.read()

with open('final_output_jpg_10_gram\\merged_output17.txt', 'r', encoding='latin-1') as file:
    merged_output17_jpg = file.read()

with open('final_output_jpg_10_gram\\merged_output18.txt', 'r', encoding='latin-1') as file:
    merged_output18_jpg = file.read()

with open('final_output_jpg_10_gram\\merged_output19.txt', 'r', encoding='latin-1') as file:
    merged_output19_jpg = file.read()

with open('final_output_jpg_10_gram\\merged_output20.txt', 'r', encoding='latin-1') as file:
    merged_output20_jpg = file.read()

#-------------------------------------------------------------------------------------------------------------------------
#----------------------------------------- INSTRUCTIONS ------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------

correct_example = """
Sentence: He wanted to be introduced to Lucy wo he fancied. 

Reason: Misspelling of 'who' as 'wo' and lack of punctuation. 

Suggested change: He wanted to be introduced to Lucy, whom he fancied.
"""

true_positive_example = """
### Sentence 3:
- **Source Sentence**: He wanted to be introduced to Lucy wo he fancied.
- **Deviations Corrected**: "wo" should be "who".
- **Reason**: The correct relative pronoun in this context is "who".
- **New Sentence**: He wanted to be introduced to Lucy who he fancied.
"""

false_positive_example = """
**3. Original:**
"He wanted to be introduced to Lucy wo he fancied."

**Correction:**
"He wanted to be introduced to Lucy, whom he fancied."

**Deviations Corrected:**
- Spelling error "wo" corrected to "whom."
- Added comma for clarity.

**Reason:**
Correct spelling and punctuation enhance readability and grammatical accuracy.

**New Sentence:**
"He wanted to be introduced to Lucy, whom he fancied."
"""

#-------------------------------------------------------------------------------------------------------------------------
#----------------------------------------- TEXT --------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------

grammar_instruction_txt = f"""

You as an expert analys of the quality of the reviews, your role is to assign a point if the review is done correctly or not. You won't give any additional explanation, because you are an analysis that cares only about the numbers.
You will keep the count by naming the mistake and then writing an appropiate count.
Here is an example of how the output of your analysis should look like:
"Mistake "gone" -> "went": 
- True Positive: 1
- False Negative: 2
- False Positive: 0
- True Negative: 0"

As you can see, as an analysis, you will create a confusion matrix to every separate mistake that could be done in each review.
At the end of every analysis you will create a confusion matrix that will sum up all od the matrixes to one and it will look like that:
"- True Positive: 32
- False Negative: 46
- False Positive: 8
- True Negative: 0"

Now I will show you when to count a mistake as each of the points that appeared above.
Here you can see the example of perfect and correct review that you will use for comparison and points assignment purposes. It is delimited by XXX: 
XXX
{correct_example}
XXX

If part of the review that I will give you for the analysis will have similar content to this one:
XXX
{true_positive_example}
XXX
then you will assigne one point to the True Positive confusion matrix which will look like that:
"Mistake "wo" -> "who": 
- True Positive: 1
- False Negative: 0
- False Positive: 0
- True Negative: 0"

If part of the review that I will give you for the analysis will have similar content to this one:
XXX
{false_positive_example}
XXX
then you will assigne one point to the False Positive confusion matrix which will look like that:
"Mistake "wo" -> "who": 
- True Positive: 0
- False Negative: 0
- False Positive: 1
- True Negative: 0"

If this mistake won't be mention in my review at all, then you will assign one point to the False Negative confusion matriv which will look like that:
"Mistake "wo" -> "who": 
- True Positive: 0
- False Negative: 1
- False Positive: 0
- True Negative: 0"

You have seen all of the rules of the points assigning. You need to remember to keep track of the numbers in the confusion matrix, because you will get many files at once for the analysis, so there will be a lot of things to count.

You will do the analysis in accordance with "Correct review rules" that contain the proper review without any mistakes or errors.
You won't add anything to it, but just keep it as a perfect example used for the comparison with other reviews. Because of the comparison with "Correct review rules" you will know which type of point should be assigned.

Now, as you know everything, I can give you all of the texts for the analysis. Analyse the texts very cerfully to not make any mistakes. It is an important analysis!!!
You will get 10 reviews of the same text. I want you to create an confusion matrix for every mistake of the text (remember to add the same mistakes to one condusion matrix) and at the end create a summary confusion matrix, which will contain all of the analysis results at once.
Please analyse the following documents using the "Correct review rules" provided above. The documents to review are delimited by XXX below: 
XXX 
{merged_output11_txt}
XXX

XXX 
{merged_output12_txt}
XXX

XXX 
{merged_output13_txt}
XXX

XXX 
{merged_output14_txt}
XXX

XXX 
{merged_output15_txt}
XXX

XXX 
{merged_output16_txt}
XXX

XXX 
{merged_output17_txt}
XXX

XXX 
{merged_output18_txt}
XXX

XXX 
{merged_output19_txt}
XXX

XXX 
{merged_output20_txt}
XXX
"""

#-------------------------------------------------------------------------------------------------------------------------
#----------------------------------------- IMAGE -------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------

grammar_instruction_jpg = f"""

You as an expert analys of the quality of the reviews, your role is to assign a point if the review is done correctly or not. You won't give any additional explanation, because you are an analysis that cares only about the numbers.
You will keep the count by naming the mistake and then writing an appropiate count.
Here is an example of how the output of your analysis should look like:
"Mistake "gone" -> "went": 
- True Positive: 1
- False Negative: 2
- False Positive: 0
- True Negative: 0"

As you can see, as an analysis, you will create a confusion matrix to every separate mistake that could be done in each review.
At the end of every analysis you will create a confusion matrix that will sum up all od the matrixes to one and it will look like that:
"- True Positive: 32
- False Negative: 46
- False Positive: 8
- True Negative: 0"

Now I will show you when to count a mistake as each of the points that appeared above.
Here you can see the example of perfect and correct review that you will use for comparison and points assignment purposes. It is delimited by XXX: 
XXX
{correct_example}
XXX

If part of the review that I will give you for the analysis will have similar content to this one:
XXX
{true_positive_example}
XXX
then you will assigne one point to the True Positive confusion matrix which will look like that:
"Mistake "wo" -> "who": 
- True Positive: 1
- False Negative: 0
- False Positive: 0
- True Negative: 0"

If part of the review that I will give you for the analysis will have similar content to this one:
XXX
{false_positive_example}
XXX
then you will assigne one point to the False Positive confusion matrix which will look like that:
"Mistake "wo" -> "who": 
- True Positive: 0
- False Negative: 0
- False Positive: 1
- True Negative: 0"

If this mistake won't be mention in my review at all, then you will assign one point to the False Negative confusion matriv which will look like that:
"Mistake "wo" -> "who": 
- True Positive: 0
- False Negative: 1
- False Positive: 0
- True Negative: 0"

You have seen all of the rules of the points assigning. You need to remember to keep track of the numbers in the confusion matrix, because you will get many files at once for the analysis, so there will be a lot of things to count.

You will do the analysis in accordance with "Correct review rules" that contain the proper review without any mistakes or errors.
You won't add anything to it, but just keep it as a perfect example used for the comparison with other reviews. Because of the comparison with "Correct review rules" you will know which type of point should be assigned.

Now, as you know everything, I can give you all of the texts for the analysis. Analyse the texts very cerfully to not make any mistakes. It is an important analysis!!!
You will get 10 reviews of the same text. I want you to create an confusion matrix for every mistake of the text (remember to add the same mistakes to one condusion matrix) and at the end create a summary confusion matrix, which will contain all of the analysis results at once.
Please analyse the following documents using the "Correct review rules" provided above. The documents to review are delimited by XXX below: 
XXX 
{merged_output11_jpg}
XXX

XXX 
{merged_output12_jpg}
XXX

XXX 
{merged_output13_jpg}
XXX

XXX 
{merged_output14_jpg}
XXX

XXX 
{merged_output15_jpg}
XXX

XXX 
{merged_output16_jpg}
XXX

XXX 
{merged_output17_jpg}
XXX

XXX 
{merged_output18_jpg}
XXX

XXX 
{merged_output19_jpg}
XXX

XXX 
{merged_output20_jpg}
XXX
"""

def analysis_txt():
    # first review code
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that reviews the documents."},
            {"role": "user", "content": f"{grammar_instruction_txt}"},
        ]
    )
    with open("Gram\\analysis_txt.txt", "w") as f:
        f.write(response.choices[0].message.content)

def analysis_jpg():
    # first review code
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that reviews the documents."},
            {"role": "user", "content": f"{grammar_instruction_jpg}"},
        ]
    )
    with open("Gram\\analysis_jpg.txt", "w") as f:
        f.write(response.choices[0].message.content)

analysis_txt()
analysis_jpg()