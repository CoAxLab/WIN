
# coding: utf-8

# In[2]:

if __name__ == "__main__":


    def WIN_list(filename,colNames):

        open('WIN_completed.xlsx', 'r')
        import pandas as pd
        text = pd.read_excel('WIN_completed.xlsx')
        text.head()
        # colNames=['Sex', 'base_age','yrs_edu','base_payoff'] 

        new_data=text[colNames]
        exportFilename=filename+'.txt'


        return new_data.to_csv(exportFilename, index=False, sep='\t')

    #WIN_list('WIN_gender',['Sex','yrs_edu'])
 
#in command line write python -c 'import WIN_connect; (WIN_gender,['col1','col2'])


# In[ ]:



