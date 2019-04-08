import os

'''
Basic OS functions
printing current directory
Making a new direcoty
Renaming and removing directories
'''

# get current directory
current_directory = os.getcwd();
print(current_directory);

# make new directory
os.mkdir('logFiles');

# rename directory
os.rename('logFiles','logs');

#remove directory
os.rmdir('logs');