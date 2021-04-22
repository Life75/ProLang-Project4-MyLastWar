(defun demo() 
 (setq fp (open "theString.txt" :direction :input)) 
(setq here (read fp "done")) 
(princ "processing") 
(princ here)
 (state0 here)
 )

(setq x' (x x))
(setq y' (y y))
(setq z' (z z))
(setq a' (a a))

(defun state0(list)
(COND ((null list) nil)
((EQUAL (car list) (car x)) (state0(cdr list)))
((EQUAL (car list) (car y)) (state1(cdr list)))

(t nil)
))

(defun state1(list)
(COND ((null list) T)
((EQUAL (car list) (car x)) (state2(cdr list)))

(t nil)
))

(defun state2(list)
(COND ((null list) nil)
((EQUAL (car list) (car x)) (state2(cdr list)))
((EQUAL (car list) (car y)) (state3(cdr list)))

(t nil)
))

(defun state3(list)
(COND ((null list) T)
((EQUAL (car list) (car x)) (state3(cdr list)))
((EQUAL (car list) (car z)) (state4(cdr list)))

(t nil)
))

(defun state4(list)
(COND ((null list) nil)
((EQUAL (car list) (car x)) (state4(cdr list)))
((EQUAL (car list) (car a)) (state1(cdr list)))

(t nil)
))
