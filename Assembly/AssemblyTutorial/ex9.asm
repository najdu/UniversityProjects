global _start
section .text

_start:
    push 21
    call times2
    mov eax, 1
    int 0x80
    
times2:
    push ebp
    mov ebp, esp
    mov ebx, [ebp+8]
    add ebx, ebx
    mov esp, ebp
    pop ebp
    ret