
(cl:in-package :asdf)

(defsystem "kondo_webots-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "servo_command" :depends-on ("_package_servo_command"))
    (:file "_package_servo_command" :depends-on ("_package"))
  ))