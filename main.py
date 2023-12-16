import os
import re


import variables_calculation
import read_data
from get_scrape_articles import df, get_scrape_data
from nltk.tokenize import word_tokenize
import nltk
import get_scrape_articles
nltk.download('stopwords')

#scraping data from website and storing in articles directory
get_scrape_articles.get_scrape_data()

#creating dataframe with all the required columns in output file
df_output= df
df_output[['POSITIVE SCORE','NEGATIVE SCORE','POLARITY SCORE','SUBJECTIVITY SCORE','AVG SENTENCE LENGTH',
    'PERCENTAGE OF COMPLEX WORDS','FOG INDEX','AVG NUMBER OF WORDS PER SENTENCE','COMPLEX WORD COUNT',
    'WORD COUNT','SYLLABLE PER WORD','PERSONAL PRONOUNS','AVG WORD LENGTH']] = ""

# Getting date from scrap articles ank Making separate files after cleaning are removing stop words
for indx,file in enumerate(os.listdir("articles")):
    with (open(f"articles/{file}",'r',encoding="utf-8") as f):
        print('reading...'+ file+'\n')
        art_data = f.read()
        art_clean = re.sub("[^0-9a-zA-Z '-]+", " ", art_data)
        tok_data = word_tokenize(art_clean)
        clean_data = [i.lower() for i in tok_data if i not in read_data.get_stopwords()]

        with open(f"with_no_stopwords/clean_{file}",'w',encoding="utf-8") as w:
            print('Creating...' + file+'\n')
            w.write(' '.join(clean_data))
            w.close()
        print("Calculating variables for....."+file)
#Calculating positive score
        p_words=variables_calculation.positive_score(clean_data)
        df_output['POSITIVE SCORE'][indx]= len(p_words)

#Calculating positive score
        n_words = variables_calculation.negative_score(clean_data)
        df_output['NEGATIVE SCORE'][indx] = len(n_words)

#Calculating Polarity Score
        try:
            polarity_Score = ((len(p_words)-len(n_words))/(len(p_words)+len(n_words))) +0.000001
            df_output['POLARITY SCORE'][indx] = polarity_Score
        except ZeroDivisionError as e:
            print("Error: Cannot divide by zero")

#Calculating Subjectivity Score
        try:
            subjectivity_score = ((len(p_words)+len(n_words))/len(tok_data)) + 0.000001
            df_output['SUBJECTIVITY SCORE'][indx] = subjectivity_score
        except ZeroDivisionError as e:
            print("Error: Cannot divide by zero")

#Calculating AVG SENTENCE LENGTH
        try:
            word_list1,sentence_list1 = variables_calculation.AverageSentenceLength(art_data)
            avg_sent_len = len(word_list1)/len(sentence_list1)
            df_output['AVG SENTENCE LENGTH'][indx] = avg_sent_len
        except ZeroDivisionError as e:
            print("Error: Cannot divide by zero")

#Calculating PERCENTAGE OF COMPLEX WORDS
        try:
            comp_word = variables_calculation.percentage_of_complex_words(art_data)
            p_of_complex_word = len(comp_word)/len(tok_data)
            df_output['PERCENTAGE OF COMPLEX WORDS'][indx] = p_of_complex_word
        except ZeroDivisionError as e:
            print("Error: Cannot divide by zero")

#Calculating FOG INDEX
        avg_sen_len = variables_calculation.fog_index(art_data)
        fog_index= (avg_sen_len + p_of_complex_word)*0.4
        df_output['FOG INDEX'][indx] = fog_index


#Calculating AVG NUMBER OF WORDS PER SENTENCE
        try:
            avg_no_of_wrd_pr_sent = len(word_list1)/len(sentence_list1)
            df_output['AVG NUMBER OF WORDS PER SENTENCE'][indx] = avg_no_of_wrd_pr_sent
        except ZeroDivisionError as e:
            print("Error: Cannot divide by zero")

#Calculating 'COMPLEX WORD COUNT'
        comp_word_cnt= len(comp_word)
        df_output['COMPLEX WORD COUNT'][indx] = comp_word_cnt

#Calculating 'WORD COUNT'
        cleaned_word=variables_calculation.word_count(art_data)
        word_count= len(cleaned_word)
        df_output['WORD COUNT'][indx] = word_count

#Calculating 'SYLLABLE PER WORD',
        stl_per_word = variables_calculation.syllable_count_per_word(art_clean)
        df_output['SYLLABLE PER WORD'][indx] = stl_per_word

#Calculating 'PERSONAL PRONOUNS'
        per_pro= variables_calculation.personal_pronouns(art_data)
        df_output['PERSONAL PRONOUNS'][indx] = per_pro

#Calculating AVG WORD LENGTH
        avg_word_len = variables_calculation.average_word_length(art_clean)
        df_output['AVG WORD LENGTH'][indx] = avg_word_len
        print('Calculated variables for...'+file+" moving to DataFrame")
        #df_output2 = df_output.copy()
        df_output.to_excel('Output_Data_Structure.xlsx', index=False)
        print('finished..'+ file)

'''with pd.ExcelWriter('Output_Data_Structure.xlsx') as writer:
    df_output2.to_excel(writer, sheet_name='Sheet_name_1')'''