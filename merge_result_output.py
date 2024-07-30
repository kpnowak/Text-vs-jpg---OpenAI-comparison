
def merge(i_folder, o_folder, type_, n):
    for i in range(n):
        # File paths
        file1_path = f'{i_folder}\\result{i+1}_{type_}.txt'
        file2_path = f'{i_folder}\\output{i+1}_{type_}.txt'
        output_path = f'{o_folder}\\merged_output{i+1}.txt'

        # Separator and header
        separator = "-" * 94
        header = "-" * 40 + " Chief Output " + "-" * 40

        try:
            # Read the contents of the first file
            with open(file1_path, 'r') as file1:
                content1 = file1.read()
                
            # Read the contents of the second file
            with open(file2_path, 'r') as file2:
                content2 = file2.read()
                
            # Prepare the merged content
            merged_content = f"{content1}\n\n{separator}\n{header}\n{separator}\n\n{content2}"
            
            # Write the merged content to the output file
            with open(output_path, 'w') as output_file:
                output_file.write(merged_content)
            
            print(f"Files merged successfully into {output_path}")
            
        except Exception as e:
            print(f"An error occurred: {e}")

i_folder = 'review_txt_10_gram'
o_folder = 'final_output_txt_10_gram'
type_ = ('txt')
n = 20

#merge(i_folder, o_folder, type_, n)
#merge('review_jpg_10_gram', 'final_output_jpg_10_gram', 'jpg', 20)
merge('review_txt_10_non-prom', 'final_output_txt_10_non-prom', 'txt', 20)
merge('review_jpg_10_non-prom', 'final_output_jpg_10_non-prom', 'jpg', 20)