# advent_of_code_2019
 Solutions to Advent of Code 2019 challenge

 Not necessarily done well or efficiently, lol.

#

# Thoughts on IntCode Structure _(as of Day 7, Part 1)_

Yes, geography and code ideas are still fluid.

### Ship System and its Program
- Gravity Assist Program (Day 2) - No Ship System
- Thermal Environment Supervision Terminal (TEST)
    - Air Conditioner (system ID 1) - Diagnostic Program
    - Thermal Radiators (system ID 5) - Diagnostic Program
- Amplifiers - Amplifier Controller Software

#### Custom Imports

aoc

**Adjectives:**
- programs_available_dictionary
- opcode_dictionary

**Verbs:**
- read_program(txtfile)


### IntCode Class (Computer) _(as currently implemented)_
**Nouns:**
Computer(library = dictionary of information regarding programs)
- OS _(not implemented)_
- I/O _(not implemented)_
- CPU
- Stack _(not implemented)_
- Memory
- Program


**Adjectives:**
- name = 'HAL'
- programs_available_dictionary = library
- program_loaded = None
- ip = None


**Verbs:**
- boot()
- instruction_next(memory, pointer)
- program_load()
- program_menu(program_list)
- programs_available()

-(not implemented yet)_
- get_input(program_id):
- return_output(program_id, *args):


### OS_AoC19 Class _(Conceptual stage)_
**Nouns:**


**Adjectives:**
- name = 'AdventofCode2019'


**Verbs:**
- opcode_switch(instruction)
- execute_instruction(instruction, message='')


### Stack Class _(Conceptual stage)_
**Nouns:**


**Adjectives:**


**Verbs:**
- Operations
    - Push
    - Pop


### Hardware:  CPU Class _(as currently implemented)_
**Nouns:**
CPU(instruction=[])


**Adjectives:**
- name = 'The Little Train That Could'
- instruction = instruction


**Verbs:**
- instruction_execute(memory, ip, inst)
- add(i, j)
- multiply(i, j):


### Hardware:  I/O Class _(Conceptual stage)_
**Nouns:**


**Adjectives:**


**Verbs:**
- SysIn
- SysOut


### Program Class (Applications) _(as currently implemented)_
**Nouns:**
Program(programID)


**Adjectives:**
- programID = programID
- name = programID['name']
- binary = programID['binary']
- code = read_binary()


**Verbs:**
- read_binary(program_binary=None):


### Instruction Class _(as currently implemented)_
**Nouns:**
Instruction(memory, ip=None, dictionary=aoc.opcode_dictionary)


**Adjectives:**
- raw_opcode = memory.address(ip)
- opcode = dictionary[raw_opcode]['opcode']
- modes = dictionary[raw_opcode]['modes']
- parameters = dictionary[raw_opcode]['parameters']
- length = dictionary[raw_opcode]['length']
- instruction = {'opcode': opcode,
                 'parameters': decode_parameters(memory, self.length, ip),
                 'length': length}


**Verbs:**
- decode_parameters(self, memory, length, ip)


### Hardware:  Memory Class _(as currently implemented)_
**Nouns:**
Memory(code=[])


**Adjectives:**
- register = flash(code)


**Verbs:**
- flash(code)
- address(i)


