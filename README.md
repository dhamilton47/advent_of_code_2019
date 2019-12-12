# advent_of_code_2019
 Solutions to Advent of Code 2019 challenge

 Not necessarily done well or efficiently, lol.
 
#

# Thoughts on IntCode Structure _(as of Day 7, Part 1)_

Yes, geography and code ideas are still fluid.

### IntCode Class
**Nouns:**
- OS
- I/O
- CPU
- Stack
- Memory
- Programs

**Adjectives:**
- name = 'HAL'
- input_source = input_source
- programs = []
- program_names = []

**Verbs:**
- load_program(self, name, code):
- get_input(self, program_id):
- return_output(self, program_id, *args):
- address(self, i):
- execute_instruction(self, instruction, message=''):
- run_program(self):

        
### Program Class (Applications)
**Nouns:**
- Instruction

**Adjectives:**
- name = name
- program = []
- program_txtfile = code
- instruction_length_dict = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 99: 1}
- instruction_pointer = 0
- memory = []
- memory_size = 0
- txtfile = ''

**Verbs:**
- read_intcode_text_file(self):
- initialize_memory(self):
- get_instruction(self, ip):
- get_instruction_length(self, code):
- set_opcode(self, ip):
        return self.memory[ip] % 100

### Instruction Class
**Nouns:**

**Adjectives:**
- instruction = instruction
- instruction_length = len(instruction)
- opcode = self.set_opcode()
- parameters = self.set_parameters()
- parameter_modes = self.set_parameter_modes()

**Verbs:**
- decode_opcode(self):
- set_opcode(self, *args):
- set_parameter(self, i):
- set_parameters(self):
- set_parameter_mode(self, i):
- set_parameter_modes(self):
- address(self, i):

### Memory Class
**Nouns:**

**Adjectives:**
- name = name
- memory = memory
- memory_size = len(self.memory_size)  

**Verbs:**
- Initialize
- Retrieve
- Store

### OS_AoC19 Class
**Nouns:**

**Adjectives:**
- name = 'AdventofCode2019'

**Verbs:**
- opcode_switch(self, instruction)
- execute_instruction(self, instruction, message='')

### Stack Class
**Nouns:**

**Adjectives:**

**Verbs:**
- Operations
    - Push
    - Pop

### Hardware:  CPU Class
**Nouns:**

**Adjectives:**
- name = 'Rudolf'

**Verbs:**
- read_stack(self):
- execute_instruction(self, instruction, message=''):
- opcode1(self, parameters):
- opcode2(self, parameters):
- opcode3(self, parameters, input_source):
- opcode4(self, parameters):
- opcode5(self, parameters):
- opcode6(self, parameters):
- opcode7(self, parameters):
- opcode8(self, parameters):
- opcode99(self):
- opcode_generic(self, i):

### Hardware:  I/O Class
**Nouns:**

**Adjectives:**

**Verbs:**
- SysIn
- SysOut
