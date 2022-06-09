global _start
section .data
	addr DB "yellow", 0x0a
section .text
_start:
	mov [addr], byte 'H'
	mov [addr + 5], byte '!' 
	mov eax, 4
	mov ebx, 1
	mov ecx, addr
	mov edx, 7
	int 0x80

	mov eax, 1
	mov ebx, 0
	int 0x80
