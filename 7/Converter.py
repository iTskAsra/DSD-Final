import re

def convert_assign_to_always_block(right, left):
    return f'''\n
    always @ ({left}) begin
        {right} <= {left};
    end\n'''

def convert_dataflow_to_behavioral(file_input, file_output):
    assign_regex = 'assign\s*(?P<delay>#\d+)?\s*(?P<lhs>[\w\[\]{},:]+)\s*=\s*(?P<rhs>[a-zA-Z0-9\[\]\(\)!~&|^\+\-\{\}*/%<>=\?:\s,]+);'
    output_regex = 'output (\w+)'
    file = open(file_input, 'r')
    verilog = file.readlines()
    file.close()
    output_file = open(file_output, 'w+')

    for line in verilog:
        assign_found = re.search(assign_regex, line)
        match_output = re.search(output_regex, line)
        if assign_found:
            right = assign_found.group(1)
            left = assign_found.group(2)
            output_file.write(convert_assign_to_always_block(right, left))
        elif match_output:
            output_file.write(line.replace('output', 'output reg', 1))
        else:
            output_file.write(line)
    output_file.close()

file_input = input()
file_output = input()

convert_dataflow_to_behavioral(file_input, file_output)