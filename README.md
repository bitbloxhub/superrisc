# superrisc: a simple computer

programs operate on a infinite sequence of infinitely large unsigned integers

the program has a pointer to the memory, starting at address 0

the opcodes (none of them taking arguments) (the ascii value is the binary opcode):
* `[`: increments the pointer
* `]`: decrements the pointer
* `J`: jump to the code at the address of the value of the pointer
* `R`: runs the opcode at the currently addressed part of the memory
* `+`: adds 1 to the memory location currently addressed
* `-`: subtracts 1 to the memory location currently addressed
* `C`: if the value of the current address is not 0, exectute the next operation, otherwise skip

