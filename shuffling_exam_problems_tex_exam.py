#!/usr/bin/env python
# coding: utf-8

import random
n_versions = 3
input_folder = 'original_exam/'
output_folder = 'shuffled_exams/'
input_filename = 'sample_exam'
output_filename = 'sample_exam'

prequestions = []  # a list of string representing the latex document in python
questions = []
postquestions = []
linenumber = 0
separators = []

# read the .tex file, and modify the lines
with open(input_folder+input_filename+'.tex') as fin1:
    for line in fin1:
        linenumber += 1
        if((line.find('\\question')!=-1)or(line.find('\\end{questions}')!=-1)):
            separators.append(linenumber)

linenumber = 0
with open(input_folder+input_filename+'.tex') as fin2:
    for line in fin2:
        linenumber+=1
        if (linenumber < separators[0]):
            prequestions.append(line)
        if (linenumber >= separators[0]) and (linenumber < separators[-1]):
            questions.append(line)
        if (linenumber >= separators[-1]):
            postquestions.append(line)
            
seps_within_questions = []
counter = 0
for line in questions:    
    if(line.find('\\question')!=-1):
        seps_within_questions.append(counter)
    counter += 1
    
n_problems = len(seps_within_questions)

seps_within_questions.append(len(questions))

problems_list = []
mycounter = 0
for i in range(n_problems):
    problem = []
    while((mycounter >= seps_within_questions[i]) and (mycounter < seps_within_questions[i+1])):
        problem.append(questions[mycounter])
        mycounter += 1
    problems_list.append(problem)

problems_indices = list(range(n_problems))
mydict = {0:'A',1:'B',2:'C',3:'D'}
solution_key = []
for index in problems_indices:
    myproblem = problems_list[index]
    seps_within_problem = []
    ind = 0
    for line in myproblem:
        if (line.find('\\choice')!=-1)or(line.find('\\CorrectChoice')!=-1):
             seps_within_problem.append(ind)
        ind += 1
    answers = []
    for k in seps_within_problem:
        answers.append(myproblem[k])

    for i in range(len(answers)):
        if (answers[i].find('\\CorrectChoice')!=-1):
            solution_key.append((index+1,mydict[i]))

list_of_shuffled_solution_keys = []
list_of_shuffled_problems_lists = []

for l in range(n_versions):
    random.shuffle(problems_indices)
    shuffled_problems_list = []
    shuffled_solution_key = []
    counter = 0
    for index in problems_indices:
        myproblem = problems_list[index]
        seps_within_problem = []
        ind = 0
        for line in myproblem:
            if (line.find('\\choice')!=-1)or(line.find('\\CorrectChoice')!=-1):
                 seps_within_problem.append(ind)
            ind += 1
        preanswers = []
        answers = []
        postanswers = []
        for i in range(seps_within_problem[0]):
            preanswers.append(myproblem[i])
        for k in seps_within_problem:
            answers.append(myproblem[k])
        for i in range(seps_within_problem[-1]+1,len(myproblem)):
            postanswers.append(myproblem[i])
        random.shuffle(answers)
        for i in range(len(answers)):
            if (answers[i].find('\\CorrectChoice')!=-1):
                shuffled_solution_key.append((counter+1,mydict[i],index+1))
        shuffled_problem = preanswers + answers + postanswers
        shuffled_problems_list.append(shuffled_problem)
        counter += 1
    list_of_shuffled_solution_keys.append(shuffled_solution_key)
    list_of_shuffled_problems_lists.append(shuffled_problems_list)

for l in range(n_versions):
# write back the new document
    with open(output_folder+output_filename+'_v'+str(l+1)+'.tex', 'w') as fout:
        for i in range(len(prequestions)):
            fout.write(prequestions[i])
        for i in range(len(list_of_shuffled_problems_lists[l])):
            for j in range(len(list_of_shuffled_problems_lists[l][i])):
                fout.write(list_of_shuffled_problems_lists[l][i][j])
        for i in range(len(postquestions)):
            fout.write(postquestions[i])


with open(output_folder+output_filename+'_solution_keys.txt', 'w') as fout2:
    fout2.write('Original Solution Key:\n')
    for item in solution_key:
        fout2.write(str(item)+'\n')
    for l in range(n_versions):
        fout2.write('\n'+'Solution Key for version ' + str(l+1)+'\n')
        for myitem in list_of_shuffled_solution_keys[l]:
            fout2.write(str(myitem)+'\n')

list_of_shuffled_solution_keys