# job_profile_match
match your cv with the job profile.


==================== ** Scope of Project ** ====================

It will gives you suggestion what to add in technical scope and
what to add in non-technical Area.

==================== ** What user should give ** ====================

Need to add all the details of the job via link or text.
Also need to add all the details of the potential employee.



==================== ** For developement ** ====================

App usecase Steps:
1. Try creating a common web parser for Linkedin and fetch all the details of the job
    a. If that doent work, user will have to manually copy and paste all the job
       informations to input text.
2. User will upload his/her CV.
3. System will generate common and uncommon traits between job requirement and CV.
4. At output system will gives how much that job fits to the CV and also
   to fit to the cv it will also gives the suggestion what should user do.

Technical steps:
1. Test parser
    a. If doesn't work create a text box for that.
2. User upload pdf file of CV.
2. Use OpenAI and huggingface embeddings
3. Ask OpenAI for giving score between 0 to 10 for job profiling.
4. Also gives output for what to do to match to the job.



