/* -- sumatoria de cuadrados*/
.data
.balign 4 @ First message
message1: .asciz "Holaaa, escribe un numero: "
.balign 4
message2: .asciz "%d numero de veces %d\n"
.balign 4 @ Format pattern for scanf
scan_pattern: .asciz "%d"
.balign 4 @ Where scanf will store the number read
number_read: .word 0
.balign 4
return: .word 0
.balign 4
return2: .word 0

.text
/* mult_by_5 function */
loop:

    mul r3, r6, r6 
    add r4, r3, r3 
    cmp r6, r5 
    bgt end
    add r6, r6, #1
    b loop
    

.global main
main:
    mov r3, #0   @mult
    mov r4, #0   @sum
    mov r5, r0   @value
    mov r6, #1   @index
    ldr r1, =return @ r1 <- &return
    str lr, [r1] @ *r1 <- lr
    ldr r0, =message1 @ r0 <- &message1
    bl printf @ call to printf
    ldr r0, =scan_pattern @ r0 <- &scan_pattern
    ldr r1, =number_read @ r1 <- &number_read
    bl scanf @ call to scanf
    ldr r0, =number_read @ r0 <- &number_read
    ldr r0, [r0] @ r0 <- *r0
    bl loop
    mov r2, r0 @ r2 <- r0
    ldr r1, =number_read @ r1 <- &number_read
    ldr r1, [r1] @ r1 <- *r1
    ldr r0, =message2 @ r0 <- &message2
    bl printf @ call to printf
    ldr lr, =return @ lr <- &return
    ldr lr, [lr] @ lr <- *lr
    bx lr @ return from main using lr
/* External */
.global printf
.global scanf
