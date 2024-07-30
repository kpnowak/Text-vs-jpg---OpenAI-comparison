from openai import AzureOpenAI
import base64
import os



client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version=os.getenv("OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

#-------------------------------------------------------------------------------------------------------------------------
#----------------------------------------- TEXT --------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------

with open('final_output_txt_10_non-prom\\merged_output11.txt', 'r', encoding='latin-1') as file:
    merged_output11_txt = file.read()

with open('final_output_txt_10_non-prom\\merged_output12.txt', 'r', encoding='latin-1') as file:
    merged_output12_txt = file.read()

with open('final_output_txt_10_non-prom\\merged_output13.txt', 'r', encoding='latin-1') as file:
    merged_output13_txt = file.read()

with open('final_output_txt_10_non-prom\\merged_output14.txt', 'r', encoding='latin-1') as file:
    merged_output14_txt = file.read()

with open('final_output_txt_10_non-prom\\merged_output15.txt', 'r', encoding='latin-1') as file:
    merged_output15_txt = file.read()

with open('final_output_txt_10_non-prom\\merged_output16.txt', 'r', encoding='latin-1') as file:
    merged_output16_txt = file.read()

with open('final_output_txt_10_non-prom\\merged_output17.txt', 'r', encoding='latin-1') as file:
    merged_output17_txt = file.read()

with open('final_output_txt_10_non-prom\\merged_output18.txt', 'r', encoding='latin-1') as file:
    merged_output18_txt = file.read()

with open('final_output_txt_10_non-prom\\merged_output19.txt', 'r', encoding='latin-1') as file:
    merged_output19_txt = file.read()

with open('final_output_txt_10_non-prom\\merged_output20.txt', 'r', encoding='latin-1') as file:
    merged_output20_txt = file.read()

#-------------------------------------------------------------------------------------------------------------------------
#----------------------------------------- IMAGE -------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------

with open('final_output_jpg_10_non-prom\\merged_output11.txt', 'r', encoding='latin-1') as file:
    merged_output11_jpg = file.read()

with open('final_output_jpg_10_non-prom\\merged_output12.txt', 'r', encoding='latin-1') as file:
    merged_output12_jpg = file.read()

with open('final_output_jpg_10_non-prom\\merged_output13.txt', 'r', encoding='latin-1') as file:
    merged_output13_jpg = file.read()

with open('final_output_jpg_10_non-prom\\merged_output14.txt', 'r', encoding='latin-1') as file:
    merged_output14_jpg = file.read()

with open('final_output_jpg_10_non-prom\\merged_output15.txt', 'r', encoding='latin-1') as file:
    merged_output15_jpg = file.read()

with open('final_output_jpg_10_non-prom\\merged_output16.txt', 'r', encoding='latin-1') as file:
    merged_output16_jpg = file.read()

with open('final_output_jpg_10_non-prom\\merged_output17.txt', 'r', encoding='latin-1') as file:
    merged_output17_jpg = file.read()

with open('final_output_jpg_10_non-prom\\merged_output18.txt', 'r', encoding='latin-1') as file:
    merged_output18_jpg = file.read()

with open('final_output_jpg_10_non-prom\\merged_output19.txt', 'r', encoding='latin-1') as file:
    merged_output19_jpg = file.read()

with open('final_output_jpg_10_non-prom\\merged_output20.txt', 'r', encoding='latin-1') as file:
    merged_output20_jpg = file.read()

#-------------------------------------------------------------------------------------------------------------------------
#----------------------------------------- INSTRUCTIONS ------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------

correct_example = """
2. you feel a change could be beneficial.
Please confirm this with medical - is it appropriate to say that it is for the patient alone to feel a need for change? It should be clear that this is an assessment made both by the HCP and patient which I do not think is the case here.
"""

all_correct = """
1. When you’re living with type 2 diabetes, it’s common to reevaluate and change your treatment to ad...
-> Buse2020_Article_2019UpdateToManagementOfHyperg (v1.0) - REWRITE Campaign DWN Article How to talk about treatment options: GLP-1 RA Patient Awareness Campaign (p.5)

2. you feel a change could be beneficial.
Please confirm this with medical - is it appropriate to say that it is for the patient alone to feel a need for change? It should be clear that this is an assessment made both by the HCP and patient which I do not think is the case here.

3. The patient would not know these would be his/her goals. As part of patient awareness material, it would better fit that we say these are your goals, may be discuss it with your doctor

4. Share your personal goals, whether it’s better blood sugar control, weight management, or reducing ...
Again, is it for the patient to set these goals alone? I do not think so, would a patient set a goal of reducing CV risk without that being pointed out by a HCP? Please discuss this with medical to ensure an appropriate picture

5. ask
recommend to include "if relevant" here

6. The patient would not know this. The language needs to be changed and the patient share his concerns look for suggestions from the doctor

7. how a new treatment might
Why this focus on a new treatment only - this is an article about treatment in general? Please be mindful that for many people a new treatment is not the answer better rather adherence to current treatment or lifestyle changes. Recommend to rephrase to clarify that a new treatment could be relevant in some situations

8. easy to take or maybe you don’t have time to exercise as much as you would like, and you would pre...
Please confirm with medical that this is appropriate - should we push the message that if you do not want to exercise you can take medication instead? Sounds wrong to me

9. have about trying a new medication
Again, the same focus on new medication. Please see my comment above - recommend to rephrase to ensure this is seen as one of several options and that side effects and concerns for current medical is also covered

10. switch to something else
if clinically relevant [LIAU (Line Dahlfelt Marcussen)]
Agree [URQP (Usha Rani Patted)]

11. new treatment
again, same comment - do not recommend this focus on new treatment as it implies that it is the only option

12. Discuss when you should follow-up on how your new treatment is working. Typically type 2 diabetes p...
-> Buse2020_Article_2019UpdateToManagementOfHyperg (v1.0) - REWRITE Campaign DWN Article How to talk about treatment options: GLP-1 RA Patient Awareness Campaign (p.5)

13. new treatment
same comment

14. their doctor every
see their doctor to do what? revaluate treatment?

15. plan that’ll empower you on
that could empover or similar - please be mindful not to overpromise here [LIAU (Line Dahlfelt Marcussen)]
Agree [URQP (Usha Rani Patted)]
"""

true_positive_example = """
### Section: Body Content (Empowerment)
**Original Sentence:**
"It�s important that you feel empowered and ready to talk to your doctor whenever you feel a change could be beneficial."

**Deviation:**
- Could unintentionally imply encouragement for a change in treatment which could be seen as indirect promotion.
- According to [Source - EFPIA Chapter 3: Article 20], content must focus on communication without suggesting treatment adjustments.

**Expert Reviewer's Original Suggested Change:**
"It�s important to feel confident and prepared to discuss your healthcare needs with your doctor."

**Explanation for New Change:**
The expert�s change is almost adequate but the phrase �discuss your healthcare needs� can still be more general. Emphasizing the aspect of communication without hinting at treatment changes is crucial.

**New Suggested Sentence:**
"It�s important to feel empowered and ready to discuss your health with your doctor."
"""

false_positive_example = """
**Original Sentence:**
`It's important that you feel empowered and ready to talk to your doctor whenever you feel a change could be beneficial. It can be difficult to start these conversations, but with your treatment goals in mind�and by educating yourself more about type 2 diabetes (like you're doing right now!)�you'll be able to communicate with your doctor more openly about treatment.`

**Guideline Source:**
[Source - Communicate With Care Pocket Guide]

**Deviations:**
- According to Article 2, Section i "Maintain Professional Tone," avoid using casual phrases like "like you're doing right now!" which might undermine the professional tone.

**Replacement Sentence:**
`It's important that you feel empowered and ready to talk to your doctor whenever you feel a change could be beneficial. Starting these conversations can be challenging, but by keeping your treatment goals in mind and educating yourself more about type 2 diabetes, you'll be able to communicate with your doctor more openly about treatment.`

**Reason for Replacement:**
Ensures the text maintains a professional tone and avoids casual or colloquial language, adhering to proper communication standards.
"""

#-------------------------------------------------------------------------------------------------------------------------
#----------------------------------------- TEXT --------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------

grammar_instruction_txt = f"""

You as an expert analys of the quality of the reviews, your role is to assign a point if the review is done correctly or not. You won't give any additional explanation, because you are an analysis that cares only about the numbers.
You will keep the count by naming the mistake and then writing an appropiate count.
Here is an example of how the output of your analysis should look like:
"Mistake 'It's important that you feel empowered and ready to talk to your doctor whenever you feel a change could be beneficial.': 
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
Here you can see couple of examples of perfect and correct review that you will use for comparison and points assignment purposes. It is delimited by XXX: 
XXX
{all_correct}
XXX

If part of the review that I will give you for the analysis will have similar content to this one:
XXX
{true_positive_example}
XXX
then you will assigne one point to the True Positive confusion matrix which will look like that:
"Mistake 'It's important that you feel empowered and ready to talk to your doctor whenever you feel a change could be beneficial.': 
- True Positive: 1
- False Negative: 0
- False Positive: 0
- True Negative: 0"

If part of the review that I will give you for the analysis will have similar content to this one:
XXX
{false_positive_example}
XXX
then you will assigne one point to the False Positive confusion matrix which will look like that:
"Mistake 'It's important that you feel empowered and ready to talk to your doctor whenever you feel a change could be beneficial.': 
- True Positive: 0
- False Negative: 0
- False Positive: 1
- True Negative: 0"

If this mistake won't be mention in my review at all, then you will assign one point to the False Negative confusion matriv which will look like that:
"Mistake 'It's important that you feel empowered and ready to talk to your doctor whenever you feel a change could be beneficial.': 
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
"Mistake 'It's important that you feel empowered and ready to talk to your doctor whenever you feel a change could be beneficial.': 
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
"Mistake 'It's important that you feel empowered and ready to talk to your doctor whenever you feel a change could be beneficial.': 
- True Positive: 1
- False Negative: 0
- False Positive: 0
- True Negative: 0"

If part of the review that I will give you for the analysis will have similar content to this one:
XXX
{false_positive_example}
XXX
then you will assigne one point to the False Positive confusion matrix which will look like that:
"Mistake 'It's important that you feel empowered and ready to talk to your doctor whenever you feel a change could be beneficial.': 
- True Positive: 0
- False Negative: 0
- False Positive: 1
- True Negative: 0"

If this mistake won't be mention in my review at all, then you will assign one point to the False Negative confusion matriv which will look like that:
"Mistake 'It's important that you feel empowered and ready to talk to your doctor whenever you feel a change could be beneficial.': 
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
    with open("Non-prom\\analysis_txt.txt", "w") as f:
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
    with open("Non-prom\\analysis_jpg3.txt", "w") as f:
        f.write(response.choices[0].message.content)

analysis_txt()
#analysis_jpg()