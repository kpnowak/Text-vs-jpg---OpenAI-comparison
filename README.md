# Image vs Text Review Research - middle-way project

This repository is made to research the problem of using text and image inputs for GPT-4o. There are plenty of algorithms created to get the same input as a text and as an image. Then both outputs can be compared.

**Files explanation**

prompts.py - Initial file with all of the instructions later given to GPT-4o

**pdf_to_jpg.py** - Algorithm that changes pdf file into an image by using pdf2immage library. It is needed to run this algorithm before running image review. Outputs are saved in jpgs_to_review folder

**gram_text_vs_photo.py** - First reviewing algorithm. It, firstly, uses GPT-4o to convert image into text. Then, with the use of instruction for grammatical review from prompts.py, there are 2 types of reviews done. Firstly, you can find 2 functions for grammatical review with the text (from pdf) as an input, where first function generates one output and second function generates 10 outputs. Outputs are saved in Gram and review_txt_10_gram folders, respectively. Then you can find another 2 functions for grammatical review with the image (of pdf) as an input, where first function generates one output and second function generates 10 outputs. Outputs are saved in Gram and review_jpg_10_gram folders, respectively.

**non-prom_text_vs_photo.py** - Second reviewing algorithm. It, firstly, uses GPT-4o to convert image into text. Then, with the use of instruction for non-promotional review from prompts.py, there are 2 types of reviews done. Firstly, you can find 2 functions for non-promotional review with the text (from pdf) as an input, where first function generates one output and second function generates 10 outputs. Outputs are saved in Non-prom and review_txt_10_non-prom folders, respectively. Then you can find another 2 functions for non-promotional review with the image (of pdf) as an input, where first function generates one output and second function generates 10 outputs. Outputs are saved in Non-prom and review_jpg_10_non-prom folders, respectively.

**non-prom_text_and_photo.py** - Third reviewing algorithm that combines both text and image review, by firstly doing a text review, then image review and at the end both reviews are combined by last prompt to GPT-4o. Only non-promotional review was done with the use of this algorithm. Results are saved in review_comb_10_non-prom folder.

merge_result_output.py - Algorithm used to combine the result of initial and expert output of each reviewer. Outputs of this algorithm are saved in final_output_jpg_10_gram, final_output_jpg_10_non-prom, final_output_txt_10_gram and final_output_txt_10_non-prom folders.

analysis_output.py - test file for analysing the output of reviewing algorithms.

**analysis_gram.py** - Algorithm that uses outputs of Grammatical Reviewers and analyse (with the use of GPT-4o) them by creating confusion matrix. Output of this algorithm is saved in Gram folder as an analysis_txt.txt and analysis_jpg.txt.

**analysis_non-prom.py** - Algorithm that uses outputs of Non-promotional Reviewers and analyse (with the use of GPT-4o) them by creating confusion matrix. Output of this algorithm is saved in Non-prom folder as an analysis_txt.txt and analysis_jpg.txt.

**analysis_comb.py** - Algorithm that uses outputs of Combined Reviewers and analyse (with the use of GPT-4o) them by creating confusion matrix. Output of this algorithm is saved in Comb_non-prom folder as an analysis_txt.txt and analysis_jpg.txt.

Docs to review - is a folder that contains examples of pdfs for the reviewing purpose.

All of the needed things to run the algorithm are already inside each file.
Simply, just add a key for OpenAI API to run the algorithm with the use of GPT-4o.