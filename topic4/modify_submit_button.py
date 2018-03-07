import os

def buildform(filename):
    print "dealing with %s"%filename
    pattern = '<button type="submit" class="btn btn-primary">Submit</button>'
    with open(filename, 'r') as input_file, open(filename+'.modified', 'w') as output_file:
        for line in input_file:
            if line.strip() == '<button type="submit" class="btn btn-primary">Submit</button>':

                output_file.write('<button type="submit" class="btn btn-primary">Check for Answers</button>\n')
                print("found button")
            elif 'id="form-title"' in line.strip():
                try:
                    lines = line.split(" - ")
                    line0 = lines[0].replace("Unit 6", '<a href="/module6">Unit 6</a> | ')
                    line0 = line0.replace("Topic "+lines[0][lines[0].index("Topic")+6], '<a href="/module6/topic'+lines[0][lines[0].index("Topic")+6]+'">Topic '+lines[0][lines[0].index("Topic")+6]+'</a> | ')
                    line0 = line0.replace("h3", "p")
                    line0 = line0+"</h3>\n".replace("h3", "p")
                    output_file.write(line0)
                    output_file.write("<h3>"+lines[1].strip()+"\n")
                    print("titile found")
                except Exception as e:
                    pass
                else:
                    pass
                finally:
                    pass
                
            else:
                output_file.write(line)
    return "done with %s"%filename
# buildform()

for x in os.listdir('.'):
    if x.endswith(".html"):
        print buildform(x)

