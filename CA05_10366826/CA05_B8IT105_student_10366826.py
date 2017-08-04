
## Assigning the dataset to a variable
changes_file = 'changes_python.log'

## Opening the raw data file and reading all of the lines.
## Using strip to strip out spaces and trim the line.
data = [line.strip() for line in open(changes_file, 'r')]

## Defining the point where I will separate out the different types of data
sep = 72*'-'

## Creating the commit class to hold each of the elements, this resulted in 422
## elements not including the headers.
class Commit:
    ##class for commits

    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment

    def get_commit_comment(self):
        return 'svn merge -r' + str(self.revision-1) + ':' + str(self.revision) + ' by ' \
                + self.author + ' with the comment ' + ','.join(self.comment) \
                + ' and the changes ' + ','.join(self.changes)

commits = []
current_commit = None
index = 0

author = {}
while True:
    try:
        ## Parsing each of the commits and putting them into a list of commits
        current_commit = Commit()
        details = data[index + 1].split('|')
        current_commit.revision = int(details[0].strip().strip('r'))
        current_commit.author = details[1].strip()
        current_commit.date = details[2].strip()
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
        current_commit.changes = data[index+2:data.index('',index+1)]
        #print(current_commit.changes)
        index = data.index(sep, index + 1)
        current_commit.comment = data[index-current_commit.comment_line_count:index]
        commits.append(current_commit)
    except IndexError:
        break

commits.reverse()

for index, commit in enumerate(commits):
    print(commit.get_commit_comment())

## Outputting the cleaned data to a csv file with headers
output_file  = "changes.csv"
my_file = open(output_file, 'w')
my_file.write("Revision,Author,Date,# Lines, Comment, Files Changed\n")
for commit in commits:
    my_file.write(str(commit.revision) + ',' + commit.author + ',"' + commit.date + '",' + str(commit.comment_line_count) + ',' + ''.join(commit.comment) + ',' + '  ,  '.join(commit.changes) + '\n')


my_file.close()
