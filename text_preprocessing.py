import os

# These functions have been useful for me in preprocessing text data for deep
# learning. The first three can be used individually with a single text file or
# a directory containing text files as an input and a single text file as an
# output. The preprocess function combines the three preceding functions to
# produce a single text file.

def char_remove(input, output, char_bar=None, division=None, input_type='file', preprocess=False):
    # This funtion removes garbage characters by setting a bar for character
    # frequency. Any characters which fall below the bar are removed.
    if input_type == 'file':
        char_dict = {}
        output_file = open(output, 'w')
        f = open(input, 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            for c in line:
                try:
                    char_dict[c] = char_dict[c] + 1
                except:
                    char_dict[c] = 1
        for line in lines:
            for c in line:
                if char_dict[c] > char_bar:
                    output_file.write(c)
        output_file.close()
        if preprocess == True:
            output_file = open(output, 'r')
            lines = output_file.readlines()
            output_file.close()
            return blank_remove(lines, output, division, preprocess=True)
            print(lines)
    else:
        if preprocess == True:
            inp_listdir = os.listdir(input)
            char_dict = {}
            for file in inp_listdir:
                f = open(input+'/'+file, 'r')
                lines = f.readlines()
                f.close()
                for line in lines:
                    for c in line:
                        try:
                            char_dict[c] = char_dict[c] + 1
                        except:
                            char_dict[c] = 1
            return char_dict
        else:
            inp_listdir = os.listdir(input)
            char_dict = {}
            output_file = open(output, 'w')
            for file in inp_listdir:
                f = open(input+'/'+file, 'r')
                lines = f.readlines()
                f.close()
                for line in lines:
                    for c in line:
                        try:
                            char_dict[c] = char_dict[c] + 1
                        except:
                            char_dict[c] = 1
            for file in inp_listdir:
                f = open(input+'/'+file, 'r')
                lines = f.readlines()
                f.close()
                for line in lines:
                    for c in line:
                        if char_dict[c] > char_bar:
                            output_file.write(c)
            output_file.close()

def blank_remove(input, output, division=None, input_type='file', preprocess=False):
    # Removes empty lines from text.
    if preprocess == True:
        if input_type == 'file':
            output_file = open(output, 'w')
            for line in input:
                if len(line) > 1:
                    output_file.write(line)
            output_file.close()
            output_file = open(output, 'r')
            lines = output_file.readlines()
            output_file.close()
            return structure_mark(lines, output, division, preprocess=True)
    else:
        if input_type == 'file':
            output_file = open(output, 'w')
            f = open(input, 'r')
            lines = f.readlines()
            f.close()
            for line in lines:
                if len(line) > 1:
                    output_file.write(line)
            output_file.close()
        else:
            inp_listdir = os.listdir(input)
            output_file = open(output, 'w')
            for file in inp_listdir:
                f = open(input+'/'+file, 'r')
                lines = f.readlines()
                f.close()
                for line in lines:
                    if len(line) > 1:
                        output_file.write(line)
            output_file.close()

def structure_mark(input, output, division, input_type='file', preprocess=False):
    # This places 'structure marks' throughout a text to help a model learn the
    # structure of longer pieces of text (e.g. novels). Division refers to the
    # number of divisions you want in the text. For example, if you want your
    # model to pay attention to what happens in different quarters of a text,
    # you should set division to 4. 5 marks would be placed:
    # <|start|>, <|div1/4|>, <|div2/4|>, <|div3/4|>, and <|end|>.
    if preprocess == True:
        if input_type == 'file':
            divs = division - 1
            output_file = open(output, 'w')
            lines = input
            div_index = round(len(lines)/division)
            counter = 1
            for div in range(divs):
                marker = '<|div'+str(counter)+'/'+str(division)+'|>\n'
                lines.insert(div_index-1, marker)
                div_index += round(len(lines)/division)
                counter += 1
            lines.insert(0, '<|start|>\n')
            lines.append('<|end|>\n')
            for line in lines:
                output_file.write(line)
            output_file.close()
    else:
        if input_type == 'file':
            divs = division - 1
            output_file = open(output, 'w')
            f = open(input, 'r')
            lines = f.readlines()
            f.close()
            div_index = round(len(lines)/division)
            counter = 1
            for div in range(divs):
                marker = '<|div'+str(counter)+'/'+str(division)+'|>\n'
                lines.insert(div_index-1, marker)
                div_index += round(len(lines)/division)
                counter += 1
            lines.insert(0, '<|start|>\n')
            lines.append('<|end|>\n')
            for line in lines:
                output_file.write(line)
            output_file.close()
        else:
            divs = division - 1
            inp_listdir = os.listdir(input)
            output_file = open(output, 'w')
            for file in inp_listdir:
                f = open(input+'/'+file, 'r')
                lines = f.readlines()
                f.close()
                div_index = round(len(lines)/division)
                counter = 1
                for div in range(divs):
                    marker = '<|div'+str(counter)+'/'+str(division)+'|>\n'
                    lines.insert(div_index-1, marker)
                    div_index += round(len(lines)/division)
                    counter += 1
                lines.insert(0, '<|start|>\n')
                lines.append('<|end|>\n')
                for line in lines:
                    output_file.write(line)
            output_file.close()

def preprocess(input, output, char_bar, division, input_type='file'):
    # Run a single text file through the three preceding functions.
    if input_type == 'file':
        char_remove(input, output, char_bar, division, preprocess=True)
    # Turn a directory into a single text file. Make sure that output is a
    # directory, not a file. The functions aren't called in this case because it
    # would make marking structure much more difficult. I will probably rewrite
    # some of the code to make it happen in the future.
    else:
        char_dict = char_remove(input, output, char_bar, input_type='directory', preprocess=True)
        inp_listdir = os.listdir(input)
        count = 1
        for file in inp_listdir:
            temp = open(output+'/'+str(count), 'w')
            f = open(input+'/'+file, 'r')
            lines = f.readlines()
            f.close()
            for line in lines:
                for c in line:
                    if char_dict[c] > char_bar:
                        temp.write(c)
            temp.close()
            count += 1
        out_listdir = os.listdir(output)
        for file in out_listdir:
            f = open(output+'/'+file, 'r')
            lines = f.readlines()
            f.close()
            f = open(output+'/'+file, 'w')
            for line in lines:
                if len(line) > 1:
                    f.write(line)
            f.close()
            f = open(output+'/'+file, 'r')
            lines = f.readlines()
            f.close()
            f = open(output+'/'+file, 'w')
            divs = division - 1
            div_index = round(len(lines)/division)
            counter = 1
            for div in range(divs):
                marker = '<|div'+str(counter)+'/'+str(division)+'|>\n'
                lines.insert(div_index-1, marker)
                div_index += round(len(lines)/division)
                counter += 1
            lines.insert(0, '<|start|>\n')
            lines.append('<|end|>\n')
            for line in lines:
                f.write(line)
            f.close()
        output_file = open(output+'/'+'combined_preprocess.txt', 'w')
        for file in out_listdir:
            f = open(output+'/'+file, 'r')
            lines = f.readlines()
            f.close()
            for line in lines:
                output_file.write(line)
        output_file.close()
        for file in out_listdir:
            os.system('rm %s/%s' %(output, file))
