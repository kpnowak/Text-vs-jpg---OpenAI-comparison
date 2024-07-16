from openai import OpenAI
import base64

client = OpenAI(api_key = 'sk-proj-hjIsgHjRy9fKmrGuNkkOT3BlbkFJ3XHrmXXHhsrgrobZ53Wt')

MULTILANGUAGE_GUIDELINES = """
1. Grammar and Punctuation: 
    i. Correct any grammatical errors, taking into account the specific rules of the language. 
    ii. Fix punctuation mistakes, including commas, periods, semicolons, colons, and quotation marks, according to the standards of the language. Ignore the lack of period at the end of the sentence.
    ii. Ensure correct use of capitalization, especially for proper nouns and at the beginning of sentences.
    iii. Avoid hyphen usage corrections.
2. Sentence Structure: 
    i. Ensure all sentences are complete and properly structured as per the syntax and grammar rules of the language. 
    ii. Reorganize sentences if necessary to improve clarity and readability while preserving the original meaning.
3. Consistency: 
    i. Maintain consistent verb tenses throughout the document, as per the conventions of the language. 
    ii. Ensure consistent use of pronouns, articles, and other language-specific constructs.
    ii. Standardize terminology and style across the document.
4. Spelling: 
    i. Correct any spelling mistakes, considering the spelling rules of the language.
    ii. Do not correct medical terminology. Some components of the text may contain typical medical jargon (such as sentence fragments related to dosage and use). These are not grammatical errors but rather standard formulations in the medical industry.
5. Clarity and Readability: 
    i. Improve the clarity of sentences where needed, considering the nuances and complexities of the language. 
    ii. Simplify complex sentences if they hinder understanding, while respecting the language’s structure and style. 
    iii. Ensure the overall readability of the document, taking into account the reading habits and preferences of speakers of the language.
6. Language-Specific Rules: 
    i. Apply language-specific rules and conventions for Mandarin, French, Dutch, Slovak, etc., as each language has unique characteristics and rules.
    ii. For German, replace "Wenn" with "Als" to indicate a specific event that happened in the past.
    iii. Apply language-specific correct relative pronoun replace the relative pronoun with the one that accurately conveys the relationship based on the verb and preposition used.
    iv. Apply language-specific Correct the Idiomatic Expression ensure the idiomatic expression is used correctly according to standard usage
    v. Ensure reflexive pronouns agree with the verb and are in the correct case (e.g., in German, "mir" instead of "mich" when the verb requires the dative case).
    vi. Capitalize nouns, especially when they can be easily confused with other parts of speech (e.g., "Paar" instead of "paar" when referring to a specific number of items).
7. Formality and Tone:
    i. Assess the overall formality of the document, considering the intended audience and purpose.
    ii. Adapt the language, style, and tone to match the required level of formality. Use formal or informal expressions, vocabulary, and structures as appropriate.
    iii. Numbers can be written numerically or with words. Do not correct.
"""

with open('jpg_to_txt.txt', 'r', encoding='latin-1') as file:
    jpg_to_txt_content = file.read()

multi_lang_grammar_review_prompt_template_txt = f"""

You are the expert writing reviewer that specifies in correcting spelling and grammar in [document_language] language.
Your role is to meticulously review a document for grammatical accuracy.
It is imperative to follow the steps and instructions provided and ensure your response meets the required standards.

The extracted text below is a very long string and is the result of an actual medical document that was run through a text extractor. Some of the structure may be missing or hard to identify due to the extraction process. When reviewing, please focus on correcting grammatical issues and avoid making changes related to potential structural problems caused by the extraction process.
The document to review is delimited by XXX below: 
XXX 
{jpg_to_txt_content} 
XXX

Step 1: Carefully identify the prominent language of the document. Pay special attention to local languages that may be similar to more widely spoken languages (for example, Catalan vs Spanish). Once identified, store the specific language of the document in [document_language].
Step 2: If [document_language] == French and English, then [document_language] == English. Skip reviewing any French content
Step 2: If [document_language] == zh, then [document_language] == zh_TW.
Step 3: If [document_language] != English then translate the prompt below in [document_language] language:
Step 4: Study the prompt and "Grammar & Spelling Guidelines", "IMPORTANT CONSIDERATIONS WHILE REVIEWING". 
Step 5: Work through each sentence, one at a time. Only review, strictly, sentences in [document_language] language. Never translate anything.
Step 6: Provide reviews and corrections for each sentence that meets the criteria. Only sentences in [document_language] language

"Grammar & Spelling Guidelines" delimited by XXX below: 
XXX 
{MULTILANGUAGE_GUIDELINES}
XXX

IMPORTANT CONSIDERATIONS WHILE REVIEWING:
1. THINGS YOU MUST FOLLOW:
    i. Some components of the text may contain typical medical jargon (such as sentence fragments related to dosage and use). These are not grammatical errors but rather standard formulations in the medical industry.
    ii. Double-check your working, ensuring that you have considered the entire document provided and your comments refer clearly to the "Grammar & Spelling Guidelines". 
    iii. Evaluate the difference between the source sentence and the suggested sentence. Make sure they are not the same. Remove the review if they are
    iv. When reviewing English sentences, please do so according to British English.
    v. Try to correct as many deviations as you can.
2. THINGS YOU MUST AVOID:
    i. AVOID providing a response or a review when skipping the review due to French content identified in English content
    ii. AVOID suggesting translating document sentences to maintain consistency. You are correcting grammar in [document_language] language not translating document content!
    iii. AVOID providing a response for URLs, file names, formulas, citations, slogans, logos, references, HTML format.
    iv. AVOID suggesting to add a period at the end of sentences.
    v. AVOID suggesting a review when there is no grammatical error or deviation noted.
    vi. AVOID suggesting reviewing hyphens/dashes formatting.
    vii. AVOID suggesting reviewing citation formatting.
    viii. AVOID reviewieving medical compounds.
    ix. AVOID providing duplicate comments. No two comments in your response should be the same. If there are any duplicate comments, remove them from your response, keeping the original.
    x. AVOID providing a review when there are no grammatical error or deviation noted in a sentence.
    xi. AVOID providing a response if you DO NOT find any relevant issue with the sentence being reviewed.

Please provide the following response for each of the comments you've improved upon: 
- The source sentence your new sentence replaces
- The deviations your new sentence corrects.
- The reason for replacing the source sentence with your new sentence and how it resolves the referenced deviations.
- Your new sentence
"""

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = r"C:\Users\krzys\OneDrive\Pulpit\Infosys\For Kris\For Kris\Find_mistakes_1.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)

# Transcription of the text from jpg file that was a pdf before
def jpg_to_text():
    url = f"data:image/jpeg;base64,{base64_image}"
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role":"assistant","content":"Your role is to create a transcription of the text that is on the image."},
        {
        
        "role": "user",
        "content": [
            {"type": "text", "text": "Transcribe the text that is on the image. Do it the best as you can."},
            {
            "type": "image_url",
            "image_url": {
                "url": url,
            },
            },
        ],
        }
        
    ],
    max_tokens=300,
    )
    
    with open("jpg_to_txt.txt", "w") as f:
        f.write(response.choices[0].message.content)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------- TEXT -------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

def text_review():

    # first review code
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that reviews the documents."},
        {"role": "user", "content": f"{multi_lang_grammar_review_prompt_template_txt}"},
    ]
    )
    with open("result_txt.txt", "w") as f:
        f.write(response.choices[0].message.content)

    # chef review instruction
    chief_multi_lang_grammar_review_prompt_template_txt = f"""
    You are the chief reviewer for reviews performed for "Grammar & Spelling Guidelines" in [document_language] language. 
    It is imperative to follow the steps and instructions provided and ensure your response meets the required standards.

    Below are the guidelines for the "Grammar & Spelling Guidelines" delimited by XXX: 
    XXX 
    {MULTILANGUAGE_GUIDELINES} 
    XXX
        
    Below are document reviews from your team of expert reviewers. You are responsible for checking over their reviews and providing feedback to the reviewers before publishing the reviews to the client.
    Please conduct a review upon the Expert's comments below delimited by XXX: 
    XXX 
    {response.choices[0].message.content}
    XXX

    Step 1: Carefully identify the prominent language of the document. Pay special attention to local languages that may be similar to more widely spoken languages (for example, Catalan vs Spanish). Once identified, store the specific language of the document in [document_language].
    Step 2: If [document_language] == French and English, then [document_language] == English. Skip reviewing any French content
    Step 3: If [document_language] != English then translate the prompt below in [document_language] language:
    Step 4: Study the prompt and "Grammar & Spelling Guidelines", "IMPORTANT CONSIDERATIONS WHILE REVIEWING".
    Step 6: Work through each of the comments provided by the expert reviewer.
    Step 7: Next you should verify that the expert's suggested change adheres to the guidelines. If there can be an improvement to the expert's suggested change or is inadequate with regards to the "Grammar & Spelling Guidelines" or [document_language] language specific rules, please create a new suggested change which better adhere's to all of the guidelines, this can be a completely new sentence if needed. 
            
    IMPORTANT CONSIDERATIONS WHILE REVIEWING:
    1. THINGS YOU MUST FOLLOW:
        i. In your review you should make sure that your suggested changes are not just copies of the source sentence nor a copy of the expert reviewer's sentence and they adhere to the guidelines.
        ii. Make sure there are no duplicated comments in Expert's comments. If there are any duplicate comments, remove them from your response, keeping the original. 
        iii. Take your time to work through the comments systematically in a step-by-step process.
        iv. Double check that you've examined every comment provided by the expert reviewer, if there are any you missed on your initial check, please go back and review them in the same manner as previously defined. If a suggestion by the expert reviewer is correct and adheres to the guidelines, you should skip it and do not mention it in your response.
        v. Comments which you have not improved upon can be left out of your response
    2. THINGS EXPERT REVIEWER COMMENTS MUST AVOID:
        i. AVOIDING providing a response or a review when skipping the review due to French content identified in English content
        ii. AVOIDING suggesting translating document sentences to maintain consistency. You are correcting grammar in [document_language] language not translating document content!
        iii. AVOIDING providing a response for URLs, file names, formulas, citations, slogans, logos, references, HTML format.
        iv. AVOIDING suggesting to add a period at the end of sentences.
        v. AVOIDING suggesting a review when there is no grammatical error or deviation noted.
        vi. AVOIDING suggesting reviewing hyphens/dashes formatting.
        vii. AVOIDING suggesting reviewing citation formatting.
        viii. AVOIDING reviewieving medical compounds.
        ix. AVOIDING providing duplicate comments. No two comments in your response should be the same. If there are any duplicate comments, remove them from your response, keeping the original.
        x. AVOIDING providing a review when there are no grammatical error or deviation noted in a sentence.
        xi. AVOIDING providing a response if you DO NOT find any relevant issue with the sentence being reviewed.

    Please provide the following response for each of the comments you've improved upon: 
        - The original sentence
        - The deviation from the guidelines originally provided by the expert reviewer.
        - The expert reviewer's original suggested change
        - An explanation for the reason behind your new suggested change in the same language as the issue.
        - Your new suggested sentence
    """

    # chef review code
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that reviews the documents."},
        {"role": "user", "content": f"{chief_multi_lang_grammar_review_prompt_template_txt}"},
    ]
    )
    with open("output_txt.txt", "w") as f:
        f.write(response.choices[0].message.content)


def text_review_10():
    for i in range(10):
        # first review code
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that reviews the documents."},
            {"role": "user", "content": f"{multi_lang_grammar_review_prompt_template_txt}"},
        ]
        )
        with open(f"review_txt_10/result{i + 1}_txt.txt", "w") as f:
            f.write(response.choices[0].message.content)

        # chef review instruction
        chief_multi_lang_grammar_review_prompt_template_txt = f"""
        You are the chief reviewer for reviews performed for "Grammar & Spelling Guidelines" in [document_language] language. 
        It is imperative to follow the steps and instructions provided and ensure your response meets the required standards.

        Below are the guidelines for the "Grammar & Spelling Guidelines" delimited by XXX: 
        XXX 
        {MULTILANGUAGE_GUIDELINES} 
        XXX
        
        Below are document reviews from your team of expert reviewers. You are responsible for checking over their reviews and providing feedback to the reviewers before publishing the reviews to the client.
        Please conduct a review upon the Expert's comments below delimited by XXX: 
        XXX 
        {response.choices[0].message.content}
        XXX

        Step 1: Carefully identify the prominent language of the document. Pay special attention to local languages that may be similar to more widely spoken languages (for example, Catalan vs Spanish). Once identified, store the specific language of the document in [document_language].
        Step 2: If [document_language] == French and English, then [document_language] == English. Skip reviewing any French content
        Step 3: If [document_language] != English then translate the prompt below in [document_language] language:
        Step 4: Study the prompt and "Grammar & Spelling Guidelines", "IMPORTANT CONSIDERATIONS WHILE REVIEWING".
        Step 6: Work through each of the comments provided by the expert reviewer.
        Step 7: Next you should verify that the expert's suggested change adheres to the guidelines. If there can be an improvement to the expert's suggested change or is inadequate with regards to the "Grammar & Spelling Guidelines" or [document_language] language specific rules, please create a new suggested change which better adhere's to all of the guidelines, this can be a completely new sentence if needed. 
            
        IMPORTANT CONSIDERATIONS WHILE REVIEWING:
        1. THINGS YOU MUST FOLLOW:
            i. In your review you should make sure that your suggested changes are not just copies of the source sentence nor a copy of the expert reviewer's sentence and they adhere to the guidelines.
            ii. Make sure there are no duplicated comments in Expert's comments. If there are any duplicate comments, remove them from your response, keeping the original. 
            iii. Take your time to work through the comments systematically in a step-by-step process.
            iv. Double check that you've examined every comment provided by the expert reviewer, if there are any you missed on your initial check, please go back and review them in the same manner as previously defined. If a suggestion by the expert reviewer is correct and adheres to the guidelines, you should skip it and do not mention it in your response.
            v. Comments which you have not improved upon can be left out of your response
        2. THINGS EXPERT REVIEWER COMMENTS MUST AVOID:
            i. AVOIDING providing a response or a review when skipping the review due to French content identified in English content
            ii. AVOIDING suggesting translating document sentences to maintain consistency. You are correcting grammar in [document_language] language not translating document content!
            iii. AVOIDING providing a response for URLs, file names, formulas, citations, slogans, logos, references, HTML format.
            iv. AVOIDING suggesting to add a period at the end of sentences.
            v. AVOIDING suggesting a review when there is no grammatical error or deviation noted.
            vi. AVOIDING suggesting reviewing hyphens/dashes formatting.
            vii. AVOIDING suggesting reviewing citation formatting.
            viii. AVOIDING reviewieving medical compounds.
            ix. AVOIDING providing duplicate comments. No two comments in your response should be the same. If there are any duplicate comments, remove them from your response, keeping the original.
            x. AVOIDING providing a review when there are no grammatical error or deviation noted in a sentence.
            xi. AVOIDING providing a response if you DO NOT find any relevant issue with the sentence being reviewed.

        Please provide the following response for each of the comments you've improved upon: 
            - The original sentence
            - The deviation from the guidelines originally provided by the expert reviewer.
            - The expert reviewer's original suggested change
            - An explanation for the reason behind your new suggested change in the same language as the issue.
            - Your new suggested sentence
        """

        # chef review code
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"{chief_multi_lang_grammar_review_prompt_template_txt}"},
        ]
        )
        with open(f"review_txt_10/output{i + 1}_txt.txt", "w") as f:
            f.write(response.choices[0].message.content)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------- PHOTO ---------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

multi_lang_grammar_review_prompt_template_jpg = f"""

You are the expert writing reviewer that specifies in correcting spelling and grammar in [document_language] language.
Your role is to meticulously review a document for grammatical accuracy.
It is imperative to follow the steps and instructions provided and ensure your response meets the required standards.

The image that you are provided with is the document that is the result of an actual medical document that was run through a text extractor. Some of the structure may be missing or hard to identify due to the extraction process. When reviewing, please focus on correcting grammatical issues and avoid making changes related to potential structural problems caused by the extraction process.
You are provided with an image that consist a document for the review.

Step 1: Carefully identify the prominent language of the document. Pay special attention to local languages that may be similar to more widely spoken languages (for example, Catalan vs Spanish). Once identified, store the specific language of the document in [document_language].
Step 2: If [document_language] == French and English, then [document_language] == English. Skip reviewing any French content
Step 2: If [document_language] == zh, then [document_language] == zh_TW.
Step 3: If [document_language] != English then translate the prompt below in [document_language] language:
Step 4: Study the prompt and "Grammar & Spelling Guidelines", "IMPORTANT CONSIDERATIONS WHILE REVIEWING". 
Step 5: Work through each sentence, one at a time. Only review, strictly, sentences in [document_language] language. Never translate anything.
Step 6: Provide reviews and corrections for each sentence that meets the criteria. Only sentences in [document_language] language

"Grammar & Spelling Guidelines" delimited by XXX below: 
XXX 
{MULTILANGUAGE_GUIDELINES}
XXX

IMPORTANT CONSIDERATIONS WHILE REVIEWING:
1. THINGS YOU MUST FOLLOW:
    i. Some components of the text may contain typical medical jargon (such as sentence fragments related to dosage and use). These are not grammatical errors but rather standard formulations in the medical industry.
    ii. Double-check your working, ensuring that you have considered the entire document provided and your comments refer clearly to the "Grammar & Spelling Guidelines". 
    iii. Evaluate the difference between the source sentence and the suggested sentence. Make sure they are not the same. Remove the review if they are
    iv. When reviewing English sentences, please do so according to British English.
    v. Try to correct as many deviations as you can.
2. THINGS YOU MUST AVOID:
    i. AVOID providing a response or a review when skipping the review due to French content identified in English content
    ii. AVOID suggesting translating document sentences to maintain consistency. You are correcting grammar in [document_language] language not translating document content!
    iii. AVOID providing a response for URLs, file names, formulas, citations, slogans, logos, references, HTML format.
    iv. AVOID suggesting to add a period at the end of sentences.
    v. AVOID suggesting a review when there is no grammatical error or deviation noted.
    vi. AVOID suggesting reviewing hyphens/dashes formatting.
    vii. AVOID suggesting reviewing citation formatting.
    viii. AVOID reviewieving medical compounds.
    ix. AVOID providing duplicate comments. No two comments in your response should be the same. If there are any duplicate comments, remove them from your response, keeping the original.
    x. AVOID providing a review when there are no grammatical error or deviation noted in a sentence.
    xi. AVOID providing a response if you DO NOT find any relevant issue with the sentence being reviewed.

Please provide the following response for each of the comments you've improved upon: 
- The source sentence your new sentence replaces
- The deviations your new sentence corrects.
- The reason for replacing the source sentence with your new sentence and how it resolves the referenced deviations.
- Your new sentence
"""

def jpg_review():
    url = f"data:image/jpeg;base64,{base64_image}"
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role":"assistant","content":"Your role is to review an image."},
        {
        
        "role": "user",
        "content": [
            {"type": "text", "text": f"{multi_lang_grammar_review_prompt_template_jpg}"},
            {
            "type": "image_url",
            "image_url": {
                "url": url,
            },
            },
        ],
        }
        
    ],
    max_tokens=300,
    )
    
    with open("result_jpg.txt", "w") as f:
        f.write(response.choices[0].message.content)

    # chef review instruction
    chief_multi_lang_grammar_review_prompt_template_jpg = f"""
    You are the chief reviewer for reviews performed for "Grammar & Spelling Guidelines" in [document_language] language. 
    It is imperative to follow the steps and instructions provided and ensure your response meets the required standards.

    Below are the guidelines for the "Grammar & Spelling Guidelines" delimited by XXX: 
    XXX 
    {MULTILANGUAGE_GUIDELINES} 
    XXX
        
    You are provided with an image of the document that your team of experts already reviewed.
    Below are document reviews from your team of expert reviewers. You are responsible for checking over their reviews and providing feedback to the reviewers before publishing the reviews to the client.
    Please conduct a review upon the image of the document that you are provided with and the Expert's comments below delimited by XXX: 
    XXX 
    {response.choices[0].message.content}
    XXX

    Step 1: Carefully identify the prominent language of the document. Pay special attention to local languages that may be similar to more widely spoken languages (for example, Catalan vs Spanish). Once identified, store the specific language of the document in [document_language].
    Step 2: If [document_language] == French and English, then [document_language] == English. Skip reviewing any French content
    Step 3: If [document_language] != English then translate the prompt below in [document_language] language:
    Step 4: Study the prompt and "Grammar & Spelling Guidelines", "IMPORTANT CONSIDERATIONS WHILE REVIEWING".
    Step 6: Work through each of the comments provided by the expert reviewer.
    Step 7: Next you should verify that the expert's suggested change adheres to the guidelines. If there can be an improvement to the expert's suggested change or is inadequate with regards to the "Grammar & Spelling Guidelines" or [document_language] language specific rules, please create a new suggested change which better adhere's to all of the guidelines, this can be a completely new sentence if needed. 
            
    IMPORTANT CONSIDERATIONS WHILE REVIEWING:
    1. THINGS YOU MUST FOLLOW:
        i. In your review you should make sure that your suggested changes are not just copies of the source sentence nor a copy of the expert reviewer's sentence and they adhere to the guidelines.
        ii. Make sure there are no duplicated comments in Expert's comments. If there are any duplicate comments, remove them from your response, keeping the original. 
        iii. Take your time to work through the comments systematically in a step-by-step process.
        iv. Double check that you've examined every comment provided by the expert reviewer, if there are any you missed on your initial check, please go back and review them in the same manner as previously defined. If a suggestion by the expert reviewer is correct and adheres to the guidelines, you should skip it and do not mention it in your response.
        v. Comments which you have not improved upon can be left out of your response
    2. THINGS EXPERT REVIEWER COMMENTS MUST AVOID:
        i. AVOIDING providing a response or a review when skipping the review due to French content identified in English content
        ii. AVOIDING suggesting translating document sentences to maintain consistency. You are correcting grammar in [document_language] language not translating document content!
        iii. AVOIDING providing a response for URLs, file names, formulas, citations, slogans, logos, references, HTML format.
        iv. AVOIDING suggesting to add a period at the end of sentences.
        v. AVOIDING suggesting a review when there is no grammatical error or deviation noted.
        vi. AVOIDING suggesting reviewing hyphens/dashes formatting.
        vii. AVOIDING suggesting reviewing citation formatting.
        viii. AVOIDING reviewieving medical compounds.
        ix. AVOIDING providing duplicate comments. No two comments in your response should be the same. If there are any duplicate comments, remove them from your response, keeping the original.
        x. AVOIDING providing a review when there are no grammatical error or deviation noted in a sentence.
        xi. AVOIDING providing a response if you DO NOT find any relevant issue with the sentence being reviewed.

    Please provide the following response for each of the comments you've improved upon: 
        - The original sentence
        - The deviation from the guidelines originally provided by the expert reviewer.
        - The expert reviewer's original suggested change
        - An explanation for the reason behind your new suggested change in the same language as the issue.
        - Your new suggested sentence
    """


    url = f"data:image/jpeg;base64,{base64_image}"
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role":"assistant","content":"Your role is to review an image."},
        {
        
        "role": "user",
        "content": [
            {"type": "text", "text": f"{chief_multi_lang_grammar_review_prompt_template_jpg}"},
            {
            "type": "image_url",
            "image_url": {
                "url": url,
            },
            },
        ],
        }
        
    ],
    max_tokens=300,
    )
    
    with open("output_jpg.txt", "w") as f:
        f.write(response.choices[0].message.content)


def jpg_review_10():
    for i in range(10):
        url = f"data:image/jpeg;base64,{base64_image}"
        response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role":"assistant","content":"Your role is to review an image."},
            {
            
            "role": "user",
            "content": [
                {"type": "text", "text": f"{multi_lang_grammar_review_prompt_template_jpg}"},
                {
                "type": "image_url",
                "image_url": {
                    "url": url,
                },
                },
            ],
            }
            
        ],
        max_tokens=300,
        )
        
        with open(f"review_jpg_10/result{i + 1}_jpg.txt", "w") as f:
            f.write(response.choices[0].message.content)

        # chef review instruction
        chief_multi_lang_grammar_review_prompt_template_jpg = f"""
        You are the chief reviewer for reviews performed for "Grammar & Spelling Guidelines" in [document_language] language. 
        It is imperative to follow the steps and instructions provided and ensure your response meets the required standards.

        Below are the guidelines for the "Grammar & Spelling Guidelines" delimited by XXX: 
        XXX 
        {MULTILANGUAGE_GUIDELINES} 
        XXX
            
        You are provided with an image of the document that your team of experts already reviewed.
        Below are document reviews from your team of expert reviewers. You are responsible for checking over their reviews and providing feedback to the reviewers before publishing the reviews to the client.
        Please conduct a review upon the image of the document that you are provided with and the Expert's comments below delimited by XXX: 
        XXX 
        {response.choices[0].message.content}
        XXX

        Step 1: Carefully identify the prominent language of the document. Pay special attention to local languages that may be similar to more widely spoken languages (for example, Catalan vs Spanish). Once identified, store the specific language of the document in [document_language].
        Step 2: If [document_language] == French and English, then [document_language] == English. Skip reviewing any French content
        Step 3: If [document_language] != English then translate the prompt below in [document_language] language:
        Step 4: Study the prompt and "Grammar & Spelling Guidelines", "IMPORTANT CONSIDERATIONS WHILE REVIEWING".
        Step 6: Work through each of the comments provided by the expert reviewer.
        Step 7: Next you should verify that the expert's suggested change adheres to the guidelines. If there can be an improvement to the expert's suggested change or is inadequate with regards to the "Grammar & Spelling Guidelines" or [document_language] language specific rules, please create a new suggested change which better adhere's to all of the guidelines, this can be a completely new sentence if needed. 
                
        IMPORTANT CONSIDERATIONS WHILE REVIEWING:
        1. THINGS YOU MUST FOLLOW:
            i. In your review you should make sure that your suggested changes are not just copies of the source sentence nor a copy of the expert reviewer's sentence and they adhere to the guidelines.
            ii. Make sure there are no duplicated comments in Expert's comments. If there are any duplicate comments, remove them from your response, keeping the original. 
            iii. Take your time to work through the comments systematically in a step-by-step process.
            iv. Double check that you've examined every comment provided by the expert reviewer, if there are any you missed on your initial check, please go back and review them in the same manner as previously defined. If a suggestion by the expert reviewer is correct and adheres to the guidelines, you should skip it and do not mention it in your response.
            v. Comments which you have not improved upon can be left out of your response
        2. THINGS EXPERT REVIEWER COMMENTS MUST AVOID:
            i. AVOIDING providing a response or a review when skipping the review due to French content identified in English content
            ii. AVOIDING suggesting translating document sentences to maintain consistency. You are correcting grammar in [document_language] language not translating document content!
            iii. AVOIDING providing a response for URLs, file names, formulas, citations, slogans, logos, references, HTML format.
            iv. AVOIDING suggesting to add a period at the end of sentences.
            v. AVOIDING suggesting a review when there is no grammatical error or deviation noted.
            vi. AVOIDING suggesting reviewing hyphens/dashes formatting.
            vii. AVOIDING suggesting reviewing citation formatting.
            viii. AVOIDING reviewieving medical compounds.
            ix. AVOIDING providing duplicate comments. No two comments in your response should be the same. If there are any duplicate comments, remove them from your response, keeping the original.
            x. AVOIDING providing a review when there are no grammatical error or deviation noted in a sentence.
            xi. AVOIDING providing a response if you DO NOT find any relevant issue with the sentence being reviewed.

        Please provide the following response for each of the comments you've improved upon: 
            - The original sentence
            - The deviation from the guidelines originally provided by the expert reviewer.
            - The expert reviewer's original suggested change
            - An explanation for the reason behind your new suggested change in the same language as the issue.
            - Your new suggested sentence
        """


        url = f"data:image/jpeg;base64,{base64_image}"
        response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role":"assistant","content":"Your role is to review an image."},
            {
            
            "role": "user",
            "content": [
                {"type": "text", "text": f"{chief_multi_lang_grammar_review_prompt_template_jpg}"},
                {
                "type": "image_url",
                "image_url": {
                    "url": url,
                },
                },
            ],
            }
            
        ],
        max_tokens=300,
        )
        
        with open(f"review_jpg_10/output{i + 1}_jpg.txt", "w") as f:
            f.write(response.choices[0].message.content)


#jpg_to_text()
#text_review()
#text_review_10()
#jpg_review()
jpg_review_10()