# This is the repository for the "Iterative Soft Prompt-tuning for Unsupervised Domain Adaptation".

You should install OpenPrompt https://github.com/thunlp/OpenPrompt

First, Predict initial pseudo-label for the target domain from source domain data.

Second, Adjust initial target domain data pseudo-label, divide target domain data and iterative training model.

Then, Adjust all target domain data pseudo-label and voted invariant label.

Final, Average the experimental results three times.

Note that the file paths should be changed according to the running environment. 

example shell scripts:

- python fewshot.py --result_file ./output_fewshot.txt --dataset newsgroups1 --template_id 0 --seed 144 --shot 20 --verbalizer manual
- python adj_data.py
- python div_data.py
- python itera_model.py
- python adj_label.py
- python voted_label.py
- python final_test.py