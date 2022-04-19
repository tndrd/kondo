
(cl:in-package :asdf)

(defsystem "servo_module-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "servos" :depends-on ("_package_servos"))
    (:file "_package_servos" :depends-on ("_package"))
  ))