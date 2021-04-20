(setq l' (x x y x x x y x x z x x a)) ;| TODO ADD FILE IO |;
(setq x' (x x))
(setq y' (y y))
(setq z' (z z))
(setq a' (a a))

(defun begin(list)
    (COND ((null list) nil)
        ((EQUAL (car list) (car x))  (begin (cdr list))) ;|This is to check for x|;
        ((EQUAL (car list) (car y)) (secondState (cdr list)))
        (t nil)
    )   
)

;| Accept State |;
(defun secondState(list)
    (COND ((null list) T)
        ((EQUAL (car list) (car x)) (thirdState (cdr list)))
        (t nil)
    )
)

(defun thirdState(list)
    (COND ((null list) nil)
        ((EQUAL (car list) (car x)) (thirdState (cdr list)))
        ((EQUAL (car list) (car y)) (fourthState (cdr list)))
        (t nil)
    )
)

;| Accept State |;
(defun fourthState(list)
    (COND ((null list) T)
        ((EQUAL (car list) (car x)) (fourthState (cdr list)))
        ((EQUAL (car list) (car z)) (fifthState (cdr list)))
        (t nil)
    )
)

(defun fifthState(list)
    (COND ((null list) nil)
        ((EQUAL (car list) (car x)) (fifthState (cdr list)))
        ((EQUAL (car list) (car a)) (secondState (cdr list)))
        (t nil)
    )
)



(defun run()
    (begin l)
)


