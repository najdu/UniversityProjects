global _start
section .text
_start:
	mov eax, 1
	mov ebx, 42
	jmp skip
	mov ebx, 13
skip:
	int 0x80
