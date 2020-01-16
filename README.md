# advent_of_code_2019
 Solutions to Advent of Code 2019 challenge

 Not necessarily done well or efficiently, lol.

#

# Thoughts on IntCode Structure

    _(as of Day 11, Part 1)_
    _(as of Day 17, Part 2)_
    _(as of Day 21, Part 1)_
    _(as of Day 23, Part 1)_


Yes, geography and code ideas are still fluid.

Current pain points:
1. Tracking movement/arrays correctly and efficiently
2. Communication of repetitive I/O cycles.
3. Communication between IntCode computer instances.


#### Custom Imports

aoc

**Adjectives:**
- programs_available_dictionary
- opcode_dictionary

**Verbs:**
- read_intcode_program(txtfile)


### IntCode Class (Computer)
**Nouns:**
Computer(library = dictionary of information regarding programs)
- CPU
- Instruction
- I/O
- Memory
- Program


**Adjectives:**
- computer_name = 'HAL'
- halt_condition = False
- ip = 0
- library = library
- program_name = None
- program_loaded = None
- program_to_load = program_to_load


**Verbs:**
- boot()
- flash_memory()
- instruction_next()
- process_run()
- program_load()


### Instruction Class
**Nouns:**
Instruction(computer, op_dictionary=aoc.OPCODE_DICTIONARY,
            mode_dictionary=aoc.MODE_DICTIONARY)


**Adjectives:**
- raw_opcode = computer.memory.value(computer.ip)
- opcode = op_dictionary[raw_opcode % 100]['opcode']
- length = op_dictionary[raw_opcode % 100]['length']
- function = op_dictionary[raw_opcode % 100]['func']
- parameters = op_dictionary[raw_opcode % 100]['params']
- modes = mode_dictionary[raw_opcode // 100]['modes']
- instruction = {'opcode': opcode,
                 'parameters': decode_parameters(
                    computer.memory,
                    length,
                    computer.ip),
                'length': length}


**Verbs:**
- decode_parameters(memory, length, ip)


### Program Class
**Nouns:**
Program(program)


**Adjectives:**
- code = read_binary(program['binary'])
- description = program['description']
- name = program['name']


**Verbs:**
- read_binary(program_binary):


### Hardware:  CPU Class
**Nouns:**
CPU(instruction=None)


**Adjectives:**
- instruction = instruction
- name = 'The Little Train That Could'
- print_flag = False


**Verbs:**
- add(i, j)
- instruction_execute(computer, instruction)
- multiply(i, j):


### Hardware:  I/O Class
**Nouns:**
IO

**Adjectives:**
- halt_condition (?)
- input_value
- output_value

**Verbs:**
- get_input
- return_output


### Hardware:  Memory Class
**Nouns:**
Memory(program={})


**Adjectives:**
- bank = flash(code)
- base_offset


**Verbs:**
- extend_memory(bank, address)
- flash(program)
- value(address)

